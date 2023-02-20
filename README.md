# DroneFormer
Building domain-specific automated systems in the real world is painstaking, requiring massive codebases for exception handling and robust testing of behavior for all kinds of contingencies — automated packaging, drone delivery, home surveillance, and search and rescue are all enormously complex tasks and result in highly specialized industries and products that take thousands of engineering hours to prototype.

But it doesn’t have to be this way! Large language models have made groundbreaking strides towards helping out with the similarly tedious task of writing, thus giving novelists, marketing agents, and researchers alike a tool to iterate quickly and produce high-quality writing exhibiting both semantic precision and masterful high-level planning.

Let’s bring this paradigm into the real world. What if asking “find the child in the blue shirt and lead them to the dinner table” was all it took to create that domain-specific application?

Taking the first steps towards generally intelligent embodied AI, DroneFormer turns high-level natural language commands into long scripts of low-level drone control code leveraging advances in language and visual modeling. The interface is the simplest imaginable (using natural language alone), yet the applications and end result can adapt to the most complex real-world tasks.


# What can DroneFormer do?
DroneFormer is a no-code framework that enables one to program a drone via generative AI and Large Language Models. You can easily control your drone with simple written high-level instructions in natural English. Simply type up the command you want and the drone will execute it — flying in spirals, exploring caves to locate lost people with depth-first search, or even capturing stunning aerial footage to map out terrain. The drone receives a natural language instruction from the user (e.g. "find my keys") and explores the room until it finds the object.


# Implementation Details
Our prototype compiles natural language instructions down into atomic actions for DJI Tello via in-context learning using the OpenAI GPT-3 API. These actions include primitive actions from the DJITelloPy SDK (e.g. forward, back, clockwise turn) as well as custom object detection and visual language model query actions we built leveraging zero-shot image and multimodal models such as YOLOv5 and image processing frameworks such as OpenCV. We include a demo for searching for and locating objects using the onboard Tello camera and object detection. DroneFormer successfully generates complex 20+ line instructions to detect and navigate to arbitrary objects given a simple natural language instruction to do so (e.g. “explore, find the bottle, and land next to it”).

At a high level, a natural language command is combined with a series of actions that the drone is allowed to take and sent to a Large Language Model. The Large Language Model returns a series of actions in the language of the SDK that the drone is compatible with, and these commands are sent to the Drone over a Wi-Fi network. After the command sequence begins, the drone uses onboard sensors to first conduct a brief survey of the environment, identifying the object or task of interest (if none of these are detected, the drone enters an abort mode and lands safely). After the exploration phase is complete, the drone enters an exploitation phase, in which the task specified by the natural language command is executed, after which the drone is commanded to land.


# Challenges
One significant challenge was deciding on a ML model that best fit our needs of performant real-time object detection. We experimented with state-of-the-art models such as BLIP and GLIP which either were too slow at inference time, or were not performing as expected in terms of accuracy. Ultimately, we settled on YOLOv5 as having a good balance between latency and ability to collect knowledge about an image. We were also limited by the lack of powerful onboard compute, which meant the drone needs to connect to an external laptop (which needed to serve both the drone and internet networks, which we resolved using Ethernet and wireless at the same time) which in turn connects to the internet for OpenAI API inference.

Furthermore, embodied ML is a completely different beast than even a simulated reinforcement learning environment, and working with noisy control systems adds many sources of error on top of long-term language planning. To deal with this, we iterated much more frequently and added functionality to deal with new corner cases and ambiguity as necessary over the course of the project, rewriting as necessary. Additionally, connectivity issues arose often due to the three-tiered nature of the system between the drone, laptop, and cloud backends.

# Future Work
We were primarily constrained by the short battery life of the Tello drone, as well as a limited indoor environment (Stanford Engineering School) to test the Drone in. Expanding to larger and more complex hardware, environments, and tasks, we expect the DroneFormer framework to handily adapt, given a bit of prompt engineering, to emergent sophisticated behaviors such as:

- Watching over a child wandering around the house and reporting any unexpected behavior according to a fine-tuned classifier
- Finding that red jacket that you could swear was on the hanger but which has suddenly disappeared
- Checking in “person” if the small coffee shop down the street is still open despite the out-of-date Google Maps schedule
- Sending you a picture of the grocery list you forgot at home

We intend to replace YOLOv5 with more sophisticated VQA (Visual Question-Answering) models as they become more mainstream; these models will give us the abilities to apply natural language queries directly upon images themselves, and have the model draw bounding boxes for areas of interest as opposed to using YOLOv5 for the same task. VQA will allow for more dynamic operational modes and enable the drone to be more robust - adjusting its action sequence based on its observations of the environment on the fly. 

OpenAI Whisper will be implemented to decode live audio into natural language prompts, thus enabling voice commands and computer-free operation. Additionally, DroneFormer will be modified and tested on larger drones with longer battery life and the ability to hold more sensors (such that autonomous operations will not rely on visual data alone). 

DroneFormer will be a new type of personal assistant — one that always has your back and can bring the magic of complex language model planning to the embodied real world.

