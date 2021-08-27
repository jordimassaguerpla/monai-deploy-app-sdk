<p align="center">
<img src="https://raw.githubusercontent.com/Project-MONAI/MONAI/dev/docs/images/MONAI-logo-color.png" width="50%" alt='project-monai'>
</p>

# MONAI Deploy Application SDK

MONAI Deploy Application SDK offers a framework and associated tools to design, verify and analyze performance of AI-driven applications in healthcare domain.

## Features

> _The codebase is currently under active development._

- Pythonic Framework for app development
- A mechanism to locally run an app via App Runner
- A lightweight app analytics module
- A lightweight 2D/3D visualization module
- A development console
- A set of sample applications
- API documentation & User's Guide

## Installation

To install [the current release](https://pypi.org/project/monai-app-sdk/), you can simply run:

```bash
pip install monai-app-sdk  # NOTE: monai-app-sdk package is not available in PyPI for now.
```

## Getting Started

```bash
pip install monai-app-sdk  # NOTE: monai-app-sdk package is not available in PyPI for now.

# Clone monai-app-sdk repository for accessing examples.
git clone https://github.com/Project-MONAI/monai-app-sdk.git
cd monai-app-sdk

# Install necessary dependencies for simple_imaging_app
pip install scikit-image

# Execute the app locally
python examples/apps/simple_imaging_app/app.py -i examples/apps/simple_imaging_app/brain_mr_input.jpg -o output

# Package app (creating MAP docker image), using `-l DEBUG` option to see progress.
monai-deploy package examples/apps/simple_imaging_app -t simple_app:latest -l DEBUG

# Run the app with docker image and input file locally

# NOTES:
# For now, we need to make sure that the output folder is available, otherwise, it would cause a permission issue.
# - https://github.com/Project-MONAI/monai-app-sdk/issues/67
mkdir -p output

monai-deploy run simple_app:latest examples/apps/simple_imaging_app/brain_mr_input.jpg output
```

[MedNIST demo](TBD) is available on Colab.

[Examples](https://github.com/Project-MONAI/monai-app-sdk/tree/main/examples) and [notebook tutorials](https://github.com/Project-MONAI/monai-app-sdk/tree/main/notebooks) are located at [Project-MONAI/monai-app-sdk](https://github.com/Project-MONAI/monai-app-sdk).

Technical documentation is available at [docs.monai.io](https://docs.monai.io).

## Contributing

For local development, please execute the following command:

```bash
./run setup
```

This will set up the development environment, installing necessary packages.

For guidance on making a contribution to MONAI Deploy Application SDK, see the [contributing guidelines](CONTRIBUTING.md).

## Community

Join the conversation on Twitter [@ProjectMONAI](https://twitter.com/ProjectMONAI) or join our [Slack channel](https://forms.gle/QTxJq3hFictp31UM9).

## Links

- Website: <https://monai.io>
- API documentation: <https://docs.monai.io/projects/deploy>
- Code: <https://github.com/Project-MONAI/monai-app-sdk>
- Project tracker: <https://github.com/Project-MONAI/monai-app-sdk/projects>
- Issue tracker: <https://github.com/Project-MONAI/monai-app-sdk/issues>
- Wiki: <https://github.com/Project-MONAI/monai-app-sdk/wiki>
- Test status: <https://github.com/Project-MONAI/monai-app-sdk/actions>
- PyPI package: <https://pypi.org/project/monai-app-sdk>
<!-- - Docker Hub: <https://hub.docker.com/r/projectmonai/monai-app-sdk> -->
