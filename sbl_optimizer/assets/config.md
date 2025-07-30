## Config File Documentation (`config.json`)

| Key                 | Type  | Description                                                   |
|---------------------|-------|---------------------------------------------------------------|
| `swell_temperature` | float | Target temperature for swelling in °C.                        |
| `light_power`       | float | Light source power in watts.                                  |
| `light_diameter`    | float | Diameter of the light circle on paper in meters.              |
| `alpha`             | float | Thermal diffusivity in m²/s.                                  |
| `verbose`           | int   | Bool enabling logging. 0: turned off; 1: turned on.           |
| `resolution`        | int   | Number of cells paper is divided into in thermal simulations. |