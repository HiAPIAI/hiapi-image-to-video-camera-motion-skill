# Source Image Analysis

Analyze the approved still before directing motion. The source image is not merely a reference; in most image-to-video systems it acts as the first frame and constrains composition, subject, light, style, and initial geometry.

## Contents

- Assessment sequence
- Depth confidence
- Edge reserve
- Occlusion and unseen surfaces
- Identity and geometry risks
- Subject-specific guidance
- Movement feasibility matrix
- Repairing an unsuitable source

## Assessment Sequence

Inspect in this order:

1. Identify the focal subject and the visual evidence that must remain readable.
2. Classify shot size, camera height, angle, and lens feel.
3. Trace perspective lines, horizon, and vanishing direction.
4. Separate foreground, midground, and background.
5. Measure visual reserve around the subject and frame edges.
6. Identify hidden surfaces a requested move would expose.
7. Mark fragile details: face, hands, text, logo, product edges, jewelry, glass, liquid, mirrors, screens, repeated patterns.
8. Decide whether camera, subject, environment, or stillness should carry the shot.
9. Set depth confidence and maximum safe movement.

Do not let a polished image override structural evidence. A beautiful flat frame can still be unsuitable for a translating camera.

## Depth Confidence

### High

Evidence includes:

- distinct foreground, midground, and background layers;
- visible floor, road, table, corridor, or other receding plane;
- consistent perspective and strong leading lines;
- clear subject separation;
- enough background texture to support parallax;
- no major hidden anatomy or product surfaces required by the move.

Possible moves: small to medium dolly, truck, tracking, limited arc, or restrained crane.

### Medium

Evidence includes:

- some depth cues but shallow separation;
- moderate background blur;
- subject overlaps important scene elements;
- uncertain surface continuity near edges;
- reflections or shadows that may not survive viewpoint change.

Possible moves: small push, short pan or tilt, macro glide, 5-20 degree arc, restrained tracking.

### Low

Evidence includes:

- flat graphic or poster composition;
- telephoto compression with little visible depth;
- uniform background;
- heavy depth-of-field blur that removes scene structure;
- cropped subject touching several frame edges;
- visible artifacts, malformed anatomy, or inconsistent geometry;
- front-only product view with no side information.

Prefer: locked frame, zoom, small push, focus change, isolated subject motion, environment micro-motion, or prepared 2.5D layers.

## Edge Reserve

Edge reserve is the amount of plausible visual information available around the subject and movement direction.

### High

- subject occupies less than roughly two-thirds of the frame;
- clean negative space exists in the movement direction;
- head, limbs, product silhouette, and shadows are fully contained;
- background can expand without exposing obvious missing content.

### Medium

- one side is tight but the intended move goes toward open space;
- moderate crop is acceptable;
- small movement will not expose hidden parts.

### Low

- subject touches or crosses the frame boundary;
- face, hand, product, shadow, or reflection is cropped;
- requested pull-out would need to invent missing body or environment;
- requested pan or truck moves toward an empty image boundary;
- typography or UI is close to the edge and must remain legible.

With low edge reserve, reduce travel, keep subject scale stable, or rebuild the still with a wider crop.

## Occlusion and Unseen Surfaces

Every translating move changes which surfaces are visible. Ask:

- What is behind the subject?
- What is hidden by hair, arms, packaging, foreground objects, or furniture?
- Will a side move reveal a missing ear, limb, product side, label edge, room wall, or reflection source?
- Does the requested angle cross the subject's profile?
- Does the source contain a plausible continuation of floor, table, backdrop, or architecture?

Risk levels:

- **Low**: small angle change reveals little new information.
- **Medium**: move reveals partial side surfaces or changes overlap.
- **High**: move requires a back view, full profile, hidden limbs, new room geometry, or extensive reflection reconstruction.

## Identity and Geometry Risks

### Faces and people

Check:

- eyes are aligned and sharp;
- teeth, hands, fingers, ears, and hairline are coherent;
- body pose has a plausible continuation;
- wardrobe layers and accessories are unambiguous;
- the motion does not require an unseen profile or back view.

Artifacts in the first frame often intensify during motion. Repair the still before generation when identity matters.

### Rigid products

Check:

- silhouette and proportions are correct;
- logo and typography are legible;
- ports, buttons, seams, dial markings, and materials are consistent;
- the product has enough side information for the requested arc;
- the support surface and shadow agree with the lighting;
- reflective highlights have a plausible source.

Rigid manufactured objects expose errors quickly. Reduce movement before accepting shape drift.

### Text, logos, UI, and packaging

Generated motion frequently deforms small text. Treat text as protected evidence.

Prefer:

- constant or slowly changing subject scale;
- shallow camera angle changes;
- short clips;
- clean source text at sufficient resolution;
- separate post-production overlays when perfect legibility is required.

### Glass, metal, jewelry, and mirrors

Reflections must change with viewpoint, but the source image contains incomplete information about the surrounding set. Use small, slow moves and describe reflection motion as supporting detail. Avoid large orbits around mirrored products without multiple references.

### Repeated patterns and architecture

Grids, windows, shelves, keyboards, fabric weave, and tile lines reveal temporal warping. Favor locked perspective, straight dolly, or small pan/tilt. Avoid roll and complex diagonal camera paths.

## Subject-Specific Guidance

### Portrait

Strong defaults:

- subtle breathing and eye movement;
- very slow push-in;
- small shoulder-level drift;
- hair or clothing response to a gentle breeze;
- soft focus transition toward the eyes.

Avoid large face rotation unless profile references exist. Keep expression change small and emotionally motivated.

### Full-body character

Require a readable path for walking or following shots. Check foot placement, ground contact, limb separation, and available space. When the pose is static and frontal, prefer camera movement or micro-action over inventing a complex walk cycle.

### Product

Choose the commercial goal:

- hero reveal;
- material inspection;
- feature reveal;
- scale or lifestyle context;
- packaging presentation;
- before/after transformation.

Use shallow arc, macro glide, pedestal, small truck, push-in, or focus transfer. Lock label, silhouette, and proportions. For a 360 deliverable, request multiple views or a 3D asset before generation.

### Landscape

Layered landscapes can support pan, small truck, drone-like push, or rising reveal. Let environment motion carry life: clouds, water, fog, foliage, dust, or light. Preserve horizon and avoid making every layer move at the same speed.

### Architecture and interior

Use perspective lines as rails. Straight dolly into corridors, slow tilt for height, small pedestal for product-like inspection, or locked wide observation. Protect vertical lines and room geometry. Avoid wide orbit in narrow spaces.

### Food and beverage

Use macro glide, push-in, rack focus, steam, bubbles, pour, melt, drip, or garnish motion. Keep camera travel shallow because shape, liquid physics, and texture already create motion complexity.

### Illustration, poster, or artwork

Decide whether the goal is:

- camera motion over a flat surface;
- 2.5D parallax from separated layers;
- animation inside the artwork;
- full volumetric reinterpretation.

Do not imply real 3D orbit unless the artwork has been prepared with depth layers or the user accepts reinterpretation.

## Movement Feasibility Matrix

| Source evidence | Safe | Conditional | Unsafe without more references |
| --- | --- | --- | --- |
| Flat headshot | zoom, push, focus, micro-drift | 5-15 degree arc | profile reveal, 180-360 orbit |
| Front product on seamless backdrop | push, macro glide, pedestal | 10-25 degree arc | full side/back reveal |
| Product with multiple visible planes | push, truck, small arc | 25-45 degree arc | 360 unless multiple views exist |
| Corridor with strong perspective | dolly-in, follow, tilt | small truck | orbit through walls |
| Layered landscape | pan, push, small truck | crane-like rise | rapid multi-axis flight |
| Tight crop touching edges | static, focus, micro-motion | tiny zoom-in | pull-out or large side move |
| Reflective jewelry close-up | macro glide, focus, small arc | controlled pedestal | wide orbit with changing set reflections |
| Graphic poster | pan, zoom, 2.5D parallax | local element animation | photoreal 3D camera orbit |

## Repairing an Unsuitable Source

When the requested shot exceeds the source:

1. **Widen the frame**: outpaint or regenerate with more margin.
2. **Create additional views**: front, three-quarter, side, and back for products or characters.
3. **Create a turnaround sheet**: keep lighting and scale consistent.
4. **Prepare layers**: separate foreground, subject, and background for 2.5D parallax.
5. **Repair artifacts**: hands, face, text, logo, product edges, reflections.
6. **Simplify the move**: convert orbit to arc, truck to pan, pull-out to static wide, or follow to subject-only motion.
7. **Use a reference video or explicit motion-control workflow** when matching a specific path matters more than free generation.

State the repair needed and why. Do not conceal source limitations behind more elaborate prompt language.
