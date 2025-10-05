# Project Overview: Beyond Gardens

[cite_start]Welcome to the **Beyond Gardens** project, created for the 2025 NASA Space Apps Challenge[cite: 2].

[cite_start]Beyond Gardens is an ambitious expansion for Minecraft that completely transforms the game's agriculture into an immersive and educational simulation experience[cite: 9]. [cite_start]With this modification, we forget about just planting and waiting; here, each seed is the beginning of a new scientific challenge[cite: 9]. [cite_start]This add-on will allow players to explore and master realistic agricultural scenarios, where the success of their crops depends directly on environmental factors based on real data provided by NASA[cite: 9].

You can find the demo and the full project at the following links:
* [cite_start]**Project Demonstration:** 🚧 [cite: 6, 7]
* [cite_start]**Project:** 🚧 [cite: 6, 7]


### Project Goals:

* [cite_start]To design a Minecraft Bedrock add-on that converts open NASA data (soil moisture, precipitation, vegetation vigor, surface temperature) into playable agricultural missions[cite: 5].
* [cite_start]To democratize data literacy in a familiar environment (Minecraft) and accelerate practical learning[cite: 5].
* [cite_start]To promote evidence-based sustainable agricultural practices[cite: 5].
* [cite_start]To offer a layer of strategic and challenging gameplay for veteran Minecraft players[cite: 9].
* [cite_start]To serve as a powerful scientific outreach tool capable of being used in advanced educational settings[cite: 9].

### How does it work?

[cite_start]The core of Beyond Gardens is its dynamic simulation engine, which integrates real-world information to control crucial in-game variables[cite: 9]:

* [cite_start]**Dynamic Climate:** Experience realistic weather patterns[cite: 9]. [cite_start]Unexpected rains, droughts, or frosts will follow models based on historical and current climate data from specific regions of the Earth[cite: 9].
* [cite_start]**Living Soils:** The add-on introduces different soil types, such as Mollisols or Chernozem, each with its own properties for nutrients, drainage, and pH, based on NASA data[cite: 9].
* [cite_start]**Realistic Temperature:** The temperature will fluctuate according to the biome and climate, directly affecting the growth rate and survival of your plants[cite: 9].
* [cite_start]**Plant Quality of Life:** Plants will have complex needs that depend on a perfect balance of water, sunlight, soil nutrients, and the right temperature[cite: 9].
* [cite_start]**Pests:** When planting, crops will be threatened by a pest that you must combat[cite: 9]. [cite_start]At the end of each season, players will have to face various creatures that will endanger their entire garden[cite: 9].

### Tools and Technologies Used

* **Software:**
    * [cite_start]**Bridge .:** An IDE created specifically to facilitate the creation of add-ons and custom content for Minecraft: Bedrock Edition, where we can edit using the JSON format[cite: 9].
    * [cite_start]**Blockbench:** A 3D modeling program whose main function is to allow users to design, texture, and animate 3D models in a low-poly style, which fits perfectly with Minecraft's cubic aesthetic[cite: 9].
    * [cite_start]**Visual Studio Code:** A free and open-source source code editor[cite: 9].
* **Languages:**
    * [cite_start]**Python:** Used to extract necessary information from the datasheets[cite: 9].
    * [cite_start]**JavaScript:** Used for programming the entities and behaviors added to the add-on[cite: 9].

### NASA Data and Resources

[cite_start]We extracted the following datasheets from NASA EARTHDATA with the goal of using the obtained parameters to simulate the climatic conditions in our project[cite: 13].

* [cite_start][https://search.earthdata.nasa.gov/search/granules?p=C2723754864-GES_DISC&pg[0][v]=f&pg[0][gsk]=-start_date&q=GPM_3IMERGDF&tl=1321626333.007!5](https://search.earthdata.nasa.gov/search/granules?p=C2723754864-GES_DISC&pg[0][v]=f&pg[0][gsk]=-start_date&q=GPM_3IMERGDF&tl=1321626333.007!5) [cite: 13]
* [cite_start][https://search.earthdata.nasa.gov/search/granules?p=C2927902887-POCLOUD&pg[0][v]=f&pg[0][gsk]=-start_date&q=CYGNSS_L3_SOIL_MOISTURE_V3.2&tl=1646360790.476!4](https://search.earthdata.nasa.gov/search/granules?p=C2927902887-POCLOUD&pg[0][v]=f&pg[0][gsk]=-start_date&q=CYGNSS_L3_SOIL_MOISTURE_V3.2&tl=1646360790.476!4) [cite: 13]
* [cite_start][https://search.earthdata.nasa.gov/search/granules?p=C2565788897-LPCLOUD&pg[0][v]=f&pg[0][gsk]=-start_date&q=MOD11C3_061&tl=1354501677.001!5](https://search.earthdata.nasa.gov/search/granules?p=C2565788897-LPCLOUD&pg[0][v]=f&pg[0][gsk]=-start_date&q=MOD11C3_061&tl=1354501677.001!5) [cite: 13]
* [cite_start][https://search.earthdata.nasa.gov/search/granules?p=C3543139481-LPCLOUD&pg[0][v]=f&pg[0][gsk]=-start_date&q=CAM5K30EM_003&tl=1327968000!5](https://search.earthdata.nasa.gov/search/granules?p=C3543139481-LPCLOUD&pg[0][v]=f&pg[0][gsk]=-start_date&q=CAM5K30EM_003&tl=1327968000!5) [cite: 13]
