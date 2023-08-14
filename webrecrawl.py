import shutil, os
import web_utils, file_utils, graph_utils

urls_output_file = "output.json"
site = "0x4f.in"

if "://" not in site and  "http" not in site: site = "https://" + site

# delete previous output file if it exists
if os.path.isfile(os.getcwd() + urls_output_file): shutil.rmtree(urls_output_file)

try: 
    urls = web_utils.grab_urls(web_utils.get_page(site))
    print(f"{site}: Found {len(urls)} url(s).")
    file_utils.append_to_file(urls_output_file, site, urls)
            
    while 1:
        file_data = file_utils.read_from_file(urls_output_file)

        for key in file_data.keys():
            values = file_data[key]
            for value in values:
                urls = web_utils.grab_urls(web_utils.get_page(value))
                print(f"{value}: Found {len(urls)} url(s).")
                file_utils.append_to_file(urls_output_file, value, urls)
    
except KeyboardInterrupt:
    print ("Visualizing data...")
    data_to_visualize = file_utils.read_from_file(urls_output_file)
    graph_utils.render_graph(data_to_visualize)