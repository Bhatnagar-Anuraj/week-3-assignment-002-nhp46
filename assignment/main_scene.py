"""
DIGM 131 - Assignment 3: Function Library (main_scene.py)
==========================================================

OBJECTIVE:
    Use the functions you wrote in scene_functions.py to build a complete
    scene. This file demonstrates how importing and reusing functions makes
    scene creation clean and readable.

REQUIREMENTS:
    1. Import scene_functions (the module you completed).
    2. Call each of your 5+ functions at least once.
    3. Use place_in_circle with at least one of your create functions.
    4. The final scene should contain at least 15 objects total.
    5. Comment your code explaining what you are building.

GRADING CRITERIA:
    - [30%] All 5+ functions from scene_functions.py are called.
    - [25%] place_in_circle is used at least once.
    - [20%] Scene contains 15+ objects and looks intentional.
    - [15%] Code is well-commented.
    - [10%] Script runs without errors from top to bottom.
"""

import maya.cmds as cmds
import scene_functions as sf

# ---------------------------------------------------------------------------
# Scene Setup
# ---------------------------------------------------------------------------
cmds.file(new=True, force=True)

# Create a ground plane.
ground = cmds.polyPlane(name="ground", width=60, height=60,
                        subdivisionsX=1, subdivisionsY=1)[0]

# ---------------------------------------------------------------------------
# Scene Building
# ---------------------------------------------------------------------------

# -------------------------
# Create buildings (city area)
# -------------------------
# These are the main structures of the scene.
sf.create_building(width=6, height=10, depth=6, position=(-15, 0, 10))
sf.create_building(width=5, height=8, depth=5, position=(0, 0, 10))
sf.create_building(width=7, height=12, depth=6, position=(15, 0, 10))

# -------------------------
# Create trees (environment detail)
# -------------------------
# Scattered trees around the scene for natural environment feel.
sf.create_tree(position=(-20, 0, -5))
sf.create_tree(position=(-10, 0, -8))
sf.create_tree(position=(10, 0, -7))

# -------------------------
# Create fence (structure divider)
# -------------------------
# Fence separates part of the scene like a park boundary.
sf.create_fence(length=15, post_count=8, position=(-7, 0, 0))

# -------------------------
# Create lamp posts (lighting elements)
# -------------------------
# Adds street lighting to the environment.
sf.create_lamp_post(position=(5, 0, 0))
sf.create_lamp_post(position=(10, 0, 0))
sf.create_lamp_post(position=(15, 0, 0))

# -------------------------
# Circular tree arrangement (park area)
# -------------------------
# Uses place_in_circle to generate repeated objects automatically.
sf.place_in_circle(
    sf.create_tree,
    count=8,
    radius=12,
    center=(0, 0, -10),
    trunk_height=4,
    canopy_radius=2
)


# ---------------------------------------------------------------------------
# Final viewport framing (do not remove).
# ---------------------------------------------------------------------------
if __name__ == "__main__":
    cmds.viewFit(allObjects=True)
    print("Main scene built successfully!")
