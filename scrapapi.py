import http.client

conn = http.client.HTTPSConnection("api.webscrapingapi.com")

conn.request("POST", "/v1?api_key=s5gROMlF1KrGj8UkQG5zFpK7gL96lKTr&device=desktop&proxy_type=datacenter&url=https%3A%2F%2Fwww.amazon.in%2Fdp%2FB01AL1B3HG%2Fref%3Ds9_acsd_al_bw_c2_x_0_i%3Fpf_rd_m%3DA1K21FY43GMZF8%26pf_rd_s%3Dmerchandised-search-5%26pf_rd_r%3DYS2T34WYQD14HPB93Z2J%26pf_rd_t%3D101%26pf_rd_p%3Db02f3a56-5f4b-468b-9099-f61590c61cb8%26pf_rd_i%3D1380442031")

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))