#malware detecte pattrun
pattern = []
#pattern.append(".*?wget.+?(https?[\/\w\:\.\-\%]+?)([\"\s\;\%\`\)\<\+]|\.\.)")
pattern.append(".*?wget.+?(https?[\/\w\:\.\-\%]+?)([^\/\w\:\.\-\%]|\.\.)")
pattern.append(".*?wget[\s\+]+([[\/\w\.\-\:\%^(\-g)]{6,}?)([^\/\w\:\.\-\%]|\.\.)")
pattern.append(".*?curl.+?(https?[\/\w\:\.\-\%]+?)([^\/\w\:\.\-\%]|\.\.)")
pattern.append(".*?fetch.+?(https?[\/\w/:\.\-\%]+?)([^\/\w\:\.\-\%]|\.\.)")
pattern.append(".*?java.net.URL.+?(https?[\/\w\:\.\-\%]+?)([^\/\w\:\.\-\%]]|\.\.)")
pattern.append(".*?urlopen.+?(https?[\/\w/:\.\-\%]+?)([^\/\w\:\.\-\%]|\.\.)")
pattern.append(".*?powershell.+?(https?[\/\w/:\.\-\%]+?)([^\/\w\:\.\-\%]|\.\.)")
pattern.append(".*?bitsadmin.+?(https?[\/\w/:\.\-\%]+?)([^\/\w\:\.\-\%]|\.\.)")
pattern.append(".*?explorer.+?(https?[\/\w\:\.\-\%]+?)([^\/\w\:\.\-\%]|\.\.)")
pattern.append(".*?certutil.+?(https?[\/\w/:\.\-\%]+?)([^\/\w\:\.\-\%]|\.\.)")
pattern.append(".*?Wscript.+?(https?[\/\w/:\.\-\%]+?)([^\/\w\:\.\-\%]|\.\.)")
pattern.append(".*?getstore.+?(https?[\/\w/:\.\-\%]+?)([^\/\w\:\.\-\%]|\.\.)")
pattern.append(".*?DownloadFile.+?(https?[\/\w/:\.\-\%]+?)([^\/\w\:\.\-\%]|\.\.)")
pattern.append(".*?address\=(https?[\/\w\:\.\-\%]+?)([^\/\w\:\.\-\%]|\.\.)")
pattern.append(".*?HTTP.start.+(https?[\/\w\:\.\-\%]+?)([^\/\w\:\.\-\%]|\.\.)")
pattern.append(".*?mshta.start.+(https?[\/\w/:\.\-\%]+?)([^\/\w\:\.\-\%]|\.\.)")
pattern.append(".*?lwp\-download.+(https?[\/\w/:\.\-\%]+?)([^\/\w\:\.\-\%]|\.\.)")
pattern.append(".*?(ftps?://[\w/:\.\-]+?)([\"\s\;\%\`\<\)]|\.\.)")
