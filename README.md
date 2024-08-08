A script generating the probabilities of results in the European lottery (called EuroMillions in France, but known under different names across Europe).

It should incrementally add the results of the Tuesday and Friday draws to the list and remove the oldest ones, as the estimation will be based on the last 12 months.

I haven't been able to extract data from a CSV edited by the FDJ (Fédération Française des loteries) yet.

--BEGIN UPDATE---

The V2 include the import .csv data.
You can find the results here https://www.fdj.fr/jeux-de-tirage/euromillions-my-million/historique?msockid=19e4fa7c7bfc69c70b3deeaf7aa1688c
When you DL, the .zip, extract the .csv, then, keep andformat your file in 7 columns
boule_1	boule_2	boule_3	boule_4	boule_5	etoile_1	etoile_2

---END OF UPDATE---


V3 is the Latest version 

--BEGIN UPDATE---

The V3 include the import .csv data and date
You can find the results here https://www.fdj.fr/jeux-de-tirage/euromillions-my-million/historique?msockid=19e4fa7c7bfc69c70b3deeaf7aa1688c
When you DL, the .zip, extract the .csv, then, keep andformat your file in 8 columns
date_de_tirage	boule_1	boule_2	boule_3	boule_4	boule_5	etoile_1	etoile_2

---END OF UPDATE---

Enjoy

---WARNING---

This script is used to calculate probabilities and does not in any way reflect the draw or the final result. Predicting with 100% accuracy would be Divine or quantum... You will not win anything by playing these numbers. Like alcohol, the abuse of gambling is harmful to oneself and one's surroundings

---WARNING---

---WARNING DOUBLE TAPE---

WARNING!!! This script is used to learn and work with the PANDAS library in PYTHON. It’s a personal project designed to manipulate and analyze data. If we take the EuroMillions 'Template', it remains quite basic…

What is EuroMillions? It’s a lottery game. And what is the lottery? Well, it’s a series of numbers that are drawn in sets of 5 numbers + 2 additional numbers (7 numbers in total) twice a week, on Tuesdays and Fridays.

The script will analyze the files provided by the FDJ (all the drawn numbers, which can be refined by removing or adding dates as needed), then estimate the probabilities of numbers being drawn and display the date of the next draw.

Of course, I must repeat, these are not the winning numbers that will come up, only a probability based on the history of draws provided in the file. To achieve a 100% prediction would require divine intervention or quantum computing.

So, this script does not have a predictive purpose in the literal sense but rather aims to take into account all the draw elements over a given period (FDJ data), which can be adjusted, and then estimate probabilities.

This script is open-source, and of course, I am available to discuss and explain it if needed.

---WARING DOUBLE TAPE---
