<div align="center">
  <img src="assets/images/open-agent-banner.png" alt="AI-Builder" />
</div>

<div align="center">
    <h1>Open Agent</h1>
</div>

<div align="center">
  <!-- Build Status -->
  <a href="https://github.com/AttuneEngineering/open-agent/actions">
    <img src="https://github.com/AttuneEngineering/ai-builder/actions/workflows/main.yml/badge.svg" alt="Build Status" />
  </a>
  <!-- Code Size -->
  <a href="">
    <img src="https://img.shields.io/github/languages/code-size/attuneengineering/open-agent" alt="Code Size" />
  </a>
  <!-- Contributers -->
  <a href="https://github.com/attuneengineering/open-agent/graphs/contributors">
    <img src="https://img.shields.io/github/contributors/attuneengineering/open-agent.svg" alt="Contributers" />
  </a>
  <!-- GitHub Issues -->
  <a href="https://github.com/attuneengineering/open-agent/issues">
    <img src="https://img.shields.io/github/issues/attuneengineering/open-agent.svg" alt="GitHub Issues" />
  </a>
  <!-- Forks -->
  <a href="https://github.com/attuneengineering/open-agent/network/members">
    <img src="https://img.shields.io/github/forks/attuneengineering/open-agent.svg" alt="Forks" />
  </a>
  <!-- Followers -->
  <a href="https://github.com/attuneengineering?tab=followers" target="_blank">
    <img src="https://img.shields.io/github/followers/attuneengineering?style=social" alt="Follow on GitHub">
  </a>
  <!-- Stars -->
  <a href="https://github.com/attuneengineering/open-agent/stargazers" target="_blank">
    <img src="https://img.shields.io/github/stars/attuneengineering/open-agent?style=social" alt="GitHub stars">
  </a>
  <!-- Commit Activity -->
  <a href="https://github.com/attuneengineering/open-agent/commits" target="_blank">
    <img src="https://img.shields.io/github/commit-activity/m/attuneengineering/open-agent" alt="GitHub commits">
  </a>
  <!-- Last Commit -->
  <a href="https://github.com/attuneengineering/open-agent/commits" target="_blank">
    <img src="https://img.shields.io/github/last-commit/attuneengineering/open-agent" alt="GitHub last commit">
  </a>
  <!-- License -->
  <a href="https://www.gnu.org/licenses/gpl-3.0">
      <img src="https://img.shields.io/badge/license-GPL%20v3-blue.svg" alt="License" />
  </a>
</div>

<div align="center">
    <p>For support, either <a href="https://github.com/AttuneEngineering/open-agent/issues/new/choose"> add an issue</a> or reach out to <a href="mailto:contact@attuneengineering.com">contact@attuneengineering.com</a>.</p>
    <a href="https://www.youtube.com/channel/UCNMrLvZji3XeWghxsAWKXjg"><img src="https://img.shields.io/youtube/channel/subscribers/UCNMrLvZji3XeWghxsAWKXjg?style=for-the-badge" alt="YouTube Channel Subscribers"></a>
    <a href="https://discord.gg/sAbbvBNU"><img src="https://img.shields.io/discord/1199192124290257058.svg?style=for-the-badge&label=Join%20Community&color=7289DA" alt="Join Community Badge"/></a><br>
    <em>created and maintained by <a href="https://github.com/mrbende" target="_blank">Reed Bender</a></em></p>
    <a href="https://gitpod.io/#https://github.com/AttuneEngineering/open-agent" target="_blank"><img src="https://gitpod.io/button/open-in-gitpod.svg" alt="Open-in-Gitpod"></a>
</div>
</div>

>“I believe that at the end of the century the use of words and general educated opinion will have altered so much that one will be able to speak of machines thinking without expecting to be contradicted.”
>
>– Alan Turing

---

### Abstract

Function calling and agential decision making is a notoriously difficult task in natural language processing. How can we get an LLM to not only respond with factual information, but actually take proactive steps to solve problems or retrieve data before compiling a response. This `function calling` step is the missing link between AI being a useful search engine to becoming an agential player in _reality_.

`Open Agent` is a software architecture for creating these types of intelligent agents with `GPT-4`'s native API and a self-defined collection of tools. Using this native tool-formatting and function calling structure, we can then unplug OpenAI as the reasoning engine and provide substitute in our own self-hosted open source **fully open source** LLMs, fine-tuned specificially for performing function calling.

---

# Table of Contents
- [Building Your Environment](#building-your-environment)
- [Usage](#usage)
- [License](#license)

---
---

# Building Your Environment

### (a) Developing with Gitpod

Attune Engineering configures all of our repositories to work with [Gitpod](https://www.gitpod.io/docs/configure/workspaces), enabling you to deploy a preconfigured development environment to provisioned cloud resources. You are granted a free 50 hours of development per month, which is more than enough to get started.

<div align="center">
    <a href="https://gitpod.io/#https://github.com/AttuneEngineering/open-agent" target="_blank"><img src="https://gitpod.io/button/open-in-gitpod.svg" alt="Open-in-Gitpod"></a>
</div>

Once working in Gitpod, you can launch the Jupyter Lab environment with the following...
  ```bash
  launch-jupyter
  ```

---

### (b) Running Docker on your local machine

1. Install [Docker](https://docs.docker.com/get-docker/) on your machine if it is not already installed.

2. Clone the `Open Agent` repository to your local machine.
    ```bash
    git clone git@github.com:AttuneEngineering/open-agent.git
    cd open-agent
    ```

3. Build the Docker image yourself _OR_ pull the image from Attune Engineering.
    ```bash
    ### BUILD FROM SOURCE...
    export REGISTRY_IMAGE="YOUR_GITHUB_USERNAME/open-agent"
    docker build -f Dockerfile -t $REGISTRY_IMAGE:main .

    ### ...OR PULL FROM ATTUNE ENGINEERING
    export REGISTRY_IMAGE="ghcr.io/attuneengineering/open-agent"
    docker pull $REGISTRY_IMAGE:main
    ```

4. Run the Docker container.
    ```bash
    docker run -it --rm -p 8888:8888 $REGISTRY_IMAGE:main
    ```
    By default, this container will open an interactive bash environment. If you'd rather work in Jupyter, the following flag can be appended...
      * `--launch-jupyter`; launch a Jupyter Lab server on port 8888.

5. _optional_ Push the Docker image to your own Github Container Registry.
    This will require you to have a personal access token with `read:packages` and `write:packages` permissions. You can create a token [here](https://github.com/settings/tokens). Note that you'll also need to either fork the `AI Builder` repository or create a new repository in your own account.
    ```bash
    export GITHUB_TOKEN="xxx" 
    export REGISTRY_IMAGE="ghcr.io/YOUR_GITHUB_USERNAME/open-agent"
    docker build -f Dockerfile -t $REGISTRY_IMAGE:main .
    echo $GITHUB_TOKEN | docker login ghcr.io -u YOUR_GITHUB_USERNAME --password-stdin
    docker push $REGISTRY_IMAGE:main
    ```
    _note_... Your `GITHUB_TOKEN` is already managed by the Github actions we are triggering with `.github/workflows/main.yml`, so it does not need to be added in addition.

    Additionally, this process can be automated with Github Actions. In order for the Github Workflows to successfully build the image and push it to your Github Container Registry, you must add the following to your `Repository Settings` --> `Secrets and Variables` --> `Actions` --> `Repository Secrets`...
    ```
    REGISTRY_IMAGE="ghcr.io/YOUR_GITHUB_USERNAME/ai-builder"
    ```

---

### (c) Building the environment locally

This is not ideal, as all of the source code is organized relative to the container's home directory within (`/workspace/open-agent/src`). If you're simply looking to adapt the code to your own purposes, however, you can simply install the necessary requirements and update your environment's `PYTHONPATH` to point to your local `src` directory.
  ```bash
  pip install -r requirements.txt
  ```
    
---
---

# Usage 

### Setting API Keys 

> [!IMPORTANT]
> You must make the following API keys available as environment variables. This can be done by creating a `.env` file with the following keys, or otherwise by adding them to your environment.
  ```bash
  OPENAI_API_KEY="xxx"
  ```

This is all that is required to then instantiate the `OpenAgent` class, as defined in `src/my_agent.py`

### Building in Jupyter Lab

  ```bash
  ### IN GITPOD
  launch-jupyter

  ### LOCALLY BUILT IMAGE
  source /workspace/open-agent/bin/jupyter-lab.sh
  ```
Check out `dev.ipynb` to get started. To see further documentation about the Python source code contained within the instantiated `OpenAgent` class, see `src/README.md`.

---
---

# License

This project is licensed under the terms of the [GNU General Public License](https://github.com/AttuneEngineering/ai-builder/blob/main/LICENSE). This license is designed to ensure that software remains free and open, allowing users to run, study, share, and modify the software while allowing provisions for source-code that is sold for a fee. The license is clear that the definition of _**free**_ is free to use once accessed, not explicitly free to access.

This means that once you have purchased any code from Attune Engineering, you are free to do with it as you wish - be it share or modify. The stipulation to this, however, is that all forthcoming versions of the software must also be made available as complete source code with an accompyaning GPL license for all downstream applications. The aim of this license is not to prohibit the sale of derivative works, but rather to ensure free and open access to the source code provided under the _GPL-3_ license.

The rights granted to you as a purchaser of Attune Engineering's gated source code (or that which has been made available as open source) are as follows:

- **Freedom to Run**: The license grants users the freedom to run the program for any purpose.
- **Freedom to Modify**: Users can modify the software or any portion of it, thus allowing for the creation of derivatives that must also be licensed under GPL-3.
- **Freedom to Distribute**: Users can distribute copies of the original software to others, with or without modifications, under the same GPL-3 license terms - _See Discord for community stipulations_.
- **Source Code**: The license requires that all distributed software, including modifications and derived works, must be made available in source code form.
- **Patent Rights**: GPL-3 includes an express grant of patent rights from contributors to users, protecting users from patent litigation.
- **Tivoization**: GPL-3 addresses "Tivoization", ensuring that if the software is used in consumer products, users can still modify the software on those devices.
- **Compatibility with Other Licenses**: GPL-3 provides certain provisions for combining or linking with code under certain other licenses.

### Author's Note:

Attune Engineering is committed to distributing and supporting free and open source software development. If we envision a future where both the LLMs and the accompanying software architectures are democratized and open source, it's best to start building that vision now.

> "Popularity is tempting, and it is easy for a library developer to rationalize the idea that boosting the popularity of that one library is what the community needs above all...
>
> But we should not listen to these temptations, because we can achieve much more if we stand together. We free software developers should support one another. By releasing libraries that are limited to free software only, we can help each other's free software packages outdo the proprietary counterparts. The whole free software movement will have more popularity, because free software as a whole will stack up better against the competition."
- _[Why you shouldn't use the Lesser GPL for your next library](https://www.gnu.org/licenses/why-not-lgpl.html)_

>Software is like sex: it’s better when it’s free. 
>~ Linus Torvalds

Happy Hacking!

---
---