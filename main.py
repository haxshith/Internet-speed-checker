import speedtest


def check_speed():
    st = speedtest.Speedtest()


    download_speed = st.download()


    upload_speed = st.upload()


    ping = st.results.ping


    download_speed_mbps = download_speed / (1024 * 1024)
    upload_speed_mbps = upload_speed / (1024 * 1024)

    print(f"Download Speed: {download_speed_mbps:.2f} Mbps")
    print(f"Upload Speed: {upload_speed_mbps:.2f} Mbps")
    print(f"Ping: {ping} ms")


if __name__ == "__main__":
    check_speed()
