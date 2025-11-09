"""Discovery helper for Syncleo Kettle."""
from __future__ import annotations

import logging
import threading
import zeroconf
from typing import Dict, List, Optional

_LOGGER = logging.getLogger(__name__)
_LOGGER.setLevel(logging.DEBUG)

class SyncleoDiscovery:
    """Class to handle Syncleo device discovery."""
    
    _instance = None
    
    @classmethod
    def get_instance(cls) -> SyncleoDiscovery:
        """Get singleton discovery instance."""
        if cls._instance is None:
            cls._instance = SyncleoDiscovery()
        return cls._instance

    def __init__(self):
        """Initialize the discovery."""
        self._devices: Dict[str, dict] = {}
        self._zc: Optional[zeroconf.Zeroconf] = None
        self._browser: Optional[zeroconf.ServiceBrowser] = None
        self._lock = threading.Lock()
        self._started = False
        self._is_shared_zeroconf = False

    def set_zeroconf_instance(self, zc: zeroconf.Zeroconf) -> None:
        """Set shared Zeroconf instance."""
        self._zc = zc
        self._is_shared_zeroconf = True
        _LOGGER.debug("Set shared Zeroconf instance")

    def start_discovery(self) -> None:
        """Start discovering devices."""
        if self._started:
            _LOGGER.debug("Discovery already started")
            return
            
        try:
            # Если Zeroconf instance не установлен, создаем свой
            if self._zc is None:
                _LOGGER.info("Creating internal Zeroconf instance for discovery")
                self._zc = zeroconf.Zeroconf()
                self._is_shared_zeroconf = False
            else:
                _LOGGER.info("Using shared Zeroconf instance for discovery")
            
            self._browser = zeroconf.ServiceBrowser(
                self._zc, "_syncleo._udp.local.", self
            )
            self._started = True
            _LOGGER.info("Started Syncleo device discovery")
        except Exception as err:
            _LOGGER.error("Failed to start discovery: %s", err)

    def stop_discovery(self) -> None:
        """Stop discovering devices."""
        if not self._started:
            return
            
        if self._browser:
            self._browser.cancel()
            self._browser = None
        
        # Закрываем только если это наш собственный экземпляр
        if self._zc and not self._is_shared_zeroconf:
            self._zc.close()
            self._zc = None
            
        with self._lock:
            self._devices.clear()
            
        self._started = False
        _LOGGER.info("Stopped Syncleo device discovery")

    def get_devices(self) -> List[dict]:
        """Get list of discovered devices."""
        with self._lock:
            return list(self._devices.values())

    def add_service(self, zc: zeroconf.Zeroconf, type_: str, name: str) -> None:
        """Service added callback."""
        self._update_service("add_service", zc, type_, name)

    def update_service(self, zc: zeroconf.Zeroconf, type_: str, name: str) -> None:
        """Service updated callback."""
        self._update_service("update_service", zc, type_, name)

    def remove_service(self, zc: zeroconf.Zeroconf, type_: str, name: str) -> None:
        """Service removed callback."""
        _LOGGER.debug("Service removed: %s", name)
        mac = self._extract_mac_from_name(name)
        if mac:
            with self._lock:
                if mac in self._devices:
                    del self._devices[mac]
            _LOGGER.info("Device removed: %s", mac)

    def _update_service(self, method: str, zc: zeroconf.Zeroconf, type_: str, name: str) -> None:
        """Handle service updates."""
        try:
            info = zc.get_service_info(type_, name)
            if not info:
                return

            mac = self._extract_mac_from_name(name)
            if not mac:
                return

            # Convert properties with proper error handling
            properties = {}
            if info.properties:
                for key, value in info.properties.items():
                    try:
                        key_str = key.decode('utf-8') if isinstance(key, bytes) else str(key)
                        value_str = value.decode('utf-8') if isinstance(value, bytes) else str(value)
                        properties[key_str] = value_str
                    except Exception as prop_err:
                        _LOGGER.debug("Error decoding property %s: %s", key, prop_err)
                        continue

            # Convert addresses to strings
            addresses = []
            if info.addresses:
                for addr in info.addresses:
                    try:
                        # Convert bytes to IP string
                        if len(addr) == 4:  # IPv4
                            addresses.append(".".join(str(b) for b in addr))
                        else:  # IPv6 or other
                            addresses.append(str(addr))
                    except Exception as addr_err:
                        _LOGGER.debug("Error converting address: %s", addr_err)
                        addresses.append(str(addr))

            device_info = {
                'mac': mac,
                'name': name,
                'addresses': addresses,
                'port': info.port,
                'devtype': properties.get('devtype', 'Unknown'),
                'vendor': properties.get('vendor', 'Unknown'),
                'basetype': properties.get('basetype', 'Unknown'),
                'firmware': properties.get('firmware', 'Unknown'),
                'public_key': properties.get('public', ''),
                'curve': properties.get('curve', ''),
                'protocol': properties.get('protocol', ''),
            }

            with self._lock:
                self._devices[mac] = device_info

            _LOGGER.info("Discovered device: %s - %s:%s (devtype: %s, vendor: %s)", 
                        mac, addresses[0] if addresses else 'unknown', info.port,
                        device_info['devtype'], device_info['vendor'])
            
        except Exception as exc:
            _LOGGER.error("Error processing service update: %s", exc)

    def _extract_mac_from_name(self, name: str) -> Optional[str]:
        """Extract MAC address from service name."""
        try:
            if name.startswith('_') or '.' not in name:
                return None
                
            mac_part = name.split('.')[0].lower()
            # Check if it looks like a MAC address (12 hex characters)
            if len(mac_part) == 12 and all(c in '0123456789abcdef' for c in mac_part):
                return mac_part
            return None
        except Exception:
            return None