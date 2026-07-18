# Task: Make artifact.html the Universal Detail Viewer for data.js

## Checklist
- [x] Fix TYPE_CONFIG in artifact.html to match UNESCO genres (instrumental, singings, belief, festival, craft)
- [x] Remove 3D model viewer code from artifact.html (hero button, model-section, modal wiring)
- [x] Augment data.js with derived fields: `type` (from genre), `quote` (from desc_vi), empty `script` object
- [x] Update VNMT.js: change province-modal row clicks to navigate to `artifact.html?id=` instead of inline modal
- [x] Update database.html: change table row clicks to navigate to `artifact.html?id=` instead of VNMT.html filter
- [x] All implementation complete - artifact.html now works as universal detail viewer for data.js