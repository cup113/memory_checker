# Changelog

## [1.0.0] - 2026-06-09

### Added
- Version number (`VERSION`) displayed in tray menu
- Installer: autostart via Registry `Run` key on login
- Installer: `PrivilegesRequired=lowest` for per-user install

## [0.2.0] - 2026-06-08

### Added
- Rounded-rectangle fill on tray icon with semi-transparent color for visual at-a-glance usage indication
- Hover tooltip now shows used/total GB and swap usage alongside percentage

### Changed
- Icon font size reduced from 48 to 44 for better fit in smaller icon
- Tooltip and icon refresh logic now update independently (GB values no longer tied to integer percent changes)
- `update_loop()` sleep interval reduced from 3 to 2 seconds

### Fixed
- README.md corrected: color thresholds now match actual `interpolate_color()` implementation
- README.md corrected: refresh rate 3s → 2s
- README.md corrected: removed non-existent "top 5 processes" feature

## [0.1.0] - 2026-04-26

### Added
- Initial release: system tray memory monitor with color-coded percentage display
- Dynamic tray icon with green-to-red color interpolation
- Right-click Exit menu
- Auto-refresh every 2 seconds
