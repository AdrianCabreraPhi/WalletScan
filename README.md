# WALLET SCAN
*Software tool to analyze your crypto wallet. Available in 9 chains*

## Instructions
1. Get api key from https://goldrush.dev/
2. Use name GOLD_RUSH_API_KEY

## Install & Run
### 1. Docker
  ```bash
 docker run -e GOLD_RUSH_API_KEY='your_api_key' -p 8501:8501 acabrera809/walletscan
  ```
### 2. Run locally
  1. Create conda environment
  ```bash
  conda env create -f environment.yml
  ```
   2. Activate conda environment
   ```bash
   conda activate walletscan
   ```
   3. Execute app
   ```bash
   streamlit run main.py
   ```

<img width="1919" height="997" alt="wallet_scan2" src="https://github.com/user-attachments/assets/89835032-878b-4952-ad14-0a1f7db10f8a" />

<img width="1919" height="992" alt="wallet_scan3" src="https://github.com/user-attachments/assets/7a27be05-05a8-43db-b388-af8ae3edd4ef" />


## About Software
- *Software was developed with python and streamlit to generate a GUI*
- *This software was developed for educational purposes only.*
