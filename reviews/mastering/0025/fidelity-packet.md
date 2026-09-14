# Fidelity Gate — Chapter 25

Audit the complete assembled English chapter against the Korean source.
Report only genuine source-fidelity defects: wrong action, subject, object,
causality, quantity, mechanism, terminology, ambiguity, joke logic, register,
or physical detail. Check repeated UI labels and counters against how they
behave across the whole scene. Interpret idioms by their function, not by
translating their component words. Do not report optional stylistic rewrites.

Return exactly one JSON object and no Markdown fence:

{
  "summary": "brief assessment",
  "findings": [
    {
      "id": "F01",
      "severity": "critical|major|minor",
      "source": "source location",
      "current": "exact uniquely occurring English span",
      "defect": "specific fidelity defect",
      "replacement": "finished replacement only when necessary",
      "rationale": "source-grounded reason",
      "confidence": 0.0
    }
  ]
}

Use an empty findings array when the chapter is faithful. A critical or major
finding blocks promotion; minor findings are recorded for human inspection.

## Korean source

```text
  1|＃25화
  2|
  3|
  4|
  5|“이곳은 저승인가?”
  6|
  7|중년인이 깨어나자마자 한 말이었다.
  8|
  9|내가 대답하기도 전에 조그마한 뭔가가 튀어나와 중년인의 품에 안겼다.
 10|
 11|눈가에 눈물이 대롱대롱 매달린 꼬마가 외쳤다.
 12|
 13|“공 숙부!”
 14|
 15|“천아! 무사했구나. 그런데 이게 도대체……?”
 16|
 17|혼란스러워하는 중년인에게 꼬마가 울음 섞인 목소리로 설명했다. 언덕 위에서 우리를 만났고, 내 손에 적들이 모두 죽었다는 말을 들은 중년인이 눈을 크게 떴다.
 18|
 19|“본가의 인물이시오?”
 20|
 21|“예. 맞습니다.”
 22|
 23|“아, 하늘이 도왔구나!”
 24|
 25|“…….”
 26|
 27|내가 도운 거지, 이 양반아.
 28|
 29|“난 분명히 산 밑으로 추락했는데…… 그걸로 끝이라고 생각했소.”
 30|
 31|“거의 그럴 뻔했지요. 운이 좋았습니다.”
 32|
 33|나는 손가락으로 능선 밑을 가리켰다. 적으로 추정되는 시체 두 구가 나무에 머리를 박고 누워 있었다.
 34|
 35|그가 미끄러졌던 경로에 풀숲이 무성하지 않았다면, 그도 저 꼴이 났을 것이다.
 36|
 37|‘나도 처음에는 몰랐지.’
 38|
 39|중년인의 존재를 깨달은 건 퀘스트창 덕분이었다.
 40|
 41|적들을 다 물리쳤는데도 [삭주 지부의 생존자] 퀘스트가 완료되지 않았던 것이다. 그건 생존자가 더 있다는 뜻이었다.
 42|
 43|‘문제는 이 사람 말고도 생존자가 더 있냐는 건데…….’
 44|
 45|일말의 불안감은 지친 중년인을 부축한 순간 간단히 해소됐다.
 46|
 47|띠링.
 48|
 49|
 50|
 51|- [생존자] 퀘스트를 완료했습니다!
 52|
 53|- 연계 퀘스트가 생성되었습니다!
 54|
 55|- 레벨이 올랐습니다!
 56|
 57|- 레벨이 올랐습니다!
 58|
 59|- 공적치와 명성이 상승합니다!
 60|
 61|
 62|
 63|* * *
 64|
 65|
 66|
 67|“후우.”
 68|
 69|중년인이 호흡을 토해 냈다. 짧은 운기조식이었지만 최소한의 기력을 회복한 듯, 훨씬 나아진 모습이었다.
 70|
 71|그는 자리에서 일어나 정중히 포권을 취했다.
 72|
 73|“은인께서 모두를 살리셨습니다.”
 74|
 75|“아닙니다. 마땅히 해야 할 일을 한 것뿐인데요.”
 76|
 77|이제는 입만 열리면 거짓말이 술술 나온다. 한편으로는 틀린 말도 아니다. 어떻게든 퀘스트는 깨야 했으니까.
 78|
 79|‘오히려 내가 고맙다고 절을 해야 할 판이지.’
 80|
 81|하지만 이런 내 태도에 산타클로스, 아니 생존자들은 적잖이 감격한 모양이었다.
 82|
 83|“뛰어난 무공에 의협심까지. 이 공야청, 진심으로 탄복했소.”
 84|
 85|“소천과 소율이 대협께 큰 은혜를 입었습니다.”
 86|
 87|덕분에 이름을 알았다. 중년인은 공야청, 어린 남매는 소천과 소율이다.
 88|
 89|“실례가 안 된다면 은인의 성함을 여쭈어도 되겠소?”
 90|
 91|“제 이름은…….”
 92|
 93|그때, 문득 한 가지 생각이 뇌리를 스쳤다.
 94|
 95|‘이거, 내 이름 들으면 칼 들고 달려드는 거 아냐?’
 96|
 97|어떤 음모가 있었건 간에 이 전쟁의 도화선에 불을 붙인 건 다름 아닌 이 몸, 진태경이다. 터전과 가족을 잃은 두 사람이 내게 좋은 감정이 있을 것 같지 않았다.
 98|
 99|그래, 선의의 거짓말이 필요한 시점이다.
100|
101|“홍길동. 저는 홍길동이라고 합니다.”
102|
103|“홍길동…… 처음 듣는 이름이오. 그러나 영웅의 풍모가 느껴지는구려.”
104|
105|소천이 옆에서 거들었다.
106|
107|“동에 번쩍 서에 번쩍. 신출귀몰할 것 같은 이름입니다.”
108|
109|……저 녀석이 어떻게 알았지?
110|
111|나는 호부호형 얘기가 나오기 전에 서둘러 화제를 돌렸다.
112|
113|“그보다, 어떻게 된 일입니까?”
114|
115|두 사람의 얼굴에 그림자가 짙게 내려앉았다.
116|
117|말문을 연 것은 공야청이었다.
118|
119|“불과 며칠 전의 일이었소.”
120|
121|전쟁을 알리는 전서구가 도착했을 때는 이미 삭주 지부가 물 샐 틈 없이 포위된 상태였다. 항산검문이 고용한 낭인들이 사람들을 도륙하고, 건물을 불태웠다고 했다.
122|
123|“그 숫자가 물경 일백에 달했소. 지부장과 휘하 무사들이 시간을 벌어 준 덕분에 비밀 통로로 빠져나올 수 있었지요. 탈출한 이들 대부분이 무공을 모르는 여인과 아이들이었소.”
124|
125|다른 이들이 어떻게 되었는지는 물어보지 않아도 알 수 있었다.
126|
127|내가 갖고 있는 시스템은 절대적이며 사실적이다. 퀘스트창이 알려 준 삭주 지부의 생존자는 세 사람이 전부였다.
128|
129|“적들에 관해 알고 싶습니다.”
130|
131|“낭인들이오.”
132|
133|“낭인?”
134|
135|“은인도 알다시피, 돈이라면 뭐든 하는 놈들이지. 그중에서도 특히 악질인 놈들이 항산검문의 의뢰를 받아 우리를 습격했소.”
136|
137|“악질치고는 약하던데요.”
138|
139|“악하고 선함에 강자와 약자가 따로 있겠소? 이번에 고용한 놈들은 널리고 널린 수준의 낭인이오. 다만 우두머리가 문제였지.”
140|
141|공야청이 이를 악물었다.
142|
143|“일문일살 조필. 그놈이었소. 지부장께서는 놈을 보자마자 패배를 직감하고 내게 식솔들을 부탁하셨지.”
144|
145|소천의 작은 주먹이 부르르 떨렸다.
146|
147|“제 손으로 직접 사지를 찢어 죽일 겁니다.”
148|
149|꼬맹이치고는 남다른 어휘 선택이었지만, 뼈에 사무친 원한을 생각하면 당연하게 생각되었다.
150|
151|나는 소천의 머리를 쓰다듬어 주었다.
152|
153|“꼭 그렇게 될 것이다. 내 도와주마.”
154|
155|“정말이십니까?”
156|
157|“남아일언중천금. 내 한 입으로 두말할 것 같으냐? 내 반드시 그놈을 잡아 레벨 업을…….”
158|
159|“예?”
160|
161|“아니, 놈을 죽여 원한을 갚아 주마.”
162|
163|“아아, 감사합니다. 정말 감사합니다. 홍 대협!”
164|
165|“고맙소. 정말로 고맙소!”
166|
167|두 사람은 연신 감사를 표했다. 아, 뭔가 되게 야비한 놈이 된 기분이라 가슴 한구석이 심하게 찔려 온다.
168|
169|‘아니지. 저쪽은 원수가 죽어서 좋고, 나는 레벨 업 해서 좋고. 상부상조지. 상부상조.’
170|
171|애써 자기합리화를 시키며 물었다.
172|
173|“머릿수가 얼마나 됩니까?”
174|
175|“적들의 위치를 파악하는 도중에 놈들이 하는 이야기를 들었소. 조필을 포함해 서른 남짓이라고 하더군.”
176|
177|“서른? 삼십 명이요?”
178|
179|“그렇소. 그러니 어서 피해야…….”
180|
181|공야청의 목소리가 멀어진다. 그 대신 저 멀리서 희미한 소리가 가까워졌다. 띠링. 띠링. 띠링.
182|
183|들린다. 레벨 업 하는 소리가. 로그아웃하는 소리가!
184|
185|나는 자꾸만 치솟는 입꼬리를 억누르며 말했다.
186|
187|“여기서 나머지 놈들을 기다립시다.”
188|
189|“기다린다니. 그게 무슨 말이오?”
190|
191|“일망타진! 그런 악독한 놈들을 살려 둘 수 없습니다!”
192|
193|“아니, 홍 대협. 내 말을 좀…….”
194|
195|“은인 같은 고수라면 할 수 있습니다! 감사합니다. 은인!”
196|
197|소천이 눈물을 글썽이며 내 품에 달려들었다. 나는 두 팔 벌려 녀석을 끌어안았다.
198|
199|“그래. 놈들을 다 죽이자!”
200|
201|“죽이자!”
202|
203|“조필 개새끼!”
204|
205|“개새끼!”
206|
207|그때 공야청이 입을 열었다.
208|
209|“조필은 절정 고수요.”
210|
211|“조필 씹새…… 예?”
212|
213|“일문일살 조필. 산서성을 통틀어도 몇 안 되는 절정 고수란 말이오. 놈이 온갖 은원에 얽혀 있으면서도 지금까지 살아남을 수 있었던 이유가 무엇이겠소?”
214|
215|“설마…….”
216|
217|“그에게 덤비는 자는 다 죽었소. 조필은 그런 자요. 잔혹하고, 그만큼 강하지.”
218|
219|“아.
220|
221|뭔가 이상함을 감지한 어린 눈동자가 나를 올려다본다.
222|
223|“소천아.”
224|
225|“예. 대협.”
226|
227|“생각해 보니 지금은 때가 아닌 것 같다.”
228|
229|“예?”
230|
231|“내가 어리석었다. 우선 너희 남매를 본가로 생환시키는 게 최우선인데. 그렇지?”
232|
233|“…….”
234|
235|“실은 아까 싸우다가 부상을 입기도 했고, 내 부하들도 많이 지쳐서 힘든 싸움이 될 듯싶다.”
236|
237|소천의 눈동자가 내 위아래를 훑었다. 적들의 피로 흠뻑 젖어 있긴 했지만 찢어진 곳 하나 없이 멀쩡한 옷이다. 상처가 있을 리 만무했다.
238|
239|“내상을 입었단다.”
240|
241|“…….”
242|
243|이번에는 고개를 돌려 정찰조원들을 바라봤다. 칼 한 번 안 휘두르고 전투가 끝난 바람에 쌩쌩하다 못해 펄펄 날아다닌다.
244|
245|“보이는 게 다가 아니지.”
246|
247|“……대협.”
248|
249|슬그머니 소천을 떼어 내고 외쳤다.
250|
251|“본가로 돌아간다. 모두 출발 준비해!”
252|
253|잽싸게 조원들에게 돌아가려는데, 소천의 손이 옷깃을 꽉 붙잡고 놔주질 않는다. 동그란 눈에는 눈물이 글썽하다.
254|
255|“대협.”
256|
257|“야, 빨리빨리 안 움직여! 소천아, 내가 지금 좀 바빠서 그런데 이따 이야기하자. 알았지?”
258|
259|“홍 대혀엽.”
260|
261|“공야청 아저씨. 아니, 공 대협은 뭐 하세요. 한시가 급한데.”
262|
263|“……소천아, 이리 오거라.”
264|
265|공야청이 나를 병신 보듯이 바라보며 소천을 떼어 냈다. 저건 마치 범죄자의 접근을 차단하는 보호자의 손길.
266|
267|소천이 거의 통곡했다.
268|
269|“홍길동 대혀업!”
270|
271|그리고 그 말이 신호탄이었다.
272|
273|쾅! 굉음과 함께 오두막의 문이 박살 나며 한 사람이 나타났다.
274|
275|
276|
277|[Lv.22 혁무진]
278|
279|
280|
281|“진태경 이 씨발 새끼야아아!”
282|
283|쒸익쒸익. 혁무진의 분노에 찬 눈동자가 정확히 나를 향하고 있었다. 공야청과 소천이 멍한 얼굴로 나를 바라봤다.
284|
285|“홍 대협?”
286|
287|“홍길동 대협?”
288|
289|“아. 그게. 그러니까.”
290|
291|……에이, 시발.
292|
293|
294|
295|* * *
296|
297|
298|
299|“흠.”
300|
301|조필은 물끄러미 시체를 내려다보았다. 일그러진 표정에 부릅뜬 눈. 피와 눈으로 얼어붙은 그는 흑산도라는 별호로 불렸었다.
302|
303|“쯧쯧. 이 친구, 어쩌다 이렇게 되었나.”
304|
305|제법 충성심이 깊고 똘똘한 놈이었는데, 이렇게 허망하게 갈 줄은 몰랐다.
306|
307|“그러게, 내가 누누이 말하지 않았나. 두 눈 크게 뜨고 다니라고.”
308|
309|조필은 흑산도의 부릅뜬 눈을 잡고 벌렸다.
310|
311|얼어붙은 살이 찢어지며 끔찍한 소리가 새어 나온다.
312|
313|찌직. 찌지직.
314|
315|다른 이들은 숨도 못 쉬고 그 모습을 지켜봤다.
316|
317|평소와 다름없는 표정과 말투였지만 그들은 조필이 분노했다는 사실을 온몸으로 느끼고 있었다.
318|
319|절정 고수가 뿜어내는 살기에 숨이 막히고 식은땀이 흘렀다.
320|
321|‘그럴 만도 하지.’
322|
323|이십여 명이 전멸했다. 그것도 고작 삭주 지부의 잔당이나 처리하는 임무에.
324|
325|일문일살. 마음에 드는 적을 만나면 꼭 한 가지 질문을 하고 죽인다는 괴악한 성격의 조필이다.
326|
327|낭인들은 흑산도가 죽어서 다행이라고 생각했다. 살아 있었다면 한층 더 끔찍한 일을 겪었을 테니까.
328|
329|“이제 좀 낫구먼.”
330|
331|조필이 바지춤에 피를 닦아 내며 일어났다.
332|
333|“그래, 다들 어떻게 생각하나? 가감 없이 말해 보게.”
334|
335|“당연히 명령대로 움직여야지.”
336|
337|한 사람이 나섰다. 단정한 복장과 점잖은 태도의 중년인, 그리고 그 뒤로 시립한 십여 명의 무사들은 항산검문이 낭인들을 통제하기 위해 보낸 감시자이자 길잡이였다.
338|
339|조필이 빙긋 웃었다.
340|
341|“아, 그래. 우리 대항산검문의 당주님을 잊고 있었구려. 그런데 명령이라니?”
342|
343|“삭주 지부를 지우고 본대와 합류하라. 소문주의 명령을 벌써 잊은 건가?”
344|
345|“명령이라, 의뢰를 받은 기억은 있소만.”
346|
347|“그게 그거 아닌가!”
348|
349|중년인이 불쾌한 얼굴로 조필을 응시했다.
350|
351|“애초에 여기까지 온 것부터가 그대의 독단이었지. 한데 그 결과가 어떤가? 일개 지부 잔당 따위한테 스물이 넘는 수하들을 잃지 않았나!”
352|
353|“그러니까 쫓아야지. 반나절이면 놈들을 끝장낼 수 있소.”
354|
355|“정양까지는 모르나, 혼주까지 쫓는다면 역공당할 우려가 있지. 이 이상의 독단은 내가 허락하지 않겠다.”
356|
357|“허락이라, 허락…….”
358|
359|곰곰이 생각에 잠겨 있던 조필이 입을 열었다.
360|
361|“안 되겠어. 마음에 안 드는군.”
362|
363|“그게 뭐……!”
364|
365|퍼걱. 목뼈가 으스러진 그는 말을 끝마치지 못하고 절명했다. 빛살 같은 속도로 중년인의 목을 꺾은 조필이 입술을 핥았다.
366|
367|“나는 전쟁이 좋아. 누가 죽어도 잊히거든.”
368|
369|“이노옴!”
370|
371|상황을 파악한 항산검문의 무사들이 병장기를 빼 들었지만, 조필은 이미 그들 사이로 파고든 뒤였다.
372|
373|퍼걱, 촤악!
374|
375|눈밭 위로 더운 피가 쏟아졌다. 조필이 맹수처럼 날뛸 때마다 누군가의 목이, 팔이, 다리가 뜯겨 훨훨 날았다.
376|
377|“끄아아…….”
378|
379|이름 모를 무사의 신음이 마지막이다.
380|
381|시체 더미 위, 짓눌린 침묵 속에서 조필이 말했다.
382|
383|“놈들을 추격한다.”
384|
385|이번에는 아무도 입을 열지 않았다. 도망치듯 준비를 서두르는 수하들의 모습을 뒤로하고, 조필은 시신들을 바라봤다.
386|
387|‘어떤 놈일까.’
388|
389|그는 절정 고수다. 시신들의 몸에 남은 상흔과 족적을 통해 상대의 모습을 그려 낼 수 있었다.
390|
391|단 한 사람. 뛰어난 실력의 창수(槍手)가 이 자리에 있었다. 다른 이십여 명을 도륙한 것도 바로 그자다.
392|
393|‘흑산도를 일격에 죽인 놈이니 오죽할까.’
394|
395|특히 가슴을 관통한 마지막 일격은…… 조필이 흥미를 갖기에 충분했다.
396|
397|‘재미있는 싸움이 되겠어.’
398|
399|누구일까. 태원진가의 고수? 아니면 알려지지 않은 누군가?
400|
401|아무래도 상관없다. 조필은 기분 좋은 웃음을 터트렸다.
402|
403|“조만간 만나자고. 친구.”
404|
405|
406|
407|* * *
408|
409|
410|
411|“들어온 소식은?”
412|
413|“없습니다. 그저 최대한 빨리 이동하는 수밖에는…….”
414|
415|“젠장, 젠장!”
416|
417|위팽은 분통을 터트렸다. 하지만 방법이 없었다. 수하의 말처럼 최대한 빨리 삼공자를 찾아 보호하는 수밖에는.
418|
419|‘일문일살 조필…….’
420|
421|놈의 악명은 익히 들어서 알고 있다. 만일 삼공자가 놈의 손에 들어간다면 결과는 죽음뿐이다.
422|
423|‘그렇게 되면 주군을 볼 면목이 없다.’
424|
425|진위경은 초인적인 인내심으로 참아 냈다.
426|
427|그는 현재 태원진가의 머리이자 중심에 있다. 누구보다 사랑하는 동생과 수백의 식솔을 저울에 올려놨고, 장고 끝에 가장 믿는 수하인 위팽을 동생에게 보냈다.
428|
429|그런데 만약 실패한다면…….
430|
431|‘주군을 볼 면목이 없어.’
432|
433|고삐를 잡은 손에 힘이 들어간다. 위팽은 박차를 가했다. 그의 뒤로 이십여 기의 기마가 꼬리를 물고 달렸다.
```

## Assembled English

```markdown
[P1]
# Chapter 25

[P2]
“Is this the afterlife?”

[P3]
That was the first thing the middle-aged man said when he woke up.

[P4]
Before I could answer, something small sprang forward and threw itself into his arms.

[P5]
The child, tears dangling from the corners of his eyes, shouted.

[P6]
“Uncle Gong!”

[P7]
“Socheon! You’re safe. But what in the world…?”

[P8]
The confused middle-aged man listened as the child explained through sobs. When he heard that we had met on the hill and that all the enemies had died by my hand, his eyes widened.

[P9]
“Are you from the main family?”

[P10]
“Yes. That’s right.”

[P11]
“Ah, Heaven has helped us!”

[P12]
“…”

[P13]
*I helped you, you old man.*

[P14]
“I was sure I’d fallen all the way down the mountain… I thought that was the end of me.”

[P15]
“It nearly was. You were lucky.”

[P16]
I pointed below the ridge. Two corpses presumed to belong to the enemy lay with their heads rammed into trees.

[P17]
If the grass along the path where he had slipped had not been so thick, he would have ended up just like them.

[P18]
*I didn’t realize it at first, either.*

[P19]
I only became aware of the middle-aged man’s existence thanks to the Quest Window.

[P20]
Even after I defeated all the enemies, the **Survivors of the Sakju Branch** Quest had not been completed. That meant there were more survivors.

[P21]
*The question was whether there were any survivors besides this man…*

[P22]
The last trace of unease vanished the moment I helped the exhausted middle-aged man to his feet.

[P23]
Ding.

[P24]
> **System**
>
> - You completed the **Survivors of the Sakju Branch** Quest!
> - A Chain Quest has been created!
> - You leveled up!
> - You leveled up!
> - Merit and Fame increase!

[P25]
* * *

[P26]
“Whew.”

[P27]
The middle-aged man exhaled. He had only circulated his qi briefly, but he seemed to have recovered enough strength to look much better.

[P28]
He rose and respectfully clasped his hands in salute.

[P29]
“Benefactor, you saved us all.”

[P30]
“Not at all. I only did what needed to be done.”

[P31]
These days, lies came pouring out whenever I opened my mouth. Then again, it wasn’t entirely untrue. I had to clear the Quest somehow.

[P32]
*If anything, I should be the one bowing and thanking them.*

[P33]
Still, Santa Claus—or rather, the survivors—seemed deeply moved by my attitude.

[P34]
“Outstanding martial arts and a sense of chivalry, too. I, Gong Yacheong, sincerely admire you.”

[P35]
“Socheon and Soyul owe you a great debt, Great Hero.”

[P36]
Thanks to that, I learned their names. The middle-aged man was Gong Yacheong, and the young siblings were Socheon and Soyul.

[P37]
“If it isn’t too impertinent, may I ask our Benefactor’s name?”

[P38]
“My name is…”

[P39]
A sudden thought flashed through my mind.

[P40]
*Wait. If they hear my name, won’t they come running at me with swords?*

[P41]
Whatever conspiracy lay behind it, the person who had lit the fuse on this war was none other than yours truly, Jin Taekyung. I doubted two people who had lost their home and family would feel particularly kindly toward me.

[P42]
*Right. This calls for a well-intentioned lie.*

[P43]
“Hong Gil-dong. My name is Hong Gil-dong.”[^1]

[P44]
“Hong Gil-dong… I’ve never heard that name before. But I can feel the bearing of a hero.”

[P45]
Socheon chimed in from the side.

[P46]
“Here one moment, there the next. It sounds like the name of someone who appears and disappears like a ghost.”

[P47]
*…How did that kid know?*

[P48]
Before he could bring up the part about calling one’s father Father and one’s elder brother Brother,[^2] I hurriedly changed the subject.

[P49]
“More importantly, what happened?”

[P50]
Dark shadows fell across both their faces.

[P51]
Gong Yacheong spoke first.

[P52]
“It happened only a few days ago.”

[P53]
By the time the carrier pigeon bearing word of the war arrived, the Sakju Branch had already been surrounded so tightly that not even a drop of water could slip through. Wandering martial artists hired by the Mount Heng Sword Sect slaughtered the people and burned the buildings.

[P54]
“There were a full hundred of them. The Branch Leader and the martial artists under his command bought us enough time to escape through a secret passage. Most of those who got out were women and children who knew no martial arts.”

[P55]
I didn’t need to ask what had happened to the others.

[P56]
The System was absolute and factual. The three people here were the only survivors of the Sakju Branch identified by the Quest Window.

[P57]
“I want to know about the enemy.”

[P58]
“They’re wandering martial artists.”

[P59]
“Wandering martial artists?”

[P60]
“As you know, they’re bastards who’ll do anything for money. The especially vile ones among them took a commission from the Mount Heng Sword Sect and attacked us.”

[P61]
“They seemed pretty weak for such vile bastards.”

[P62]
“Do good and evil determine who is strong and who is weak? The men they hired this time were ordinary wandering martial artists, common as dirt. Their leader was the problem.”

[P63]
Gong Yacheong gritted his teeth.

[P64]
“Jopil, One Question, One Kill. That was the man. The Branch Leader sensed defeat the moment he saw him and entrusted his family members to me.”

[P65]
Socheon’s small fists trembled.

[P66]
“I’ll tear him limb from limb and kill him with my own hands.”

[P67]
It was an unusual choice of words for a kid, but understandable given the grudge carved into his bones.

[P68]
I gently patted Socheon on the head.

[P69]
“That is exactly what will happen. I’ll help you.”

[P70]
“Really?”

[P71]
“A man’s word is worth a thousand pieces of gold. Do you think I’d say one thing and do another? I’ll definitely catch that bastard and level u—”

[P72]
“Huh?”

[P73]
“No, I mean I’ll kill him and avenge your grudge.”

[P74]
“Ah… Thank you. Thank you so much, Great Hero Hong!”

[P75]
“Thank you. Truly, thank you!”

[P76]
They thanked me over and over. I felt like a complete scumbag, and a sharp stab tore through one corner of my chest.

[P77]
*No. They’ll be happy when their enemy dies, and I’ll be happy when I level up. It’s mutually beneficial. Mutually beneficial.*

[P78]
After forcing myself to accept that justification, I asked, “How many of them are there?”

[P79]
“While we were trying to determine the enemies’ position, I overheard them talking. They said there were about thirty, including Jopil.”

[P80]
“Thirty? Thirty men?”

[P81]
“That’s right. So we need to flee at once…”

[P82]
Gong Yacheong’s voice faded into the distance. In its place, a faint sound from far away drew closer.

[P83]
Ding. Ding. Ding.

[P84]
I could hear it. The sound of leveling up. The sound of logging out!

[P85]
Suppressing the corners of my mouth as they kept creeping upward, I said,

[P86]
“Let’s wait here for the rest of them.”

[P87]
“Wait? What do you mean?”

[P88]
“Wipe them all out! We can’t let such vile bastards live!”

[P89]
“No, Great Hero Hong, listen to me…”

[P90]
“A master like you can do it! Thank you, Benefactor!”

[P91]
Socheon rushed into my arms with tears in his eyes. I spread my arms and pulled him into a hug.

[P92]
“That’s right. Let’s kill them all!”

[P93]
“Let’s kill them!”

[P94]
“Jopil, you son of a bitch!”

[P95]
“Son of a bitch!”

[P96]
That was when Gong Yacheong spoke.

[P97]
“Jopil is a Peak master.”

[P98]
“Jopil, you fucking son of a—huh?”

[P99]
“Jopil, One Question, One Kill. He’s one of the few Peak masters in all of Shanxi. Why do you think he has survived this long despite being tangled up in all kinds of grudges and vendettas?”

[P100]
“Don’t tell me…”

[P101]
“Everyone who challenged him died. That’s the kind of man Jopil is. Cruel—and every bit as strong.”

[P102]
“Ah.”

[P103]
Sensing something was wrong, Socheon looked up at me.

[P104]
“Socheon.”

[P105]
“Yes, Great Hero.”

[P106]
“Now that I think about it, this probably isn’t the right time.”

[P107]
“Huh?”

[P108]
“I was being foolish. Our first priority should be getting you and your sister safely back to our family. Right?”

[P109]
“…”

[P110]
“I was also injured in the fight earlier, and my men are exhausted. It would probably be a difficult battle.”

[P111]
Socheon looked me up and down. My clothes were drenched in the enemies’ blood, but they were perfectly intact, without a single tear. There was no way I could have been injured.

[P112]
“I have an internal injury.”

[P113]
“…”

[P114]
He turned toward the reconnaissance squad. They hadn’t swung their swords even once before the fight ended and were so fresh they looked ready to fly.

[P115]
“What you see isn’t everything.”

[P116]
“…Great Hero.”

[P117]
I slipped Socheon off me and shouted,

[P118]
“We’re returning to the main family. Everyone, prepare to leave!”

[P119]
I hurried back toward the squad, but Socheon’s hand clutched my collar tightly and refused to let go. Tears glimmered in his round eyes.

[P120]
“Great Hero.”

[P121]
“Hey, why aren’t you moving? Move, move! Socheon, I’m a little busy right now, so let’s talk later. Okay?”

[P122]
“Great Heeero.”

[P123]
“Mister Gong Yacheong. No, Great Hero Gong, what are you doing? Every second counts.”

[P124]
“…Socheon, come here.”

[P125]
Gong Yacheong looked at me as if I were an idiot and pulled Socheon away. His hand came between me and Socheon like a guardian blocking a criminal.

[P126]
Socheon almost wailed.

[P127]
“Great Hero Hong Gil-dooong!”

[P128]
And that was the starting gun.

[P129]
Boom!

[P130]
With a thunderous crash, the cabin door was smashed apart, and someone burst in.

[P131]
> **System**
>
> - **Level 22 Hyuk Mujin**

[P132]
“Jin Taekyung, you fucking bastard!”

[P133]
Hyuk Mujin huffed and puffed, his furious eyes fixed squarely on me. Gong Yacheong and Socheon stared at me blankly.

[P134]
“Great Hero Hong?”

[P135]
“Great Hero Hong Gil-dong?”

[P136]
“Ah. Well. You see…”

[P137]
*…Fuck.*

[P138]
* * *

[P139]
“Hmm.”

[P140]
Jopil stared down at the corpse. The face was twisted, its eyes wide open. Frozen beneath blood and snow, the man had been known by the nickname Black Mountain Blade.

[P141]
“Tsk, tsk. How did you end up like this, friend?”

[P142]
He had been loyal and clever. Jopil had never imagined he would die so pointlessly.

[P143]
“See? Haven’t I told you time and again to walk around with both eyes wide open?”

[P144]
Jopil grabbed Black Mountain Blade’s wide-open eyes and pried them even farther open.

[P145]
A horrible sound escaped as the frozen flesh tore.

[P146]
Rip. Riiip.

[P147]
The others watched without even daring to breathe.

[P148]
His expression and tone were no different from usual, but they could feel to their bones that Jopil was furious.

[P149]
The killing intent pouring from the Peak master choked the breath from their throats and sent cold sweat trickling down their backs.

[P150]
*No wonder.*

[P151]
More than twenty men had been wiped out. And all on a mission to deal with the remnants of the Sakju Branch.

[P152]
One Question, One Kill. Jopil was a bizarre man who always asked an enemy he liked exactly one question before killing them.

[P153]
The wandering martial artists considered Black Mountain Blade lucky to be dead. Had he survived, he would have suffered something far more horrifying.

[P154]
“That’s better.”

[P155]
Jopil wiped the blood on the waist of his trousers and rose.

[P156]
“Well, what does everyone think? Tell me without holding back.”

[P157]
“We should obviously follow the order.”

[P158]
One man stepped forward. The neatly dressed, dignified middle-aged man and the ten-odd martial artists standing at attention behind him were the overseers and guides the Mount Heng Sword Sect had sent to keep the wandering martial artists under control.

[P159]
Jopil smiled faintly.

[P160]
“Ah, yes. I’d forgotten our great Mount Heng Sword Sect Hall Master was here. But what’s this about an order?”

[P161]
“Wipe out the Sakju Branch and join the main force. Have you already forgotten the Young Sect Leader’s order?”

[P162]
“An order? I remember accepting a commission.”

[P163]
“Isn’t that the same thing?”

[P164]
The middle-aged man glared at Jopil, displeased.

[P165]
“Coming this far was your own unilateral decision in the first place. And what came of it? You lost more than twenty subordinates to the remnants of a single branch!”

[P166]
“Which is why we should pursue them. We can finish them off in half a day.”

[P167]
“Jeongyang might be another matter, but if you pursue them as far as Honju, we risk a counterattack. I won’t permit any more unilateral decisions.”

[P168]
“Permission. Permission…”

[P169]
Jopil mulled the word over, then spoke.

[P170]
“No. That won’t do. I don’t like it.”

[P171]
“What do you mea—”

[P172]
Crunch.

[P173]
The middle-aged man’s neck shattered, and he died before he could finish speaking. Jopil had twisted it at blinding speed. He licked his lips.

[P174]
“I like war. No matter who dies, they’re forgotten.”

[P175]
“You bastard!”

[P176]
The Mount Heng Sword Sect’s martial artists realized what had happened and drew their weapons, but Jopil had already plunged into their midst.

[P177]
Crunch! Slash!

[P178]
Warm blood poured onto the snowfield. Every time Jopil rampaged like a wild beast, someone’s neck, arm, or leg was torn free and sent flying.

[P179]
“Gaaah…”

[P180]
An unnamed martial artist’s groan was the last sound.

[P181]
Standing atop the heap of corpses, Jopil spoke into the crushing silence.

[P182]
“We’re pursuing them.”

[P183]
This time, no one said a word. As his subordinates hurried to prepare as though fleeing for their lives, Jopil continued to stare at the bodies.

[P184]
*What kind of man was he?*

[P185]
Jopil was a Peak master. From the scars on the corpses and the footprints, he could picture what his opponent looked like.

[P186]
A single man. A highly skilled spearman had been here, and he was the one who had slaughtered the other twenty-odd men.

[P187]
*He killed Black Mountain Blade in one strike. How could he be anything less?*

[P188]
The final strike that pierced through Black Mountain Blade’s chest had been particularly interesting.

[P189]
*This should be a fun fight.*

[P190]
Who was he? A master of the Jin Family of Taiyuan? Or someone unknown?

[P191]
It didn’t matter. Jopil let out a pleased laugh.

[P192]
“Let’s meet soon, friend.”

[P193]
* * *

[P194]
“What news has come in?”

[P195]
“None, sir. All we can do is move as quickly as possible…”

[P196]
“Damn it! Damn it!”

[P197]
Wipeng seethed with frustration, but there was nothing else he could do. As his subordinate had said, their only option was to find the Third Young Master as quickly as possible and protect him.

[P198]
*Jopil, One Question, One Kill…*

[P199]
Wipeng knew the man’s reputation well. If the Third Young Master fell into his hands, death would be the only possible outcome.

[P200]
*If that happens, I won’t be able to face my lord.*

[P201]
Jin Wikyung endured with superhuman patience.

[P202]
He was currently the head and center of the Jin Family of Taiyuan. He had placed the younger brother he loved more than anyone and hundreds of family members on the scales, and after much deliberation, he had sent his most trusted subordinate, Wipeng, to his brother.

[P203]
*But if I fail…*

[P204]
*I won’t be able to face my lord.*

[P205]
Wipeng’s grip tightened on the reins. He spurred his horse onward. More than twenty mounted riders followed in a long line behind him.

[P206]
[^1]: Hong Gil-dong is a legendary Korean outlaw and folk hero.

[P207]
[^2]: In the Hong Gil-dong tale, he demands the right to address his father as “Father” and his elder brother as “Brother.”
```


## Accepted baseline for regression comparison

This is the accepted English copy before mastering. Use it as a regression
anchor: report a finding when the assembled copy loses an established term,
source-specific image, formatting convention, continuity fact, or other detail
that the baseline preserved, unless the Korean source clearly requires the
change.

```markdown
[P1]
# Chapter 25

[P2]
“Is this the afterlife?”

[P3]
That was the first thing the middle-aged man said when he woke up.

[P4]
Before I could answer, something small sprang forward and threw itself into his arms.

[P5]
The child, tears dangling from the corners of his eyes, shouted.

[P6]
“Uncle Gong!”

[P7]
“Socheon! You’re safe. But what in the world…?”

[P8]
The confused middle-aged man listened as the child explained through sobs. When he heard that we had met on the hill and that all the enemies had died by my hand, his eyes widened.

[P9]
“Are you from the main family?”

[P10]
“Yes. That’s right.”

[P11]
“Ah, Heaven has helped us!”

[P12]
“…”

[P13]
*I helped you, you old man.*

[P14]
“I was sure I’d fallen to the bottom of the mountain… I thought that was the end of me.”

[P15]
“You nearly did. You were lucky.”

[P16]
I pointed below the ridge. Two corpses presumed to belong to the enemy lay with their heads buried in trees.

[P17]
If the grass along the path where he had slipped had not been so thick, he would have ended up just like them.

[P18]
*I didn’t realize it at first, either.*

[P19]
I only became aware of the middle-aged man’s presence thanks to the Quest window.

[P20]
Even after I defeated all the enemies, the **Survivors of the Sakju Branch** Quest had not been completed. That meant there were more survivors.

[P21]
*The question was whether there were any survivors besides this man…*

[P22]
The last trace of unease vanished the moment I helped the exhausted middle-aged man to his feet.

[P23]
Ding.

[P24]
> **System**
>
- You completed the **Survivors of the Sakju Branch** Quest!
> - A Chain Quest has been created!
> - You leveled up!
> - You leveled up!
> - Merit and Fame increase!

[P25]
* * *

[P26]
“Whew.”

[P27]
The middle-aged man exhaled. Though he had only circulated his qi briefly, his complexion had improved noticeably.

[P28]
He rose and respectfully clasped his hands in a salute.

[P29]
“Benefactor, you saved everyone.”

[P30]
“Not at all. I only did what anyone should have done.”

[P31]
Every time I opened my mouth, lies came spilling out. It wasn’t entirely wrong, either. I had to clear the Quest somehow.

[P32]
*If anything, I’m the one who should be bowing to them and thanking them.*

[P33]
Still, Santa Claus—or rather, the survivors—seemed deeply moved by my attitude.

[P34]
“Outstanding martial arts and a sense of chivalry, too. I, Gong Yacheong, sincerely admire you.”

[P35]
“Socheon and Soyul owe Great Hero an enormous debt of gratitude.”

[P36]
Thanks to that, I learned their names. The middle-aged man was Gong Yacheong, and the young siblings were Socheon and Soyul.

[P37]
“If it isn’t too impertinent, may I ask our Benefactor’s name?”

[P38]
“My name is…”

[P39]
Then I had a thought.

[P40]
*Wait. If I tell them my name, won’t they come running at me with swords?*

[P41]
Whatever conspiracy had been involved, the person who had lit the fuse on this war was none other than me, Jin Taekyung. It was hard to believe that two people who had lost their home and family would look kindly on me.

[P42]
*Yes. This is the moment for a well-intentioned lie.*

[P43]
“Hong Gil-dong. My name is Hong Gil-dong.”[^1]

[P44]
“Hong Gil-dong… I’ve never heard that name before. But I can feel the bearing of a hero.”

[P45]
Socheon chimed in from the side.

[P46]
“Here one moment, there the next. It sounds like the name of someone who appears and disappears like a ghost.”

[P47]
*…How did that kid know?*

[P48]
Before he could bring up the tale’s business about calling one’s father Father and one’s elder brother Brother,[^2] I hurriedly changed the subject.

[P49]
“More importantly, what happened?”

[P50]
Dark shadows fell across both their faces.

[P51]
Gong Yacheong spoke first.

[P52]
“It happened only a few days ago.”

[P53]
By the time the carrier pigeon bearing word of war arrived, the Sakju Branch had already been surrounded so tightly that not even a drop of water could get through. The wandering martial artists hired by the Mount Heng Sword Sect had slaughtered people and burned down the buildings.

[P54]
“There must have been a full hundred of them. Thanks to the Branch Leader and the martial artists under him buying us time, we were able to escape through a secret passage. Most of those who escaped were women and children who knew no martial arts.”

[P55]
I didn’t need to ask what had happened to the others.

[P56]
The System was absolute and factual. Those three were all the survivors of the Sakju Branch identified by the Quest Window.

[P57]
“I want to know about the enemy.”

[P58]
“They’re wandering martial artists.”

[P59]
“Wandering martial artists?”

[P60]
“As you know, they’re bastards who’ll do anything for money. The especially vile ones among them were hired by the Mount Heng Sword Sect to attack us.”

[P61]
“They seemed pretty weak for such vile bastards.”

[P62]
“Do good and evil determine who is strong and who is weak? The ones they hired this time were ordinary wandering martial artists, common as dirt. The leader was the problem.”

[P63]
Gong Yacheong gritted his teeth.

[P64]
“Jopil, One Question, One Kill. That was the man. The Branch Leader sensed defeat the moment he saw him and entrusted his family members to me.”

[P65]
Socheon’s small fists trembled.

[P66]
“I’ll tear him limb from limb and kill him with my own hands.”

[P67]
That was an unusual choice of words for a child, but considering the grudge carved into his bones, it was understandable.

[P68]
I gently patted Socheon on the head.

[P69]
“That is exactly what will happen. I’ll help you.”

[P70]
“Really?”

[P71]
“A man’s word is worth a thousand pieces of gold. Do you think I’d say one thing and do another? I’ll definitely catch that bastard and level u—”

[P72]
“Huh?”

[P73]
“No, I mean I’ll kill him and avenge your grudge.”

[P74]
“Ah… Thank you. Thank you so much, Great Hero Hong!”

[P75]
“Thank you. Truly, thank you!”

[P76]
The two of them repeatedly expressed their gratitude. I felt like a real scumbag, and a sharp stab tore through one corner of my chest.

[P77]
*No. They’ll be happy when their enemy dies, and I’ll be happy when I level up. It’s mutually beneficial. Mutually beneficial.*

[P78]
I forced myself to accept that justification and asked,

[P79]
“How many of them are there?”

[P80]
“While we were trying to determine the enemies’ position, I overheard them talking. They said there were about thirty, including Jopil.”

[P81]
“Thirty? Thirty men?”

[P82]
“That’s right. So we need to flee at once…”

[P83]
Gong Yacheong’s voice began to fade. In its place, a faint sound from far away drew closer.

[P84]
Ding. Ding. Ding.

[P85]
I could hear it. The sound of leveling up. The sound of logging out!

[P86]
Suppressing the corners of my mouth as they kept creeping upward, I said,

[P87]
“Let’s wait here for the rest of them.”

[P88]
“Wait? What do you mean?”

[P89]
“Wipe them all out! We can’t let such vile bastards live!”

[P90]
“No, Great Hero Hong, listen to me…”

[P91]
“A master like you can do it! Thank you, Benefactor!”

[P92]
Socheon came running into my arms with tears in his eyes. I opened both arms and pulled him into a hug.

[P93]
“That’s right. Let’s kill them all!”

[P94]
“Let’s kill them!”

[P95]
“Jopil, you son of a bitch!”

[P96]
“Son of a bitch!”

[P97]
That was when Gong Yacheong spoke.

[P98]
“Jopil is a Peak master.”

[P99]
“Jopil is a fucking bast—huh?”

[P100]
“Jopil, One Question, One Kill. He’s one of the few Peak masters in all of Shanxi. What do you think is the reason he has survived until now, despite being tangled up in all kinds of grudges and vendettas?”

[P101]
“Don’t tell me…”

[P102]
“Everyone who challenged him died. That’s the kind of man Jopil is. Cruel—and every bit as strong.”

[P103]
“Ah.”

[P104]
Sensing that something was wrong, Socheon looked up at me.

[P105]
“Socheon.”

[P106]
“Yes, Great Hero.”

[P107]
“Now that I think about it, this probably isn’t the right time.”

[P108]
“Huh?”

[P109]
“I was being foolish. The priority should be getting you and your sister safely back to our family. Right?”

[P110]
“…”

[P111]
“I was injured during the fight earlier, too, and my men are exhausted. It looks like it would be a difficult battle.”

[P112]
Socheon looked me up and down. My clothes were soaked in the enemies’ blood, but they were perfectly intact, without a single tear. There was no way I could have been injured.

[P113]
“I have an internal injury.”

[P114]
“…”

[P115]
He turned to the reconnaissance squad. They had not even swung their swords once, and they were bursting with energy.

[P116]
“What you see isn’t everything.”

[P117]
“…Great Hero.”

[P118]
I slipped Socheon off me and shouted,

[P119]
“We’re returning to the main family. Everyone, prepare to leave!”

[P120]
I hurried back toward the squad, but Socheon’s hand clutched my collar tightly and refused to let go. Tears glimmered in his round eyes.

[P121]
“Great Hero.”

[P122]
“Hey, why aren’t you moving? Move, move! Socheon, I’m a little busy right now, so let’s talk later. Okay?”

[P123]
“Great Heeero.”

[P124]
“Mister Gong Yacheong. No, Great Hero Gong, what are you doing? Every second counts.”

[P125]
“…Socheon, come here.”

[P126]
Gong Yacheong looked at me as if I were an idiot and pulled Socheon away. His hand came between me and Socheon like a guardian blocking a criminal.

[P127]
Socheon almost wailed.

[P128]
“Great Hero Hong Gil-dooong!”

[P129]
And that was the starting gun.

[P130]
With a thunderous boom, the cabin door was smashed apart, and someone burst in.

[P131]
> **System**
>
> - **Level 22 Hyuk Mujin**

[P132]
“Jin Taekyung, you fucking bastard!”

[P133]
Hyuk Mujin huffed and puffed, his furious eyes locked on me. Gong Yacheong and Socheon stared at me with blank expressions.

[P134]
“Great Hero Hong?”

[P135]
“Great Hero Hong Gil-dong?”

[P136]
“Ah. Well, you see…”

[P137]
*…Fuck.*

[P138]
[^1]: Hong Gil-dong is a legendary Korean outlaw and folk hero.

[P139]
[^2]: In the Hong Gil-dong tale, he demands the right to address his father as “Father” and his elder brother as “Brother.”

[P140]
* * *

[P141]
“Hmm.”

[P142]
Jopil stared down at the corpse. The face was twisted, its eyes wide open. Frozen beneath blood and snow, the man had been known by the nickname Black Mountain Blade.

[P143]
“Tsk, tsk. How did you end up like this, friend?”

[P144]
He had been loyal and clever. Jopil had never imagined he would die so pointlessly.

[P145]
“See? Haven’t I always told you to walk around with both eyes wide open?”

[P146]
Jopil grabbed Black Mountain Blade’s bulging eyes and pried them farther open.

[P147]
A horrible sound escaped as the frozen flesh tore.

[P148]
Rip. Riiip.

[P149]
The others watched without even daring to breathe.

[P150]
His expression and tone were no different from usual, but they could feel to their bones that Jopil was furious.

[P151]
The killing intent radiating from a Peak master made it hard to breathe, and cold sweat trickled down their backs.

[P152]
*It was understandable.*

[P153]
More than twenty men had been wiped out. And all on a mission to deal with the remnants of the Sakju Branch.

[P154]
Jopil, One Question, One Kill, was a bizarre man. Whenever he encountered an enemy he liked, he asked exactly one question before killing them.

[P155]
The wandering martial artists thought it was fortunate that Black Mountain Blade was dead. If he had still been alive, they would have suffered something even more horrifying.

[P156]
“That’s better.”

[P157]
Jopil wiped the blood on his trousers and rose.

[P158]
“Well, what does everyone think? Tell me without holding back.”

[P159]
“We should obviously follow the order.”

[P160]
One man stepped forward. The neatly dressed, dignified middle-aged man and the ten-odd martial artists standing at attention behind him were the overseers and guides the Mount Heng Sword Sect had sent to keep the wandering martial artists under control.

[P161]
Jopil smiled faintly.

[P162]
“Ah, yes. I’d forgotten our Mount Heng Sword Sect Hall Master was here. But what’s this about an order?”

[P163]
“Wipe out the Sakju Branch and join the main force. Have you already forgotten the Young Sect Leader’s order?”

[P164]
“An order? I remember accepting a commission.”

[P165]
“Isn’t that the same thing?”

[P166]
The middle-aged man glared at Jopil, displeased.

[P167]
“Coming here in the first place was your own arbitrary decision. And what came of it? You lost more than twenty subordinates to the remnants of a single branch!”

[P168]
“Then we should pursue them. We can finish them off in half a day.”

[P169]
“Jeongyang might be another matter, but if you pursue them as far as Honju, we risk a counterattack. I won’t permit any more unilateral decisions.”

[P170]
“Permission. Permission…”

[P171]
After mulling it over, Jopil spoke.

[P172]
“No. That won’t do. I don’t like it.”

[P173]
“What do you mea—”

[P174]
Crunch.

[P175]
The middle-aged man’s neck shattered, and he died before he could finish speaking. Jopil had twisted it at blinding speed. He licked his lips.

[P176]
“I like war. No matter who dies, people forget.”

[P177]
“You bastard!”

[P178]
The Mount Heng Sword Sect’s martial artists realized what had happened and drew their weapons, but Jopil had already plunged into their midst.

[P179]
Crunch. Slash!

[P180]
Warm blood poured onto the snowfield. Every time Jopil rampaged like a wild beast, someone’s neck, arm, or leg was torn free and sent flying.

[P181]
“Gaaah…”

[P182]
The groan of an unnamed martial artist was the last sound.

[P183]
Standing atop the heap of corpses, Jopil spoke into the crushing silence.

[P184]
“We’re pursuing them.”

[P185]
This time, no one said a word. As his subordinates hurried to prepare as though fleeing for their lives, Jopil continued to stare at the bodies.

[P186]
*What kind of man was it?*

[P187]
Jopil was a Peak master. From the scars on the corpses and the footprints, he could picture what his opponent looked like.

[P188]
*Only one man.*

[P189]
A highly skilled spearman had been here. He was the one who had slaughtered the other twenty-plus men.

[P190]
*If he killed Black Mountain Blade in one strike, he must be something else.*

[P191]
The final strike that pierced through Black Mountain Blade’s chest had been particularly interesting.

[P192]
*This should be a fun fight.*

[P193]
Who was he? A master from the Jin Family of Taiyuan? Or someone unknown?

[P194]
It didn’t matter. Jopil let out a pleased laugh.

[P195]
“Let’s meet soon, friend.”

[P196]
* * *

[P197]
“What news have we received?”

[P198]
“None, sir. All we can do is move as quickly as possible…”

[P199]
“Damn it! Damn it!”

[P200]
Wipeng was furious. But there was nothing he could do. As his subordinate had said, the only thing they could do was find the Third Young Master and protect him.

[P201]
*Jopil, One Question, One Kill…*

[P202]
Wipeng knew the man’s reputation well. If the Third Young Master fell into his hands, death would be the only possible outcome.

[P203]
*If that happens, I won’t be able to face my lord.*

[P204]
Jin Wikyung endured with superhuman patience.

[P205]
He was currently at the head of the Jin Family of Taiyuan, its central pillar. He had placed his beloved younger brother and hundreds of family members on the scales, and after much deliberation, he had sent his most trusted subordinate, Wipeng, to his brother.

[P206]
*But if I fail…*

[P207]
*I won’t be able to face my lord.*

[P208]
Wipeng’s grip tightened on the reins. He spurred his horse onward. More than twenty mounted riders followed in a long line behind him.
```


## Deterministic QA

```json
{
  "version": 1,
  "chapter": 25,
  "passed": true,
  "metrics": {
    "source_characters": 6343,
    "translation_characters": 14346,
    "length_ratio": 2.262,
    "source_paragraphs": 207,
    "translation_paragraphs": 207
  },
  "errors": [],
  "warnings": [
    {
      "code": "terminology",
      "message": "matched preferred term is absent",
      "details": {
        "korean": "운기조식",
        "preferred": "circulate one's qi"
      }
    },
    {
      "code": "terminology",
      "message": "matched preferred term is absent",
      "details": {
        "korean": "상태",
        "preferred": "Status"
      }
    },
    {
      "code": "terminology",
      "message": "matched preferred term is absent",
      "details": {
        "korean": "로그아웃",
        "preferred": "Logout"
      }
    },
    {
      "code": "terminology",
      "message": "matched preferred term is absent",
      "details": {
        "korean": "대협",
        "preferred": "Great Hero or Sir depending tone"
      }
    }
  ]
}
```

## Binding editorial rules

# Translation Rules

## Fidelity

- Translate the Korean source—not the wiki, manhwa, fan translations, or expected plot.
- Semantic fidelity outranks elegance. Never improve rhythm, humor, or localization by changing a physical action, negation, relationship, hierarchy, mechanism, quantity, or causal detail.
- Preserve every fact, causal link, joke, emotional beat, repetition, and intentional omission. Add nothing.
- Preserve small action verbs and pragmatic cues exactly: nodding versus shaking one's head, pretending nothing happened, and mild or approachable impressions are characterization, not expendable texture.
- Preserve viewpoint and tense. Resolve omitted subjects only when context supports it; retain genuine ambiguity.
- Match each speaker's hierarchy, intimacy, humor, and profanity naturally. Do not mechanically retain every honorific or classical self-reference.
- Do not censor or soften content.

## Terminology

- `compendium.md` and `docs/NAMES.md` are binding for established names, titles, ranks, techniques, organizations, system terms, items, and locations. Profile headings and aliases join that ledger.
- Search only exact Korean terms already present in the current chapter; the compendium contains future-sensitive entries.
- Never re-romanize established names or invent grand names for uncertain terms. First use of an unlisted name or title almost always needs a footnote or a mapped ledger term.
- Use `qi` for Murim energy and `mana` for the modern Hunter system when the source distinguishes them. Preserve an established chapter-specific rendering such as `internal energy` when the exact glossary and surrounding Korean distinguish accumulated `공력` from resulting `기운`.
- In System panels, render `등급` as `**Grade:**` for quest, item, skill, and martial-art classifications. Reserve `rank` for Hunter classifications or ordinary prose; never replace a System `Grade` field with `Rank`.

## English and Markdown

- Use contemporary US English and natural action-comedy prose; avoid Korean syntax calques and generic cultivation MTL phrasing.
- File: `translations/NNNN.md`; heading: `# Chapter N`.
- Speech: curly double quotes. Direct thoughts: italics without quotes.
- Use em dashes without spaces, the ellipsis character `…`, and `* * *` for source scene breaks.
- Format each actual game System-message panel as one Markdown blockquote window headed `> **System**`. Keep all consecutive notices, fields, and lines inside that same blockquote; separate windows when prose intervenes. Do not enclose System notices or UI terms in square brackets; the `System` heading and framed blockquote identify the panel. Do not label manuals, ordinary quotations, warnings printed in a manual, or other non-System material as `System`; use a normal blockquote or a specific heading instead. Do not wrap each complete notice in outer `**`; retain bold only for meaningful labels or emphasis inside the panel.
- Keep the final file English-only reading copy: no audit notes, Korean text, summaries, or model metadata.

### Tone and Style

- Write like a polished commercial webnovel: brisk, vivid, accessible, and easy to read aloud.
- Preserve the series’ contrast between danger and comedy. Let absurdity, bad timing, blunt reactions, and grim situations create dark humor without adding jokes absent from the Korean.
- Jin Taekyung’s narration is conversational, observant, self-mocking, and occasionally profane. It may be irreverent even when the situation is serious.
- Keep deadpan punchlines short and well-timed. Do not explain a joke after delivering it.
- Preserve the source's level of explicitness. A euphemism may remain euphemistic even when its meaning is sexual or crude; do not replace it with more graphic English merely for impact.
- Make dialogue spontaneous and character-specific. Preserve hierarchy and intimacy through word choice, address, rhythm, and restraint—not archaic wuxia English.
- Use strong profanity when the Korean is strong, but neither intensify nor sanitize it. Do not make ordinary lines uniformly vulgar. Profanity should reveal mood or relationship.
- Keep action and injury vivid but clear rather than purple. Do not make violence funny unless the source’s framing does.
- Avoid stiff literalism, translator-added melodrama, dated internet slang, and quippy superhero-style banter.
- On the second pass, correct awkward English collocations and word choices without changing meaning or voice. Prefer ordinary, spoken English over stiff Latinate or ceremonial wording when the scene is brisk or comic: “goose bumps” rather than “gooseflesh,” and “laid into them” rather than “launched into a solemn denunciation.” Read the prose aloud and replace any phrase that sounds like a formal essay, legal document, or literal dictionary gloss unless the source deliberately calls for that register.

## Footnotes

Use `[^1]` Markdown footnotes when a brief, factual, spoiler-free explanation materially helps an English reader understand:

- a Korean institution, living arrangement, food, holiday, myth, historical reference, or local custom;
- a Korean word, phrase, idiom, wordplay, or culturally specific image that cannot be conveyed fully by the best natural English analogy;
- a deliberately literal rendering whose cultural or linguistic force would otherwise be lost.

For example, render `고시원` as “goshiwon” when the setting or connotations matter, with a concise footnote explaining that it is a very small, inexpensive room-for-rent housing arrangement. Prefer the best natural English analogy in the prose. Use a literal translation plus a concise footnote when the Korean wording itself matters. Define a term at its first meaningful occurrence and do not repeat the note unnecessarily. Footnotes must be rare, useful, and non-spoiling; do not footnote ordinary vocabulary, fully preserved jokes, or uncertainty. Record consequential uncertainty in `docs/STATE.md`.

## Spoilers and Scope

- Safe profiles contain only facts revealed through the latest completed chapter.
- Never read `characters/spoilers/` during drafting. Reviewers may consult one relevant sealed profile only for a specific unresolved continuity issue after the draft is complete.
- Future knowledge may prevent contradiction but may not add early names, pronouns, certainty, motives, or foreshadowing.
- Translate exactly one requested chapter unless the user explicitly requests a batch. Never modify Korean source files under `source/`.

# Master Editorial Brief

You are the final English-language editor of an existing Korean-to-English novel translation.

The Korean source is the authority for meaning. The existing English is the baseline you are editing, not a draft to discard. Your task is to make the chapter read like professionally written native English commercial fiction while preserving the author's exact story, characterization, humor, register, pacing, ambiguity, and cultural texture.

## Editorial authority

You may freely recast sentences and paragraphs when the English is stiff, literal, repetitive for accidental reasons, awkwardly collocated, over-explained, or syntactically shaped by Korean. You may tighten dialogue, improve rhythm, repair transitions, and make action easier to follow. A technically correct sentence may still need rewriting if a fluent English novelist would not naturally phrase it that way.

Do not change text merely to make it different. If the baseline is already strong, leave it alone.

The accepted baseline is also the project's style and terminology anchor. Do not
replace an established rendering, cultural term, System label, Markdown form, or
recurring phrase with a synonym merely because the synonym sounds smoother.
Make that change only when the Korean source, `RULES.md`, or the exact glossary
requires it. In particular, do not turn a source-specific image into a nearby
English image, or change a gold-spoon joke, item name, technique name, or UI
label into a different expression without source support.

## Fidelity constraints

Never invent, omit, explain away, generalize, intensify, soften, or reinterpret source-supported content. In particular, preserve:

- exact actions, subjects, objects, directionality, causality, quantities, and physical details;
- deliberate ambiguity, euphemism, implication, profanity level, repetition, and withheld information;
- jokes and comic specificity, even when a more generic English joke would sound smoother;
- hierarchy, kinship, forms of address, characterization, and speaker attitude;
- System mechanics, Murim concepts, names, ranks, techniques, items, organizations, and established terminology.
- chapter-level logical consistency: interpret labels, counters, notifications, and repeated facts from how they behave across the scene, not from an isolated surface gloss;
- idioms by their narrative function rather than their component words, and jokes with their setup, recognition, and punchline timing intact;
- cross-sentence implications: do not create a claim that contradicts “again,” an increasing value, an earlier action, or the explanation immediately around it;
- repeated terminology and formatting: once the baseline or glossary establishes a rendering, keep it consistent throughout the chapter unless the source clearly changes the sense;

Do not add jokes, metaphors, explanations, emotional conclusions, or colorful details that are absent from the Korean. Do not replace a specific source image with a generic equivalent merely because the generic version is smoother.

When natural English and literal form conflict, preserve the source meaning and pragmatic effect while changing the English form as much as necessary.

Before returning the chapter, perform a silent continuity pass: trace every
counter, quantity, repeated System label, item or technique name, joke setup and
payoff, and physical cause-and-effect sequence from the Korean through the
finished English. Correct any local sentence that contradicts the sequence.

## Relationship to project files

`RULES.md` is binding. `POLISH.md` describes known translation-English failure modes and should guide the edit. Exact glossary matches are binding unless the packet explicitly marks them otherwise. Character/continuity material is context only and must never override the chapter's Korean source.

## Output

Return only the complete edited English Markdown chapter. Preserve the required chapter heading and project Markdown conventions. Do not provide commentary, a change log, explanations, or a Markdown code fence.
