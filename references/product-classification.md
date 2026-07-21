# Product Classification and Confirmation

Classify the real subject before selecting motion. The category determines which assets are truthful, which movement is safe, and whether generative I2V is appropriate.

## Confirmation Gate

Before direction or generation:

1. Inspect the supplied image, file, URL, page, or description.
2. Name one proposed class or mark it `unknown`.
3. State the visible evidence and confidence level.
4. State what the finished shot must prove or show.
5. List available and missing assets.
6. Propose the production path.
7. Ask the user to confirm or correct the classification and path.

Before confirmation, allow only read-only inspection, source collection, feasibility notes, and a material checklist. Do not create speculative product assets, finalize a motion prompt, upload files, or spend generation credits.

## Classes and Material Routes

| Class | Verify | Preferred assets | Default production path |
| --- | --- | --- | --- |
| `website-ui` | real URL, page purpose, desktop or mobile target | live page captures, logo, key pages, responsive states | deterministic screen capture, scroll, pan, zoom, crop, and compositing; preserve exact text and layout |
| `software-interface` | app identity, workflow, platform | approved screenshots or recording, cursor path, empty and populated states | deterministic UI motion and callouts; generative redraw only for explicitly conceptual work |
| `consumer-electronics` | device model, front, side, ports, screen | clean hero frame, side and back views, logo, screen artwork | push, macro glide, pedestal, or small arc; require multiple views for larger rotation |
| `industrial-product` | scale, function, moving parts, safety facts | multi-view photography, dimensions, mechanism references | controlled inspection, detail reveal, or 3D workflow for exact geometry |
| `food-beverage` | dish, ingredients, temperature, serving state | hero image, texture close-ups, steam, pour, cut, or garnish references | macro glide, push-in, rack focus, restrained ingredient or atmospheric motion |
| `beauty-packaging` | bottle or package shape, label, cap, liquid | front and three-quarter views, label artwork, material references | pedestal, label push, shallow arc, controlled reflections |
| `fashion-accessory` | garment or item identity, fit, material | front, side, back, detail, model or mannequin references | tracking, fabric micro-motion, macro detail, or small inspection arc |
| `vehicle` | exact model, body lines, wheels, interior | exterior angles, interior, road or studio references | tracking, low dolly, detail glide; use multi-view or 3D for orbit |
| `architecture-interior` | real place, layout, verticals, access path | wide views, floor plan when available, adjacent viewpoints | pan, tilt, straight dolly, or controlled parallax with strict line preservation |
| `person-character` | identity, wardrobe, role, action | identity views, full body when needed, expression or motion reference | push-in, tracking, follow, or performance transfer with anatomy protection |
| `artwork-graphic` | flat or layered artwork, intended framing | high-resolution master, layer files when available | pan, zoom, 2.5D parallax, light or texture animation; avoid fake full orbit |
| `environment` | real or designed location, depth, weather | wide frame, adjacent angles, foreground and background plates | pan, truck, drone-like push, or atmospheric animation according to depth |
| `other` | user-defined subject and evidence | assets required by the stated truth claims | propose a conservative route and confirm it explicitly |
| `unknown` | insufficient evidence | request the product name, URL, additional view, or intended use | stop before motion planning |

## Confidence

- `high`: the product or subject is directly verified from supplied material or a real source.
- `medium`: the class is clear, but exact model, version, or deliverable purpose needs confirmation.
- `low`: several classes remain plausible or critical evidence is missing.

Do not convert low confidence into invented certainty. Ask one concise clarification question or request the smallest missing asset.

## Confirmation Card

```text
I identify this as: [product class]
Evidence: [specific visible or verified facts]
The finished shot should show: [commercial or narrative proof]
Proposed production path: [method and why]
Available assets: [list]
Required or missing assets: [list]
Please confirm or correct the classification and production path before I begin.
```

After confirmation, set `classification.user_confirmed: true`, update any corrected facts, then continue to source analysis and motion design.
