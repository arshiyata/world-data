####################### project ############################
import re 
import requests 
import os
from datetime import date 
#-------------------------------------------------------
base_url = 'https://www.worlddata.info/'

asia =['armenia','azerbaijan','bahrain','cyprus','georgia','iraq','israel','jordan','kuwait','lebanon','oman','palestine','qatar','saudi-arabia','syria','turkey','arab-emirates'
,'yemen','kazakhstan','kyrgyzstan','tajikistan','turkmenistan','uzbekistan','afghanistan'
,'bangladesh','bhutan','india','iran','maldives','nepal','pakistan','sri-lanka','brunei','cambodia','east-timor','indonesia','laos','malaysia'
,'burma','philippines','singapore','thailand','vietnam','china','hong-kong','japan','macao','mongolia','north-korea','south-korea','taiwan']

africa = ['algeria','egypt','libya','morocco','south-sudan','sudan','tunisia','western-sahara','botswana','eswatini'
,'lesotho','namibia','south-africa','benin','burkina-faso','cape-verde','gambia','ghana','guinea','guinea-bissau','ivory-coast','liberia','mali'
,'mauritania','niger','nigeria','saint-helena','senegal','sierra-leone','togo','british-indian-ocean-territory','burundi','comoros'
,'djibouti','eritrea','ethiopia','kenya','madagascar','malawi','mauritius','mayotte','mozambique','reunion','rwanda','seychelles','somalia','tanzania'
,'uganda','zambia','zimbabwe','angola','cameroon','central-african-republic','chad','congo-kinshasa','equatorial-guinea','gabon'
,'congo-brazzaville','sao-tome-and-principe']

america = ['bermuda','america','greenland','mexico','stpierre-miquelon','belize','costa-rica','el-salvador','guatemala','honduras','nicaragua','panama','argentina','bolivia'
,'bouvet-island','brazil','chile','colombia','ecuador','falkland-islands','french-guiana','guyana','paraguay','peru','southgeorgia-sandwichislands','suriname','uruguay','venezuela',
'anguilla','antigua-barbuda','aruba','bahamas','barbados','british-virgin-islands','caribbean-netherlands','cayman-islands','cuba','curacao','dominica','dominican-republic','grenada',
'guadeloupe','haiti','jamaica','martinique','montserrat','puerto-rico','saint-barthelemy','stkitts-nevis','saint-lucia','saint-martin','stvincent-grenadines','sint-maarten','trinidad-and-tobago',
'turks-and-caicos-islands','virgin-islands']

europe = ['austria','belgium','france','germany','liechtenstein','luxembourg','netherlands','monaco','switzerland','belarus','bulgaria','czechia',
'hungary','moldova','poland','romania','russia','slovakia','ukraine','aland','denmark','estonia','faroe-islands','finland','guernsey','iceland','ireland',
'isle-of-man','jersey','latvia','lithuania','norway','svalbard','sweden','united-kingdom','albania','andorra','bosnia-and-herzegovina','croatia','gibraltar','greece',
'italy','kosovo','malta','montenegro','northmacedonia','portugal','san-marino','serbia','slovenia','spain','vatican']

oceania =['australia','christmas-island','cocos-islandscocos-islands','heard-and-mcdonald-islan','norfolk-island','american-samoa','cook-islands'
,'french-polynesia','niue','pitcairn-islands','samoa','tokelau','tonga','tuvalu','wallis-and-futuna','fiji','new-caledonia','papua-new-guinea','solomon-islands',
'vanuatu','micronesia','guam','kiribati','marshall-islands','nauru','northern-marianas','palau','us-minor-outlying-islands']


continent = [africa,asia,america,europe,oceania]
continent_str = ["africa","asia","america","europe","oceania"]

dateT=str(date.today())
os.mkdir(r"D:\project_data"+dateT)

for i in range(len(continent)):
            os.mkdir(r"D:\project_data"+dateT+"\\"+continent_str[i])
            for j in continent[i]:
                try:
                    final_url=base_url+continent_str[i]+"/"+j+"/index.php"
                    response=requests.get(final_url)
                    str_data=response.text
                except:
                    final_url=base_url+continent_str[i]+"/"+j+"/index.php"
                    response=requests.get(final_url)
                    str_data=response.text
                finally:
                    final_url=base_url+continent_str[i]+"/"+j+"/index.php"
                    response=requests.get(final_url)
                    str_data=response.text

                os.mkdir(r"D:\project_data"+dateT+"\\"+continent_str[i]+r"\\"+j) 
                #  Population 

                result = re.findall(r"Population:</a>\S{1,}</div>",str_data)
                for item in result :
                    clear_data= re.sub(r'</a>',' ',item)
                    clear_data= re.sub(r'</div>','',clear_data)
                    text=open(r"D:\project_data"+dateT+"\\"+continent_str[i]+r"\\"+j+r"\\"+"Population"+".txt","a+")
                    text.write(clear_data+"\n")
                    text.close()
                    print(clear_data)

                result = re.findall(r"Population per km²:</a>\S{1,}</div><div>",str_data)    
                for item in result :
                    clear_data= re.sub(r'</a>',' ',item)
                    clear_data= re.sub(r'</div>','',clear_data)
                    clear_data= re.sub(r'<div>','',clear_data)
                    text=open(r"D:\project_data"+dateT+"\\"+continent_str[i]+r"\\"+j+r"\\"+"Population"+".txt","a+")
                    text.write(clear_data+"\n")
                    text.close()
                    print(clear_data)

                result = re.findall(r"Life expectancy males:</a>\S{,} \S{,} \w{,}</div><div>",str_data)   
                for item in result :
                    clear_data= re.sub(r'</a>',' ',item)
                    clear_data= re.sub(r'</div>','',clear_data)
                    clear_data= re.sub(r'<div>','',clear_data)
                    clear_data= re.sub(r'&#216;','Ø',clear_data)
                    text=open(r"D:\project_data"+dateT+"\\"+continent_str[i]+r"\\"+j+r"\\"+"Population"+".txt","a+")
                    text.write(clear_data+"\n")
                    text.close()
                    print(clear_data)
                
                result = re.findall(r"Life expectancy females:</div>\S{,} \S{,} \w{,}</div><div>",str_data)
                for item in result :
                    clear_data= re.sub(r'</div>','',item)
                    clear_data= re.sub(r'<div>','',clear_data)
                    clear_data= re.sub(r'&#216;','Ø',clear_data)
                    text=open(r"D:\project_data"+dateT+"\\"+continent_str[i]+r"\\"+j+r"\\"+"Population"+".txt","a+")
                    text.write(clear_data+"\n")
                    text.close()
                    print(clear_data)
                
                result = re.findall(r"Birth rate:</div>\S{1,5} \S{1,1}</div><div><div>",str_data)
                for item in result :
                    clear_data= re.sub(r'</div>',' ',item)
                    clear_data= re.sub(r'<div>','',clear_data)
                    text=open(r"D:\project_data"+dateT+"\\"+continent_str[i]+r"\\"+j+r"\\"+"Population"+".txt","a+")
                    text.write(clear_data+"\n")
                    text.close()
                    print(clear_data)

                result = re.findall(r"Death rate:</div>\S{1,5} \S{1,1}</div><div><div>",str_data)
                for item in result :
                    clear_data= re.sub(r'</div>',' ',item)
                    clear_data= re.sub(r'<div>','',clear_data)
                    text=open(r"D:\project_data"+dateT+"\\"+continent_str[i]+r"\\"+j+r"\\"+"Population"+".txt","a+")
                    text.write(clear_data+"\n")
                    text.close()
                    print(clear_data)

                result = re.findall(r"Males/Females:</div>\S{1,} : \S{1,}</div></div></div>",str_data)
                for item in result :
                    clear_data= re.sub(r'</div>',' ',item)
                    clear_data= re.sub(r'<div>','',clear_data)
                    text=open(r"D:\project_data"+dateT+"\\"+continent_str[i]+r"\\"+j+r"\\"+"Population"+".txt","a+")
                    text.write(clear_data+"\n")
                    text.close()
                    print(clear_data)

                # Languages

                result_1 = re.findall(r"\w{1,}</a></td><td>\d{1,}.\d{1,} %",str_data) 
                result_2 = re.findall(r"\w{1,}</td><td>\d{1,}.\d{1,} %",str_data)
                result = result_1 + result_2
                for item in result :
                    clear_data= re.sub(r'</a>',' ',item)
                    clear_data= re.sub(r'</td>',' ',clear_data)
                    clear_data= re.sub(r'<td>',': ',clear_data)
                    clear_data= re.sub(r'ā','a',clear_data)
                    text=open(r"D:\project_data"+dateT+"\\"+continent_str[i]+r"\\"+j+r"\\"+"Languages"+".txt","a+")
                    text.write(clear_data+"\n")
                    text.close()
                    print(clear_data)

                # Religions

                result_3 = re.findall(r'<tr><td>\D{1,}</td><td>\d{1,}.\d{1,}%</td></tr>' , str_data)
                for item in result_3 :
                    clear_data = re.sub(r"</td>" , "" ,item)
                    clear_data = re.sub(r"<td>" , "" ,clear_data)
                    clear_data = re.sub(r"</tr>" , "" ,clear_data)
                    clear_data = re.sub(r"<tr>" , "" ,clear_data)
                    text=open(r"D:\project_data"+dateT+"\\"+continent_str[i]+r"\\"+j+r"\\"+"Religions"+".txt","a+")
                    text.write(clear_data+"\n")
                    text.close()
                    print(clear_data)
                
                # Economy

                result_4=re.findall(r"GDP:</td><td>\S{1,} \w{,2}",str_data)
                for item in result_4 :
                    clear_data = re.sub(r"</td>" , "" ,item)
                    clear_data = re.sub(r"<td>" , " " ,clear_data)
                    text=open(r"D:\project_data"+dateT+"\\"+continent_str[i]+r"\\"+j+r"\\"+"Economy"+".txt","a+")
                    text.write(clear_data+" $"+"\n")
                    text.close()
                    print(clear_data +" $")

                result_5=re.findall(r"Exportations:</td><td>\S{1,} \w{,2}",str_data)
                for item in result_5 :
                    clear_data = re.sub(r"</td>" , "" ,item)
                    clear_data = re.sub(r"<td>" , " " ,clear_data)
                    text=open(r"D:\project_data"+dateT+"\\"+continent_str[i]+r"\\"+j+r"\\"+"Economy"+".txt","a+")
                    text.write(clear_data+" $"+"\n")
                    text.close()
                    print(clear_data +" $")

                result_6=re.findall(r"Importations:</td><td>\S{1,} \w{,2}",str_data)
                for item in result_6 :
                    clear_data = re.sub(r"</td>" , "" ,item)
                    clear_data = re.sub(r"<td>" , " " ,clear_data)
                    text=open(r"D:\project_data"+dateT+"\\"+continent_str[i]+r"\\"+j+r"\\"+"Economy"+".txt","a+")
                    text.write(clear_data+" $"+"\n")
                    text.close()
                    print(clear_data +" $")
                
                result_7=re.findall(r"Tourism receipts\S{,}:</td><td>\S{1,} \w{,2}",str_data)
                for item in result_7 :
                    clear_data = re.sub(r"</td>" , "" ,item)
                    clear_data = re.sub(r"<td>" , " " ,clear_data)
                    clear_data = re.sub(r"</a>" , "" ,clear_data)
                    text=open(r"D:\project_data"+dateT+"\\"+continent_str[i]+r"\\"+j+r"\\"+"Economy"+".txt","a+")
                    text.write(clear_data+" $"+"\n")
                    text.close()
                    print(clear_data +" $")
                
                result_8=re.findall(r"Debt rate\S{,}:</td><td>\S{1,}",str_data)
                for item in result_8 :
                    clear_data = re.sub(r"</td>" , "" ,item)
                    clear_data = re.sub(r"<td>" , " " ,clear_data)
                    clear_data = re.sub(r"</a>" , "" ,clear_data)
                    text=open(r"D:\project_data"+dateT+"\\"+continent_str[i]+r"\\"+j+r"\\"+"Economy"+".txt","a+")
                    text.write(clear_data+" %"+"\n")
                    text.close()
                    print(clear_data+" %")
                
                result_9=re.findall(r"Unemployment rate\S{,}:</td><td>\S{1,}",str_data)
                for item in result_9 :
                    clear_data = re.sub(r"</td>" , "" ,item)
                    clear_data = re.sub(r"<td>" , " " ,clear_data)
                    clear_data = re.sub(r"</a>" , "" ,clear_data)
                    text=open(r"D:\project_data"+dateT+"\\"+continent_str[i]+r"\\"+j+r"\\"+"Economy"+".txt","a+")
                    text.write(clear_data+" %"+"\n")
                    text.close()
                    print(clear_data+" %")
                    
                result_10=re.findall(r"Inflation rate\S{,}:</td><td>\S{1,}",str_data)
                for item in result_10 :
                    clear_data = re.sub(r"</td>" , "" ,item)
                    clear_data = re.sub(r"<td>" , " " ,clear_data)
                    clear_data = re.sub(r"</a>" , "" ,clear_data)
                    text=open(r"D:\project_data"+dateT+"\\"+continent_str[i]+r"\\"+j+r"\\"+"Economy"+".txt","a+")
                    text.write(clear_data+"\n")
                    text.close()
                    print(clear_data)
                
                result_11=re.findall(r"Corruption index\S{,}:</td><td>\S{1,} \S{1,}",str_data)
                if result_11 !=[]:
                    for item in result_11 :
                        clear_data = re.sub(r"<td>›" , "" ,item)
                        clear_data = re.sub(r"<td>" , " " ,clear_data)
                        clear_data = re.sub(r"</td>" , "" ,clear_data)
                        clear_data = re.sub(r"</tr>" , "" ,clear_data)
                        clear_data = re.sub(r"<tr>" , "" ,clear_data)
                        clear_data = re.sub(r"</a>" , "" ,clear_data)
                        text=open(r"D:\project_data"+dateT+"\\"+continent_str[i]+r"\\"+j+r"\\"+"Economy"+".txt","a+")
                        text.write(clear_data+"\n")
                        text.close()
                        print(clear_data)
                
                result_10=re.findall(r"Energy consumption\S{,}:</td><td>\S{1,} \D{1,7}",str_data)
                for item in result_10 :
                    clear_data = re.sub(r"</td>" , "" ,item)
                    clear_data = re.sub(r"<td>" , " " ,clear_data)
                    clear_data = re.sub(r"</a>" , "" ,clear_data)
                    clear_data = re.sub(r"<" , "" ,clear_data)
                    clear_data = re.sub(r"/" , "" ,clear_data)
                    text=open(r"D:\project_data"+dateT+"\\"+continent_str[i]+r"\\"+j+r"\\"+"Economy"+".txt","a+")
                    text.write(clear_data+"\n")
                    text.close()
                    print(clear_data)
     
                # land use

                result_13=re.findall(r"<tr><td>\S{,} \D{,}:</td><td>\S{,} km²</td></tr>",str_data)
                for item in result_13 :
                    clear_data = re.sub(r"</td>" , " " ,item)
                    clear_data = re.sub(r"<td>" , "" ,clear_data)
                    clear_data = re.sub(r"<tr>" , "" ,clear_data)
                    clear_data = re.sub(r"</tr>" , "" ,clear_data)
                    text=open(r"D:\project_data"+dateT+"\\"+continent_str[i]+r"\\"+j+r"\\"+"land use"+".txt","a+")
                    text.write(clear_data+"\n")
                    text.close()
                    print(clear_data)

                # Transport

                result_14=re.findall(r"<tr><td>\D{,5}\S{5,8}:</td><td>\S{,}\D{,3}</td></tr>",str_data)
                for item in result_14 :
                    clear_data = re.sub(r"</td>" , " " ,item)
                    clear_data = re.sub(r"<td>" , "" ,clear_data)
                    clear_data = re.sub(r"<tr>" , "" ,clear_data)
                    clear_data = re.sub(r"</tr>" , "" ,clear_data)
                    text=open(r"D:\project_data"+dateT+"\\"+continent_str[i]+r"\\"+j+r"\\"+"Transport"+".txt","a+")
                    text.write(clear_data+"\n")
                    text.close()
                    print(clear_data)
                #    City
                lst_city=[]
                lst_pop=[]
                result_city = re.findall(r"<tr><td>\D{1,}</td><td><a",str_data)
                result_pop = re.findall(r"</a></td><td>\d{1,3}\S{,1}\d{,3}\S{,1}\d{,3}</td></tr>",str_data)
                text=open(r"D:\project_data"+dateT+"\\"+continent_str[i]+r"\\"+j+r"\\"+"City"+".txt","a+")
                for j1 in result_pop:
                        clear_data2 = re.sub(r"</td>" , "" ,j1)
                        clear_data2 = re.sub(r"<td>" , "" ,clear_data2)
                        clear_data2 = re.sub(r"</tr>" , "" ,clear_data2)
                        clear_data2 = re.sub(r"<tr>" , "" ,clear_data2)
                        clear_data2 = re.sub(r"</a>" , "" ,clear_data2)
                        clear_data2 = re.sub(r"<a" , "" ,clear_data2)
                        lst_pop.append(clear_data2)
                for i1 in result_city:
                            clear_data1 = re.sub(r"</td>" , "" ,i1)
                            clear_data1 = re.sub(r"<td>" , "" ,clear_data1)
                            clear_data1 = re.sub(r"</tr>" , "" ,clear_data1)
                            clear_data1 = re.sub(r"<tr>" , "" ,clear_data1)
                            clear_data1 = re.sub(r"</a>" , "" ,clear_data1)
                            clear_data1 = re.sub(r"<a" , "" ,clear_data1)
                            clear_data1 = re.sub(r"ế" , "e" ,clear_data1)
                            clear_data1 = re.sub(r"ă" , "a" ,clear_data1)
                            clear_data1 = re.sub(r"ạ" , "a" ,clear_data1)
                            lst_city.append(clear_data1)
                lst_sum=[]
                for f in range(len(lst_pop)):
                    lst_sum.append("city : "+lst_city[f]+"\nPopulation : "+lst_pop[f]+"\n")
                    print("city : "+lst_city[f]+"\nPopulation : "+str(lst_pop[f])+"\n")
                for s in lst_sum:
                    text.write(s+"\n")
                text.close()
