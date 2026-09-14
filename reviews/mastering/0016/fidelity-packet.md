# Fidelity Gate — Chapter 16

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
  1|＃16화
  2|
  3|
  4|
  5|“후우, 드디어 끝났군.”
  6|
  7|진위경이 붓을 내려놓으며 한 말이었다. 언제나처럼 문가 옆 의자에 앉아 있던 위팽이 고개를 들었다.
  8|
  9|“점점 일 처리가 빨라지시는군요. 오늘도 고생하셨…….”
 10|
 11|위팽이 말꼬리를 흐렸다. 아직 탁자 위에 산더미처럼 쌓인 서류를 발견했기 때문이었다.
 12|
 13|그러고 보니 아직 정오 무렵밖에 되지 않았다. 저 정도 양의 업무를 해치울 수 있는 시간이 아니었다.
 14|
 15|‘잘못 들었나?’
 16|
 17|“좋아. 이 정도면…….”
 18|
 19|이번엔 환청이 아니었다. 서류 더미 위로 불쑥 솟은 진위경의 얼굴이 그 증거였다.
 20|
 21|“위팽, 이리 와 보게. 아주 중요한 일이야.”
 22|
 23|너무나도 진지한 음성에 위팽은 살짝 걱정되었다.
 24|
 25|무슨 큰일이라도 났나?
 26|
 27|서류에서 심각한 비리가 발견됐다거나, 호시탐탐 기회를 엿보고 있는 장로원에서 큰 사건을 터트렸을 수도 있다.
 28|
 29|‘큰일이군. 아직 항산검문의 일도 마무리되지 않았는데.’
 30|
 31|그리고 잠시 후, 진위경이 내민 문제의 서류를 받아 든 위팽의 표정이 괴상하게 일그러졌다.
 32|
 33|“……뭡니까, 이게?”
 34|
 35|“보면 모르나? 그림이지.”
 36|
 37|진위경의 말대로였다. 위팽이 생각한 문제의 서류는 온데간데없고, 건네받은 것은 그림이 그려진 화선지 한 장이었다.
 38|
 39|“아니, 그 말이 아니잖습니까. 난데없이 이게 무슨…….”
 40|
 41|진위경이 비밀스러운 미소를 지으며 말을 잘랐다.
 42|
 43|“자세히 보게. 평범한 그림이 아니야.”
 44|
 45|평범한 그림이 아니다? 순간 위팽의 눈이 번쩍 뜨였다.
 46|
 47|머릿속에는 무림에 떠도는 온갖 전설들이 휙휙 스쳐 지나갔다.
 48|
 49|한 폭의 그림을 보고 우화등선한 도사. 오래된 동굴의 벽화를 보고 깨달음을 얻은 절대 고수!
 50|
 51|한참 동안 화선지를 누비던 위팽의 시선이 어느 순간, 벼락 맞은 것처럼 파르르 떨렸다.
 52|
 53|“이, 이것은 설마……!”
 54|
 55|“알아차렸군. 맞네.”
 56|
 57|진위경이 후후후, 웃으며 말을 이었다.
 58|
 59|“어제의 비무를 그려 봤네.”
 60|
 61|“…….”
 62|
 63|“쓰러진 이소군과 당당히 서 있는 태경이! 훗날 천하제일인이 될 젊은 영웅의 머리 위로 펼쳐진 하늘!”
 64|
 65|“…….”
 66|
 67|“일부러 밑에서 올려다보는 구도로 그렸는데, 자네 소감은 어떤가. 잘 그렸지. 응? 잘 그렸지?”
 68|
 69|화선지를 붙든 위팽의 손이 바들바들 떨렸다. 마음 같아서는 구기고, 찢고, 그 위에 일주일 치 대소변을 갈긴 다음 잘 말린 후 불태우고 싶었지만.
 70|
 71|“……잘 그리셨군요.”
 72|
 73|위팽은 이성적인 사내였다. 절정의 경지에 오른 무인의 위대한 정신력을 발휘해 냈다.
 74|
 75|물론 그에겐 정신 상태가 의심되는 주군을 질책할 만한 용기도 있었다.
 76|
 77|“지금 밀린 일이 얼마나 많은데, 아침부터 지금까지 겨우 이 그림 한 장 그렸다는 게 말이 됩니까!”
 78|
 79|“당연히 말이 안 되지.”
 80|
 81|“그걸 아시는 분이…….”
 82|
 83|“내가 세 시진 동안 하나만 붙잡고 있었을까 봐?”
 84|
 85|“예?”
 86|
 87|“당연히 하나 더 그렸지. 나중에 보여 주려고 했는데 역시 눈치가 빠르구먼.”
 88|
 89|위팽은 부들부들 떨리는 손으로 진위경이 건네는 화선지를 받아들었다. 진위경은 싱글벙글 웃으며 그림 설명을 시작했다.
 90|
 91|“비무 직후 상황을 그려봤네. 현재에 만족하지 않고 수련동으로 돌아가겠다고 선언하는 젊은 영웅! 그리고 그 모습을 우러러보는 사람들!”
 92|
 93|“뭐, 그 부분에 대해서는 저도 상당 부분 동의합니다. 삼공자, 정말 많이 변했더군요.”
 94|
 95|“그렇지? 나도 깜짝 놀랐지 뭔가.”
 96|
 97|이소군과의 비무에서 승리한 진태경은 모두의 예상을 깨고 수련동으로 돌아갔다. 전날의 기억을 떠올리는 진위경의 눈동자가 몽롱해졌다.
 98|
 99|“언제고 이런 날이 올 줄 알았지. 막내는 천응(天鷹)이야. 위팽, 자네에게는 들리지 않나? 태경이의 힘찬 날갯짓 소리가…….”
100|
101|“날갯짓 소리는 모르겠고, 헛소리는 들립니다.”
102|
103|위팽이 모든 걸 포기한 한숨과 함께 화선지를 내려놓은 순간이었다.
104|
105|푸드득.
106|
107|“헉.”
108|
109|“거봐! 들리잖아!”
110|
111|황급히 고개를 돌린 위팽의 시선이 창문을 향했다. 막 내려앉은 매 한 마리가 깃털을 고르고 있었다. 발목에는 작은 통 하나가 매달려 있었다.
112|
113|“전서응(傳書鷹)입니다.”
114|
115|새끼 때부터 고도의 훈련을 거쳐 투입된 연락용 매.
116|
117|태원진가에도 두 마리밖에 없는 전서응은 극히 긴급한 일에만 날리게 되어 있었다.
118|
119|“문제가 생겼군.”
120|
121|진위경이 가라앉은 목소리로 중얼거렸다.
122|
123|그리고 그것은 곧 현실로 나타났다.
124|
125|
126|
127|* * *
128|
129|
130|
131|“한엽이라고 합니다.”
132|
133|“예?”
134|
135|“만나 뵙게 되어 영광입니다.”
136|
137|뜬금없는 자기소개였다. 물론 아는 얼굴이긴 했다.
138|
139|수련동에 들어온 이후 가장 자주 본 사람이었으니까.
140|
141|‘수련동 경비원이라고 해야 하나?’
142|
143|경비원. 경비무사. 용어가 어찌 됐건 눈앞의 NPC는 수련동을 담당하는 태원진가의 무사였다. 내게 식사와 탕약을 가져다주는 것도 그의 임무 중 하나고.
144|
145|‘그런데 갑자기 웬 통성명?’
146|
147|지금까지 말 한마디 섞어 본 적 없는 NPC다. 내게 악감정은 없어 보였지만 그렇다고 특별히 호의적이지도 않았다.
148|
149|“아, 예. 저도 반가워요.”
150|
151|떨떠름한 대답에도 경비원, 아니 한엽의 얼굴이 환하게 밝아졌다. 뭐야, 갑자기 왜 이래?
152|
153|“저도 어제 그 자리에 있었습니다.”
154|
155|“그 자리? 아.”
156|
157|비무를 말하는 거구나. 워낙 많은 사람이 몰렸으니 그중 한엽이 있었다고 해도 놀랄 만한 일은 아니다.
158|
159|“처음부터 끝까지 지켜봤지요. 그 악랄한 항산검문의 이소군에게 맞서 싸우던 공자님의 영웅적인 모습을!”
160|
161|악랄해? 영웅적인 모습?
162|
163|‘그게 그렇게 되나?’
164|
165|솔직히 현대인의 시선에서 바라보자면 그놈이 그놈이다.
166|
167|아니, 오히려 이소군의 손을 들어 주고 싶을 정도다. 나도 한 사람의 오빠로서, 내 여동생 성격이 아무리 지랄맞아도 진태경 같은 놈이랑 연애질한다고 하면 눈 뒤집힐 것 같거든.
168|
169|물론 항산검문의 태도나 제안은 말도 안 되는 거였다. 그래서 어쩔 수 없이 싸운 거고.
170|
171|“보는 내내 가슴이 떨렸습니다. 저뿐만 아니라 그 자리에 있던 모든 사람이 같은 마음이었을 겁니다.”
172|
173|한엽은 상기된 얼굴로 말을 이어 갔다. 이거 단단히 착각하고 있는 것 같은데, 어느 타이밍에서 멈춰야 할지 모르겠다.
174|
175|“저도 한때 공자님을 오해했던 적이 있습니다. 하지만 이제는 가문의 모두가 진실을 알고 있습니다.”
176|
177|이번에는 반문하지 않을 수 없었다.
178|
179|“진실? 무슨 진실?”
180|
181|“그건…….”
182|
183|한엽이 잔뜩 숨죽인 목소리로 속삭였다. 귀에 닿은 뜨거운 숨결은 둘째치고, 그 내용에 소름이 돋는다.
184|
185|그러니까, 그 내용인즉슨.
186|
187|“내가 태원진가의 비밀 병기다?”
188|
189|“네, 네!”
190|
191|한엽이 맹렬하게 고개를 끄덕였다.
192|
193|“사실 지금까지의 모습은 모두 위장이고, 어릴 때부터 뼈를 깎는 수련을 거치며 문무겸전에 덕과 의를 갖춘, 잠. 잠……”
194|
195|이 말만은 도저히 못 하겠다. 오그라드는 손발을 보호하려는 나를 대신해 한엽이 나섰다.
196|
197|“산서잠룡! 지금 가문 내에 모르는 사람이 없습니다. 공자님께서 아직 하늘에 오르지 않고 물에 몸을 숨긴 산서성의 잠룡이라는 사실 말입니다!”
198|
199|아, 제발. 살려 줘. 큰 소리로 외치지도 말아 줘.
200|
201|잠룡이라니. 가문에 모르는 사람이 없다니!
202|
203|‘만약 내가 죽는다면 사인은 수치사다, 수치사.’
204|
205|극심한 심적 고통에 몸부림치는 내게, 한엽이 반짝거리는 눈빛으로 물었다.
206|
207|“사실이지요? 실례인 줄은 알지만, 저한테만 살짝…….”
208|
209|안 되겠다. 누가 뿌렸는지 모를 이 말도 안 되고 오그라드는 헛소문을 진압하기로 다짐하고 입을 열었다.
210|
211|“도대체 누가 그런 소문을 퍼트렸는지 모르겠지만…….”
212|
213|그때였다.
214|
215|띠링.
216|
217|
218|
219|- 태원진가에 [잠룡]에 대한 소문이 퍼지고 있습니다.
220|
221|- 소문에 의한 영향으로 명성이 10 오릅니다.
222|
223|- 소문을 믿는 사람이 많아질수록, 명성이 상승합니다.
224|
225|
226|
227|나는 근엄한 얼굴로 말을 이었다.
228|
229|“전부 틀림없는 사실입니다.”
230|
231|“역시! 저는 철석같이 믿고 있었습니다!”
232|
233|환희에 찬 얼굴로 떠나는 한엽의 등을 바라보며, 나는 한줄기 눈물을 흘렸다.
234|
235|‘시발…….’
236|
237|아, 엄마 보고 싶다.
238|
239|
240|
241|* * *
242|
243|
244|
245|이소군과의 비무를 통해 여러 가지 사실을 깨달았다.
246|
247|첫째.
248|
249|‘나는 강하다.’
250|
251|게임 초기, 튜토리얼 NPC로 나온 천력부를 일격에 쓰러트린 일이 있었다. 당시의 짐작이 지금은 확신으로 바뀌었다.
252|
253|나는 강하다. 30레벨인 이소군을 어렵지 않게 쓰러트릴 정도로. 전투 경험의 차이도 영향이 있겠지만 기본적으로 능력치가 월등하다.
254|
255|‘힘, 체력, 민첩. 모두 비슷하거나 내가 약간 앞섰지.’
256|
257|스탯(Stat). 즉 능력치의 차이다. 이 게임 속에서 나는 유저고, 시스템을 이용한 성장을 거듭해 왔다.
258|
259|무공 습득, 수련과 여러 가지 퀘스트를 통해 빠른 속도로 스탯을 올렸고 그 결과는 비무에서 드러났다.
260|
261|그리고 두 번째.
262|
263|‘공력이 부족해.’
264|
265|공력 하나만큼은 이소군이 나보다 앞섰다. 아니, 월등했다.
266|
267|뭘 먹고 컸는지 창대로 수십 번을 후려쳐도, 마운트 자세에서 일방적으로 때려도 놈은 견뎌 냈다. 반격까지 하고 마지막 순간에도 공력을 끌어 올렸다.
268|
269|‘현재 내 공력은 십 년.’
270|
271|이소군은 내 두 배인 이십 년은 될 거다. 여기서 세 번째 사실을 깨달았다.
272|
273|‘공력의 차이가 무공의 단계를 가른다.’
274|
275|나는 일류인 이소군을 꺾었다. 하지만 시스템이 표시하는 내 경지는 여전히 이류다.
276|
277|나는 그 이유가 공력에 있다고 생각했다. 내게 부족한 단 하나의 능력치를 올렸을 때, 그때 비로소 내 경지도 오르지 않을까?
278|
279|거기까지 정리를 마치고 나니 문득 드는 생각이 있었다.
280|
281|‘이거 완전히 헌터 등급 나누기네.’
282|
283|최초 각성자는 반드시 지정된 센터에서 보유 능력과 적성 직업, 마나량을 체크받아야 하는데, 신체 능력이 아무리 높아도 마나량이 부족하면 등급 심사에서 찬바람을 맞는다.
284|
285|마법사들이 최하 D등급부터 시작하는 이유이기도 하다. 마법사들은 직업 특성상 기본 마나부터가 빵빵하니까.
286|
287|‘그래도 게임이 현실보단 낫네.’
288|
289|여긴 그나마 성장이라도 하지. 현실은 그런 거 없다. 나만 해도 7년 동안 뭐 빠지게 굴러서 E급들 사이에 낀 거지, F급 헌터인 건 변함없었으니까.
290|
291|아무튼 이제 대략적인 스케치는 그려졌다.
292|
293|‘스탯은 충분. 공력은 시간 날 때마다 진가심법 돌리고, 경험치 위주로 퀘스트를 받자.’
294|
295|이 빌어먹을 게임에 갇힌 지 일주일이 넘었다. 현실에서 무슨 헛짓거리를 하는지는 몰라도 구조받기는 글렀다.
296|
297|확실하게 준비해서 끝내야지.
298|
299|“퀘스트창 오픈.”
300|
301|띠링.
302|
303|
304|
305|퀘스트
306|
307|
308|
309|[로그아웃]
310|
311|이제 당신은 이 험난한 무림을 헤쳐 나가야 합니다.
312|
313|더욱더 강해지고, 유명해지십시오.
314|
315|언젠가 다가올 그 날을 위해…….
316|
317|
318|
319|등급 : 메인 퀘스트
320|
321|제한 : 진태경
322|
323|임무 : [일류] 경지 달성 (미완료)
324|
325|         Lv.30 달성 (17 / 30)
326|
327|         명성 500 달성 (70 / 500)
328|
329|보상 : [로그아웃]
330|
331|
332|
333|
334|
335|“아, 빡세다.”
336|
337|나는 가부좌를 틀었다. 폐관 완료까지 이틀. 최대한 공력을 끌어모을 생각이었다.
338|
339|
340|
341|- [잠룡]에 대한 소문의 영향으로 명성이 3 상승합니다.
342|
343|
344|
345|틈틈이 울리는 명성 상승 메시지가 한줄기 위로가 되었다.
346|
347|
348|
349|* * *
350|
351|
352|
353|늦은 밤. 대회의장에 불이 켜졌다. 소가주인 진위경의 요청에 의해 비밀리에 이루어진 가로회의였다.
354|
355|워낙 늦은 시각이었고, 갑작스러운 소집이라 뚱한 표정을 짓고 있는 중진들도 있었다.
356|
357|“갑자기 소집이라니. 이게 무슨 일이랍니까?”
358|
359|“그러니까. 이유도 안 알려 주고 이 늦은 시각에.”
360|
361|“소가주가 아직 젊어서 그래. 절차와 예의를 몰라.”
362|
363|“어제 일로 상당히 기세등등해졌나 봅니다. 하긴, 유일한 약점이 사라진 셈이니까요. 삼공자가 그 정도일 줄은 아무도 예상 못 했습니다.”
364|
365|“장로원에서 김 좀 샜겠군. 삼공자 건으로 크게 한번 터트리려고 준비 중이었을 텐데.”
366|
367|“허어, 지금이라도 대장로께서 나서서 가문을 바로 잡으셔야 할 터인데.”
368|
369|“어허. 말조심…….”
370|
371|그때, 모든 소리가 뚝 끊겼다. 회의실의 문이 양옆으로 열리고 진위경이 들어왔기 때문이었다.
372|
373|중진들 사이에서는 평가가 분분한 소가주였지만 진위경의 등장과 동시에 내려앉은 침묵은 그에게 우두머리의 자질이 있음을 알려 주는 증거였다.
374|
375|“늦은 밤에 소집에 응해 주신 모든 분께 감사드립니다.”
376|
377|상석에 앉은 진위경은 첫 마디를 꺼냈지만 쉽사리 말을 이어 가지 못했다.
378|
379|무슨 말을, 어디서부터 어떻게 꺼내야 한단 말인가. 머리가 지끈거렸다. 하지만 알려야 하는 일이었다.
380|
381|“제가 오늘 이 자리를 마련한 이유는…….”
382|
383|그 순간이었다.
384|
385|“항산검문 때문이겠지.”
386|
387|그건 기이한 목소리였다. 처음에는 늙은이의 그것이었고, 한편으로는 젊었으며 거칠거나 부드러웠다. 그리고 알 수 없는 울림이 있었다.
388|
389|‘설마.’
390|
391|진위경의 얼굴이 일그러졌다. 다시는 열릴 것 같지 않았던 회의장의 문이 열리고 있었다.
392|
393|저벅. 저벅. 저벅.
394|
395|미끄러지듯이 걸어 들어오는 다섯 명의 노인. 그리고 가장 앞에 선 노인을 확인한 모두가 황급히 일어나 고개를 숙였다.
396|
397|“노야(老爺)를 뵙습니다!”
398|
399|노야. 수년간 두문불출하던 대장로의 등장이었다.
```

## Assembled English

```markdown
[P1]
# Chapter 16

[P2]
“Whew. Finally done.”

[P3]
Jin Wikyung set down his brush as he spoke. Wipeng, who was sitting in a chair beside the door as always, raised his head.

[P4]
“You’re getting faster at handling your work. You’ve worked hard toda—”

[P5]
Wipeng trailed off. He had just noticed the mountain of documents still piled on the table.

[P6]
Come to think of it, it was only around noon. There was no way anyone could finish that much work in so little time.

[P7]
*Did I hear him wrong?*

[P8]
“Good. This should do…”

[P9]
This time, it wasn’t a hallucination. Jin Wikyung’s face popped up above the pile of documents, proving he had heard correctly.

[P10]
“Wipeng, come here. This is very important.”

[P11]
His voice was so serious that Wipeng grew slightly concerned.

[P12]
*Did something major happen?*

[P13]
Perhaps the documents had revealed serious corruption. Or maybe the Elder Council, which was always watching for an opportunity, had caused some major incident.

[P14]
*This is bad. We haven’t even finished dealing with the Mount Heng Sword Sect yet.*

[P15]
A moment later, Wipeng accepted the document in question that Jin Wikyung held out. His expression twisted into something bizarre.

[P16]
“…What is this?”

[P17]
“Can’t you tell? It’s a drawing.”

[P18]
The alarming document Wipeng had imagined was nowhere to be seen. Instead, Jin Wikyung had handed him a single sheet of rice paper with a drawing on it.

[P19]
“No, that’s not what I meant. Why would you suddenly…”

[P20]
Jin Wikyung cut him off with a secretive smile.

[P21]
“Look closely. It isn’t an ordinary drawing.”

[P22]
*It isn’t an ordinary drawing?*

[P23]
Wipeng’s eyes flashed open.

[P24]
All kinds of legends circulating through Murim flashed through his mind.

[P25]
A Daoist who ascended to immortality after gazing upon a single painting. An absolute master who attained enlightenment after seeing a mural in an ancient cave!

[P26]
Wipeng’s gaze roamed across the rice paper for a long while. Then it suddenly quivered as if struck by lightning.

[P27]
“T-this couldn’t be…!”

[P28]
“You noticed. That’s right.”

[P29]
Jin Wikyung continued with a chuckle.

[P30]
“I tried drawing yesterday’s duel.”

[P31]
“……”

[P32]
“Lee Seogeun lying defeated, and Taekyung standing proudly! The sky spread above the head of the young hero who would one day become the greatest under heaven!”

[P33]
“……”

[P34]
“I deliberately chose a composition looking up from below. What do you think? It’s good, isn’t it? Isn’t it?”

[P35]
Wipeng’s hands trembled around the rice paper. He wanted to crumple it, tear it apart, cover it with a week’s worth of piss and shit, dry it thoroughly, and then set it on fire.

[P36]
But—

[P37]
“…It’s very well drawn.”

[P38]
Wipeng was a rational man. He summoned the magnificent mental fortitude of a martial artist at the Peak realm.

[P39]
Of course, he also had enough courage to reprimand a lord whose sanity was in serious doubt.

[P40]
“With this much work piled up, how could you spend the entire morning drawing a single picture?”

[P41]
“Of course I couldn’t.”

[P42]
“And yet you—”

[P43]
“Did you think I spent six hours working on just one?”

[P44]
“Pardon?”

[P45]
“Of course I drew another one. I was going to show it to you later, but you really are quick to catch on.”

[P46]
Wipeng accepted the second sheet of rice paper from Jin Wikyung with trembling hands. Grinning from ear to ear, Jin Wikyung began explaining the drawing.

[P47]
“I tried to depict the scene immediately after the duel. The young hero declares that he won’t rest on his laurels and will return to the training hall! And the people gazing up at him in admiration!”

[P48]
“Well, I agree with a considerable part of that. The Third Young Master really has changed a great deal.”

[P49]
“Hasn’t he? I was surprised myself.”

[P50]
After defeating Lee Seogeun in the duel, Jin Taekyung had defied everyone’s expectations and returned to the training hall. Jin Wikyung’s eyes grew hazy as he recalled the events of the previous day.

[P51]
“I always knew a day like this would come. The youngest is a heavenly eagle. Wipeng, can’t you hear it? The powerful sound of Taekyung’s wings beating…”

[P52]
“I can’t hear any wings, but I can hear you spouting nonsense.”

[P53]
Wipeng lowered the rice paper with a sigh of complete resignation.

[P54]
Flap.

[P55]
“Gasp.”

[P56]
“See? You can hear it!”

[P57]
Wipeng hurriedly turned toward the window. A hawk that had just landed was preening its feathers. A small container hung from its ankle.

[P58]
“It’s a messenger hawk.”

[P59]
These hawks were rigorously trained from the time they were fledglings before being put into service.

[P60]
The Jin Family of Taiyuan had only two messenger hawks, and they were sent out only for matters of extreme urgency.

[P61]
“We have a problem.”

[P62]
Jin Wikyung muttered in a subdued voice.

[P63]
And that soon became a reality.

[P64]
* * *

[P65]
“My name is Han Yeop.”

[P66]
“Pardon?”

[P67]
“It’s an honor to meet you.”

[P68]
The introduction came out of nowhere. Of course, I recognized his face.

[P69]
I had seen him more often than anyone else since entering the training hall.

[P70]
*Should I call him the training hall guard?*

[P71]
Guard. Martial-artist guard. Whatever the proper term was, the NPC in front of me was a Jin Family of Taiyuan martial artist assigned to the training hall. Bringing me meals and herbal decoctions was one of his duties, too.

[P72]
*But why is he suddenly introducing himself?*

[P73]
I had never exchanged a single word with this NPC. He didn’t seem to harbor any ill will toward me, but he wasn’t especially friendly, either.

[P74]
“Ah, yes. Nice to meet you, too.”

[P75]
Despite my lukewarm response, the guard’s—or rather, Han Yeop’s—face lit up.

[P76]
*What the hell? Why is he suddenly acting like this?*

[P77]
“I was there yesterday as well.”

[P78]
“There? Oh.”

[P79]
He meant the duel. So many people had gathered that there was nothing surprising about Han Yeop being among them.

[P80]
“I watched from beginning to end. I saw the heroic way you fought against that vicious Lee Seogeun of the Mount Heng Sword Sect!”

[P81]
*Vicious? Heroic?*

[P82]
*Is that really how it looked?*

[P83]
Honestly, from a modern man’s perspective, one was as bad as the other.

[P84]
No, I almost wanted to take Lee Seogeun’s side. As an older brother myself, no matter how fucking awful my little sister’s personality was, I’d lose my mind if she were dating a bastard like Jin Taekyung.

[P85]
Of course, the Mount Heng Sword Sect’s attitude and proposal had been absurd. That was why I had no choice but to fight.

[P86]
“My heart trembled the entire time I watched. I’m sure everyone there felt the same way.”

[P87]
Han Yeop continued, his face flushed with excitement. He seemed to be under a serious misunderstanding, but I had no idea when I was supposed to stop him.

[P88]
“I once misunderstood you too, Young Master. But now everyone in the family knows the truth.”

[P89]
This time, I couldn’t help asking.

[P90]
“The truth? What truth?”

[P91]
“That is…”

[P92]
Han Yeop whispered in a tightly hushed voice. Never mind the hot breath against my ear—the actual words sent goose bumps down my skin.

[P93]
In other words—

[P94]
“I’m the Jin Family of Taiyuan’s secret weapon?”

[P95]
“Yes, yes!”

[P96]
Han Yeop nodded furiously.

[P97]
“Everything you’ve shown us until now was a disguise, and ever since you were young, you’ve undergone grueling training, becoming a man accomplished in both civil and martial arts, with virtue and righteousness, a sl—sl—”

[P98]
I couldn’t bring myself to say that word. Han Yeop stepped in before my hands and feet could curl up from embarrassment.

[P99]
“The Sleeping Dragon of Shanxi! Everyone in the family knows now! You’re Shanxi’s Sleeping Dragon, still hiding in the water instead of ascending to the heavens!”

[P100]
*Oh, please. Somebody save me. And don’t shout it out loud.*

[P101]
The Sleeping Dragon? There wasn’t a single person in the family who didn’t know?

[P102]
*If I die, the cause of death will be death by embarrassment.*

[P103]
As I writhed in agony, Han Yeop asked with shining eyes,

[P104]
“It’s true, isn’t it? I know it’s rude, but just between us…?”

[P105]
This wouldn’t do. I resolved to stamp out this ridiculous, cringe-inducing rumor whose origin I couldn’t even guess, then opened my mouth.

[P106]
“I have no idea who spread such an absurd rumor, but…”

[P107]
That was when it happened.

[P108]
Ding.

[P109]
> **System**
>
> A rumor about the **Sleeping Dragon of Shanxi** is spreading throughout the **Jin Family of Taiyuan**.
>
> Fame has risen by 10 due to the influence of the rumor.
>
> The more people believe the rumor, the more Fame will rise.

[P110]
I continued with a solemn expression.

[P111]
“Every word of it is true.”

[P112]
“I knew it! I believed it without a doubt!”

[P113]
I watched Han Yeop’s retreating back, his face still alight with rapture, and shed a single tear.

[P114]
*Fuck…*

[P115]
*Ah, I miss my mom.*

[P116]
* * *

[P117]
My duel with Lee Seogeun had taught me several things.

[P118]
First.

[P119]
*I’m strong.*

[P120]
Early in the game, I had knocked down the Heavenly Axe, the tutorial NPC, with a single blow. What had been mere suspicion back then was now a certainty.

[P121]
I was strong. Strong enough to defeat a Level 30 like Lee Seogeun without much trouble. The difference in combat experience had certainly played a part, but my basic stats were overwhelmingly superior.

[P122]
*Strength, Stamina, Agility. They were all similar, or I had a slight edge.*

[P123]
Stats. In other words, the difference in abilities. In this game, I was a player, and I had continued growing by using the System.

[P124]
Learning martial arts, training, and completing various Quests had rapidly increased my stats. The results had been plain to see during the duel.

[P125]
And second.

[P126]
*I don’t have enough internal energy.*

[P127]
In terms of internal energy alone, Lee Seogeun had been ahead of me. No, he had been overwhelmingly ahead.

[P128]
What the hell had he eaten growing up? I had smashed him dozens of times with the shaft of my spear and pounded him one-sidedly from the mount, yet he had endured it all. He had even counterattacked and drawn on more internal energy at the very end.

[P129]
*I currently have ten years of internal energy.*

[P130]
Lee Seogeun probably had twenty years—twice as much as I did. That led me to a third realization.

[P131]
*The difference in internal energy determines the stage of one’s martial arts.*

[P132]
I had defeated Lee Seogeun, a First Rate martial artist. Yet the realm displayed by the System still listed me as Second Rate.

[P133]
I thought the reason lay in internal energy. Once I raised the one ability I lacked, wouldn’t my realm finally rise as well?

[P134]
After organizing my thoughts that far, another idea suddenly occurred to me.

[P135]
*This is basically just Hunter rank classification.*

[P136]
Every newly awakened Hunter had to visit a designated center to have their abilities, suitable profession, and mana capacity assessed. No matter how high their physical abilities were, anyone with insufficient mana received a frosty reception during their rank evaluation.

[P137]
That was also why mages started at D-rank at the lowest. Because of their profession, mages had plenty of basic mana from the start.

[P138]
*Still, the game is better than reality.*

[P139]
At least you could grow here. Reality had no such thing. Even I had only managed to get lumped in with the E-ranks after working my ass off for seven years. I was still an F-rank Hunter.

[P140]
Anyway, I had now drawn a rough outline.

[P141]
*My stats are high enough. I’ll cycle the Jin Family’s Cultivation Technique whenever I have time and prioritize Quests that reward EXP.*

[P142]
It had been over a week since I was trapped in this godforsaken game. I didn’t know what kind of nonsense was happening in the real world, but I could forget about being rescued.

[P143]
I needed to prepare properly and finish this.

[P144]
“Open Quest window.”

[P145]
Ding.

[P146]
> **System**
>
> **Quest**
>
> **Logout**
>
> You must now make your way through this harsh Murim.
>
> Become stronger and more famous.
>
> For the day that will someday come…
>
> **Grade:** Main Quest  
> **Restriction:** Jin Taekyung  
> **Mission:** Achieve the **First Rate** realm (Incomplete)
>
> &nbsp;&nbsp;&nbsp;&nbsp;Reach Level 30 (17 / 30)
>
> &nbsp;&nbsp;&nbsp;&nbsp;Reach Fame 500 (70 / 500)
>
> **Reward:** **Logout**

[P147]
“Ugh. This is brutal.”

[P148]
I sat cross-legged. Two days remained before my seclusion ended. I intended to gather as much internal energy as possible.

[P149]
> **System**
>
> Fame has risen by 3 due to the influence of the **Sleeping Dragon of Shanxi** rumor.

[P150]
The Fame-increase messages that chimed from time to time offered a small measure of comfort.

[P151]
* * *

[P152]
Late that night, the lights came on in the main assembly hall. At the Lesser Family Head’s request, a secret meeting of the family council had been convened.

[P153]
The hour was late and the summons abrupt, leaving several senior members with sour expressions.

[P154]
“A sudden summons? What is this about?”

[P155]
“Exactly. Calling us here at this hour without even telling us why…”

[P156]
“That’s what happens when the Lesser Family Head is still young. He doesn’t know procedure or etiquette.”

[P157]
“He must have grown rather full of himself after yesterday’s events. Though I suppose his only weakness has disappeared. No one expected the Third Young Master to be that capable.”

[P158]
“That must have taken the wind out of the Elder Council’s sails. They were probably preparing to make a major move over the Third Young Master.”

[P159]
“Hmph. Even now, the Head Elder ought to step forward and set the family straight.”

[P160]
“Careful. Watch your tongue…”

[P161]
At that moment, every sound abruptly stopped. The doors to the meeting room opened from both sides, and Jin Wikyung entered.

[P162]
Opinions of the Lesser Family Head varied among the senior members, but the silence that settled over the room the instant he appeared proved that he possessed the qualities of a leader.

[P163]
“Thank you all for answering my summons at this late hour.”

[P164]
Jin Wikyung took the seat of honor and spoke his opening words, but he found it difficult to continue.

[P165]
*What should he say? Where—and how—should he begin?*

[P166]
His head throbbed. But this was something he had to tell them.

[P167]
“The reason I called everyone here today is…”

[P168]
That was when a strange voice interrupted him.

[P169]
“It must be because of the Mount Heng Sword Sect.”

[P170]
The voice was bizarre. At first, it sounded like an old man’s. And yet it was young as well—rough one moment, smooth the next. There was also an inexplicable resonance to it.

[P171]
*Could it be…?*

[P172]
Jin Wikyung’s face twisted.

[P173]
The doors to the meeting hall, which had seemed as though they would never open again, began to part.

[P174]
Step. Step. Step.

[P175]
Five old men walked in as if they were gliding across the floor. The instant everyone recognized the old man at the front, they hurriedly stood and bowed their heads.

[P176]
“We pay our respects, Head Elder!”

[P177]
The Head Elder. He had appeared after keeping himself shut away from the world for years.
```


## Accepted baseline for regression comparison

This is the accepted English copy before mastering. Use it as a regression
anchor: report a finding when the assembled copy loses an established term,
source-specific image, formatting convention, continuity fact, or other detail
that the baseline preserved, unless the Korean source clearly requires the
change.

```markdown
[P1]
# Chapter 16

[P2]
“Whew. Finally done.”

[P3]
Jin Wikyung set down his brush as he spoke. Wipeng, who was sitting in a chair beside the door as always, raised his head.

[P4]
“You’re getting faster at handling your work. You must be exhausted toda—”

[P5]
Wipeng let his words trail off. He had just noticed the mountain of documents still piled on the table.

[P6]
Come to think of it, it was only around noon. There was no way anyone could finish that much work in so little time.

[P7]
*Did I hear him wrong?*

[P8]
“Good. This should be enough…”

[P9]
This time, it wasn’t a hallucination. Jin Wikyung’s face suddenly popped up above the pile of documents, proof enough of that.

[P10]
“Wipeng, come here. This is very important.”

[P11]
His voice was so serious that Wipeng grew slightly concerned.

[P12]
*Did something major happen?*

[P13]
Perhaps they had discovered some serious embezzlement in the documents. Or maybe the Elder Council, which had been constantly watching for an opportunity, had caused some kind of incident.

[P14]
*This is bad. We haven’t even finished dealing with the Mount Heng Sword Sect yet.*

[P15]
A moment later, Wipeng accepted the document in question from Jin Wikyung. His expression twisted into something bizarre.

[P16]
“…What is this?”

[P17]
“You can’t tell? It’s a drawing.”

[P18]
The document Wipeng had feared was nowhere to be found. Instead, Jin Wikyung had handed him a single sheet of rice paper covered in drawings.

[P19]
“No, that’s not what I meant. Why are you suddenly—”

[P20]
Jin Wikyung cut him off with a secretive smile.

[P21]
“Look closely. It isn’t an ordinary drawing.”

[P22]
*It isn’t an ordinary drawing?*

[P23]
Wipeng’s eyes lit up.

[P24]
All kinds of legends circulating through Murim flashed through his mind.

[P25]
A Daoist who achieved ascension after looking at a single painting. An absolute master who attained enlightenment after seeing a mural in an ancient cave!

[P26]
Wipeng’s gaze roamed over the rice paper for a long while. Then, at some point, it began to tremble as if struck by lightning.

[P27]
“T-this is, perhaps…!”

[P28]
“You noticed. That’s right.”

[P29]
Jin Wikyung continued with a chuckle.

[P30]
“I tried drawing yesterday’s duel.”

[P31]
“……”

[P32]
“Lee Seogeun lying defeated, and Taekyung standing proudly! The sky spread above the head of the young hero who would one day become the greatest under heaven!”

[P33]
“……”

[P34]
“I deliberately chose a composition looking up from below. What do you think? It’s good, right? Isn’t it?”

[P35]
Wipeng’s hands trembled around the rice paper. If he had been acting on impulse, he would have crumpled it, torn it apart, covered it with a week’s worth of piss and shit, dried it thoroughly, and burned it.

[P36]
But—

[P37]
“…It’s very well drawn.”

[P38]
Wipeng was a rational man. He summoned the magnificent mental fortitude of a martial artist at the Peak realm.

[P39]
Of course, he also had enough courage to reprimand a lord whose sanity was in serious doubt.

[P40]
“How can you say that when there’s so much work piled up? Are you telling me that you spent the entire morning drawing this one picture?”

[P41]
“Of course not.”

[P42]
“Then you know how ridiculous this is—”

[P43]
“Did you think I spent three hours focusing on only one thing?”

[P44]
“What?”

[P45]
“Of course I drew another one. I was going to show it to you later, but you really are quick to catch on.”

[P46]
Wipeng accepted the next sheet of rice paper from Jin Wikyung with trembling hands. Grinning from ear to ear, Jin Wikyung began explaining the drawing.

[P47]
“I tried to depict the scene immediately after the duel. The young hero declares that he won’t rest on his laurels and will return to the training hall! And the people gazing up at him in admiration!”

[P48]
“I agree with a considerable part of that. The Third Young Master really has changed a great deal.”

[P49]
“Right? I was surprised myself.”

[P50]
After defeating Lee Seogeun in the duel, Jin Taekyung had defied everyone’s expectations and returned to the training hall. Jin Wikyung’s eyes grew hazy as he recalled the events of the previous day.

[P51]
“I always knew a day like this would come. The youngest is a heavenly eagle. Wipeng, can’t you hear it? The powerful sound of Taekyung’s wings beating…”

[P52]
“I don’t know about wings, but I can hear you spouting nonsense.”

[P53]
Wipeng lowered the rice paper with a sigh of complete resignation.

[P54]
Flap.

[P55]
“Gasp.”

[P56]
“See? You can hear it!”

[P57]
Wipeng hurriedly turned toward the window. A hawk that had just landed was preening its feathers. A small container hung from its ankle.

[P58]
“It’s a messenger hawk.”

[P59]
These hawks were trained intensively from the time they were fledglings before being put to use as messengers.

[P60]
The Jin Family of Taiyuan had only two messenger hawks, and they were sent out only for matters of extreme urgency.

[P61]
“We have a problem.”

[P62]
Jin Wikyung muttered in a subdued voice.

[P63]
And that problem soon made itself known.

[P64]
* * *

[P65]
“My name is Han Yeop.”

[P66]
“Pardon?”

[P67]
“It’s an honor to meet you.”

[P68]
It was a sudden introduction. Of course, I knew his face.

[P69]
He was the person I had seen most often since entering the training hall.

[P70]
*Should I call him the training hall’s guard?*

[P71]
Guard. Martial-artist guard. Whatever the proper term was, the NPC in front of me was a Jin Family of Taiyuan martial artist assigned to the training hall. Bringing me meals and herbal decoctions was one of his duties, too.

[P72]
*But why is he introducing himself all of a sudden?*

[P73]
This was an NPC I had never exchanged a single word with. He didn’t seem to bear me any ill will, but he wasn’t especially friendly, either.

[P74]
“Ah, yes. Nice to meet you, too.”

[P75]
Despite my lukewarm response, the guard’s—or rather, Han Yeop’s—face brightened.

[P76]
*What the hell? Why is he suddenly acting like this?*

[P77]
“I was there yesterday, too.”

[P78]
“There? Oh.”

[P79]
He meant the duel. So many people had gathered that it wasn’t surprising for Han Yeop to have been among them.

[P80]
“I watched from beginning to end. I saw the heroic way you fought against that vicious Lee Seogeun of the Mount Heng Sword Sect!”

[P81]
*Vicious? Heroic?*

[P82]
*That’s how it looked?*

[P83]
Honestly, from a modern man’s perspective, one was as bad as the other.

[P84]
No, I almost wanted to take Lee Seogeun’s side. As an older brother myself, even if my little sister’s personality were fucking awful, I’d lose my mind if she said she was dating a guy like Jin Taekyung.

[P85]
Of course, the Mount Heng Sword Sect’s attitude and proposal had been absurd. That was why I had no choice but to fight.

[P86]
“My heart trembled the entire time I watched. I’m sure everyone there felt the same way.”

[P87]
Han Yeop continued with an excited expression. He seemed to be under a serious misunderstanding, and I had no idea when I was supposed to stop him.

[P88]
“I used to misunderstand you, too, Young Master. But now everyone in the family knows the truth.”

[P89]
This time, I couldn’t help asking.

[P90]
“The truth? What truth?”

[P91]
“That is…”

[P92]
Han Yeop whispered in a voice so hushed that it was practically a secret. Leaving aside the hot breath against my ear, what he was saying gave me goose bumps.

[P93]
In other words—

[P94]
“I’m the Jin Family of Taiyuan’s secret weapon?”

[P95]
“Yes, yes!”

[P96]
Han Yeop nodded furiously.

[P97]
“Your behavior until now was all an act, and ever since you were young, you’ve undergone bone-shattering training, becoming a man accomplished in both civil and martial arts, with virtue and righteousness, a sl—sl—”

[P98]
I couldn’t bring myself to say that word. Han Yeop came to my rescue before my hands and feet could curl up from embarrassment.

[P99]
“The Sleeping Dragon of Shanxi! Everyone in the family knows now! You’re Shanxi’s Sleeping Dragon, still hiding in the water instead of ascending to the heavens!”

[P100]
*Oh, please. Somebody save me. And don’t shout it out loud.*

[P101]
The Sleeping Dragon? There wasn’t a single person in the family who didn’t know?

[P102]
*If I die, the cause of death will be death by embarrassment.*

[P103]
As I writhed in agony, Han Yeop asked with shining eyes,

[P104]
“It’s true, isn’t it? I know it’s rude, but just between us…?”

[P105]
This wouldn’t do. I decided to suppress this ridiculous, cringe-inducing rumor whose origin I couldn’t even guess, then opened my mouth.

[P106]
“I have no idea who started such an absurd rumor, but…”

[P107]
That was when it happened.

[P108]
Ding.

[P109]
> **System**
>
> A rumor about the **Sleeping Dragon of Shanxi** is spreading throughout the **Jin Family of Taiyuan**.
>
> Fame has risen by 10 due to the influence of the rumor.
>
> The more people believe the rumor, the more Fame will rise.

[P110]
I continued with a solemn expression.

[P111]
“Every word of it is true.”

[P112]
“I knew it! I believed it with all my heart!”

[P113]
I watched Han Yeop walk away with a face full of rapture and shed a single tear.

[P114]
*Fuck…*

[P115]
*Ah, I miss my mom.*

[P116]
* * *

[P117]
I realized several things through my duel with Lee Seogeun.

[P118]
First.

[P119]
*I’m strong.*

[P120]
Early in the game, I had knocked down the Heavenly Axe, who had appeared as the tutorial NPC, in a single hit. What had only been a suspicion back then had now become a certainty.

[P121]
I was strong. Strong enough to defeat a Level 30 like Lee Seogeun without much trouble. The difference in combat experience had certainly played a part, but my basic stats were overwhelmingly superior.

[P122]
*Strength, Stamina, Agility. They were all similar, or I had a slight edge.*

[P123]
Stats. In other words, the difference in abilities. In this game, I was a player, and I had continued growing by using the System.

[P124]
I had raised my stats rapidly by learning martial arts, training, and completing various Quests. The result had shown itself in the duel.

[P125]
And second.

[P126]
*I don’t have enough internal energy.*

[P127]
Lee Seogeun had surpassed me in internal energy. No, he had been overwhelmingly ahead.

[P128]
What had he been eating growing up? Even after I smashed him dozens of times with the spear shaft, and even when I beat him one-sidedly from a mount, he endured it. He even counterattacked and drew on more internal energy at the final moment.

[P129]
*I currently have ten years of internal energy.*

[P130]
Lee Seogeun probably had twenty years—twice as much as I did. That led me to a third realization.

[P131]
*The difference in internal energy determines the stage of one’s martial arts.*

[P132]
I had defeated Lee Seogeun, who was First Rate. But the realm displayed by the System still said I was Second Rate.

[P133]
I thought the reason lay in internal energy. Once I raised the one ability I lacked, wouldn’t my realm finally rise as well?

[P134]
After organizing my thoughts that far, another idea suddenly occurred to me.

[P135]
*This is basically just Hunter rank classification.*

[P136]
A newly awakened Hunter had to be tested at a designated center for their abilities, suitable profession, and mana capacity. No matter how high their physical abilities were, if their mana capacity was lacking, they received a cold reception during the rank evaluation.

[P137]
That was also why mages started at D-rank at the lowest. Because of their profession, mages had plenty of basic mana from the start.

[P138]
*Still, the game is better than reality.*

[P139]
At least you could grow here. Reality had no such thing. Even I had only managed to get lumped in with the E-ranks after working my ass off for seven years. I was still an F-rank Hunter.

[P140]
Anyway, I had now drawn a rough outline.

[P141]
*My stats are sufficient. I’ll keep cycling the Jin Family’s Cultivation Technique whenever I have time, and focus on taking Quests that reward EXP.*

[P142]
It had been over a week since I was trapped in this godforsaken game. I didn’t know what kind of nonsense was happening in the real world, but I could forget about being rescued.

[P143]
I needed to prepare properly and finish this.

[P144]
“Open Quest window.”

[P145]
Ding.

[P146]
> **System**
>
> **Quest**
>
> **Logout**
>
> You must now make your way through this harsh Murim.
>
> Become stronger and more famous.
>
> For the day that will come someday…
>
> **Grade:** Main Quest  
> **Restriction:** Jin Taekyung  
> **Mission:** Achieve the **First Rate** realm (Incomplete)
>
> &nbsp;&nbsp;&nbsp;&nbsp;Reach Level 30 (17 / 30)
>
> &nbsp;&nbsp;&nbsp;&nbsp;Reach Fame 500 (70 / 500)
>
> **Reward:** **Logout**

[P147]
“Ugh. This is brutal.”

[P148]
I sat cross-legged. Two days remained before my seclusion ended. I intended to gather as much internal energy as possible.

[P149]
> **System**
>
> Fame has risen by 3 due to the influence of the Sleeping Dragon of Shanxi rumor.

[P150]
The Fame-increase messages that chimed from time to time were a small source of comfort.

[P151]
* * *

[P152]
Late at night, the lights came on in the main assembly hall. At the request of the Lesser Family Head, a secret meeting of the family council was taking place.

[P153]
It was very late, and the summons had been so sudden that several of the senior members wore sour expressions.

[P154]
“A sudden summons? What is this about?”

[P155]
“Exactly. They didn’t even tell us why they were calling us here at this hour.”

[P156]
“That’s what happens when the Lesser Family Head is still young. He doesn’t know procedure or etiquette.”

[P157]
“He must have grown rather full of himself after yesterday’s events. Though I suppose his only weakness has disappeared. No one expected the Third Young Master to be that capable.”

[P158]
“The Elder Council must have been deflated. They were probably preparing to make a major move over the Third Young Master.”

[P159]
“Hmph. Even now, the Head Elder should step forward and set the family straight.”

[P160]
“Careful. Watch your tongue…”

[P161]
At that moment, every sound abruptly stopped. The doors to the meeting room opened from both sides, and Jin Wikyung entered.

[P162]
The senior members had varying opinions of their Lesser Family Head, but the silence that settled over the room the instant he appeared proved that he possessed the qualities of a leader.

[P163]
“Thank you all for answering my summons at this late hour.”

[P164]
Jin Wikyung took the seat of honor and spoke his opening words, but he found it difficult to continue.

[P165]
*What should he say? Where should he begin, and how?*

[P166]
His head throbbed. But this was something he had to tell them.

[P167]
“The reason I called everyone here today is…”

[P168]
That was when a strange voice interrupted him.

[P169]
“It must be because of the Mount Heng Sword Sect.”

[P170]
The voice was bizarre. At first, it sounded like an old man’s. And yet it was young as well—rough one moment, smooth the next. There was also an inexplicable resonance to it.

[P171]
*Could it be…?*

[P172]
Jin Wikyung’s face twisted.

[P173]
The doors to the meeting room, which had seemed permanently sealed, began to part.

[P174]
Step. Step. Step.

[P175]
Five old men walked in as if they were gliding across the floor. The instant everyone recognized the old man at the front, they hurriedly stood and bowed their heads.

[P176]
“We pay our respects, Head Elder!”

[P177]
The Head Elder. He had appeared after keeping himself shut away from the world for years.
```


## Deterministic QA

```json
{
  "version": 1,
  "chapter": 16,
  "passed": true,
  "metrics": {
    "source_characters": 6346,
    "translation_characters": 14383,
    "length_ratio": 2.266,
    "source_paragraphs": 184,
    "translation_paragraphs": 177
  },
  "errors": [],
  "warnings": [
    {
      "code": "terminology",
      "message": "matched preferred term is absent",
      "details": {
        "korean": "기세",
        "preferred": "aura / momentum"
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
        "korean": "일격",
        "preferred": "One Strike"
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
        "korean": "습득",
        "preferred": "Acquired"
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
