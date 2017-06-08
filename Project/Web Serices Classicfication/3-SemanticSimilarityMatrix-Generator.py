__author__ = 'chinmay'


from nltk.corpus import wordnet
import csv

####SImilarity score calculation#################3

Words=['ability','able','abstract','academia','academic','accept','acceptance','accepted','accepts','accessed','accident','accommodation','accommodations','accomplished','according','account','accuracy','accurate','achievement','acknowledgement','acquire','action','activities','activity','actual','addison','address','addresses','adds','advantages','adventure','advertisement','affordable','age','agencies','agent','agible','agreed','agriculture','aid','airport','albe','alco','allow','allowing','allows','altitude','ambulance','america','amphitheatre','analog','analysed','analysis','anda','ango','animal','answer','anymore','apart','aped','apple','approximately','area','areas','arrange','arranges','arrival','arriving','arrow','article','articles','artificial','asian','assistant','associated','atm','atmospheric','atomic','attached','attracted','attractive','attracts','attribute','author','authorised','authorization','authorizations','authorize','authorized','authors','auto','autocar','autos','avail','availability','available','avocado','award','awards','aweather','awesome','axed','background','backpackers','ballistic','bank','banker','bankers','based','basket','bat','batch','beach','beaches','bearing','bed','beds','beer','beginning','berlin','best','beverage','bicycle','bicycles','biggest','biopsy','biscuit','bled','blue','body','bomb','bombay','book','booked','booking','bookings','bookit','books','borrowed','bounding','box','brain','brand','brands','bread','break','breakfast','bring','british','browser','burg','burgs','bus','butter','butters','buy','byproduct','cake','calc','calculate','calculated','calculates','calculator','calendar','calling','cambridge','camera','cameras','canadian','cannon','capabilities','capital','car','card','care','career','cargo','carriage','cars','cart','case','category','cation','cell','cent','center','centered','centile','centre','centred','century','cereal','certain','change','channel','charm','chase','cheap','cheapest','check','checks','chemical','chief','china','chinese','ching','choice','chosen','cities','city','client','clients','clinic','close','closed','closes','coach','coconut','code','coder','codes','coding','coff','coffee','cola','color','colors','colour','combination','combustion','comedy','comic','comments','commitment','committing','comp','compact','companies','company','comparison','competitor','complete','completely','complex','computer','computes','concise','condition','conducts','confirmation','considered','consisted','consists','contact','contain','containing','content','contracts','conversion','convert','converter','convinces','coordinate','coordinates','corn','corporation','corporations','correct','corrected','corresponding','cosines','cost','costs','count','countries','country','county','course','coverage','covering','covers','create','creates','creation','credit','criteria','critical','curing','currency','current','currently','currents','customer','customers','cycle','cycles','daily','data','database','dataset','date','dation','day','daylight','days','deacon','decimal','dedicated','deduced','defined','degree','degrees','delegated','delicious','delivering','delivers','delivery','density','depart','department','departure','depends','deplace','describes','designate','desired','destination','destinations','destruction','details','detected','detects','device','devices','diag','diagnosed','diagnosis','diagnostic','diet','differ','differences','different','digit','digital','digitals','digits','ding','dings','directions','directly','disadvantages','discover','discovery','display','distance','district','dits','doctor','documentary','dollar','dollars','dont','door','dough','dragging','drawback','drees','dried','drink','drinks','driving','drought','droughts','drug','drugs','drugstore','duration','durations','duty','dynamic','ear','earth','earthquake','easting','edited','educated','education','educational','electric','elements','elevation','elling','elsin','email','embed','emergency','emphasis','employee','encoding','encyclopedia','endeavour','endings','engine','enter','enters','entirely','entity','entrance','entries','environment','equal','equipment','erin','error','especially','estimate','estimated','euro','europe','european','euros','exactly','example','exams','expensive','experiment','experimenting','experiments','expiration','export','exportable','expression','extent','facilitate','facilities','facility','fall','family','famous','fan','fant','fantasy','farmland','farmlands','fast','favourite','features','february','fee','feed','feet','fellow','ferr','fess','fever','fiction','field','fifty','figure','file','fills','film','films','financial','financing','finder','finding','finds','finest','firm','fish','flew','flight','flights','flip','flips','flour','flying','focus','fodder','followed','food','football','fora','format','formatted','founder','france','frankfurt','free','frequent','friendly','fronts','fruit','fulfill','fulfills','fulltime','fun','functional','functionality','funding','funds','future','fuzzy','gate','gazetteer','gel','general','generic','genre','geo','geographic','geographical','geometry','geopolitic','geopolitical','germ','german','germany','gets','gift','given','gives','givin','giving','good','goog','gorge','govern','government','governments','gps','grain','grange','grasses','green','grid','grind','grocery','grow','grown','grun','hallo','handles','handy','happened','hardcover','healing','health','height','help','helpful','high','higher','highly','hikers','hiking','hipping','hish','historical','history','holder','home','honey','honorary','horizontal','hospital','hospitals','hot','hotel','hotels','hots','human','icing','icon','icons','identified','identifier','image','images','import','imported','incident','incidents','include','includes','including','income','incomplete','independently','india','indian','indicate','indicating','influence','info','inform','information','informed','informs','infos','input','inquire','inside','instance','instantly','insurance','intelligence','intends','intentional','interested','interface','internal','international','interval','invest','investigating','invocations','ion','ions','iraq','iraqi','irish','iron','issue','italy','item','items','java','job','jobs','jockey','journal','judge','key','killed','kilometer','kilometers','kind','kipe','know','known','kodak','kohl','korea','kori','label','lamp','land','landing','language','large','largest','latest','latitude','learned','learning','lecturer','lecturers','legal','lemon','lending','length','lense','lets','letter','letters','level','liability','license','lift','light','lightening','lightning','lightnings','like','line','linguistic','link','linked','lions','lips','liquid','list','litre','loading','localized','locate','located','locating','location','locations','locator','lock','locked','locks','logged','login','longitude','lookup','low','luck','luxury','machine','magazine','magical','main','mainland','major','make','mall','map','mapping','maps','markers','market','markets','mart','mass','match','matched','matcher','matches','matching','material','math','max','maximum','measure','meat','media','medias','medical','medium','meng','ment','mercantile','merchandiser','merchant','merk','message','messages','messe','mester','meters','metropolitan','mexico','mian','microwave','mile','miles','mind','mining','missile','missiles','mission','misspelled','mixer','model','models','modified','module','money','monograph','monographs','monthly','motion','motor','mountain','moves','movie','multi','multiple','munch','municipal','museum','names','national','nations','natural','nearby','nearest','needed','needs','net','network','networking','new','news','newspaper','nice','nolo','normally','north','northing','note','notes','novel','novels','number','numbers','object','objects','obligatory','obtain','obtainable','obtained','occupation','occupational','occupations','offer','offered','offering','offers','office','official','ofthe','old','oldest','omen','onboard','ones','online','open','opens','operation','opinion','opportunity','optimal','optional','options','oracle','orange','order','ordered','organism','organization','organizations','organize','organized','organizing','oscar','outcome','output','outputs','outside','oven','owned','package','page','pair','pairs','pakistan','pakistani','pan','pang','panning','paper','parameter','parameters','pard','park','parks','parkway','parsed','parser','partial','particular','parties','password','path','paths','patient','patients','people','performed','period','person','personal','personnel','persons','pets','phil','phone','photograph','photographs','physical','physician','pill','pills','pioneer','pixel','pixels','place','placed','places','plan','player','plus','points','political','polling','popular','popularity','populated','population','port','porta','portable','position','positions','positive','possessed','possible','post','postal','pots','power','powered','precision','precondition','predicting','premium','prepared','present','presented','presents','price','priced','prices','pricey','primer','printed','pro','problems','process','processes','produced','producer','product','production','productions','products','prof','profession','professional','professionals','professions','professor','professors','profile','profit','programming','project','projectile','propelled','proposed','proposition','propria','proprietor','proved','provide','provided','provider','providers','provides','providing','psize','psychological','public','publication','publications','published','publisher','publishers','publishing','purchase','purchaseable','purchased','purchasing','qualified','quality','quantity','quat','query','question','radar','radius','raining','range','rate','rated','raw','read','reader','reads','real','realized','reasoning','recommend','recommendation','recommended','recommends','record','recorded','records','recreate','reference','references','refined','refuses','region','regions','registered','regular','related','relative','released','releases','reliable','render','rent','rental','renting','report','reports','repr','represent','reputable','request','requested','requests','required','requirements','requiring','research','researcher','reservation','reserve','reserved','reserves','responds','response','responsible','rest','restore','result','results','retail','retailers','retails','retrieve','retrieved','retrieves','return','returnan','returned','returns','review','rice','rich','rival','road','roads','roadway','romantic','room','route','runs','rural','russia','russian','sale','sandwich','saturn','saving','scale','scholar','scholarship','scholarships','science','script','sea','search','searcher','searches','searching','season','seat','second','seed','seeds','select','selected','selects','self','seller','selling','send','sends','senior','sensor','sensors','sent','separately','service','services','session','ship','shipping','shirt','shop','shopping','short','shortest','showing','shown','shows','shuttle','sightseeing','signs','simple','simply','single','site','situated','situation','size','skilled','slider','slot','small','smith','smooth','soap','software','soil','sold','solution','soon','sound','source','south','space','spain','span','spatial','special','specially','specific','specifications','specified','spent','spherical','splits','sport','sports','square','staff','standard','start','state','states','static','status','sting','stock','stomach','store','stores','story','straight','streaming','street','strike','string','strings','structure','structured','student','suggestion','suitable','summary','sunrise','sunset','supervising','supply','support','supports','surfing','swiss','switch','swith','symbolic','symptom','symptoms','syndrome','takes','tansy','target','task','taste','tasting','tax','taxed','taxes','taxi','tea','teach','team','technical','technology','telephone','tell','tells','texas','text','textual','things','thumbnail','time','timemeasure','times','title','titles','topography','total','town','towns','toyota','trade','trades','traffic','train','training','translocation','transport','transports','travel','traveling','treat','treatment','tree','tremor','tries','turns','tutorial','twilight','type','types','ultra','unemployed','unexpected','unformatted','unilateral','uniliteral','unique','unit','united','unity','universities','university','unliteral','unlock','unlocked','unlocks','unstructured','unsuccessful','untangible','update','updates','urban','usable','usage','use','used','useful','user','users','uses','using','usually','valid','validity','valuable','value','vari','variety','varify','various','vehicle','vehicles','verifies','version','versions','vial','vicinity','video','view','viewport','village','visiting','wall','want','wants','warm','water','ways','weapon','weapons','weather','web','week','weekly','weeks','welfare','welfares','wellknown','west','wheat','wheeled','wheels','whiskey','wholesale','wich','wide','width','windows','wireless','witness','wonderful','words','work','working','works','world','worldwide','written','wrote','yahoo','year','years','zambia','zip','zone','zoo','zooming']







main_list=[]

#to find the semantic similarity of each word in TF-IDF matrix with every other word
for i in range(0,len(Words)):

    sublist=[]

    for j in range(0,len(Words)):


        print(i,j)

        if i==j:

            sublist.append(1.0)

        else:



            syns_i=wordnet.synsets(Words[i])
            syns_j=wordnet.synsets(Words[j])



            if len(syns_j)!=0 and len(syns_j)!=0:

                score=[]

                for k in range(0,len(syns_i)):

                    for l in range(0,len(syns_j)):

                        w1=syns_i[k]
                        w2=syns_j[l]

                        name1=str(w1)
                        name2=str(w2)

                        name1_list=name1.split(".")

                        name2_list=name2.split(".")



                        if name1_list[1]==name2_list[1]:

                            res=w1.wup_similarity(w2)

                            if res==None:

                                score.append(1.0)
                            else:
                                score.append(float(res))






                sum_scores=0



                for z in range(0,len(score)):

                    sum_scores+=score[z]


                if len(score)!=0:
                    final_val=float(sum_scores)/float(len(score))


                else:
                    final_val=0.0


                sublist.append(final_val)
            else:

                sublist.append(0.0)

    main_list.append(sublist)




#Writing the Similarity Matrix to a CSV file
with open("similarity.csv", "w",newline="") as f:
    writer = csv.writer(f)
    writer.writerows(main_list)












