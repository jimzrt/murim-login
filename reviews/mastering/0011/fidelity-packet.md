# Fidelity Gate — Chapter 11

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
  1|＃11화
  2|
  3|
  4|
  5|쉬익. 후웅-
  6|
  7|허공에서 반짝이는 수십 개의 점을 창끝이 차례차례 관통한다.
  8|
  9|한 번의 동작이 끝날 때마다 창날 아래 매달린 붉은 수실이 요동쳤다. 그저 멋으로 달아 놓은 것이 아니라, 적의 시선을 분산시키기 위한 용도다.
 10|
 11|팡!
 12|
 13|다시 한번 바람이 찢어지는 소리가 들렸다. [진가창법]을 이루는 일곱 개의 초식. 그중 마지막인 천관일(天貫軼)이다.
 14|
 15|그리고 이번 천관일은 앞서 성공시킨 아흔아홉 번의 천관일보다 정확하고, 강력했다.
 16|
 17|‘이거지.’
 18|
 19|손끝이 짜릿하다. 진가창법의 일곱 개 초식은 끊어서 펼쳐도 충분히 파괴적이지만, 이어졌을 때 진정한 효과가 드러난다.
 20|
 21|자동차 경주에 비교하자면 일 초식은 시동. 마지막 천관일은 골인이라 할 수 있겠다.
 22|
 23|“후.”
 24|
 25|더운 숨을 내뱉으며 창을 바로 세운 순간이었다.
 26|
 27|띠링.
 28|
 29|
 30|
 31|- 남은 성공 횟수 (100 / 100)
 32|
 33|- [진가창법]을 습득했습니다.
 34|
 35|- 반복된 수련의 결과로 관련 스탯이 상승합니다!
 36|
 37|- 근력, 체력, 민첩이 각각 1씩 올랐습니다.
 38|
 39|
 40|
 41|“오. 스탯 상승.”
 42|
 43|이런 방법으로 능력치를 올릴 수도 있구나. 나는 신기해하며 상태창을 띄웠다.
 44|
 45|띠링.
 46|
 47|
 48|
 49|상태창
 50|
 51|
 52|
 53|[Lv.11 진태경]
 54|
 55|직업 : 이류 무인
 56|
 57|명성 : 10
 58|
 59|칭호 : 3개 (칭호 효과 적용 중)
 60|
 61|- 명가의 자제 (모든 능력치 +5, 명성 +50)
 62|
 63|- 가문의 수치 (모든 능력치 –5, 명성 –50)
 64|
 65|- 초보 수련자 (수련 속도 +10%)
 66|
 67|근력 : 41체력 : 51
 68|
 69|민첩 : 51 지력 : 10
 70|
 71|매력 : 10 공력 : 10년
 72|
 73|잔여 포인트 : 0
 74|
 75|
 76|
 77|
 78|
 79|이 정도면…….
 80|
 81|“훌륭한 이류 나부랭이네.”
 82|
 83|하지만 현실보다는 낫다. 더욱더 위로 올라갈 수 있으니까. F급으로 각성한 날부터 매일매일 느꼈던 한계와 사회가 덮어 놓은 유리천장이 느껴지지 않으니까.
 84|
 85|“그럼 뭐 하냐. 마음대로 로그아웃도 못 하는데.”
 86|
 87|나는 한숨을 내쉬며 바닥에 주저앉았다. 몇 시간 동안 쉬지 않고 수련했더니 몸이 물먹은 솜처럼 무겁다.
 88|
 89|“어이고. 힘들다.”
 90|
 91|띠링.
 92|
 93|
 94|
 95|- 당신은 피로와 허기를 느낍니다. 음식물을 섭취하여 몸 상태를 회복시키십시오.
 96|
 97|
 98|
 99|그래. 그럴 것 같더라.
100|
101|“피로와 허기라.”
102|
103|답은 휴식밖에 없다. 잘 먹고, 잘 자는 거다. 하지만 태평하게 배나 긁으면서 쉬기에는 시간이 아깝다.
104|
105|이럴 때 회복 아이템 같은 거라도 하나 있으면…….
106|
107|“아, 맞다. 벽곡단.”
108|
109|인벤토리에 넣어 두었던 벽곡단을 꺼냈다. 희한한 냄새를 풍겼지만 찬밥 더운밥 가리면 프로 헌터가 아니다.
110|
111|나는 입을 크게 벌리고 벽곡단을 한입 가득 베어 물었다.
112|
113|그리고 생각했다.
114|
115|‘그냥 뱉을까.’
116|
117|맛이 없는 정도가 아니다. 혀가 살려 달라고 비명을 지르고 위장이 출입 금지 팻말을 걸 정도의 맛이다.
118|
119|하지만 인간은 때때로 초인적인 의지를 발휘하는 법. 나는 눈을 질끈 감고 벽곡단을 남김없이 씹어 삼켰다.
120|
121|꿀꺽.
122|
123|“으어어. 먹었어. 진짜 먹었어.”
124|
125|다음 순간 시스템 알림이 울리지 않았다면 한참을 그렇게 뒹굴었을 것이다.
126|
127|띠링.
128|
129|
130|
131|- [뛰어난 벽곡단]을 섭취했습니다.
132|
133|- 당신은 포만감을 느낍니다.
134|
135|- 피로가 회복됩니다.
136|
137|- 한 시간 동안 모든 능력치가 2씩 상승합니다.
138|
139|
140|
141|“뭐?”
142|
143|황급히 상태창을 열어 보니 공력을 제외한 모든 능력치가 2씩 올라 있었다. 거기에 피로와 허기 회복까지. 나는 쌩쌩한 몸 상태와 포만감을 느끼며 중얼거렸다.
144|
145|“완전 사긴데?”
146|
147|더럽게 맛없는 곡물 덩어리에 이런 엄청난 효능이 있을 줄이야. 아니, 잠깐만.
148|
149|“이거, 중복 효과 있나?”
150|
151|고작 하나를 먹었는데 총합 10포인트가 올랐다. 두 개, 세 개, 아니 열 개를 먹는다면?
152|
153|‘저게 고블린 똥이라도 먹어야지.’
154|
155|왠지 고블린 똥이 더 맛있을 것 같긴 한데…… 확실히 시도해 볼 만한 일이다.
156|
157|‘할 수 있다. 할 수 있다. 진태경.’
158|
159|떨리는 손으로 두 번째 벽곡단을 집어 들었다.
160|
161|그리고 잠시 뒤.
162|
163|
164|
165|- [뛰어난 벽곡단]을 섭취했습니다.
166|
167|- 효과가 중복되지 않습니다.
168|
169|- 당신은 과한 포만감을 느낍니다.
170|
171|- [과식]의 영향으로 한 시간 동안 움직임이 둔화됩니다!
172|
173|
174|
175|나는 시스템 알림과 함께 무릎을 꿇었다.
176|
177|“우웨에에엑!”
178|
179|
180|
181|* * *
182|
183|
184|
185|[과식]으로 빵빵해진 배가 겨우 꺼진 뒤에야 다시 수련을 시작할 수 있었다. 수련동에 머무는 시간은 사흘. 그동안 최대한 힘을 키워서 나가야 한다.
186|
187|“하!”
188|
189|짧은 기합과 함께 창날이 묵직한 궤적을 그렸다.
190|
191|‘자세는 낮게, 발은 무겁게, 창은 빠르게.’
192|
193|진가창법은 공격적이다. 끊임없이 적을 압박하며 나아간다. 창의 궤적은 단순하지만 치명적이다.
194|
195|‘군대에서 파생되었다고 했나?’
196|
197|게임의 설정이 어떤지는 몰라도 일개 병졸이 익힐 만한 무공은 아닌 것 같다.
198|
199|명색이 일류 무공인 데다 펼치려면 상당한 신체 능력이 필요하기 때문이다. 정예병, 혹은 지휘관들이 익혔던 무공이 아니었을까 싶다.
200|
201|‘헌터 훈련소 시절 배웠던 거랑 비교하면 천지 차이지.’
202|
203|그런 생각을 했을 때였다. 체력의 고갈인지, 아니면 잡념 때문인지 발이 꼬였다. 발이 꼬이니 손도 흐트러진다. 잔뜩 힘을 머금은 창날이 기세를 잃고 바람을 갈랐다.
204|
205|쉬익-
206|
207|시스템이 울린 것도 동시다.
208|
209|
210|
211|- [진가창법]의 숙련도가 1 오릅니다. (6 / 100)
212|
213|
214|
215|“겨우 1?”
216|
217|방금처럼 무공을 처음부터 끝까지 펼칠 때마다 숙련도가 오른다. 시스템의 판정에 따라 얻는 숙련도도 다른데, 이번에는 발이 자주 꼬여서 1이 오른 게 전부였다.
218|
219|“어떻게 갈수록 못하지?”
220|
221|습득 후 세 번째로 펼친 진가창법은 점점 형편없어지고 있었다. 처음에 얻은 숙련도는 3. 두 번째는 2. 세 번째인 지금은 1이다.
222|
223|“삼, 이, 일. 카운트 세는 것도 아니고 뭐야, 이게?”
224|
225|네 번째는 아예 숙련도를 1도 안 줄 기세다. 나는 한숨과 함께 다시 창을 잡았다. 호흡이 점점 달리는 게 느껴졌지만 다시 진가창법을 펼쳐 냈다.
226|
227|그리고 사 초식을 펼칠 무렵 균형을 잃고 쓰러졌다.
228|
229|띠링.
230|
231|
232|
233|- [진가창법]의 숙련도를 얻지 못했습니다. (6 / 100)
234|
235|
236|
237|“돌겠네.”
238|
239|그대로 누워 종유석이 매달린 수련동 천장을 바라봤다.
240|
241|자꾸 발이 꼬인다. 내가 익힌 그대로 했는데 도대체 왜? 습득할 때도 이런 일은 없었다.
242|
243|“뭐가 문제지?”
244|
245|계속 턱, 하고 걸리는 부분이 있다. 그걸 알아내야 한다.
246|
247|나는 오뚝이처럼 일어나 다시 진가창법을 펼쳤고, 이번에는 삼 초식 만에 넘어졌다.
248|
249|
250|
251|- [진가창법]의 숙련도를 얻지 못했습니다. (6 / 100)
252|
253|
254|
255|창이 아니라 발에 집중해서 펼치자 문제점이 희미하게 모습을 드러낸다. 좋아, 한 번 더.
256|
257|
258|
259|- [진가창법]의 숙련도를 얻지 못했습니다. (6 / 100)
260|
261|
262|
263|이제 알겠다. 그런데…….
264|
265|“여기서 진가보법이 왜 튀어나와?”
266|
267|처음 익힐 때 고생하긴 했다. 한나절 내내 보법만 밟았으니까. 하지만 창법을 펼칠 때 나도 모르게 섞어 쓸 정도냐, 물어보면 그건 아니다.
268|
269|‘그렇게 따지면 7년 동안 익힌 동작 다 섞었지.’
270|
271|나도 창술을 배우긴 했다. 헌터 훈련소에 입소하면 기본적으로 배우는 건데, 마나를 사용할 수 없는 F급을 대상으로 보급된 거라 우리끼리는 좆밥 창술이라고 불렀다.
272|
273|그거에 비하면 진가창법은 중급 헌터용은 된다.
274|
275|“한번 해 볼까?”
276|
277|머리 싸매고 생각해 봤자 원형 탈모만 생긴다. 기술은 일단 몸으로 부딪쳐 봐야 아는 법.
278|
279|나는 천천히 진가창법을 펼치기 시작했다. 그리고 하체로는 진가보법을 펼쳤다.
280|
281|‘동작이 부자연스러워.’
282|
283|자꾸만 어긋난다. 하지만 다르다. 지금까지는 실이 뒤죽박죽 얽혀 있었다면 이번에는 톱니바퀴가 미세하게 비껴가는 느낌이랄까. 그렇게 몇 번을 시도했을까.
284|
285|쉬익- 팡!
286|
287|단순한 찌르기 동작. 나도 모르는 사이에 마지막 일곱 번째 초식까지 펼쳤나 생각했지만 오 초식의 한 동작이다.
288|
289|“방금 뭐야?”
290|
291|등줄기가 찌릿했다. 한순간, 보법과 창법이 완벽하게 맞물린 결과였다. 손에 쥔 창이 부르르 떨렸다.
292|
293|
294|
295|- [진가창법]의 숙련도를 얻지 못했습니다. (6 / 100)
296|
297|
298|
299|이제 시스템 알림은 저 구석으로 처박고, 다시 창을 단단히 말아 쥔다. 조금 전의 느낌을 떠올리며 발을 내디뎠다. 그리고 다시 한번.
300|
301|쉭- 쉬쉭-
302|
303|이거다. 창을 뻗는 순간 느꼈다. 보법과 창법. 이 두 톱니바퀴가 정확히 맞물린다.
304|
305|이루 말할 수 없는 쾌감에 휩싸여 두 개의 톱니바퀴를 굴리고, 또 굴렸다. 내딛는 걸음이, 찌르고 베고 휘두르는 창날이 빠르고 정확했으며 강했다.
306|
307|단전이 뜨겁다. 공력은 하나의 불덩어리가 되어 창에 스며들었다. 토해 내야 했다.
308|
309|바로 지금!
310|
311|“합!”
312|
313|천관일. 하늘을 뚫는다는 진가창법의 마지막 일격이 뻗어 나갔다. 먹먹한 굉음이 터져 나왔다.
314|
315|쾅-!
316|
317|먼지가 피어오르고 돌이 사방으로 비산한다. 수련동의 벽에 박힌 창이 몸을 떨었다. 깊숙이 박혀 보이지도 않는 창날을 중심으로 커다란 구멍이 생성되어 있었다.
318|
319|구멍? 아니다. 이건 크레이터다. 숨 막히는 광경이다.
320|
321|“헉, 헉…….”
322|
323|쾌감에 등골이 오싹했다. 시발, 나야. 내가 해냈다고!
324|
325|트롤도 한 방에 끝장낼 수 있는 저런 미친 일격을 내가……!
326|
327|휘청.
328|
329|‘어?’
330|
331|떠나가라 소리를 지르고, 인증 사진도 찍어야 하는데. 쌀벌레라고 놀리던 진호 형 코를 납작하게 만들어 줘야 하는데.
332|
333|‘아, 여기. 게임이었지.’
334|
335|눈앞이 흐릿하다. 몸에 힘이 빠진다. 견딜 수 없는 졸음이 밀려와 나를 덮쳤다.
336|
337|‘졸려.’
338|
339|나는 생각하는 것을 멈추고 본능에 몸을 맡겼다. 어디선가 많이 듣던 소리가 아스라이 멀어진다.
340|
341|띠링. 띠링. 띠링.
342|
343|.
344|
345|.
346|
347|.
348|
349|- 공력이 모두 소진되었습니다.
350|
351|- 극도의 피로감을 느낍니다.
352|
353|- 업적, [물아일체]를 달성하셨습니다. 보상이 주어집니다!
354|
355|- 무공의 연계를 스스로 깨달았습니다. 보상으로 무공의 경지가 크게 상승합니다.
356|
357|- [진가심법]의 경지가…….
358|
359|- [진가보법]의 경지…….
360|
361|- [진가창법]의…….
362|
363|- 레벨 업!
364|
365|- 레벨 업!
366|
367|
368|
369|* * *
370|
371|
372|
373|- 수면 모드가 종료되었습니다.
374|
375|
376|
377|눈을 떴다. 종유석이 매달린 동굴 천장이 보인다.
378|
379|‘수련동.’
380|
381|얼마나 기절해 있었던 걸까. 반나절? 아니면 하루?
382|
383|모르겠다. 중요한 건 내가 아직 게임 속이고, 충분히 쉬었다는 사실이다.
384|
385|‘컨디션도 최상이고.’
386|
387|이상할 정도로 몸 상태가 좋다. 그러고 보니 기절하기 직전에 시스템 알림을 들었던 것도 같다.
388|
389|“메시지창 오픈.”
390|
391|다음 순간 확인 안 한 메시지들이 시야를 가렸다. 메시지를 다 읽고 생각을 정리했을 때는 십여 분이 훌쩍 흐른 뒤였다. 나는 짧게 소감을 중얼거렸다.
392|
393|“대박 났네.”
394|
395|진가보법, 창법은 삼 성으로 무려 두 단계나 뛰었고 진가심법은 이 성으로 올랐다. 거기에 더해…….
396|
397|“2레벨이나 올랐다고?”
398|
399|기쁘면서도 얼떨떨하다. 사실 수련동에서 레벨을 올릴 수 있으리란 기대는 거의 하지 않았기 때문이다.
400|
401|“보통 퀘스트 깨거나 몬스터를 잡아야 오르는 거 아니었어?”
402|
403|무공을 익히고 지금처럼 어떤 깨달음을 얻는 것으로도 레벨 업이 된다니. 게임 장르가 무협이라 그런가? 확실히 종잡을 수가 없다.
404|
405|“아, 어쩐지 몸이 가뿐하더라.”
406|
407|레벨 업 효과로 몸이 회복된 모양이다. 레벨 업 전까지 남아 있던 타박상과 약간의 통증도 모두 깨끗이 사라져 있었다.
408|
409|“상태창 오픈.”
410|
411|상태창에도 변화가 있었다. 13레벨로 오르면서 스무 개의 잔여 포인트를 얻었고, 수련의 영향으로 근력, 체력, 민첩이 소량 오른 상태다.
412|
413|“13레벨이라.”
414|
415|퀘스트 완료 조건은 일류 경지와 레벨 30, 명성 500 달성.
416|
417|빠르지는 않지만 수련만으로도 착실히 레벨을 올리고 있으니 순항하고 있는 셈이다.
418|
419|‘수련동만 나가면 돛을 피고 쭉쭉 나아가는 거지.’
420|
421|나는 흐뭇하게 웃으며 포인트를 분배했다.
422|
423|이제 [물아일체]의 업적을 이루면서 받은 보상 확인만이 남았다.
424|
425|“인벤토리 오픈.”
426|
427|
428|
429|- 신규 아이템이 1개 존재합니다. 확인하시겠습니까?
430|
431|
432|
433|어, 내놔.
```

## Assembled English

```markdown
[P1]
# Chapter 11

[P2]
Whoosh. Fwoom—

[P3]
The spearhead pierced dozens of sparkling points in the air one after another.

[P4]
Each time I completed a movement, the red tassel hanging beneath the spearhead whipped around. It wasn’t there just for show. It was meant to distract the enemy.

[P5]
Bang!

[P6]
Again, the sound of wind being torn apart rang out. It was the seventh and final form of the Jin Family’s Spear Technique: the Sky-Piercing Strike.

[P7]
And this Sky-Piercing Strike was more precise and powerful than the ninety-nine I had successfully performed before it.

[P8]
*This is it.*

[P9]
My fingertips tingled. Each of the seven forms in the Jin Family’s Spear Technique was destructive enough when performed separately, but its true effect emerged when they flowed together.

[P10]
If I compared it to a car race, the first form was starting the engine. The final Sky-Piercing Strike was crossing the finish line.

[P11]
“Whew.”

[P12]
I exhaled a hot breath and raised the spear upright.

[P13]
Ding.

[P14]
> **System**
>
> - Successful attempts: (100 / 100)
>
> - You have acquired **Jin Family’s Spear Technique**.
>
> - As a result of repeated training, related stats have increased!
>
> - Strength, Stamina, and Agility have each increased by 1.

[P15]
“Oh. My stats went up.”

[P16]
So this was another way to improve my stats. Intrigued, I opened my Status Window.

[P17]
Ding.

[P18]
> **System**
>
> **Status Window**
>
> **Lv. 11 Jin Taekyung**
>
> **Occupation:** Second Rate Martial Artist
>
> **Fame:** 10
>
> **Titles:** 3 (Title effects active)
>
> - **Child of a Prestigious Family:** All stats +5, Fame +50
>
> - **Shame of the Family:** All stats –5, Fame –50
>
> - **Novice Trainee:** Training speed +10%
>
> **Strength:** 41  
> **Stamina:** 51
>
> **Agility:** 51  
> **Intelligence:** 10
>
> **Charm:** 10  
> **Internal Energy:** 10 years
>
> **Remaining Points:** 0

[P19]
At this level…

[P20]
“What a fine second-rate nobody.”

[P21]
Still, it was better than reality. I could keep climbing higher. I no longer felt the limitations I’d sensed every day since awakening as an F-rank, or the glass ceiling society had placed over me.

[P22]
“So what? I can’t even log out whenever I want.”

[P23]
I sighed and sank to the floor. After several hours of nonstop training, my body felt as heavy as soaked cotton.

[P24]
“Oof. I’m beat.”

[P25]
Ding.

[P26]
> **System**
>
> - You feel fatigued and hungry. Consume food to restore your physical condition.

[P27]
Yeah. I figured that would happen.

[P28]
“Fatigue and hunger…”

[P29]
The only answer was rest. Eat well and sleep well. But I didn’t have time to lie around scratching my belly without a care in the world.

[P30]
If only I had some kind of recovery item…

[P31]
“Oh, right. Grain-repelling pills.”

[P32]
I took one of the grain-repelling pills from my inventory. It gave off a strange smell, but a professional Hunter couldn’t afford to be picky about whether his rice was hot or cold.

[P33]
I opened my mouth wide and took a huge bite.

[P34]
Then I thought,

[P35]
*Should I just spit it out?*

[P36]
It wasn’t merely tasteless. It tasted bad enough to make my tongue scream for mercy and my stomach hang up a no-entry sign.

[P37]
But sometimes, humans could summon superhuman willpower. I squeezed my eyes shut, chewed the grain-repelling pill thoroughly, and swallowed every last bit.

[P38]
Gulp.

[P39]
“Uuugh. I ate it. I actually ate it.”

[P40]
If the System notification hadn’t sounded the next moment, I probably would have kept rolling around on the floor for quite a while.

[P41]
Ding.

[P42]
> **System**
>
> - You have consumed an **Excellent Grain-Repelling Pill**.
>
> - You feel full.
>
> - Your fatigue has been relieved.
>
> - All stats increase by 2 for one hour.

[P43]
“What?”

[P44]
I hurriedly opened my Status Window. Every stat except Internal Energy had increased by 2. On top of that, my fatigue had lifted and my hunger was gone.

[P45]
Feeling energized and full, I muttered,

[P46]
“This is completely broken.”

[P47]
Who would have thought such a foul-tasting lump of grain could have such incredible effects?

[P48]
Wait a second.

[P49]
“Do the effects stack?”

[P50]
Just one had increased my stats by a total of 10 points. What if I ate two? Three? No, ten?

[P51]
*I’d eat those even if they were goblin shit.*

[P52]
Goblin shit might actually taste better… but it was definitely worth a try.

[P53]
*I can do this. I can do this. Jin Taekyung.*

[P54]
With trembling hands, I picked up a second grain-repelling pill.

[P55]
And a short while later—

[P56]
> **System**
>
> - You have consumed an **Excellent Grain-Repelling Pill**.
>
> - The effects do not stack.
>
> - You feel excessively full.
>
> - Your movements will be slowed for one hour due to **Overeating**!

[P57]
I dropped to my knees as the System notification sounded.

[P58]
“Bleaaargh!”

[P59]
* * *

[P60]
I could only resume training after my bloated stomach finally went down. I had three days to stay in the training hall. I needed to grow as strong as possible before leaving.

[P61]
“Hah!”

[P62]
With a short shout, the spearhead traced a heavy arc.

[P63]
*Keep my stance low, my feet heavy, and my spear fast.*

[P64]
The Jin Family’s Spear Technique was aggressive. It advanced relentlessly, constantly pressuring the enemy. Its spear movements were simple but lethal.

[P65]
*Was it derived from the military?*

[P66]
I didn’t know what the game’s setting was, but it didn’t seem like a martial art an ordinary foot soldier could learn.

[P67]
After all, it was a first-rate martial art and required considerable physical ability to perform. Perhaps it had been practiced by elite soldiers or commanders.

[P68]
*Compared with what I learned at the Hunter training camp, it’s like heaven and earth.*

[P69]
That was when my foot tangled—whether from exhaustion or distraction, I wasn’t sure. Once my foot got tangled, my hands lost their rhythm too. The spearhead, loaded with strength, lost its momentum and sliced through the air.

[P70]
Whoosh—

[P71]
The System sounded at the same time.

[P72]
> **System**
>
> - Jin Family’s Spear Technique Mastery increased by 1. (6 / 100)

[P73]
“Only 1?”

[P74]
My Mastery increased each time I performed the martial art from beginning to end. The amount I gained depended on the System’s evaluation, and this time, all I got was 1 because my feet had tangled so often.

[P75]
“Why am I getting worse the more I do it?”

[P76]
My Jin Family’s Spear Technique had gotten worse with each of the three attempts since I acquired it. The first time, I gained 3 Mastery. The second time, 2. This third time, 1.

[P77]
“Three, two, one. It’s not even a countdown. What is this?”

[P78]
At this rate, the fourth attempt wouldn’t give me any Mastery at all. I sighed and gripped the spear again. My breathing was growing ragged, but I performed the Jin Family’s Spear Technique once more.

[P79]
Around the fourth form, I lost my balance and fell.

[P80]
Ding.

[P81]
> **System**
>
> - You did not gain Mastery for Jin Family’s Spear Technique. (6 / 100)

[P82]
“This is driving me insane.”

[P83]
I lay there and stared at the training hall’s ceiling, where stalactites hung overhead.

[P84]
My feet kept getting tangled. I was performing the technique exactly as I had learned it, so why was this happening? Nothing like this had happened while I was acquiring it.

[P85]
“What’s the problem?”

[P86]
There was a hitch somewhere, catching me every time. I had to figure out what it was.

[P87]
I popped back up like a roly-poly toy and performed the Jin Family’s Spear Technique again. This time, I fell after only the third form.

[P88]
> **System**
>
> - You did not gain Mastery for Jin Family’s Spear Technique. (6 / 100)

[P89]
When I focused on my feet instead of the spear, the problem faintly began to reveal itself.

[P90]
Good. One more time.

[P91]
> **System**
>
> - You did not gain Mastery for Jin Family’s Spear Technique. (6 / 100)

[P92]
Now I understood. But…

[P93]
“Why is the Jin Family’s Manoeuvre Technique showing up here?”

[P94]
I had struggled when I first learned it. I’d spent half a day practicing nothing but footwork. But if you asked whether that was enough to make me unconsciously mix it into my spear technique, the answer was no.

[P95]
*By that logic, I’d have mixed in every movement I’ve learned over the past seven years.*

[P96]
I had learned spear fighting before, too. It was one of the basics taught at the Hunter training camp. Since it was issued to F-ranks who couldn’t use mana, we called it shitty spear fighting among ourselves.

[P97]
Compared with that, the Jin Family’s Spear Technique was good enough for intermediate Hunters.

[P98]
“Should I give it a try?”

[P99]
No matter how hard I racked my brain, all I’d get was a bald spot. The only way to understand a technique was to physically try it.

[P100]
I began performing the Jin Family’s Spear Technique slowly. At the same time, I performed the Jin Family’s Manoeuvre Technique with my lower body.

[P101]
*The movements don’t flow naturally.*

[P102]
They kept falling out of sync. But it was different. Until now, it had felt like threads tangled in a jumble. This time, it felt like gears slipping past each other by a hair.

[P103]
How many times had I tried?

[P104]
Whoosh—Bang!

[P105]
It was a simple thrust. For a moment, I wondered if I had performed all the way through the seventh and final form without realizing it, but it was only one movement from the fifth form.

[P106]
“What was that?”

[P107]
A shiver ran down my spine. For one brief moment, the footwork and spear technique had meshed perfectly. The spear in my hand trembled.

[P108]
> **System**
>
> - You did not gain Mastery for Jin Family’s Spear Technique. (6 / 100)

[P109]
I shoved the System notification into a corner of my mind and tightened my grip on the spear. Recalling the sensation from a moment ago, I stepped forward.

[P110]
And again.

[P111]
Swish—Whoosh—

[P112]
*This is it.*

[P113]
I felt it the instant I thrust the spear.

[P114]
The footwork and the spear technique. The two gears meshed perfectly.

[P115]
Overwhelmed by indescribable exhilaration, I turned those two gears again and again. My steps, and the spearhead that thrust, slashed, and swung, were fast, precise, and powerful.

[P116]
My dantian grew hot. My internal energy became a ball of fire and seeped into the spear.

[P117]
I had to release it.

[P118]
*Right now!*

[P119]
“Hah!”

[P120]
The Sky-Piercing Strike—the final blow of the Jin Family’s Spear Technique, said to pierce the heavens—shot forward.

[P121]
A deep, muffled boom erupted through the cavern.

[P122]
Bang!

[P123]
Dust billowed, and stones scattered in every direction. The spear embedded in the training hall’s wall trembled. A massive hole had formed around the spearhead, which had plunged so deeply that it was no longer visible.

[P124]
A hole? No.

[P125]
This was a crater.

[P126]
The sight stole my breath away.

[P127]
“Huff, huff…”

[P128]
The exhilaration sent a shiver down my spine.

[P129]
*Fuck, that was me. I did it!*

[P130]
I had unleashed that insane strike—the kind that could take down a troll in one blow.

[P131]
Me!

[P132]
I staggered.

[P133]
*Huh?*

[P134]
I needed to shout my head off and take a proof photo. I needed to put Big Brother Jinho in his place—he used to call me a freeloader.

[P135]
*Oh, right. This was a game.*

[P136]
My vision blurred. The strength drained from my body. An unbearable wave of sleepiness washed over me.

[P137]
*I’m sleepy.*

[P138]
I stopped thinking and surrendered my body to instinct. A familiar sound gradually faded into the distance.

[P139]
Ding. Ding. Ding.

[P140]
.

[P141]
.

[P142]
.

[P143]
> **System**
>
> - All internal energy has been depleted.
>
> - You feel extreme fatigue.
>
> - You have completed the achievement **Unity of Self and Object**. A reward will be granted!
>
> - You have realized how to link martial arts together on your own. As a reward, the realms of your martial arts will rise substantially.
>
> - The realm of **Jin Family’s Cultivation Technique**…
>
> - The realm of **Jin Family’s Manoeuvre Technique**…
>
> - The realm of **Jin Family’s Spear Technique**…
>
> - Level up!
>
> - Level up!

[P144]
* * *

[P145]
> **System**
>
> - Sleep mode has ended.

[P146]
I opened my eyes. The cave ceiling, with stalactites hanging from it, came into view.

[P147]
*The training hall.*

[P148]
How long had I been unconscious? Half a day? Or a full day?

[P149]
I didn’t know. What mattered was that I was still in the game and had gotten plenty of rest.

[P150]
*I feel great, too.*

[P151]
My body felt strangely good. Come to think of it, I seemed to have heard System notifications just before I passed out.

[P152]
“Open Message Window.”

[P153]
The next moment, unread messages covered my vision. By the time I finished reading them all and sorting through my thoughts, more than ten minutes had passed.

[P154]
I muttered a brief reaction.

[P155]
“I really hit the jackpot.”

[P156]
The Jin Family’s Manoeuvre Technique and Spear Technique had risen all the way to the Third Stage, jumping two whole stages. The Jin Family’s Cultivation Technique had reached the Second Stage.

[P157]
And on top of that…

[P158]
“I went up two Levels?”

[P159]
I was happy, but also bewildered. I’d barely expected to Level up at all in the training hall.

[P160]
“Don’t you usually Level up by completing Quests or killing monsters?”

[P161]
Apparently, learning martial arts and gaining insight like I had could also lead to a Level Up. Was it because this was a martial-arts game? I really couldn’t make sense of it.

[P162]
“No wonder my body felt so light.”

[P163]
The Level Up effect must have restored my condition. The bruises and slight pain that had remained before I leveled up had vanished completely.

[P164]
“Open Status Window.”

[P165]
The Status Window had changed too. Reaching Level 13 had given me twenty remaining points, and the effects of training had slightly increased my Strength, Stamina, and Agility.

[P166]
“Level 13…”

[P167]
The Quest completion requirements were reaching the first-rate realm, Level 30, and 500 Fame.

[P168]
I wasn’t progressing quickly, but I was steadily leveling up through training alone. That meant I was cruising along.

[P169]
*Once I leave the training hall, I can spread my sails and surge forward.*

[P170]
I smiled contentedly and distributed my points.

[P171]
Now, all that remained was to check the reward I’d received for completing the Unity of Self and Object achievement.

[P172]
“Open Inventory.”

[P173]
> **System**
>
> - You have 1 new Item. Would you like to check it?

[P174]
Yeah. Hand it over.
```


## Accepted baseline for regression comparison

This is the accepted English copy before mastering. Use it as a regression
anchor: report a finding when the assembled copy loses an established term,
source-specific image, formatting convention, continuity fact, or other detail
that the baseline preserved, unless the Korean source clearly requires the
change.

```markdown
[P1]
# Chapter 11

[P2]
Whoosh. Fwoom—

[P3]
The spearhead pierced dozens of sparkling points in the air one after another.

[P4]
Each time I completed a form, the red tassel hanging beneath the spearhead whipped around. It wasn’t just for show; it was meant to draw the enemy’s eye.

[P5]
Bang!

[P6]
Again, the sound of wind being torn apart rang out. It was the seventh and final form of the Jin Family’s Spear Technique: the Sky-Piercing Strike.

[P7]
This Sky-Piercing Strike was more precise and powerful than the ninety-nine I had successfully performed before it.

[P8]
*This is it.*

[P9]
My fingertips tingled. Each of the seven forms in the Jin Family’s Spear Technique was destructive enough when performed separately, but its true effect emerged when they flowed together.

[P10]
If I compared it to a car race, the first form was starting the engine. The final Sky-Piercing Strike was crossing the finish line.

[P11]
“Whew.”

[P12]
I exhaled a hot breath and raised the spear upright.

[P13]
Ding.

[P14]
> **System**
>
> - Successful attempts: (100 / 100)
>
> - You have acquired **Jin Family’s Spear Technique**.
>
> - As a result of repeated training, related stats have increased!
>
> - Strength, Stamina, and Agility have each increased by 1.

[P15]
“Oh. My stats went up.”

[P16]
So this was another way to improve my stats. Intrigued, I opened my Status Window.

[P17]
Ding.

[P18]
> **System**
>
> **Status Window**
>
> **Lv. 11 Jin Taekyung**
>
> **Occupation:** Second Rate Martial Artist
>
> **Fame:** 10
>
> **Titles:** 3 (Title effects active)
>
> - **Child of a Prestigious Family:** All stats +5, Fame +50
>
> - **Shame of the Family:** All stats –5, Fame –50
>
> - **Novice Trainee:** Training speed +10%
>
> **Strength:** 41  
> **Stamina:** 51
>
> **Agility:** 51  
> **Intelligence:** 10
>
> **Charm:** 10  
> **Internal Energy:** 10 years
>
> **Remaining Points:** 0

[P19]
This was…

[P20]
“What a fine second-rate nobody.”

[P21]
Still, it was better than reality. I could keep climbing higher. I no longer felt the limitations I’d sensed every day since awakening as an F-rank, or the glass ceiling society had placed over me.

[P22]
“So what? I can’t even log out whenever I want.”

[P23]
I sighed and sank to the floor. After several hours of nonstop training, I felt as heavy as a waterlogged cotton blanket.

[P24]
“Ow. I’m exhausted.”

[P25]
Ding.

[P26]
> **System**
>
> - You feel fatigued and hungry. Consume food to restore your physical condition.

[P27]
Yeah. I figured that would happen.

[P28]
“Fatigue and hunger…”

[P29]
The only answer was rest. Eat well and sleep well. But I didn’t have time to lie around leisurely scratching my belly.

[P30]
If only I had some kind of recovery item…

[P31]
“Oh, right. Grain-repelling pills.”

[P32]
I took one of the grain-repelling pills from my inventory. It gave off a strange smell, but a professional Hunter couldn’t afford to be picky about whether his rice was hot or cold.

[P33]
I opened my mouth wide and took a huge bite.

[P34]
Then I thought,

[P35]
*Should I just spit it out?*

[P36]
It wasn’t merely tasteless. It tasted bad enough that my tongue screamed for mercy and my stomach hung up a no-entry sign.

[P37]
Every now and then, humans could summon superhuman willpower. I squeezed my eyes shut, chewed the grain-repelling pill thoroughly, and swallowed every last bit.

[P38]
Gulp.

[P39]
“Uuugh. I ate it. I actually ate it.”

[P40]
If the System notification hadn’t sounded the next moment, I probably would have kept rolling around on the floor for quite a while.

[P41]
Ding.

[P42]
> **System**
>
> - You have consumed an **Excellent Grain-Repelling Pill**.
>
> - You feel full.
>
> - Your fatigue has been restored.
>
> - All stats increase by 2 for one hour.

[P43]
“What?”

[P44]
I hurriedly opened my Status Window. Every stat except Internal Energy had increased by 2. On top of that, my fatigue had lifted and my hunger was gone.

[P45]
Feeling energized and full, I muttered,

[P46]
“This is completely broken.”

[P47]
Who would have thought such a foul-tasting lump of grain could have such incredible effects? Wait a second.

[P48]
“Do the effects stack?”

[P49]
Just one had increased my stats by a total of 10 points. What if I ate two? Three? No, ten?

[P50]
*I’d eat goblin shit if I had to.*

[P51]
Goblin shit might actually taste better… but it was definitely worth a try.

[P52]
*I can do this. I can do this. Jin Taekyung.*

[P53]
With trembling hands, I picked up a second grain-repelling pill.

[P54]
And a short while later—

[P55]
> **System**
>
> - You have consumed an **Excellent Grain-Repelling Pill**.
>
> - The effects do not stack.
>
> - You feel excessively full.
>
> - Your movements will be slowed for one hour due to **Overeating**!

[P56]
I dropped to my knees as the System notification sounded.

[P57]
“Bleaaargh!”

[P58]
* * *

[P59]
I could only resume training after my bloated stomach finally went down. I had three days to stay in the training hall. I needed to grow as strong as possible before leaving.

[P60]
“Hah!”

[P61]
With a short battle cry, the spearhead traced a heavy arc.

[P62]
*Keep my stance low, my feet heavy, and my spear fast.*

[P63]
The Jin Family’s Spear Technique was aggressive, constantly advancing while pressuring the enemy. Its spear movements were simple but lethal.

[P64]
*Was it derived from the military?*

[P65]
I didn’t know what the game’s setting was, but it didn’t seem like a martial art an ordinary foot soldier could learn.

[P66]
After all, it was a first-rate martial art and required considerable physical ability to perform. Perhaps it had been practiced by elite soldiers or commanders.

[P67]
*Compared with what I learned at the Hunter training camp, it’s like heaven and earth.*

[P68]
That was when my foot tangled—whether from exhaustion or distraction, I wasn’t sure. Once my foot got tangled, my hands lost their rhythm too. The spearhead, loaded with strength, lost its momentum and sliced through the air.

[P69]
Whoosh—

[P70]
The System sounded at the same time.

[P71]
> **System**
>
> - Jin Family’s Spear Technique Mastery increased by 1. (6 / 100)

[P72]
“Only 1?”

[P73]
My Mastery increased each time I performed the martial art from beginning to end. The amount I gained depended on the System’s evaluation, and this time, all I got was 1 because my feet had tangled so often.

[P74]
“Why am I getting worse the more I do it?”

[P75]
The third time I performed the Jin Family’s Spear Technique after acquiring it, I was getting worse and worse. The first time, I gained 3 Mastery. The second time, 2. This third time, 1.

[P76]
“Three, two, one. It’s not even a countdown. What is this?”

[P77]
The fourth attempt looked like it would yield no Mastery at all. I sighed and took hold of the spear again. My breathing was becoming increasingly ragged, but I performed the Jin Family’s Spear Technique once more.

[P78]
Around the fourth form, I lost my balance and fell.

[P79]
Ding.

[P80]
> **System**
>
> - You did not gain Mastery for Jin Family’s Spear Technique. (6 / 100)

[P81]
“This is driving me insane.”

[P82]
I lay there and stared at the training hall’s ceiling, where stalactites hung overhead.

[P83]
My feet kept getting tangled. I was performing the technique exactly as I had learned it, so why was this happening? Nothing like this had happened when I acquired it.

[P84]
“What’s the problem?”

[P85]
Something kept throwing me off. I had to figure out what it was.

[P86]
I got back up like a roly-poly and performed the Jin Family’s Spear Technique again. This time, I fell after only the third form.

[P87]
> **System**
>
> - You did not gain Mastery for Jin Family’s Spear Technique. (6 / 100)

[P88]
When I focused on my feet instead of the spear, the problem started to come into focus.

[P89]
Good. One more time.

[P90]
> **System**
>
> - You did not gain Mastery for Jin Family’s Spear Technique. (6 / 100)

[P91]
Now I understood. But…

[P92]
“Why is the Jin Family’s Manoeuvre Technique showing up here?”

[P93]
I had struggled when I first learned it. I’d spent half a day practicing nothing but footwork. But if you asked whether it was enough to make me unconsciously mix it into my spear technique, the answer was no.

[P94]
*If that were the case, I’d have mixed in every movement I’ve learned over seven years.*

[P95]
I had learned spear fighting before, too. It was one of the basics taught at the Hunter training camp. Since it was distributed to F-ranks who couldn’t use mana, we called it shitty spear fighting among ourselves.

[P96]
Compared with that, the Jin Family’s Spear Technique was good enough for intermediate Hunters.

[P97]
“Should I give it a try?”

[P98]
No matter how hard I racked my brain, all I’d get was a bald spot. The only way to understand a technique was to try it with my whole body.

[P99]
I began performing the Jin Family’s Spear Technique slowly. At the same time, I performed the Jin Family’s Manoeuvre Technique with my lower body.

[P100]
*The movements don’t flow naturally.*

[P101]
They kept falling out of sync. But it was different. Until now, it had felt as if tangled threads were being pulled in every direction. This time, it felt as if gears were slipping past each other by a hair.

[P102]
How many times had I tried?

[P103]
Whoosh—Bang!

[P104]
It was a simple thrust. For a moment, I wondered if I had performed all the way through the seventh and final form without realizing it, but it was only one movement from the fifth form.

[P105]
“What was that?”

[P106]
A shiver ran down my spine. For one brief moment, the footwork and spear technique had meshed perfectly. The spear in my hand trembled.

[P107]
> **System**
>
> - You did not gain Mastery for Jin Family’s Spear Technique. (6 / 100)

[P108]
I shoved the System notification into a corner of my mind and tightened my grip on the spear. Recalling the sensation from a moment ago, I stepped forward.

[P109]
And again.

[P110]
Swish—Whoosh—

[P111]
*This is it.*

[P112]
I felt it the instant I thrust the spear. The footwork and the spear technique. The two gears meshed perfectly.

[P113]
Overwhelmed by indescribable pleasure, I turned those two gears again and again. My steps were fast and precise. The spearhead that thrust, slashed, and swung was fast, precise, and powerful.

[P114]
My dantian grew hot. My internal energy became a ball of fire and seeped into the spear.

[P115]
I had to release it.

[P116]
*Right now!*

[P117]
“Hah!”

[P118]
The Sky-Piercing Strike—the final blow of the Jin Family’s Spear Technique, said to pierce the heavens—shot forward.

[P119]
A deep, muffled boom erupted through the cavern.

[P120]
Bang!

[P121]
Dust rose, and stones scattered in every direction. The spear embedded in the training hall’s wall trembled. A massive hole had formed around the spearhead, which had plunged so deeply that it was no longer visible.

[P122]
A hole? No.

[P123]
This was a crater.

[P124]
The sight was breathtaking.

[P125]
“Huff, huff…”

[P126]
The exhilaration sent a shiver down my spine.

[P127]
*Fuck, it was me. I did it!*

[P128]
I had unleashed that insane strike—the kind that could take down a troll in one blow.

[P129]
Me!

[P130]
I staggered.

[P131]
*Huh?*

[P132]
I needed to shout my head off and take a proof photo. I needed to put Big Brother Jinho in his place—he used to call me a freeloader.

[P133]
*Oh, right. This was a game.*

[P134]
My vision blurred. The strength drained from my body. An unbearable wave of sleepiness washed over me.

[P135]
*I’m sleepy.*

[P136]
I stopped thinking and surrendered my body to instinct. A familiar sound gradually faded into the distance.

[P137]
Ding. Ding. Ding.

[P138]
.

[P139]
.

[P140]
.

[P141]
> **System**
>
> - All internal energy has been depleted.
>
> - You feel extreme fatigue.
>
> - You have completed the achievement **Unity of Self and Object**. A reward will be granted!
>
> - You have realized the connection between martial arts on your own. As a reward, the realms of your martial arts will rise substantially.
>
> - The realm of **Jin Family’s Cultivation Technique**…
>
> - The realm of **Jin Family’s Manoeuvre Technique**…
>
> - The realm of **Jin Family’s Spear Technique**…
>
> - Level up!
>
> - Level up!

[P142]
* * *

[P143]
> **System**
>
> - Sleep mode has ended.

[P144]
I opened my eyes. The cave ceiling, with stalactites hanging from it, came into view.

[P145]
*The training hall.*

[P146]
How long had I been unconscious? Half a day? Or a full day?

[P147]
I didn’t know. What mattered was that I was still in the game and had gotten plenty of rest.

[P148]
*I feel great, too.*

[P149]
My physical condition was strangely excellent. Come to think of it, I seemed to have heard System notifications just before I passed out.

[P150]
“Open Message Window.”

[P151]
The next moment, unread messages covered my vision. By the time I finished reading them all and sorting through my thoughts, more than ten minutes had passed.

[P152]
I muttered a brief reaction.

[P153]
“I really hit the jackpot.”

[P154]
The Jin Family’s Manoeuvre Technique and Spear Technique had risen all the way to the Third Stage—two whole stages. The Jin Family’s Cultivation Technique had reached the Second Stage.

[P155]
And on top of that…

[P156]
“I went up two Levels?”

[P157]
I was happy, but also bewildered. I hadn’t seriously expected to Level up in the training hall.

[P158]
“Don’t you usually Level up by completing Quests or killing monsters?”

[P159]
Apparently, learning martial arts and gaining insight like I had could also lead to a Level Up. Was it because this was a martial-arts game? It was definitely impossible to predict.

[P160]
“No wonder my body felt so light.”

[P161]
The Level Up effect must have restored my condition. The bruises and slight pain that had remained before I leveled up had vanished completely.

[P162]
“Open Status Window.”

[P163]
The Status Window had changed too. Reaching Level 13 had given me twenty remaining points, and the effects of training had slightly increased my Strength, Stamina, and Agility.

[P164]
“Level 13…”

[P165]
The Quest completion requirements were reaching the first-rate realm, Level 30, and 500 Fame.

[P166]
I wasn’t progressing quickly, but I was steadily leveling up through training alone. That meant I was cruising along.

[P167]
*Once I leave the training hall, I can spread my sails and surge forward.*

[P168]
I smiled contentedly and distributed my points.

[P169]
Now, all that remained was to check the reward I’d received for completing the Unity of Self and Object achievement.

[P170]
“Open Inventory.”

[P171]
> **System**
>
> - You have 1 new Item. Would you like to check it?

[P172]
Yeah. Give it here.
```


## Deterministic QA

```json
{
  "version": 1,
  "chapter": 11,
  "passed": true,
  "metrics": {
    "source_characters": 5859,
    "translation_characters": 13673,
    "length_ratio": 2.334,
    "source_paragraphs": 187,
    "translation_paragraphs": 174
  },
  "errors": [],
  "warnings": [
    {
      "code": "terminology",
      "message": "matched preferred term is absent",
      "details": {
        "korean": "일류",
        "preferred": "First Rate"
      }
    },
    {
      "code": "terminology",
      "message": "matched preferred term is absent",
      "details": {
        "korean": "진가심법",
        "preferred": "Jin Family's Cultivation Technique"
      }
    },
    {
      "code": "terminology",
      "message": "matched preferred term is absent",
      "details": {
        "korean": "진가보법",
        "preferred": "Jin Family's Manoeuvre Technique"
      }
    },
    {
      "code": "terminology",
      "message": "matched preferred term is absent",
      "details": {
        "korean": "진가창법",
        "preferred": "Jin Family's Spear Technique"
      }
    },
    {
      "code": "terminology",
      "message": "matched preferred term is absent",
      "details": {
        "korean": "일격",
        "preferred": "One Strike"
      }
    },
    {
      "code": "terminology",
      "message": "matched preferred term is absent",
      "details": {
        "korean": "로그아웃",
        "preferred": "Logout"
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
