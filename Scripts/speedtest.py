import speedtest

def test_internet_speed():
    st = speedtest.Speedtest()
    st.get_best_server()

    download_speed = st.download() / 1024 / 1024
    upload_speed = st.upload() / 1024 / 1024
    ping = st.results.ping

    return download_speed, upload_speed, ping

def main():
    download_speed, upload_speed, ping = test_internet_speed()

    print(f"Download Speed: {download_speed:.2f} Mbps")
    print(f"Upload Speed: {upload_speed:.2f} Mbps")
    print(f"Ping: {ping} ms")

if __name__ == "__main__":
    main()
