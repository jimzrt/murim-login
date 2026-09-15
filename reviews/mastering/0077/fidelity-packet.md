# Fidelity Gate — Chapter 77

Audit the complete assembled English chapter against the Korean source.
Report only genuine source-fidelity defects: wrong action, subject, object,
causality, quantity, mechanism, terminology, ambiguity, joke logic, register,
or physical detail. Check repeated UI labels and counters against how they
behave across the whole scene. Interpret idioms by their function, not by
translating their component words. Do not report optional stylistic rewrites.
Do not invent `current` spans that are absent from the assembled English.
Do not report a glossary-correct rendering as a defect merely because the
baseline used an older synonym.

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
  1|＃77화
  2|
  3|
  4|
  5|남자 둘이 술잔을 기울이다 보면 온갖 얘기가 다 튀어나오기 마련이다. 돈, 사람, 미래…….
  6|
  7|그중에서도 진호 형이 선호하는 대화 주제는 여자였다.
  8|
  9|그는 술만 들어갔다 하면 세상에서 가장 슬픈 남자가 되어 첫사랑을 회상하곤 했다.
 10|
 11|
 12|
 13|‘고2 때 처음 만났지.’
 14|
 15|‘이 인간 또 취했네.’
 16|
 17|‘때는 바야흐로 꽃이 만개한 3월의 새 학기. 교실 문 열고 걔가 딱 들어오는데…….’
 18|
 19|‘눈앞이 아찔했겠지. 귀에서는 막, 천국의 종소리가 댕댕 울려 퍼지고?’
 20|
 21|‘어? 어떻게 알았냐?’
 22|
 23|‘백 번도 넘게 들었으니까. 천국의 종소리는 개뿔. 아주 소설을 써라.’
 24|
 25|‘네가 사랑을 몰라서 그래, 인마. 하긴 모태 솔로가 뭘 알겠냐마는.’
 26|
 27|‘못 사귄 게 아니라 안 사귄 거거든.’
 28|
 29|‘모쏠 새끼들이 꼭 저 소리 하더라. 무슨 모쏠 가이드북이라도 있냐? 너 누구 좋아해 본 적도 없지?’
 30|
 31|‘……이, 있을걸?’
 32|
 33|‘어휴, 됐다. 백 번, 천 번 말해 봤자 뭐 하냐. 직접 겪어 봐야 알지. 술이나 한잔 더 따라 봐.’
 34|
 35|
 36|
 37|몇 달 전의 술자리가 지금 갑자기 생각난 이유는 간단했다.
 38|
 39|‘형 말이 맞았어.’
 40|
 41|댕- 대앵-
 42|
 43|들린다. 종소리가.
 44|
 45|
 46|
 47|* * *
 48|
 49|
 50|
 51|송 양.
 52|
 53|늘씬한 체구에 조막만 한 얼굴. 식재료가 가득 담긴 봉투를 양손에 주렁주렁 매단 천사가 나를 발견하고 멈칫했다.
 54|
 55|“누구?”
 56|
 57|고혹적이면서도 청량한 목소리에 정신이 아득해지고, 오밀조밀 인형 같은 이목구비에 가슴이 쿵쾅거렸다.
 58|
 59|‘세상에.’
 60|
 61|나는 마른침을 삼켰다. 지난 27년간 모태 솔로로 지내 왔던 게 바로 오늘을 위해서였다는 생각이 든다.
 62|
 63|머릿속에서는 이미 시뮬레이션이 돌아가는 중이다.
 64|
 65|‘집은 마당이 있는 전원주택. 아이는 둘에 고양이 한 마리. 완벽해.’
 66|
 67|운기조식 때도 꿈쩍 않던 연애 세포가 살아 숨 쉰다.
 68|
 69|나는 최대한 낮은 목소리로 말하려 입을 열었다. 자칭 연애 고수라는 진호 형은 마음에 드는 여성에게는 중저음을 사용하라고 누누이 강조해 왔다.
 70|
 71|“저는…….”
 72|
 73|“이쪽은 진태경. 송 양도 알지? 그 왜, 지난번에 한 번 얘기했었잖아. 내가 아끼는 동생이 C급 헌터로 재각성 했다고.”
 74|
 75|“아, 그분이세요? 생각보다 젊으시네.”
 76|
 77|“…….”
 78|
 79|나는 난데없이 끼어든 임꺽정의 발을 지그시 밟으며 재차 입을 열었다.
 80|
 81|“네. 제가 바로 그…….”
 82|
 83|“뭘 이렇게 많이 사 오셨습니까? 따로 예약해 둔 식당이 있는데요.”
 84|
 85|“비싸고 양도 적은데 거길 왜 가요? 그냥 안에서 고기나 좀 구워 먹으면 되지.”
 86|
 87|“…….”
 88|
 89|최 팀장. 당신 내 손으로 죽인다. 반드시 죽일 거야.
 90|
 91|훼방꾼들을 차례차례 노려봤다. 내 살벌한 시선에 뭔가 말하려던 김 집사가 조용히 입을 다물었다.
 92|
 93|‘기회는 지금뿐이야.’
 94|
 95|아무도 끼어들지 않는 완벽한 타이밍. 마침 송 양도 나를 보고 있다. 나는 매력적인 중저음으로 말했다.
 96|
 97|“안녕하세요. 이번에 C급 헌터가 된 스물일곱 살 진태경이라고 합니다. 생일은 4월 22일. 별자리는 황소자리고, 혈액형은 RH+A형입니다. 취미는 독서와 영화 평론. 앞으로 잘 부탁드려요.”
 98|
 99|“…….”
100|
101|“…….”
102|
103|“…….”
104|
105|아무도 입을 열지 않는 고요한 침묵, 마침내 그녀의 붉은 입술이 열렸다.
106|
107|“아, 네.”
108|
109|송 양이 사슴 같은 눈망울로 빤히 나를 바라봤다. 내 동굴 목소리에 제대로 뻑이 간 표정이다. 거기에 취미가 독서와 영화 평론이라는 지적인 면모까지 부각시켰으니 100퍼센트다.
110|
111|‘고마워 진호 형. 잘되면 술 살게.’
112|
113|마음속으로 환호성을 내지르던 그때, 최 팀장이 더듬거리는 목소리로 끼어들었다.
114|
115|“시, 식사라도 하면서 천천히 얘기해 볼까요? 송이 씨도 장 보느라 고생하셨을 텐데.”
116|
117|또다시 대화를 방해받았다는 분노는 그녀의 이름을 듣는 순간 흔적도 없이 사라졌다.
118|
119|“송이 씨요?”
120|
121|“송송이. 송송이예요. 제 이름.”
122|
123|차분한 목소리로 대답한 송 양, 아니 송이 씨가 가게 안으로 쏙 들어갔다. 나는 멍하니 서서 그녀의 이름을 되새겼다.
124|
125|“송송이…….”
126|
127|세상에, 이름도 예뻐. 매력적이야. 눈부셔.
128|
129|머리부터 발끝까지 내 스타일이다. 운명의 상대를 만났다는 생각에 반쯤 넋이 나간 나를 깨운 건 최 팀장의 목소리였다.
130|
131|“태경 씨.”
132|
133|“예, 예?”
134|
135|“저기…… 아닙니다. 천천히 들어오세요.”
136|
137|한숨을 푹 내쉰 최 팀장이 등을 돌렸다. 뭐야, 왜 저래?
138|
139|“제가 뭐 잘못했어요?”
140|
141|내 물음에 최 팀장의 뒤를 따르던 김 집사가 멈칫했다.
142|
143|“그…… 힘내십시오.”
144|
145|두 사람이 떠나자 남은 건 임꺽정과 나, 단둘뿐이었다.
146|
147|“형님. 제가 뭐 실수한 거예요?”
148|
149|“실수? 아니, 넌 죄를 저지른 거야.”
150|
151|“죄요?”
152|
153|“그래. 결코 용서받지 못할 죄를 지었지.”
154|
155|“헉.”
156|
157|내가 무슨 실수라도 했나? 가슴이 덜컥 내려앉은 그때, 임꺽정이 굳은 얼굴로 말을 이었다.
158|
159|“한 여자의 마음을 훔친 죄.”
160|
161|“……!”
162|
163|“짜식. 남자인 나도 반할 뻔했다. 송 양 표정 봤어? 완전 뻑 갔더라. 게임 끝이야, 끝!”
164|
165|“저, 정말요?”
166|
167|“축하한다, 태경아! 국수 먹자!”
168|
169|“형니임-!”
170|
171|와락!
172|
173|나는 감격을 이기지 못하고 임꺽정의 품에 안겼다. 그가 호탕하게 웃으며 내 등을 두드렸다.
174|
175|“애는 몇 명 낳을 거야? 뭐? 두 명? 그러지 말고 세 명 해! 으하하하!”
176|
177|
178|
179|* * *
180|
181|
182|
183|가게 내부.
184|
185|문 앞에 바짝 붙어 있던 최 팀장과 김 집사가 서로를 마주 보았다.
186|
187|“김 집사님, 어떻게 생각하세요?”
188|
189|“마법 아이템으로 소리를 차단한 도련님의 현명한 판단에 감탄할 뿐입니다.”
190|
191|“그렇죠?”
192|
193|“그렇습니다.”
194|
195|두 사람은 약속이라도 한 듯이 뒤를 힐끔거렸다. 송송이는 부산하게 식사를 준비 중이었다.
196|
197|“만약 방금 대화를 송이 씨가 들었으면…….”
198|
199|“송이 씨께서 당장 길드를 탈퇴하더라도 저희가 위약금 물어 줘야 됩니다.”
200|
201|“저런 멘트는 어디서 배운 걸까요? 혹시 김 집사님께서 젊었을 때…….”
202|
203|김 집사가 정색하고 대답했다.
204|
205|“도련님, 방금 말씀은 상당히 듣기 거북하군요. 저런 멘트는 대격변 이전에도 없었습니다.”
206|
207|“태경 씨, 모태 솔로겠죠?”
208|
209|“모태 솔로가 아니면 제가 오늘부터 김 집사가 아니라 박 집삽니다.”
210|
211|“임 헌터님도 문제가 있던데요.”
212|
213|“이런 말씀 드리기 좀 그렇지만, 입마개를 씌우고 싶었습니다.”
214|
215|“임 헌터님, 미혼 맞죠?”
216|
217|“안타깝게도 기혼입니다. 애도 둘 딸린.”
218|
219|“도대체 어떻게……?”
220|
221|“저도 그게 의문입니다.”
222|
223|길드의 미래가 어둡다.
224|
225|두 사람이 어두운 얼굴로 고개를 젓던 그 순간이었다.
226|
227|“저기요.”
228|
229|등 뒤에서 들려오는 목소리.
230|
231|앞치마를 걸친 송송이가 허리춤에 손을 얹고 두 사람을 바라보고 있었다.
232|
233|“두 분이서 뭘 그렇게 속닥거리세요? 준비하는데 손 하나 까딱 안 하고.”
234|
235|“아, 송이 씨. 그게.”
236|
237|“식사 후에는 저희가 치우겠습니다.”
238|
239|“됐고요. 식사 준비 끝났으니까 와서 들어요. 그리고 임씨 아저씨랑…….”
240|
241|송송이가 한숨처럼 말을 이었다.
242|
243|“그, 황소자리도 부르시고.”
244|
245|
246|
247|* * *
248|
249|
250|
251|적당히 달궈진 불판 앞.
252|
253|내가 비장한 얼굴로 입을 열었다.
254|
255|“송이 씨.”
256|
257|집게와 가위를 막 집어 든 송이 씨가 멈칫했다.
258|
259|“네?”
260|
261|“주십시오. 제가 굽겠습니다.”
262|
263|“괜찮아요. 이따 뒷정리할 때나 도와주시면 되는데.”
264|
265|“제 취미가 고기 굽기, 특기는 고기 자르기입니다.”
266|
267|“……독서와 영화 평론 아니었어요?”
268|
269|“그건 빙산의 일각에 지나지 않습니다.”
270|
271|테이블 밑으로 임꺽정의 발을 건드리자 곧장 지원 사격이 들어왔다.
272|
273|“송 양이 몰라서 하는 말인데 이 친구가 고기 하나는 끝내주게 잘 구워. 언제 한번은 불판 다섯 개를 동시에 막, 어? 고기를 씹으면 육즙이 아주 그냥 입 안에서 주르륵. 머릿속에서는 폭죽이 펑펑!”
274|
275|나는 점잖게 한마디를 보탰다.
276|
277|“별자리는 황소자리.”
278|
279|“그렇지! 황소자리 남자가 말이야, 고기도 잘 굽고 성격도 순수하고 참 우직…….”
280|
281|우지직.
282|
283|최 팀장이 부러진 나무젓가락을 내려놓으며 중얼거렸다.
284|
285|“죄송합니다. 힘 조절이 안 돼서.”
286|
287|“여기요.”
288|
289|기다렸다는 듯이 새 젓가락을 건네주는 송이 씨의 모습에 억장이 무너진다. 인정하긴 싫지만 미인과 미남. 선남선녀의 투 샷은 매우 잘 어울렸다.
290|
291|‘설마. 아니겠지?’
292|
293|애써 부정해 보지만 마음이 착잡하다.
294|
295|나는 울적한 얼굴로 고기를 불판에 올렸다.
296|
297|치이이익.
298|
299|송이 씨는 최 팀장이랑 무슨 사이일까.
300|
301|치이이익.
302|
303|예전부터 친분이 있었던 건 확실하다. 괜히 길드 창립 멤버가 아닐 테니까.
304|
305|치이이익.
306|
307|생각해 보니까 최 팀장 저 자식 수상해. 아까부터 대화를 끼어들지 않나, 멀쩡한 젓가락은 왜 부러트려서 맥을 끊어?
308|
309|치이이익.
310|
311|B급 헌터라는 놈이 힘 조절을 못 해서 그랬다는 게 말이야, 방구야. 송이 씨 앞이라고 힘 센 거 자랑하나? 나는 쇠젓가락으로 매듭도 지을 수 있는데…….
312|
313|“저기요.”
314|
315|퍼뜩 고개를 들었다. 호수처럼 맑은 눈동자가 나를 빤히 응시하고 있었다.
316|
317|“타요.”
318|
319|“예, 예?”
320|
321|“탄다구요. 고기.”
322|
323|“헉!”
324|
325|치지지직.
326|
327|황급히 고기를 뒤집었지만 이미 늦었다.
328|
329|“그냥 제가 할게요.”
330|
331|“아뇨. 제가.”
332|
333|“생각해 보니 그래도 오늘 처음 오셨는데 고기는 제가 구워서 대접하는 게 맞죠.”
334|
335|세상에, 외모만 천사 같은 게 아니다.
336|
337|‘아, 송이 씨. 당신은 도덕책.’
338|
339|그녀의 비단결 같은 마음씨에 다시 한번 반했다.
340|
341|서걱. 서걱.
342|
343|치이익.
344|
345|집게를 건네받은 그녀가 솜씨 좋게 고기를 굽고 자른다.
346|
347|나는 멍하니 그 모습을 지켜봤다.
348|
349|‘고기 굽는 모습도 예쁘네.’
350|
351|대충 틀어 올려 쪽진머리, 분주히 움직이는 희고 가느다란 손. 동작 하나하나에서 빛이 난다.
352|
353|“으음.”
354|
355|얼마나 지났을까, 신중한 얼굴로 고기를 지켜보던 그녀가 말했다.
356|
357|“다 익었다. 거기 접시 좀 주실래요?”
358|
359|“옙.”
360|
361|일회용 용기에 다 익은 고기를 척척 담아낸다. 아까부터 느낀 건데, 한두 번 해 본 솜씨가 아니다.
362|
363|“이런 거 많이 해 보셨나 봐요.”
364|
365|“네.”
366|
367|“혹시 고기 집 알바 하셨어요?”
368|
369|“네.”
370|
371|“우와. 얼마나요?”
372|
373|“2년이요.”
374|
375|“히야, 언제요?”
376|
377|“고등학교 때요.”
378|
379|“허어, 그때 알바 하는 애들 별로 없었는데.”
380|
381|“아, 네.”
382|
383|어쩜 좋아. 생활력 강한 것도 딱 내 스타일이야.
384|
385|이상하게 대답이 짧은 것 같지만 기분 탓일 거다. 호응을 위한 추임새도 마음껏 퍼부어 주었다.
386|
387|‘대화 자체는 순조로워.’
388|
389|진호 형이 말하길, 공통점부터 파고들어야 호감을 얻을 수 있다고 했다. 나는 열정적으로 말을 내뱉었다.
390|
391|“저랑 비슷하네요. 하루 두 탕, 세 탕도 뛰고 그랬는데. 어느 하루는 일 끝나고 집에 왔더니…….”
392|
393|“아, 네. 그런데 저기.”
394|
395|“네?”
396|
397|“너무 가까운 것 같아서요. 불판 아직 뜨거운데…….”
398|
399|나도 모르게 몸이 송이 씨를 향해 잔뜩 기울어진 상태였다.
400|
401|“괜찮습니다. 그까짓 거 조금 데이고 말죠. 하하하!”
402|
403|“그래도 조심하는 게.”
404|
405|“정말 괜찮아요. 걱정 안 하셔도 돼요.”
406|
407|“…….”
408|
409|어쩐지 송이 씨의 낯빛이 어둡다. 이거 설마.
410|
411|‘내가 다칠까 봐 걱정하는 건가!’
412|
413|충격이다. 오늘 처음 만난 나를 이렇게까지 생각해 주다니.
414|
415|그리고 확실히 알았다. 그녀도 내게 관심이 있다는 사실을.
416|
417|환청처럼 진호 형의 목소리가 어디선가 들려왔다.
418|
419|
420|
421|‘커플이 되는 가장 중요한 덕목이 뭔지 알아? 바로 용기야.’
422|
423|‘태경아, 명심해라. 용기 있는 자가 미인을 얻는다.’
424|
425|
426|
427|형, 나 이제야 알 것 같아. 그리고 고마워.
428|
429|‘그래. 용기를 내자.’
430|
431|나는 떨리는 마음으로 그녀를 응시했다. 지금부터 하려는 말은 27년 인생을 통틀어 난생처음으로 뱉는 거다.
432|
433|“송이 씨. 우리 오늘부터 1일…….”
434|
435|그 순간, 벌떡 일어난 최 팀장이 외쳤다.
436|
437|“1일! 오늘은 진태경 헌터님이 우리 길드 가족이 된 첫날입니다! 김 집사님?”
438|
439|“예, 도련님! 술 준비됐습니다!”
440|
441|언제나 느긋하던 김 집사가 소주잔을 번개 같은 속도로 채워 넣었다.
442|
443|콸콸콸!
444|
445|꼴꼴꼴이 아니라 콸콸콸이다.
446|
447|반은 버리고 반은 때려 붓는 모습에 어이가 없었지만 나는 반드시 해야 할 말이 있었다.
448|
449|“송이 씨. 다시 한번 말할게요. 우리…….”
450|
451|최 팀장이 술잔을 번쩍 치켜들었다.
452|
453|“우리 길드를 위하여!”
454|
455|“송이 씨. 저쪽은 신경 쓰지 말고 내 말 들어요.”
456|
457|송이 씨가 대답했다.
458|
459|“위하여!”
460|
461|“…….”
462|
463|내 말 못 들은 거겠지? 그래, 못 들었을 거야.
```

## Assembled English

```markdown
[P1]
# Chapter 77

[P2]
When two men sit around drinking, all kinds of topics are bound to come spilling out. Money, people, the future…

[P3]
Of all those topics, Jinho hyung’s favorite was women.

[P4]
Whenever he got drunk, he became the saddest man in the world and reminisced about his first love.

[P5]
*I first met her when I was a high school sophomore.*

[P6]
*This guy’s drunk again.*

[P7]
*It was March, the start of a new school year, and the flowers were in full bloom. She opened the classroom door and walked in, and then…*

[P8]
*You must’ve been dazzled. The bells of heaven must’ve started ringing in your ears—ding, ding, ding?*

[P9]
*Huh? How did you know?*

[P10]
*Because I’ve heard this story more than a hundred times. The bells of heaven, my ass. Go write a novel.*

[P11]
*That’s because you don’t understand love, you punk. Then again, what would a lifelong single know?*

[P12]
*It’s not that I couldn’t date. I chose not to.*

[P13]
*You lifelong-single bastards always say that. Is there some kind of guidebook? You’ve never even liked anyone, have you?*

[P14]
*…I-I think I have.*

[P15]
*Oh, forget it. What good is telling you a hundred or a thousand times? You have to experience it yourself to understand. Pour me another drink.*

[P16]
The reason I suddenly remembered that drinking session from a few months ago was simple.

[P17]
*Hyung was right.*

[P18]
Ding—ding—

[P19]
I could hear them. The bells.

[P20]
* * *

[P21]
Miss Song.

[P22]
She had a slender figure and a tiny face. An angel with grocery bags dangling from both hands spotted me and stopped short.

[P23]
“Who are you?”

[P24]
Her captivating yet refreshing voice made my mind go blank, while her delicate, doll-like features set my heart pounding.

[P25]
*My God.*

[P26]
I swallowed hard. It felt as though I had spent the past twenty-seven years as a lifelong single just for this day.

[P27]
A simulation was already running in my head.

[P28]
*We’ll live in a country house with a yard. Two children and one cat. Perfect.*

[P29]
The dating cells that had never budged, even while I circulated my qi, were springing to life.

[P30]
I opened my mouth, trying to make my voice as low as possible. Jinho hyung, a self-proclaimed master of romance, had repeatedly stressed that I should use a deep, resonant voice with a woman I liked.

[P31]
“I’m…”

[P32]
“This is Jin Taekyung. You’ve heard about him too, right, Miss Song? You know, the one I told you about last time. I said my beloved little brother had undergone reawakening as a C-rank Hunter.”

[P33]
“Oh, you’re that person? You’re younger than I expected.”

[P34]
“……”

[P35]
I gently stepped on Im Kkeokjeong’s foot for cutting in out of nowhere, then opened my mouth again.

[P36]
“Yes. I’m the very…”

[P37]
“Why did you buy so much? We have a restaurant reserved.”

[P38]
“It’s expensive and the portions are tiny. Why go there? We can just grill some meat inside.”

[P39]
“……”

[P40]
*Team Leader Choi. I’m going to kill you with my own hands. I definitely will.*

[P41]
I glared at the meddlers one after another. Butler Kim had been about to say something, but under my murderous stare, he quietly closed his mouth.

[P42]
*This is my only chance.*

[P43]
The timing was perfect. No one was interrupting, and Miss Song was looking right at me. I spoke in an attractive, deep voice.

[P44]
“Hello. My name is Jin Taekyung. I’m twenty-seven years old and recently became a C-rank Hunter. My birthday is April 22. I’m a Taurus, and my blood type is RH-positive, type A. My hobbies are reading and film criticism. I hope we get along.”

[P45]
“……”

[P46]
“……”

[P47]
“……”

[P48]
In the still silence, no one said a word. At last, her red lips parted.

[P49]
“Oh, yes.”

[P50]
Miss Song stared straight at me with her doe-like eyes. She looked completely spellbound by my cavernous voice. And I had even highlighted my intellectual side by mentioning reading and film criticism. This was a hundred-percent success.

[P51]
*Thank you, Jinho hyung. If this works out, drinks are on me.*

[P52]
Just as I was cheering inside, Team Leader Choi cut in with a stammer.

[P53]
“W-Why don’t we take our time and talk over a meal? Song-i must be tired from grocery shopping.”

[P54]
My anger at being interrupted again vanished without a trace the moment I heard her name.

[P55]
“Song-i?”

[P56]
“Song Song. My name is Song Song.”

[P57]
Miss Song—or rather, Song-i—answered calmly before slipping inside the store. I stood there blankly, repeating her name to myself.

[P58]
“Song Song…”

[P59]
My God, even her name was beautiful. Charming. Dazzling.

[P60]
She was my type from head to toe. I was half out of my mind at the thought that I had met my destined partner when Team Leader Choi’s voice snapped me out of it.

[P61]
“Taekyung.”

[P62]
“Yes, yes?”

[P63]
“Um… Never mind. Take your time coming in.”

[P64]
Team Leader Choi let out a deep sigh and turned away. *What was wrong with him?*

[P65]
“Did I do something wrong?”

[P66]
At my question, Butler Kim, who had been following Team Leader Choi, stopped short.

[P67]
“Um… Stay strong.”

[P68]
Once the two of them left, only Im Kkeokjeong and I remained.

[P69]
“Hyung-nim. Did I make some kind of mistake?”

[P70]
“A mistake? No. You committed a crime.”

[P71]
“A crime?”

[P72]
“Yes. A crime that can never be forgiven.”

[P73]
“Gasp.”

[P74]
Had I really done something wrong? Just as my heart sank, Im Kkeokjeong continued with a solemn expression.

[P75]
“The crime of stealing a woman’s heart.”

[P76]
“……!”

[P77]
“You little punk. Even I almost fell for you. Did you see Miss Song’s expression? She was completely smitten. It’s over. You won!”

[P78]
“R-Really?”

[P79]
“Congratulations, Taekyung! Let's eat noodles!”[^1]

[P80]
“Hyung-nim!”

[P81]
I couldn’t contain my emotion and threw myself into Im Kkeokjeong’s arms. He laughed heartily and patted me on the back.

[P82]
“How many kids are you going to have? What? Two? Don’t stop there—make it three! Hahahaha!”

[P83]
[^1]: In Korean, “eating noodles” is a traditional expression associated with celebrating someone's wedding.

[P84]
* * *

[P85]
Inside the store.

[P86]
Team Leader Choi and Butler Kim, who had been pressed right up against the door, turned to face each other.

[P87]
“What do you think, Butler Kim?”

[P88]
“I can only admire the Young Master's wise decision to block out the sound with a magic Item.”

[P89]
“Right?”

[P90]
“Precisely.”

[P91]
As if they had planned it, the two men glanced over their shoulders. Song Song was bustling around, preparing the meal.

[P92]
“If Song-i had heard that conversation just now…”

[P93]
“Even if Miss Song quit the Guild on the spot, we would have to pay the penalty.”

[P94]
“Where did he learn lines like that? Butler Kim, when you were younger, did you perhaps…?”

[P95]
Butler Kim’s expression turned stern.

[P96]
“Young Master, that remark was highly unpleasant to hear. Lines like that did not exist even before the Great Cataclysm.”

[P97]
“Taekyung has been single his entire life, right?”

[P98]
“If he isn’t, then as of today I’m no longer Butler Kim. I’m Butler Park.”

[P99]
“Hunter Im seems to have problems too.”

[P100]
“I hate to say this, but I wanted to put a muzzle on him.”

[P101]
“Hunter Im is unmarried, right?”

[P102]
“Unfortunately, he’s married. He even has two children.”

[P103]
“How on earth…?”

[P104]
“I wonder the same thing.”

[P105]
The Guild’s future was bleak.

[P106]
Just as the two men shook their heads with gloomy expressions, a voice came from behind them.

[P107]
“Excuse me.”

[P108]
Song Song stood there in an apron, one hand on her hip as she looked at the two men.

[P109]
“What are you two whispering about? You haven’t lifted a finger to help while I’ve been preparing everything.”

[P110]
“Oh, Miss Song. It’s just…”

[P111]
“We’ll clean up after the meal.”

[P112]
“Forget it. The food’s ready, so come and eat. And call Mr. Im and…”

[P113]
Song Song continued with a sigh.

[P114]
“That… Taurus, too.”

[P115]
* * *

[P116]
In front of the grill, which had been heated to just the right temperature, I opened my mouth with a solemn expression.

[P117]
“Miss Song.”

[P118]
Song Song stopped just as she picked up the tongs and scissors.

[P119]
“Yes?”

[P120]
“Give them to me. I’ll grill the meat.”

[P121]
“It’s fine. You can help clean up afterward.”

[P122]
“My hobby is grilling meat, and my specialty is cutting it.”

[P123]
“…I thought your hobbies were reading and film criticism?”

[P124]
“That was only the tip of the iceberg.”

[P125]
I nudged Im Kkeokjeong’s foot under the table, and he immediately provided backup.

[P126]
“You wouldn't know this, Miss Song, but this guy can grill meat like nobody's business. One time, he was working five grills at once, just—huh? And when you bite into it, the juices flood your mouth. Fireworks start going off in your head!”

[P127]
I added one more point in a dignified tone.

[P128]
“I'm a Taurus.”

[P129]
“That’s right! A Taurus man grills meat well, and he’s pure-hearted, honest, and so steadfast…”

[P130]
Crack.

[P131]
Team Leader Choi set down the broken wooden chopsticks and muttered, “I'm sorry. I couldn't control my strength.”

[P132]
“Here.”

[P133]
As if she had been waiting for that moment, Song Song handed him a fresh pair of chopsticks. My heart sank.

[P134]
I hated to admit it, but the beautiful woman and the handsome man looked perfect together.

[P135]
*No way. It can’t be.*

[P136]
I tried to deny it, but my heart felt heavy.

[P137]
With a gloomy expression, I placed the meat on the grill.

[P138]
Sizzle.

[P139]
What kind of relationship did Song Song have with Team Leader Choi?

[P140]
Sizzle.

[P141]
It was obvious they had known each other for a long time. She wouldn’t be a founding member of the Guild otherwise.

[P142]
Sizzle.

[P143]
Come to think of it, that bastard Team Leader Choi was suspicious. He’d been interrupting our conversation from the start. And why had he snapped a perfectly good pair of chopsticks and ruined the mood?

[P144]
Sizzle.

[P145]
A B-rank Hunter claiming he couldn’t control his strength? What kind of bullshit excuse was that? Was he showing off how strong he was in front of Song Song? I could tie metal chopsticks into a knot too…

[P146]
“Excuse me.”

[P147]
I looked up with a start. Eyes as clear as a lake were staring straight at me.

[P148]
“It’s burning.”

[P149]
“Yes, yes?”

[P150]
“The meat. It’s burning.”

[P151]
“Gasp!”

[P152]
Sizzle-sizzle-sizzle.

[P153]
I hurriedly flipped the meat, but it was already too late.

[P154]
“I’ll do it.”

[P155]
“No. I will.”

[P156]
“Come to think of it, since you're here for the first time today, it's only right that I grill the meat and serve you.”

[P157]
My God. She wasn’t just an angel on the outside.

[P158]
*Oh, Miss Song. You’re an ethics textbook.*[^2]

[P159]
[^2]: Taekyung substitutes “ethics textbook” into a Korean phrase meaning “what on earth are you?”

[P160]
I fell for her nature, gentle as silk, all over again.

[P161]
Slice. Slice.

[P162]
Sizzle.

[P163]
After taking the tongs from me, she grilled and cut the meat with practiced skill.

[P164]
I watched her in a daze.

[P165]
*She even looks beautiful grilling meat.*

[P166]
Her hair was loosely twisted into a bun, and her slender, pale hands moved busily. Every movement seemed to shine.

[P167]
“Hmm.”

[P168]
How much time had passed? She had been watching the meat carefully when she spoke.

[P169]
“It’s done. Could you hand me a plate?”

[P170]
“Yes, ma’am.”

[P171]
She neatly placed the fully cooked meat into a disposable container. I had noticed it earlier, but this was clearly not something she had done only once or twice.

[P172]
“You must’ve done this a lot.”

[P173]
“Yes.”

[P174]
“Did you work part-time at a barbecue restaurant?”

[P175]
“Yes.”

[P176]
“Wow. For how long?”

[P177]
“Two years.”

[P178]
“Wow, when?”

[P179]
“When I was in high school.”

[P180]
“Huh. Not many kids had part-time jobs back then.”

[P181]
“Oh, yes.”

[P182]
*What am I going to do? Even her resourcefulness is exactly my type.*

[P183]
Her answers seemed strangely short, but that had to be my imagination. I kept showering her with enthusiastic little responses to keep the conversation going.

[P184]
*The conversation itself is going smoothly.*

[P185]
Jinho hyung had said that if you wanted someone to like you, you had to start by finding common ground. I launched into my story with enthusiasm.

[P186]
“We're pretty similar. I used to work two or even three shifts in a day. One day, after I finished work and came home…”

[P187]
“Oh, yes. But, um…”

[P188]
“Yes?”

[P189]
“You seem a little close. The grill is still hot…”

[P190]
Without realizing it, I had leaned my entire body toward Song Song.

[P191]
“It's fine. I'll just get a little burned. Hahaha!”

[P192]
“You should still be careful.”

[P193]
“I’m really fine. You don’t have to worry.”

[P194]
“……”

[P195]
Song Song’s expression seemed strangely dark.

[P196]
*Could it be…?*

[P197]
*Is she worried I might get hurt?*

[P198]
I was stunned. She was thinking about me this much even though we had only met today.

[P199]
And then I knew for certain. She was interested in me, too.

[P200]
Jinho hyung’s voice reached me from somewhere, like an auditory hallucination.

[P201]
*Do you know what the most important virtue is when it comes to becoming a couple? Courage.*

[P202]
*Taekyung, remember this. A man with courage wins the beauty.*

[P203]
*Hyung, I think I finally understand. And thank you.*

[P204]
*That's right. Let's be brave.*

[P205]
I stared at her, my heart trembling. What I was about to say was something I had never once said in all twenty-seven years of my life.

[P206]
“Miss Song. Starting today, you and I are on day one…”

[P207]
At that moment, Team Leader Choi shot to his feet and shouted.

[P208]
“Day one! Today is Hunter Jin Taekyung’s first day as a member of our Guild family! Butler Kim?”

[P209]
“Yes, Young Master! The soju is ready!”

[P210]
The usually unhurried Butler Kim filled the shot glasses at lightning speed.

[P211]
Glug-glug-glug!

[P212]
Not a gentle trickle—it was pouring full blast.

[P213]
Half of it spilled, and the other half was poured in with brute force. The sight left me speechless, but there was something I absolutely had to say.

[P214]
“Miss Song. Let me say it again. You and I…”

[P215]
Team Leader Choi raised his glass high.

[P216]
“To our Guild!”

[P217]
“Miss Song. Ignore them and listen to me.”

[P218]
Song Song answered.

[P219]
“To our Guild!”

[P220]
“……”

[P221]
She didn’t hear me, right? Yeah. She couldn’t have heard me.
```


## Accepted baseline for regression comparison

This is the accepted English copy before mastering. Use it as a regression
anchor: report a finding when the assembled copy loses an established term,
source-specific image, formatting convention, continuity fact, or other detail
that the baseline preserved, unless the Korean source, RULES.md, or the exact
glossary requires the change. Exact glossary English wins over an older baseline
synonym for the same Korean key.

```markdown
[P1]
# Chapter 77

[P2]
When two men sit around tilting their glasses of liquor, all kinds of topics are bound to come spilling out. Money, people, the future…

[P3]
Of all those topics, the one Jinho hyung preferred was women.

[P4]
Whenever he got drunk, he became the saddest man in the world and reminisced about his first love.

[P5]
*I first met her when I was a high school sophomore.*

[P6]
*This guy's drunk again.*

[P7]
*It was March, the start of a new school year, with flowers in full bloom. She opened the classroom door and walked in, and then…*

[P8]
*You must have been dazzled. The bells of heaven must have started ringing in your ears—ding, ding, ding?*

[P9]
*Huh? How did you know?*

[P10]
*Because I've heard this story more than a hundred times. The bells of heaven, my ass. Go write a novel.*

[P11]
*That's because you don't understand love, you punk. Then again, what would a lifelong single know?*

[P12]
*It's not that I couldn't date. I chose not to.*

[P13]
*You lifelong-single bastards always say that. Is there some kind of guidebook? You've never even liked anyone, have you?*

[P14]
*……I think I have.*

[P15]
*Oh, forget it. What good is it to tell you a hundred or a thousand times? You have to experience it yourself to understand. Pour me another drink.*

[P16]
The reason I suddenly remembered that drinking session from a few months ago was simple.

[P17]
*Hyung was right.*

[P18]
Ding—ding—

[P19]
I could hear them. The bells.

[P20]
* * *

[P21]
Miss Song.

[P22]
She had a slender figure and a tiny face. An angel with grocery bags hanging from both hands spotted me and stopped short.

[P23]
“Who are you?”

[P24]
Her captivating yet refreshing voice made my mind go blank, while her delicate, doll-like features made my heart pound.

[P25]
*My God.*

[P26]
I swallowed dryly. It felt as though I had spent the past twenty-seven years as a lifelong single just for this day.

[P27]
A simulation was already running in my head.

[P28]
*Our home will be a country house with a yard. Two children and one cat. Perfect.*

[P29]
The dating cells that had never budged, even while I circulated my qi, were springing to life.

[P30]
I opened my mouth to speak in the lowest voice I could manage. Jinho hyung, a self-proclaimed master of romance, had always stressed that I should use a deep, resonant voice with a woman I liked.

[P31]
“I’m…”

[P32]
“This is Jin Taekyung. You’ve heard about him too, right, Miss Song? You know, the one I told you about last time. I said my beloved little brother had reawakened as a C-rank Hunter.”

[P33]
“Oh, you’re that person? You’re younger than I expected.”

[P34]
“……”

[P35]
I gently stepped on Im Kkeokjeong’s foot, who had interrupted me out of nowhere, and opened my mouth again.

[P36]
“Yes. I’m the very…”

[P37]
“Why did you buy so much? We have a restaurant reserved.”

[P38]
“It’s expensive and the portions are tiny. Why go there? We can just grill some meat inside.”

[P39]
“……”

[P40]
*Team Leader Choi. I’m going to kill you with my own hands. I really am.*

[P41]
I glared at the meddlers one after another. Butler Kim had been about to say something, but he quietly closed his mouth under my murderous stare.

[P42]
*This is my only chance.*

[P43]
It was the perfect moment. No one was interrupting, and Miss Song was looking right at me. I spoke in an attractive, deep voice.

[P44]
“Hello. My name is Jin Taekyung. I’m twenty-seven years old and recently became a C-rank Hunter. My birthday is April 22. I’m a Taurus, and my blood type is RH-positive, type A. My hobbies are reading and film criticism. I hope we get along.”

[P45]
“……”

[P46]
“……”

[P47]
“……”

[P48]
In the still silence, no one said a word. At last, her red lips parted.

[P49]
“Oh, yes.”

[P50]
Miss Song stared straight at me with her deerlike eyes. Her expression suggested that she had been utterly enchanted by my cavernous voice. And I had even highlighted my intellectual side by mentioning reading and film criticism. This was a hundred-percent success.

[P51]
*Thank you, Jinho hyung. If this works out, drinks are on me.*

[P52]
Just as I was cheering inside, Team Leader Choi interrupted in a stammering voice.

[P53]
“W, why don’t we talk over a meal? Miss Song must be tired from grocery shopping.”

[P54]
My anger at being interrupted again vanished without a trace the moment I heard her name.

[P55]
“Song is your first name?”

[P56]
“Song Song. Song Song is my name.”

[P57]
Miss Song—or rather, Song Song—answered in a calm voice before slipping inside the store. I stood there blankly, repeating her name to myself.

[P58]
“Song Song…”

[P59]
My God, even her name was beautiful. So charming. So dazzling.

[P60]
She was my type from head to toe. I was half out of my mind at the thought that I had met my fated partner when Team Leader Choi's voice snapped me out of it.

[P61]
“Mr. Jin.”

[P62]
“Yes, yes?”

[P63]
“Um… Never mind. Take your time coming in.”

[P64]
Team Leader Choi let out a deep sigh and turned away. *What was wrong with him?*

[P65]
“Did I do something wrong?”

[P66]
At my question, Butler Kim, who was following Team Leader Choi, stopped short.

[P67]
“Um… Stay strong.”

[P68]
Once the two of them left, only Im Kkeokjeong and I remained.

[P69]
“Hyung-nim. Did I make some kind of mistake?”

[P70]
“A mistake? No. You committed a crime.”

[P71]
“A crime?”

[P72]
“Yes. A crime you could never be forgiven for.”

[P73]
“Gasp.”

[P74]
Had I really done something wrong? Just as my heart sank, Im Kkeokjeong continued with a solemn expression.

[P75]
“The crime of stealing a woman's heart.”

[P76]
“……!”

[P77]
“You little punk. Even I almost fell for you. Did you see Miss Song's expression? She was completely smitten. It's over. You won!”

[P78]
“R-Really?”

[P79]
“Congratulations, Taekyung! Let's eat noodles!”[^1]

[P80]
“Hyung-nim!”

[P81]
I could not contain my emotion and threw myself into Im Kkeokjeong's arms. He laughed heartily and patted me on the back.

[P82]
“How many kids are you going to have? What? Two? Don't stop there—make it three! Hahahaha!”

[P83]
[^1]: In Korean, “eating noodles” is a traditional expression associated with celebrating someone's wedding.

[P84]
* * *

[P85]
Inside the store.

[P86]
Team Leader Choi and Butler Kim, who had been pressed right up against the door, turned to face each other.

[P87]
“What do you think, Butler Kim?”

[P88]
“I can only admire the Young Master's wise decision to block out the sound with a magic item.”

[P89]
“Right?”

[P90]
“Precisely.”

[P91]
As if they had planned it, the two men glanced over their shoulders. Song Song was busily preparing the meal.

[P92]
“If Miss Song heard that conversation just now…”

[P93]
“Even if Miss Song quit the Guild on the spot, we would have to pay the penalty.”

[P94]
“Where did he learn lines like that? Could it be that you used to say things like that when you were young, Butler Kim?”

[P95]
Butler Kim answered with a stern expression.

[P96]
“Young Master, that remark was highly unpleasant to hear. Lines like that did not exist even before the Great Cataclysm.”

[P97]
“Mr. Jin is a lifelong single, right?”

[P98]
“If he is not, then starting today I am no longer Butler Kim. I am Butler Park.”

[P99]
“Hunter Im seems to have problems too.”

[P100]
“I hate to say this, but I wanted to put a muzzle on him.”

[P101]
“Hunter Im is unmarried, right?”

[P102]
“Unfortunately, yes. He even has two children.”

[P103]
“How on earth…?”

[P104]
“I wonder the same thing.”

[P105]
The Guild's future was bleak.

[P106]
It was at that moment, while the two men shook their heads with gloomy expressions, that a voice came from behind them.

[P107]
“Excuse me.”

[P108]
Song Song stood there wearing an apron, one hand on her hip as she looked at the two men.

[P109]
“What are you two whispering about? You haven't lifted a finger to help while I was preparing everything.”

[P110]
“Oh, Miss Song. It's just…”

[P111]
“We'll clean up after the meal.”

[P112]
“Never mind that. The food is ready, so come and eat. And call Mr. Im and…”

[P113]
Song Song continued with a sigh.

[P114]
“That… Taurus, too.”

[P115]
* * *

[P116]
In front of the grill, which had been heated to just the right temperature, I opened my mouth with a solemn expression.

[P117]
“Miss Song.”

[P118]
Song Song stopped just as she picked up the tongs and scissors.

[P119]
“Yes?”

[P120]
“Give them to me. I'll grill the meat.”

[P121]
“It's okay. You can help clean up afterward.”

[P122]
“My hobby is grilling meat, and my specialty is cutting it.”

[P123]
“……I thought your hobbies were reading and film criticism?”

[P124]
“That was only the tip of the iceberg.”

[P125]
When I nudged Im Kkeokjeong's foot under the table, immediate backup arrived.

[P126]
“You wouldn't know this, Miss Song, but this guy can grill meat like nobody's business. One time, he was working five grills at once, just—huh? And when you bite into it, the juices flood your mouth. Fireworks start going off in your head!”

[P127]
I added one more point in a dignified tone.

[P128]
“I'm a Taurus.”

[P129]
“That's right! A Taurus man can grill meat, and he's pure-hearted and honest and so steadfast…”

[P130]
Crack.

[P131]
Team Leader Choi set down the broken wooden chopsticks and muttered, “I'm sorry. I couldn't control my strength.”

[P132]
“Here.”

[P133]
Song Song handed him a new pair of chopsticks as if she had been waiting for it. My heart sank.

[P134]
I hated to admit it, but the beautiful woman and handsome man made a wonderful pair.

[P135]
*No way. It can't be.*

[P136]
I tried to deny it, but my heart felt heavy.

[P137]
With a gloomy expression, I placed the meat on the grill.

[P138]
Sizzle.

[P139]
What kind of relationship did Song Song have with Team Leader Choi?

[P140]
Sizzle.

[P141]
It was obvious they had known each other for a long time. She wouldn't be a founding member of the Guild for no reason.

[P142]
Sizzle.

[P143]
Come to think of it, that bastard Team Leader Choi was suspicious. He had been interrupting our conversation from the start. And why had he broken perfectly good chopsticks and ruined the mood?

[P144]
Sizzle.

[P145]
A B-rank Hunter claiming he could not control his strength? What kind of excuse was that? Was he showing off how strong he was in front of Song Song? I could tie a knot in metal chopsticks, too…

[P146]
“Excuse me.”

[P147]
I looked up with a start. Eyes as clear as a lake were staring straight at me.

[P148]
“It's burning.”

[P149]
“Yes, yes?”

[P150]
“The meat. It's burning.”

[P151]
“Gasp!”

[P152]
Sizzle-sizzle-sizzle.

[P153]
I hurriedly flipped the meat, but it was already too late.

[P154]
“I'll do it.”

[P155]
“No. I will.”

[P156]
“Come to think of it, since you're here for the first time today, it's only right that I grill the meat and serve you.”

[P157]
My God. She wasn't just an angel on the outside.

[P158]
*Oh, Miss Song. You’re an ethics textbook.*[^2]

[P159]
[^2]: In Korean, “ethics textbook” is a pun on a phrase meaning “what on earth are you?”

[P160]
I fell for her gentle nature all over again.

[P161]
Slice. Slice.

[P162]
Sizzle.

[P163]
After taking the tongs from me, she grilled and cut the meat with practiced skill.

[P164]
I watched her in a daze.

[P165]
*She even looks beautiful while grilling meat.*

[P166]
Her hair was loosely twisted into a bun, and her slender, pale hands moved busily. Every one of her movements seemed to shine.

[P167]
“Hmm.”

[P168]
How much time had passed? She had been watching the meat carefully when she spoke.

[P169]
“It’s done. Could you hand me a plate?”

[P170]
“Yes, ma'am.”

[P171]
She neatly placed the fully cooked meat into a disposable container. I had noticed it earlier, but this was clearly not something she had done only once or twice.

[P172]
“You must have done this a lot.”

[P173]
“Yes.”

[P174]
“Did you work part-time at a barbecue restaurant?”

[P175]
“Yes.”

[P176]
“Wow. For how long?”

[P177]
“Two years.”

[P178]
“Wow, when?”

[P179]
“When I was in high school.”

[P180]
“Huh. Not many people worked part-time jobs back then.”

[P181]
“Oh, yes.”

[P182]
*What am I going to do? Even her resourcefulness is exactly my type.*

[P183]
Her answers seemed strangely short, but that had to be my imagination. I showered her with plenty of little responses to keep the conversation going.

[P184]
*The conversation itself is going smoothly.*

[P185]
Jinho hyung had said that you had to start by finding common ground if you wanted someone to like you. I spoke passionately.

[P186]
“We're pretty similar. I used to work two or even three shifts in a day. One day, after I finished work and came home…”

[P187]
“Oh, yes. But, um.”

[P188]
“Yes?”

[P189]
“You seem a little close. The grill is still hot…”

[P190]
Without realizing it, I had leaned my entire body toward Song Song.

[P191]
“It's fine. I'll just get a little burned. Hahaha!”

[P192]
“You should still be careful.”

[P193]
“I'm really fine. You don't have to worry.”

[P194]
“……”

[P195]
Song Song's expression seemed strangely dark. *Could it be…?*

[P196]
*Is she worried that I might get hurt?*

[P197]
It was shocking. She was thinking about me this much even though we had only met today.

[P198]
And then I knew for certain. She was interested in me, too.

[P199]
Jinho hyung's voice reached me from somewhere, like a hallucination.

[P200]
*Do you know what the most important virtue is when it comes to becoming a couple? Courage.*

[P201]
*Taekyung, remember this. A man with courage wins the beauty.*

[P202]
*Hyung, I think I finally understand. And thank you.*

[P203]
*That's right. Let's be brave.*

[P204]
I looked at her with a trembling heart. What I was about to say was something I had never once said in my entire twenty-seven years of life.

[P205]
“Miss Song. Starting today, you and I are on day one…”

[P206]
At that moment, Team Leader Choi jumped to his feet and shouted.

[P207]
“Day one! Today is the first day Hunter Jin Taekyung has become part of our Guild family! Butler Kim?”

[P208]
“Yes, Young Master! The soju is ready!”

[P209]
The usually unhurried Butler Kim filled the shot glasses at lightning speed.

[P210]
Glug-glug-glug!

[P211]
Not a gentle trickle—it was pouring full blast.

[P212]
Half of it spilled, while the other half was poured in with such force that I was left speechless. But there was something I absolutely had to say.

[P213]
“Miss Song. Let me say it again. You and I…”

[P214]
Team Leader Choi raised his glass high.

[P215]
“To our Guild!”

[P216]
“Miss Song. Ignore them and listen to me.”

[P217]
Song Song answered.

[P218]
“To our Guild!”

[P219]
“……”

[P220]
She didn't hear me, right? Yes. She couldn't have heard me.
```


## Exact glossary matches

These English spellings are binding for the matched Korean keys.

| 진태경    | **Jin Taekyung**   |
| 송송이    | **Song Song**     |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 운기조식   | **circulate one's qi**                           | Usually better as a verb than a proper-name technique |
| 상태               | **Status**                     |
| 아이템              | **Item**                       |
| 매력               | **Charm**                      |
| 헌터      | **Hunter**            |
| 길드      | **Guild**             |
| 팀장      | **Team Leader**       |
| 대격변     | **Great Cataclysm**   |
| 임꺽정 | **Im Kkeokjeong** |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 재각성 | **reawakening** | Established Hunter awakening category described as having no further stage. |
| 송이 | **Song-i** | Short form used for Song Song; Taekyung's love interest. |
| 갑자 | **jiazi** | Traditional sixty-year cycle. |
| 기해 | **qi sea** | Name for the dantian, the place where internal energy begins and gathers. |

## Deterministic QA

```json
{
  "version": 1,
  "chapter": 77,
  "passed": true,
  "metrics": {
    "source_characters": 6056,
    "translation_characters": 13216,
    "length_ratio": 2.182,
    "source_paragraphs": 221,
    "translation_paragraphs": 221
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
        "korean": "진태",
        "preferred": "Jintae"
      }
    },
    {
      "code": "terminology",
      "message": "matched preferred term is absent",
      "details": {
        "korean": "갑자",
        "preferred": "jiazi"
      }
    },
    {
      "code": "terminology",
      "message": "matched preferred term is absent",
      "details": {
        "korean": "기해",
        "preferred": "qi sea"
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
