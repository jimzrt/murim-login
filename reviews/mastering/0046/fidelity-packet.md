# Fidelity Gate — Chapter 46

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
  1|＃46화
  2|
  3|
  4|
  5|치이이익.
  6|
  7|불판 위에 고기가 올라갔다. 붉고 두툼한, 마블링이 흰 눈꽃처럼 올올이 박혀 있는 최고급 한우다.
  8|
  9|형태, 소리, 냄새. 모두 황홀했다. 한 가지 마음에 안 드는 건 가격이었지만…….
 10|
 11|“이걸로 되겠어요? 먹고 더 시키죠. 특수 부위로.”
 12|
 13|돈 많은 C급 헌터님이 내는 거니까, 뭐.
 14|
 15|‘이게 얼마 만의 한우냐.’
 16|
 17|무림의 음식은 맵고 짜고 싱겁다. 그마저도 제대로 못 먹는 날이 더 많았다. 30일간 내 위장은 육포와 벽곡단, 주먹밥으로 혹사당했다.
 18|
 19|우걱. 우걱우걱.
 20|
 21|소고기의 좋은 점은 금방 먹을 수 있다는 거다. 대충 익었다 싶으면 그대로 입으로 직행.
 22|
 23|한번 씹을 때마다 구름 위를 걷는 기분이다. 이것도, 요것도, 저것도, 하나같이 천국의 맛이다.
 24|
 25|“흐어어.”
 26|
 27|그런 나를, 최 팀장은 특유의 묘한 표정으로 바라봤다.
 28|
 29|“더 드실래요?”
 30|
 31|“아뇨. 과식은 자제해야죠.”
 32|
 33|“지금 25인분짼데…….”
 34|
 35|“각자 12인분이면 그렇게 많지도 않네요.”
 36|
 37|“전 3인분밖에 안 먹었습니다.”
 38|
 39|“아, 육회 시켜도 돼요?”
 40|
 41|“……네.”
 42|
 43|“공깃밥도.”
 44|
 45|“…….”
 46|
 47|그렇게 폭풍 같은 식사가 끝난 뒤. 드디어 최 팀장의 입이 열렸다.
 48|
 49|“제가 잡았다고 했습니다. 제사장과 대전사, 둘 다.”
 50|
 51|“아, 감사합니다.”
 52|
 53|“천만에요. 정당한 거래라고 해 둡시다. 오히려 제가 감사한 부분도 있죠.”
 54|
 55|정당한 거래라.
 56|
 57|맞는 말이다. 나는 생각할 시간을 벌었고, 그는 명성을 얻게 될 것이다. 하급 헌터 다섯을 데리고 중급 레어 몬스터를 둘이나 잡았으니까.
 58|
 59|그 과정에서 사망자 하나 나오지 않았다는 사실은 길드 홍보에도 큰 도움이 될 테고.
 60|
 61|‘만약 내가 동기화로 힘을 찾지 못했다면?’
 62|
 63|글쎄, 누군가는 죽지 않았을까 싶다. 어쩌면 아무도 살아 나오지 못했을 수도 있고.
 64|
 65|“이미 그렇게 생각하고 계셨군요.”
 66|
 67|마냥 괴짜는 아니다. 이렇게 눈치가 빠른 걸 보면.
 68|
 69|나는 어색하게 웃었다.
 70|
 71|“서로에게 좋은 일이니까요.”
 72|
 73|“서로에게 좋다. 서로에게…….”
 74|
 75|중얼거리던 최 팀장이 불쑥 물었다.
 76|
 77|“길드 가입하실래요?”
 78|
 79|“푸웁.”
 80|
 81|식탁보를 들어 물을 막아 낸 최 팀장이 세련된 솜씨로 명함 한 장을 꺼냈다.
 82|
 83|
 84|
 85|[평화 길드 1팀장 최민우]
 86|
 87|
 88|
 89|뭐야, 이거. 순간 엄청 당황했다.
 90|
 91|“스, 스카우트 제의하신 건가요. 지금?”
 92|
 93|“그렇죠. 인재는 항상 필요하니까.”
 94|
 95|명함을 받아 든 나는 왠지 감개무량해졌다.
 96|
 97|새우처럼 허리 굽히고 다니면서 면접 보던 게 엊그제 같은데…….
 98|
 99|‘오래 살다 보니 별일이 다 있네.’
100|
101|무려 인재 취급받으면서 스카우트 제의라니. F급 헌터 진태경, 많이 컸다.
102|
103|“우리 길드가 아직 신생이고 인원수도 적긴 합니다만, 실속이 매우 훌륭합니다. 음, 예를 들자면…….”
104|
105|최 팀장이 우아하게 와인잔을 흔들었다. 세상에 저건 또 언제 시켰대.
106|
107|“재정이 굉장히 탄탄하죠.”
108|
109|“오오, 재정!”
110|
111|“그렇다 보니 직원 복지도 좋고요.”
112|
113|“오오, 탄탄한 재정을 바탕으로 한 복지!”
114|
115|“길드장님은 B급 헌터시고.”
116|
117|“오오, 탄탄한 재정의 원천인 상위 헌터!”
118|
119|“구조 조정 걱정은 없습니다.”
120|
121|“오오, 안정된 직장!”
122|
123|최 팀장이 부유한 미소를 머금고 물었다.
124|
125|“오시겠습니까?”
126|
127|나는 머리를 긁적였다.
128|
129|“아뇨. 그건 좀.”
130|
131|“……예?”
132|
133|“제가, 당장은 곤란한 사정이 있어서요. 시간이 필요합니다.”
134|
135|마음 같아서는 당장 계약서에 싸인, 도장, 지장, 키스 마크까지 남기고 싶다.
136|
137|‘하지만 내일 당장 시스템이 사라져 버리면?’
138|
139|바로 개털이다.
140|
141|하루아침에 인재(人才)에서 인재(人災) 소리 듣게 되는 거지.
142|
143|“혹시 돈 문제입니까?”
144|
145|돈 문제야 항상 있지.
146|
147|하지만 이건 더 중요한 문제다. 당장 눈앞의 돈뭉치에 홀려서 덥석 결정할 수 없다.
148|
149|“말씀드리기가 어렵네요. 아쉽지만 지금 당장 결정할 문제가 아닌…….”
150|
151|“일억.”
152|
153|“억?”
154|
155|“순수 계약금만. 나머지는 최소 C급 헌터 조건으로 맞춰 드리죠.”
156|
157|위험했다. 이번엔 진짜 위험했어.
158|
159|그러나 나는 초인적인 인내심으로 참았다. 세상살이가 그렇게 호락호락한 게 아니라는 건 진즉 깨닫지 않았나.
160|
161|먹고 체하는 돈이 될 수도 있다.
162|
163|“죄송합니다.”
164|
165|나를 물끄러미 바라보던 최 팀장은 이내 고개를 끄덕였다.
166|
167|“연락 기다리겠습니다.”
168|
169|
170|
171|* * *
172|
173|
174|
175|한 사람은 떠나고, 한 사람은 남았다.
176|
177|최 팀장, 아니 최민우는 진태경이 떠난 자리를 말없이 바라보다가 핸드폰을 꺼냈다.
178|
179|뚜, 뚜, 달칵.
180|
181|- 이 자식, 귀신이네. 안 그래도 연락하려고 했는데.
182|
183|“아까 말한 거, 어떻게 됐어?”
184|
185|- 일단 네 부탁이니까 알아보긴 했는데…… 이 진태경이라는 사람, 뭐 있냐?
186|
187|“그게 궁금해서 너한테 연락한 거지. 그래서 결과는?”
188|
189|- 널리고 널린 케이스지 뭐. 7년 전 스무 살에 각성, 측정 결과 F급. 헌터 훈련소에서 수석으로 수료한 기록이 있고…….
190|
191|수화기 너머로 진태경의 지난 7년이 흘러나왔다. 그러던 어느 순간, 최민우의 눈썹이 꿈틀했다.
192|
193|“뭐? 상동역 변이 게이트?”
194|
195|- 어. 너도 그 사건 알지?
196|
197|모를 리가 있나. 불과 2년 전의 일이라 최민우도 똑똑히 기억하고 있었다.
198|
199|- 그 사건 유일한 생존자더라고. 그 부분은 나도 확인하고 좀 놀랐다.
200|
201|최민우는 물잔을 기울였다. 중급 레어 몬스터를 단신으로 잡은 F급 헌터, 그 실마리를 잡았다고 생각하니 목이 탔다.
202|
203|“그리고?
204|
205|- 반년 동안 휴직. 관리청 쪽에서 조사관들 수시로 보내고, 뭐 이래저래 마음도 추스르고 했나 보더라고. 너도 알다시피 사안이 좀 컸으니까.
206|
207|“그래서?”
208|
209|- 그게 끝. 다시 길드 복직해서 일 년 반 동안 좆 빠지게 게이트 돌다가 잘렸어. 그게 딱 사흘 전이고.
210|
211|“잘린 이유는?”
212|
213|- 일단 구조 조정이긴 한데…… 코딱지만 한 중소 길드가 무슨. 아마 그 사건 영향이 클 거야. 관리청 눈치 슬금슬금 보다가 내보낸 거지. 그쪽 입장에서는 껄끄러울 테니까.
214|
215|“그게 끝이야?”
216|
217|- 내가 보기에는. 따로 파일 보내 줘?
218|
219|“바로 보내. 그럼 끊는다.”
220|
221|- 야, 야!
222|
223|뚝.
224|
225|최민우는 긴 손가락으로 탁자를 두드렸다.
226|
227|진태경. F급 헌터. 상동역 변이 게이트의 유일한 생존자.
228|
229|그리고…….
230|
231|‘최소 C급 헌터.’
232|
233|말 그대로 최소로 잡았을 때의 이야기다. C급 레어 몬스터를 혼자, 그것도 압도적인 힘과 기술로 몰아붙이던 그 모습이 눈앞에 아른거렸다.
234|
235|‘그런데 F급이란 말이지.’
236|
237|둘 중 하나다. 힘을 숨겼거나, 최근 재각성을 했거나.
238|
239|최민우는 후자라고 짐작했지만, 그것 역시 상식을 벗어난 일임에는 변함이 없었다.
240|
241|평생 승급 한 번 못 해 보고 은퇴하는 헌터가 한둘인가.
242|
243|F급에서 C급으로의 재각성은, 단언컨대 극히 드문 일이다.
244|
245|‘이게 무슨 게임도 아니고. 도대체 정체가 뭐야?’
246|
247|최민우는 고개를 저었다. 귀신에 홀린 기분이다.
248|
249|‘좀 더 알아봐야겠군.’
250|
251|자리에서 일어나는 그에게 사장이 다가와 계산서를 내밀었다.
252|
253|“193만 7천 원입니다.”
254|
255|“…….”
256|
257|정말 귀신에 홀린 기분이다.
258|
259|
260|
261|* * *
262|
263|
264|
265|“시바, 좆 됐다.”
266|
267|나는 털썩 주저앉았다. 너저분한 분리수거장. 응당 있어야 할 물건이 보이지 않았다.
268|
269|“없다, 없어. 내 캡슐이 없어.”
270|
271|최 팀장과 헤어질 때부터 초조하긴 했다. 하지만 반나절도 안 돼서 누가 가져갈 줄이야. 나는 허공을 향해 부르짖었다.
272|
273|“어떤 새끼야!”
274|
275|그리고 대답이 들려왔다.
276|
277|“나다, 이 십새끼야.”
278|
279|고시원 건물 옥상. 아침에 봤던 그 자리에서 진호 형이 담배를 피우고 있었다. 뭔가 아련한 표정으로 담배 연기를 뿜어낸 그가 말을 이었다.
280|
281|“내가 10년 동안 울면서 후회하고 다짐했는데…….”
282|
283|“진짜 울면서 후회하게 해 줘?”
284|
285|“재미없는 새끼. 너 이 영화 모르지?”
286|
287|“장난치지 마. 지금 심각하니까.”
288|
289|“왜, 오늘 허탕 쳤냐.”
290|
291|“아니.”
292|
293|나는 힘이 쭉 빠진 목소리로 말을 이었다.
294|
295|“캡슐.”
296|
297|“……엉?”
298|
299|“어떤 새끼가 내 캡슐 가져갔어.”
300|
301|“콜록, 콜록콜록!”
302|
303|담배 연기를 잘못 빨아들였는지 미친 듯이 기침하던 진호 형이 겨우 말문을 열었다.
304|
305|“그, 필요 없어서 버린 거 아니냐?”
306|
307|“그랬지.”
308|
309|시스템이 돌아오기 전까지는.
310|
311|불과 몇 시간 만에 상황이 이렇게 변하리라곤 나도 생각하지 못했다.
312|
313|‘하루만 더 갖고 있을걸.’
314|
315|어디서부터 찾아야 하나. 나는 한숨을 푹 내쉬었다.
316|
317|“형, 혹시 누가 가져갔는지 못 봤지?”
318|
319|“어…… 그게.”
320|
321|진호 형이 머리를 긁적였다.
322|
323|“봤다면 본 거고. 못 봤다면 못 본 건데.”
324|
325|이게 말이냐, 똥이냐.
326|
327|내가 노려보자 그가 쑥스럽다는 듯 웃었다.
328|
329|“그 뭐냐, 내가 사례금 같은 걸 바라는 건 절대 아니고…….”
330|
331|사례금을 바라는 게 절대 맞는 것 같은데.
332|
333|아무튼 그게 중요한 게 아니다. 나는 벌떡 일어나 물었다.
334|
335|“봤어? 확실해?”
336|
337|“굳이 따지자면 본 쪽이지.”
338|
339|“누구? 어디로 갔어!”
340|
341|“사례금을 바라는 건 아니지만, 예상 금액은 어느 정도?”
342|
343|“……10만 원?”
344|
345|“어이구, 나도 나이가 들었나. 기억이 가물가물하네.”
346|
347|“이런 시팔.”
348|
349|“그래, 날 더운데 수고해라.”
350|
351|“사례금은 십팔만 원입니다.”
352|
353|금액이 마음에 드는지 진호 형이 환하게 웃었다.
354|
355|“네 캡슐. 내가 주웠다.”
356|
357|“……?”
358|
359|이해하는 데 딱 3초 걸렸다.
360|
361|‘이런 날강도 같은 인간을 봤나.’
362|
363|기가 막히고 코가 막힌다. 이런 식으로 사람 뒤통수를 쳐?
364|
365|“근데 마땅히 놔둘 데가 없더라고. 내 방에 놓기에는 너무 좁잖아.”
366|
367|“그래서?”
368|
369|“네 방에 다시 놔뒀어. 잘했지?”
370|
371|저 인간을 어떻게 때려야 야무지게 때렸다고 소문이 날까.
372|
373|나는 주먹을 부르르 떨었다.
374|
375|
376|
377|* * *
378|
379|
380|
381|“진짜 있네.”
382|
383|아무 일도 없던 것처럼 원룸 절반을 차지한 캡슐을 보니 헛웃음만 나왔다.
384|
385|‘이걸 운이 좋다고 해야 하나.’
386|
387|그 많은 사람 중에서 캡슐을 가져간 게 진호 형이라니.
388|
389|나는 캡슐 뚜껑을 열었다. 낡은 좌석에 던지듯 넣어 놓은 사용 설명서를 집어 들어 마지막 페이지를 펼쳤다.
390|
391|
392|
393|[주요 기능]
394|
395|- 한 사람만을 위한 맞춤형 캡슐! 사용자 등록 시 캡슐이 영구 귀속되며, 이는 사망 전까지 유효합니다.
396|
397|
398|
399|……에이, 설마.
400|
401|‘단순한 우연이겠지.’
402|
403|하지만 찜찜함이 가시지 않는다. 나는 이 모든 사건의 근원인 캡슐을 노려보았다.
404|
405|‘이거 뭐 하는 물건이야?’
406|
407|오늘 아침 캡슐을 분리수거장에 버렸던 이유는 다 잊기 위함이었다. 가뜩이나 퍽퍽한 인생, 악몽 한 번 꿨다 생각하고 지금처럼 내 인생을 살기 위해서.
408|
409|하지만 이제는 상황이 달라졌다.
410|
411|‘시스템이 생겼으니까.’
412|
413|시스템이라…….
414|
415|그때 문득 생각나는 게 있었다. 나는 캡슐 표면에 손을 올리고 중얼거렸다.
416|
417|“아이템 확인.”
418|
419|띠링.
420|
421|그럼 그렇지. 입꼬리가 올라간 그 순간이었다.
422|
423|
424|
425|- 해당 아이템을 읽을 수 없습니다.
426|
427|
428|
429|“……읽을 수 없다고?”
430|
431|이런 경우는 처음이다.
432|
433|‘무림이 아니라서 그런가?’
434|
435|나는 당황스러운 마음에 방 안의 물건들을 닥치는 대로 확인했다. TV부터 볼펜, 심지어는 베개까지. 그때마다 시스템은 정확한 정보를 표시해 줬다.
436|
437|그런데 딱 하나. 캡슐만큼은 읽을 수 없다.
438|
439|“와, 이거 골 때리네.”
440|
441|혹시 싶어 사용 설명서를 집어 들었지만 역시나.
442|
443|띠링.
444|
445|
446|
447|- 해당 아이템을 읽을 수 없습니다.
448|
449|
450|
451|나는 침대에 벌렁 드러누웠다. 낡고 누렇게 찌든 천장을 멍하니 바라보며 생각했다.
452|
453|‘무슨 일이 벌어지고 있는 거야?’
454|
455|현재로서는 이해할 수 없는 일들이다. 하지만 한 가지는 확실했다.
456|
457|‘나는 강해졌다. 비교할 수 없을 정도로.’
458|
459|전신에 올올이 스며든 힘. 단전에서 꿈틀거리는 공력.
460|
461|동기화를 거침으로써 내게는 힘이 생겼다. F급 헌터를 아득히 뛰어넘는 힘. 혼자서 C급 레어 몬스터를 쓰러트릴 수 있는 힘이.
462|
463|
464|
465|‘길드 가입하실래요?’
466|
467|
468|
469|난생처음 받아 본 스카우트 제의. 하지만 거절했다. 누군가 나를 인정해 준다는 사실에 기쁨보다 두려움이 앞서서.
470|
471|‘그럴 만도 하지.’
472|
473|F급 헌터라는 이름으로 7년을 버텼다. 흙바닥만 기어 다니던 애벌레에게 어느 날 시스템이라는 날개가 생긴 것이다.
474|
475|두려움은 당연한 감정이다.
476|
477|‘하지만 이 힘을, 시스템을 계속해서 쓸 수 있다면?’
478|
479|상상만으로도 심장이 쿵쿵 뛰었다.
480|
481|동시에 지난 7년의 시간이 머릿속을 스쳤다. 미친 듯이 노력했음에도 낙인처럼 찍혀 있던 F급이라는 이름. 타인들의 무시와 죄책감과 무력감에 몸을 떨어야 했던 2년 전의 기억까지.
482|
483|“시발…….”
484|
485|더 이상은 못 참겠다. 나는 자리에서 벌떡 일어났다. 곧장 고시원을 뛰쳐나와 지나가던 택시를 붙잡았다.
486|
487|“어디로 모실까요?”
488|
489|목적지는 이미 정해져 있었다.
490|
491|“헌터 협회 부천 지부로 가주세요.”
492|
493|헌터 등급 재측정.
494|
495|F급 헌터. 오랫동안 나를 괴롭혀 온 이 지긋지긋한 족쇄를 끊어 내는 것부터 시작이다.
496|
497|‘어디 한번 해 보자고.’
498|
499|주먹을 불끈 움켜쥔 내게 택시 기사가 말했다.
500|
501|“이거 서울 택신데요.”
502|
503|“아.”
```

## Assembled English

```markdown
[P1]
# Chapter 46

[P2]
Sizzle.

[P3]
The meat hit the grill. Thick, red, and marbled with white streaks like snowflakes—it was the finest Hanwoo beef.

[P4]
The shape, the sound, the smell. All of it was intoxicating. The only thing I didn’t like was the price…

[P5]
“Will this be enough? Let’s order more after we eat. Some special cuts, too.”

[P6]
A rich C-rank Hunter was paying, so whatever.

[P7]
*How long had it been since I’d last had Hanwoo?*

[P8]
Food in Murim was spicy, salty, and bland. And even then, more days than not, I couldn’t eat properly. For thirty days, my stomach had been abused with beef jerky, bigu pills,[^1] and rice balls.

[P9]
Chomp. Chomp-chomp.

[P10]
The best thing about beef was how quickly you could eat it. The moment it looked more or less done, it went straight into my mouth.

[P11]
Every chew felt like walking on clouds. This piece, that piece, the one over there—every last one tasted like heaven.

[P12]
“Hnnngh.”

[P13]
Team Leader Choi watched me with that peculiar look of his.

[P14]
“Would you like some more?”

[P15]
“No. I should hold back on overeating.”

[P16]
“We’re at twenty-five servings…”

[P17]
“Twelve servings each isn’t all that much.”

[P18]
“I’ve only eaten three servings.”

[P19]
“Oh, can we order some yukhoe?[^2]”

[P20]
“…Yes.”

[P21]
“Rice, too.”

[P22]
“…”

[P23]
And so that storm of a meal came to an end. At last, Team Leader Choi opened his mouth.

[P24]
“I said I was the one who killed them. The Priest and the Great Warrior, both.”

[P25]
“Oh. Thank you.”

[P26]
“Don’t mention it. Let’s call it a fair deal. If anything, I have something to thank you for as well.”

[P27]
A fair deal.

[P28]
He wasn’t wrong. I’d bought myself time to think, and he would gain a reputation. After all, he had led five low-rank Hunters and killed two mid-grade Rare Monsters.

[P29]
The fact that nobody had died in the process would be a huge help for Guild publicity, too.

[P30]
*What if I hadn’t found my strength through Synchronization?*

[P31]
Who knew? Someone probably would have died. Maybe nobody would have made it out alive.

[P32]
“You were already thinking along those lines.”

[P33]
He wasn’t just some eccentric. Not with instincts that sharp.

[P34]
I smiled awkwardly.

[P35]
“It’s good for both of us.”

[P36]
“Good for both of us. Both of us…”

[P37]
Team Leader Choi muttered to himself, then abruptly asked,

[P38]
“Would you like to join the Guild?”

[P39]
“Pffft!”

[P40]
Team Leader Choi lifted the tablecloth and blocked the water, then smoothly produced a business card with practiced elegance.

[P41]
> **Peace Guild, Team 1 Leader Choi Minwoo**

[P42]
What the hell was this? For a second I was completely thrown.

[P43]
“Y-you’re trying to recruit me? Right now?”

[P44]
“That’s right. We always need talent.”

[P45]
I took the card, and for some reason I felt deeply moved.

[P46]
It seemed like only yesterday that I’d been going to interviews with my back bent like a shrimp…

[P47]
*Live long enough and you really do see everything.*

[P48]
An actual recruitment offer—and he was treating me like talent. F-rank Hunter Jin Taekyung, you’d come a long way.

[P49]
“Our Guild is still new, and we don’t have many members yet, but we’re excellent where it counts. For example…”

[P50]
Team Leader Choi elegantly swirled his wineglass. When had he even ordered that?

[P51]
“Our finances are extremely solid.”

[P52]
“Oh, finances!”

[P53]
“And because of that, our employee benefits are excellent.”

[P54]
“Oh, benefits backed by solid finances!”

[P55]
“Our Guild Master is a B-rank Hunter.”

[P56]
“Oh, a high-ranking Hunter—the source of those solid finances!”

[P57]
“There’s no need to worry about restructuring.”

[P58]
“Oh, a stable workplace!”

[P59]
Team Leader Choi asked with an affluent smile,

[P60]
“Will you join us?”

[P61]
I scratched my head.

[P62]
“No. That’s a little…”

[P63]
“…Pardon?”

[P64]
“I have some circumstances that make it difficult right now. I need time.”

[P65]
If I followed my heart, I wanted to sign the contract right away—signature, stamp, thumbprint, even a kiss mark.

[P66]
*But what if the System vanished tomorrow?*

[P67]
I’d be dead broke.

[P68]
Overnight, I’d go from being called talent to being called a human disaster.[^3]

[P69]
“Is it about money?”

[P70]
Money was always a problem.

[P71]
But this was more important than that. I couldn’t let the wad of cash right in front of me dazzle me into making a snap decision.

[P72]
“It’s difficult to explain. I’m sorry, but this isn’t something I can decide right now…”

[P73]
“One hundred million won.”

[P74]
“One hundred million?”

[P75]
“That’s just the signing bonus. We’ll match the rest to the minimum terms for a C-rank Hunter.”

[P76]
That was dangerous. This time it was really dangerous.

[P77]
But I held out with superhuman patience. Hadn’t I learned long ago that life wasn’t that easy?

[P78]
It could be money I’d end up choking on.

[P79]
“I’m sorry.”

[P80]
Team Leader Choi looked at me quietly, then nodded.

[P81]
“I’ll wait for your call.”

[P82]
* * *

[P83]
One person left, and one person stayed.

[P84]
Team Leader Choi—no, Choi Minwoo—looked in silence at the seat Jin Taekyung had left, then took out his phone.

[P85]
Beep. Beep. Click.

[P86]
“—You bastard, you’re a ghost. I was just about to call you.”

[P87]
“What happened with that thing I asked about?”

[P88]
“—I looked into it because you asked, but… is there something about this Jin Taekyung guy?”

[P89]
“That’s why I called you. So? What did you find?”

[P90]
—It’s a dime-a-dozen case. Seven years ago he Awakened at twenty and was assessed as F-rank. There’s a record of him graduating at the top of his class from the Hunter training center…

[P91]
Jin Taekyung’s past seven years spilled from the other end of the phone. Then, at one point, Choi Minwoo’s eyebrows twitched.

[P92]
“What? The Sangdong Station Mutated Gate?”

[P93]
“—Yeah. You know about that incident, right?”

[P94]
How could he not? It had happened only two years ago, so Choi Minwoo remembered it clearly.

[P95]
“—He was the only survivor. I checked that part myself, and it surprised me, too.”

[P96]
Choi Minwoo tipped his glass of water. Thinking he’d grabbed a lead on how an F-rank Hunter had killed a mid-grade Rare Monster alone made his throat burn.

[P97]
“And?”

[P98]
“—He took six months off. The Hunter Administration kept sending investigators, and I guess he spent the time trying to get himself back together. You know how serious the incident was.”

[P99]
“And then?”

[P100]
“—That’s it. He went back to his Guild, ran Gates his ass off for a year and a half, then got fired. That was exactly three days ago.”

[P101]
“Why was he fired?”

[P102]
“—It was technically restructuring, but a booger-sized little Guild, restructuring? Please. The incident probably had a lot to do with it. They kept glancing nervously at the Administration, then pushed him out. From their perspective, he’d have been awkward to keep around.”

[P103]
“That’s all?”

[P104]
“—As far as I can tell. Want me to send you the file separately?”

[P105]
“Send it now. I’m hanging up.”

[P106]
“—Hey, hey!”

[P107]
Click.

[P108]
Choi Minwoo tapped the table with his long fingers.

[P109]
Jin Taekyung. F-rank Hunter. The sole survivor of the Sangdong Station Mutated Gate.

[P110]
And…

[P111]
*At least a C-rank Hunter.*

[P112]
That was the absolute minimum. The image of Taekyung driving a C-rank Rare Monster into a corner alone, with overwhelming strength and skill, kept flickering before his eyes.

[P113]
*And yet he’s F-rank.*

[P114]
There were only two possibilities. Either he had been hiding his strength, or he had recently reawakened.

[P115]
Choi Minwoo suspected the latter, but even that defied common sense.

[P116]
It wasn’t as if only one or two Hunters retired without ever ranking up even once.

[P117]
Reawakening from F-rank to C-rank was, without question, extraordinarily rare.

[P118]
*This isn’t some kind of game. What the hell is he?*

[P119]
Choi Minwoo shook his head. He felt as if a ghost had possessed him.

[P120]
*I’ll have to look into this further.*

[P121]
As he rose from his seat, the restaurant owner approached and held out the bill.

[P122]
“That’ll be 1,937,000 won.”

[P123]
“…”

[P124]
He really did feel as if a ghost had possessed him.

[P125]
* * *

[P126]
“Shit. I’m fucked.”

[P127]
I dropped heavily onto the ground. The recycling area was a mess. The thing that should have been there was nowhere to be seen.

[P128]
“It’s gone. It’s gone. My capsule is gone.”

[P129]
I’d been anxious ever since parting with Team Leader Choi. But I hadn’t expected someone to take it in less than half a day. I shouted into the empty air.

[P130]
“Who the fuck was it?!”

[P131]
And an answer came.

[P132]
“Me, you son of a bitch.”

[P133]
Jinho hyung was smoking on the roof of the goshiwon building,[^4] in the same spot where I’d seen him that morning. He exhaled a plume of smoke with a wistful look, then continued.

[P134]
“I spent ten years crying, regretting, and vowing…”

[P135]
“You want me to make you really cry and regret it?”

[P136]
“You’re no fun. You haven’t seen this movie, have you?”

[P137]
“Quit joking around. This is serious.”

[P138]
“What, you come up empty today?”

[P139]
“No.”

[P140]
My voice drained of strength as I went on.

[P141]
“The capsule.”

[P142]
“…Huh?”

[P143]
“Some bastard took my capsule.”

[P144]
“Cough, cough-cough!”

[P145]
Maybe he’d inhaled the cigarette smoke wrong. Jinho hyung coughed like a maniac before he finally managed to speak.

[P146]
“D-didn’t you throw it away because you didn’t need it?”

[P147]
“I did.”

[P148]
Until the System came back.

[P149]
I hadn’t expected the situation to change this much in just a few hours.

[P150]
*I should’ve kept it for one more day.*

[P151]
Where was I even supposed to start looking? I sighed heavily.

[P152]
“Hyung, you didn’t happen to see who took it, did you?”

[P153]
“Uh… well.”

[P154]
Jinho hyung scratched his head.

[P155]
“If I saw them, I saw them. If I didn’t, I didn’t.”

[P156]
Was that even an answer, or just crap?

[P157]
When I glared at him, he smiled sheepishly.

[P158]
“Look, it’s not like I’m asking for a finder’s fee or anything…”

[P159]
He was definitely asking for a finder’s fee.

[P160]
Anyway, that wasn’t the point. I shot to my feet and asked,

[P161]
“You saw them? You’re sure?”

[P162]
“If I have to pick, I saw them.”

[P163]
“Who? Where did they go?”

[P164]
“I’m not asking for a finder’s fee, but what’s the expected amount, roughly?”

[P165]
“…100,000 won?”

[P166]
“Oh, dear. Maybe I’m getting old. My memory’s a little hazy.”

[P167]
“For fuck’s sake.”

[P168]
“Right. It’s hot out, so good luck with that.”

[P169]
“The finder’s fee is 180,000 won.”[^5]

[P170]
Apparently satisfied with the amount, Jinho hyung broke into a bright smile.

[P171]
“Your capsule. I picked it up.”

[P172]
“…?”

[P173]
It took me exactly three seconds to understand.

[P174]
*Have you ever seen a daylight robber like this?*

[P175]
I was so dumbfounded I couldn’t even breathe. He’d hit me in the back of the head like this?

[P176]
“But there wasn’t anywhere suitable to put it. My room’s too small, you know.”

[P177]
“So?”

[P178]
“I put it back in your room. I did good, right?”

[P179]
How was I supposed to hit this guy so cleanly that people would say I’d really done it right?

[P180]
My fists trembled.

[P181]
* * *

[P182]
“It really is here.”

[P183]
Seeing the capsule taking up half the studio as if nothing had happened, all I could do was let out a hollow laugh.

[P184]
*Should I call this lucky?*

[P185]
Of all the people who could have taken it, it had been Jinho hyung.

[P186]
I opened the capsule lid, picked up the user manual tossed onto the worn seat, and flipped to the last page.

[P187]
> **Main Features**
>
> - A customized capsule for one person! Once a user is registered, the capsule becomes permanently bound to that user and remains so until their death.

[P188]
…Come on. No way.

[P189]
*It has to be a simple coincidence.*

[P190]
But I couldn’t shake the unease. I glared at the capsule, the source of everything that had happened.

[P191]
*What even is this thing?*

[P192]
The reason I’d thrown the capsule into the recycling area that morning was so I could forget everything. My life was already dry enough; I wanted to write it off as one nightmare and keep living my life as I was.

[P193]
But now the situation had changed.

[P194]
*Because the System is here.*

[P195]
The System…

[P196]
Then something occurred to me. I placed my hand on the surface of the capsule and murmured,

[P197]
“Item check.”

[P198]
Ding.

[P199]
Just as I thought. The corners of my mouth had just begun to rise when—

[P200]
> **System**
>
> This Item cannot be read.

[P201]
“…It can’t be read?”

[P202]
This had never happened before.

[P203]
*Is it because I’m not in Murim?*

[P204]
Flustered, I checked every object in the room at random. The television, a ballpoint pen, even the pillow. Every time, the System displayed accurate information.

[P205]
But there was one exception.

[P206]
The capsule couldn’t be read.

[P207]
“Wow. This is driving me nuts.”

[P208]
Just in case, I picked up the user manual. The result was the same.

[P209]
Ding.

[P210]
> **System**
>
> This Item cannot be read.

[P211]
I flopped onto the bed. I stared blankly at the old, yellow-stained ceiling and thought.

[P212]
*What’s going on?*

[P213]
For now, none of it made sense. But one thing was certain.

[P214]
*I’ve become stronger. Incomparably stronger.*

[P215]
Power had soaked into every fiber of my body. Internal energy writhed in my dantian.

[P216]
Synchronization had given me strength. Strength far beyond that of an F-rank Hunter. Strength enough to defeat a C-rank Rare Monster alone.

[P217]
*Would you like to join the Guild?*

[P218]
It was the first recruitment offer I’d ever received. But I refused. When someone recognized me, fear had come before joy.

[P219]
*Can’t blame me.*

[P220]
I’d endured seven years under the name of F-rank Hunter. A caterpillar that had only ever crawled through the dirt had, one day, grown wings called the System.

[P221]
Fear was only natural.

[P222]
*But what if I can keep using this power—keep using the System?*

[P223]
My heart pounded at the mere thought.

[P224]
At the same time, the past seven years flashed through my mind. The name F-rank, stamped on me like a brand despite all the insane effort I’d put in. Even the memories from two years ago, when I’d trembled at other people’s contempt, at the guilt and the helplessness.

[P225]
“Fuck…”

[P226]
I couldn’t take it anymore. I shot to my feet, burst out of the goshiwon, and flagged down a passing taxi.

[P227]
“Where would you like to go?”

[P228]
I already knew the destination.

[P229]
“Take me to the Bucheon Branch of the Hunter Association.”

[P230]
A Hunter rank reassessment.

[P231]
An F-rank Hunter. I’d start by breaking this loathsome shackle that had tormented me for so long.

[P232]
*Let’s give it a shot.*

[P233]
As I clenched my fist, the taxi driver said,

[P234]
“This is a Seoul taxi.”

[P235]
“Oh.”

[P236]
[^1]: Bigu pills are traditional fasting pills said to sustain the body without ordinary food.

[P237]
[^2]: Yukhoe is seasoned Korean raw beef.

[P238]
[^3]: The Korean words for “talent” and “human disaster” share the same pronunciation, though they use different characters.

[P239]
[^4]: A goshiwon is a very small, inexpensive room-for-rent housing arrangement.

[P240]
[^5]: In Korean, *sip-pal* (“eighteen”) echoes the swear he just used, and he switches abruptly to stiff politeness.
```


## Accepted baseline for regression comparison

This is the accepted English copy before mastering. Use it as a regression
anchor: report a finding when the assembled copy loses an established term,
source-specific image, formatting convention, continuity fact, or other detail
that the baseline preserved, unless the Korean source clearly requires the
change.

```markdown
[P1]
# Chapter 46

[P2]
Sizzle.

[P3]
The meat hit the grill. Thick, red, and marbled with white streaks like snowflakes—it was the finest Hanwoo beef.

[P4]
The shape, the sound, the smell. All of it was intoxicating. The only thing I didn’t like was the price…

[P5]
“Will this be enough? Let’s order more after we eat. Some special cuts, too.”

[P6]
A rich C-rank Hunter was paying, so whatever.

[P7]
*How long had it been since I’d last had Hanwoo?*

[P8]
Food in Murim was spicy, salty, and bland. And even then, more days than not, I couldn’t eat properly. For thirty days, my stomach had been abused with beef jerky, bigu pills,[^1] and rice balls.

[P9]
Chomp. Chomp-chomp.

[P10]
The best thing about beef was how quickly you could eat it. The moment it looked more or less done, it went straight into my mouth.

[P11]
Every chew felt like walking on clouds. This piece, that piece, that one too—every last one tasted like heaven.

[P12]
“Hnnngh.”

[P13]
Team Leader Choi watched me with that peculiar look of his.

[P14]
“Would you like some more?”

[P15]
“No. I should hold back on overeating.”

[P16]
“We’re at twenty-five servings…”

[P17]
“Twelve servings each isn’t all that much.”

[P18]
“I’ve only eaten three servings.”

[P19]
“Oh, can we order some yukhoe?[^2]”

[P20]
“…Yes.”

[P21]
“Rice, too.”

[P22]
“…”

[P23]
And so that storm of a meal came to an end. At last, Team Leader Choi opened his mouth.

[P24]
“I said I was the one who killed them. The Priest and the Great Warrior, both.”

[P25]
“Oh. Thank you.”

[P26]
“Don’t mention it. Let’s call it a fair deal. If anything, there’s something I should thank you for, too.”

[P27]
A fair deal.

[P28]
He wasn’t wrong. I’d bought myself time to think, and he would gain a reputation. After all, he had led five low-rank Hunters and killed two mid-grade Rare Monsters.

[P29]
The fact that nobody had died in the process would be a huge help for Guild publicity, too.

[P30]
*What if I hadn’t found my strength through Synchronization?*

[P31]
Who knew? Someone probably would have died. Maybe nobody would have made it out alive.

[P32]
“You were already thinking along those lines.”

[P33]
He wasn’t just some eccentric. Not with instincts that sharp.

[P34]
I smiled awkwardly.

[P35]
“It’s good for both of us.”

[P36]
“Good for both of us. Both of us…”

[P37]
Team Leader Choi muttered to himself, then asked out of nowhere,

[P38]
“Would you like to join the Guild?”

[P39]
“Pffft.”

[P40]
Team Leader Choi lifted the tablecloth and blocked the water, then smoothly produced a business card with practiced elegance.

[P41]
> **Peace Guild, Team 1 Leader Choi Minwoo**

[P42]
What the hell was this? For a second I was completely thrown.

[P43]
“Y-you’re making me a recruitment offer? Right now?”

[P44]
“That’s right. We always need talent.”

[P45]
I took the card, and for some reason I felt deeply moved.

[P46]
It seemed like only yesterday that I’d been going to interviews with my back bent like a shrimp…

[P47]
*Live long enough and you really do see everything.*

[P48]
An actual recruitment offer, treating me like talent. F-rank Hunter Jin Taekyung, you’d come a long way.

[P49]
“Our Guild is still new, and we don’t have many people, but we’re excellent where it counts. For example…”

[P50]
Team Leader Choi elegantly swirled his wineglass. When had he even ordered that?

[P51]
“Our finances are extremely solid.”

[P52]
“Oh, finances!”

[P53]
“And because of that, our employee benefits are excellent.”

[P54]
“Oh, benefits based on solid finances!”

[P55]
“Our Guild Master is a B-rank Hunter.”

[P56]
“Oh, a high-ranking Hunter—the source of those solid finances!”

[P57]
“There’s no need to worry about restructuring.”

[P58]
“Oh, a stable workplace!”

[P59]
Team Leader Choi asked with an affluent smile,

[P60]
“Will you come?”

[P61]
I scratched my head.

[P62]
“No. That’s a little…”

[P63]
“…Pardon?”

[P64]
“I have some circumstances that make it difficult right now. I need time.”

[P65]
If I followed my heart, I wanted to sign the contract right away—signature, stamp, thumbprint, even a kiss mark.

[P66]
*But what if the System vanished tomorrow?*

[P67]
I’d be dead broke.

[P68]
Overnight, I’d go from being called talent to being called a human disaster.[^3]

[P69]
“Is it a money problem?”

[P70]
There was always a money problem.

[P71]
But this was more important than that. I couldn’t get dazzled by the wad of cash right in front of me and snatch at it.

[P72]
“It’s difficult to explain. I’m sorry, but this isn’t something I can decide right now…”

[P73]
“100 million won.”

[P74]
“100 million?”

[P75]
“Just the signing bonus. The rest will match the minimum terms for a C-rank Hunter.”

[P76]
That was dangerous. This time it was really dangerous.

[P77]
But I held out with superhuman patience. Hadn’t I already learned that life wasn’t that easy?

[P78]
It could be money I’d end up choking on.

[P79]
“I’m sorry.”

[P80]
Team Leader Choi looked at me quietly, then nodded.

[P81]
“I’ll wait for your call.”

[P82]
* * *

[P83]
One person left, and one person stayed.

[P84]
Team Leader Choi—no, Choi Minwoo—looked in silence at the seat Jin Taekyung had left, then took out his phone.

[P85]
Beep. Beep. Click.

[P86]
“—You bastard, you’re a ghost. I was just about to call you.”

[P87]
“How did that thing I asked about turn out?”

[P88]
“—I looked into it because you asked, but… is there something about this Jin Taekyung guy?”

[P89]
“That’s why I called you. So? What did you find?”

[P90]
“—It’s a dime-a-dozen case. Seven years ago he Awakened at twenty and was assessed as F-rank. There’s a record he finished first at the Hunter training center…”

[P91]
Jin Taekyung’s past seven years spilled from the other end of the phone. Then, at one point, Choi Minwoo’s eyebrows twitched.

[P92]
“What? The Sangdong Station Mutated Gate?”

[P93]
“—Yeah. You know about that incident, right?”

[P94]
How could he not? It had happened only two years ago, so Choi Minwoo remembered it clearly.

[P95]
“—He was the only survivor. I checked that part myself, and it surprised me, too.”

[P96]
Choi Minwoo tipped his glass of water. Thinking he’d grabbed a lead on how an F-rank Hunter had killed a mid-grade Rare Monster alone made his throat burn.

[P97]
“And?”

[P98]
“—He took six months off. The Hunter Administration kept sending investigators, and I guess he spent the time trying to get himself back together. You know how serious the incident was.”

[P99]
“And then?”

[P100]
“—That’s it. He went back to his Guild, ran Gates his ass off for a year and a half, then got fired. That was exactly three days ago.”

[P101]
“Why was he fired?”

[P102]
“—It was technically restructuring, but a booger-sized little Guild, restructuring? Please. The incident probably had a lot to do with it. They kept glancing nervously at the Administration, then pushed him out. From their perspective, he’d have been awkward to keep around.”

[P103]
“That’s all?”

[P104]
“—As far as I can tell. Want me to send you the file separately?”

[P105]
“Send it now. I’m hanging up.”

[P106]
“—Hey, hey!”

[P107]
Click.

[P108]
Choi Minwoo tapped the table with his long fingers.

[P109]
Jin Taekyung. F-rank Hunter. The sole survivor of the Sangdong Station Mutated Gate.

[P110]
And…

[P111]
*At least a C-rank Hunter.*

[P112]
That was the absolute minimum. The image of Taekyung driving a C-rank Rare Monster into a corner alone, with overwhelming strength and skill, kept flickering before his eyes.

[P113]
*And yet he’s F-rank.*

[P114]
There were only two possibilities. He had been hiding his strength, or he had recently reawakened.

[P115]
Choi Minwoo suspected the latter, but that was still far beyond common sense.

[P116]
It wasn’t as if only one or two Hunters retired without ever ranking up even once.

[P117]
Reawakening from F-rank to C-rank was, without question, extraordinarily rare.

[P118]
*This isn’t some kind of game. What the hell is he?*

[P119]
Choi Minwoo shook his head. He felt as if a ghost had possessed him.

[P120]
*I’ll have to look into this further.*

[P121]
As he rose from his seat, the restaurant owner approached and held out the bill.

[P122]
“1,937,000 won.”

[P123]
“…”

[P124]
He really did feel as if a ghost had possessed him.

[P125]
* * *

[P126]
“Shit. I’m fucked.”

[P127]
I dropped heavily onto the ground. The recycling area was a mess. The thing that should have been there was nowhere to be seen.

[P128]
“It’s gone. It’s gone. My capsule is gone.”

[P129]
I’d been anxious ever since leaving Team Leader Choi. But I hadn’t expected someone to take it in less than half a day. I shouted into the empty air.

[P130]
“Who the fuck was it?!”

[P131]
And I got an answer.

[P132]
“Me, you son of a bitch.”

[P133]
On the roof of the goshiwon building,[^4] Jinho hyung was smoking in the same spot where I’d seen him that morning. He exhaled a plume of smoke with a wistful look, then went on.

[P134]
“I spent ten years crying, regretting it, and making vows…”

[P135]
“You want me to make you really cry and regret it?”

[P136]
“You’re no fun. You haven’t seen this movie, have you?”

[P137]
“Quit joking around. This is serious.”

[P138]
“What, you come up empty today?”

[P139]
“No.”

[P140]
My voice drained of strength as I went on.

[P141]
“The capsule.”

[P142]
“…Huh?”

[P143]
“Some bastard took my capsule.”

[P144]
“Cough, cough-cough!”

[P145]
Maybe he’d inhaled the cigarette smoke wrong. Jinho hyung coughed like a maniac before he finally managed to speak.

[P146]
“D-didn’t you throw it away because you didn’t need it?”

[P147]
“I did.”

[P148]
Until the System came back.

[P149]
I hadn’t expected the situation to change this much in just a few hours.

[P150]
*I should’ve kept it for one more day.*

[P151]
Where was I even supposed to start looking? I sighed heavily.

[P152]
“Hyung, you didn’t happen to see who took it, did you?”

[P153]
“Uh… well.”

[P154]
Jinho hyung scratched his head.

[P155]
“If I saw it, then I saw it. If I didn’t, then I didn’t.”

[P156]
Was that even an answer, or just crap?

[P157]
When I glared at him, he smiled sheepishly.

[P158]
“Look, it’s not that I want a finder’s fee or anything…”

[P159]
It definitely sounded like he wanted a finder’s fee.

[P160]
Anyway, that wasn’t the point. I shot to my feet and asked,

[P161]
“You saw them? You’re sure?”

[P162]
“If I have to pick, I saw them.”

[P163]
“Who? Where did they go?”

[P164]
“I’m not asking for a finder’s fee, but what’s the expected amount, roughly?”

[P165]
“…100,000 won?”

[P166]
“Oh, dear. Maybe I’m getting old. My memory’s a little hazy.”

[P167]
“For fuck’s sake.”

[P168]
“Right. It’s hot out, so good luck with that.”

[P169]
“The finder’s fee is 180,000 won.”[^5]

[P170]
Apparently satisfied with the amount, Jinho hyung broke into a bright smile.

[P171]
“Your capsule. I picked it up.”

[P172]
“…?”

[P173]
It took me exactly three seconds to understand.

[P174]
*Have you ever seen a daylight robber like this?*

[P175]
I was so dumbfounded I couldn’t even breathe. He’d hit me in the back of the head like this?

[P176]
“But there wasn’t anywhere suitable to put it. My room’s too small, you know.”

[P177]
“So?”

[P178]
“I put it back in your room. I did good, right?”

[P179]
How was I supposed to hit this guy so cleanly that people would say I’d really done it right?

[P180]
I clenched my fists until they shook.

[P181]
* * *

[P182]
“It really is here.”

[P183]
Seeing the capsule taking up half the studio as if nothing had happened, all I could do was let out a hollow laugh.

[P184]
*Should I call this lucky?*

[P185]
Of all the people in the world, Jinho hyung had taken the capsule.

[P186]
I opened the capsule lid. Then I picked up the user manual, which had been tossed onto the worn seat, and flipped to the last page.

[P187]
> **Main Features**
>
> - A customized capsule for one person! Once a user is registered, the capsule becomes permanently bound to that user and remains so until their death.

[P188]
…Come on. No way.

[P189]
*It has to be a simple coincidence.*

[P190]
But I couldn’t shake the unease. I stared at the capsule, the source of all these events.

[P191]
*What even is this thing?*

[P192]
The reason I’d thrown the capsule into the recycling area that morning was so I could forget everything. My life was already dry enough; I wanted to write it off as one nightmare and keep living my life as I was.

[P193]
But the situation had changed now.

[P194]
*Because the System is here.*

[P195]
The System…

[P196]
Then something occurred to me. I placed my hand on the surface of the capsule and murmured,

[P197]
“Item check.”

[P198]
Ding.

[P199]
Just as I thought. The corners of my mouth had just begun to rise when—

[P200]
> **System**
>
> This Item cannot be read.

[P201]
“…It can’t be read?”

[P202]
This had never happened before.

[P203]
*Is it because I’m not in Murim?*

[P204]
Flustered, I checked every object in the room at random. The television, a ballpoint pen, even the pillow. Every time, the System displayed accurate information.

[P205]
But there was one exception.

[P206]
The capsule couldn’t be read.

[P207]
“Wow. This is driving me nuts.”

[P208]
Just in case, I picked up the user manual. Same result.

[P209]
Ding.

[P210]
> **System**
>
> This Item cannot be read.

[P211]
I flopped onto the bed. I stared blankly at the old, yellow-stained ceiling and thought.

[P212]
*What’s going on?*

[P213]
For now, these were things I couldn’t understand. But one thing was certain.

[P214]
*I’ve become stronger. Incomparably stronger.*

[P215]
Power had soaked into every fiber of my body. Internal energy writhed in my dantian.

[P216]
Synchronization had given me strength. Strength far beyond that of an F-rank Hunter. Strength enough to defeat a C-rank Rare Monster alone.

[P217]
*Would you like to join the Guild?*

[P218]
It was the first recruitment offer I’d ever received. But I refused. When someone recognized me, fear had come before joy.

[P219]
*Can’t blame me.*

[P220]
I’d endured seven years under the name of F-rank Hunter. A caterpillar that had only ever crawled through the dirt had, one day, grown wings called the System.

[P221]
Fear was a natural feeling.

[P222]
*But what if I can keep using this power—keep using the System?*

[P223]
My heart pounded at the mere thought.

[P224]
At the same time, the past seven years flashed through my mind. The name F-rank, stamped on me like a brand despite all the insane effort I’d put in. Even the memories from two years ago, when I’d trembled at other people’s contempt, at the guilt and the helplessness.

[P225]
“Fuck…”

[P226]
I couldn’t take it anymore. I shot to my feet, burst out of the goshiwon, and flagged down a passing taxi.

[P227]
“Where would you like to go?”

[P228]
I already knew the destination.

[P229]
“Take me to the Bucheon Branch of the Hunter Association.”

[P230]
A Hunter rank reassessment.

[P231]
An F-rank Hunter. I’d start by breaking this loathsome shackle that had tormented me for so long.

[P232]
*Let’s give it a shot.*

[P233]
As I clenched my fist, the taxi driver said,

[P234]
“This is a Seoul taxi.”

[P235]
“Oh.”

[P236]
[^1]: Bigu pills are traditional fasting pills said to sustain the body without ordinary food.

[P237]
[^2]: Yukhoe is seasoned Korean raw beef.

[P238]
[^3]: The Korean words for “talent” and “human disaster” share the same pronunciation, though they use different characters.

[P239]
[^4]: A goshiwon is a very small, inexpensive room-for-rent housing arrangement.

[P240]
[^5]: In Korean, *sip-pal* (“eighteen”) echoes the swear he just used, and he switches abruptly to stiff politeness.
```


## Deterministic QA

```json
{
  "version": 1,
  "chapter": 46,
  "passed": true,
  "metrics": {
    "source_characters": 6336,
    "translation_characters": 14129,
    "length_ratio": 2.23,
    "source_paragraphs": 235,
    "translation_paragraphs": 240
  },
  "errors": [],
  "warnings": [
    {
      "code": "terminology",
      "message": "matched preferred term is absent",
      "details": {
        "korean": "살기",
        "preferred": "killing intent"
      }
    },
    {
      "code": "terminology",
      "message": "matched preferred term is absent",
      "details": {
        "korean": "가주",
        "preferred": "Family Head"
      }
    },
    {
      "code": "terminology",
      "message": "matched preferred term is absent",
      "details": {
        "korean": "명성",
        "preferred": "Fame"
      }
    },
    {
      "code": "terminology",
      "message": "matched preferred term is absent",
      "details": {
        "korean": "산서",
        "preferred": "Shanxi"
      }
    },
    {
      "code": "novel_name",
      "message": "source term was romanized without a ledger entry; use the established English or footnote the first use",
      "details": {
        "korean": "육회",
        "romanization": "yukhoe"
      }
    },
    {
      "code": "novel_name",
      "message": "source term was romanized without a ledger entry; use the established English or footnote the first use",
      "details": {
        "korean": "부천",
        "romanization": "bucheon"
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
