# Fidelity Gate — Chapter 127

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
  1|＃127화
  2|
  3|
  4|
  5|물음표가 느낌표로, 느낌표가 황당함과 분노로 바뀌는 데까지는 그리 오랜 시간이 걸리지 않았다.
  6|
  7|가장 먼저 정적을 깬 것은 진무경이었다.
  8|
  9|“너…….”
 10|
 11|벌겋게 달아오른 얼굴, 거친 숨소리. 당장이라도 내 주둥이에 한 방 먹이고 싶은지 주먹이 움찔거린다.
 12|
 13|‘음, 제대로 열받았군.’
 14|
 15|싸늘하다. 가슴에 비수가 날아와 꽂힌다. 하지만 걱정하지 마라. 내게는 든든한 방패가 있으니까.
 16|
 17|“어허, 무경아.”
 18|
 19|나직하게 들리는 목소리에 진무경의 얼굴이 와락 일그러졌다.
 20|
 21|“형님!”
 22|
 23|“태경이도 다 생각이 있었겠지. 안 그러느냐?”
 24|
 25|나는 짐짓 눈을 내리깔았다.
 26|
 27|“아닙니다. 소제(小弟)의 생각이 짧았습니다.”
 28|
 29|“응?”
 30|
 31|“호기심에 그만…… 하지만 큰형님의 이야기를 듣고 깨달았습니다. 그것은 결코 갖고 있어서도, 숨겨서도 안 되는 물건이라는 사실을 말입니다.”
 32|
 33|생각만 해도 치가 떨린다는 듯이 주먹을 부르르 떠는 연출도 잊지 않았다.
 34|
 35|“마교! 그 악독한 놈들의 이름만 들어도 치가 떨립니다!”
 36|
 37|이건 진심이다. 기왕 만드는 거 잘 좀 만들지, 광기에 젖은 살인귀가 되는 심각한 결함이 있다니!
 38|
 39|“허어.”
 40|
 41|나를 바라보는 진위경의 눈빛에 애정이 듬뿍 담겨 있었다.
 42|
 43|“나중에 커서 협의지사가 되겠다던 작고 귀여운 꼬마 아이가 생각나는구나. 그때 네 나이가 여섯 살이었다. 기억나느냐?”
 44|
 45|당연히 안 나지.
 46|
 47|재작년 일도 가물가물한데 이 몸의 원주인이 여섯 살 때 뭘 했는지 알 턱이 있나. 그러나 나는 비장하게 고개를 끄덕였다.
 48|
 49|“똑똑히 기억합니다. 제 유일한 꿈이었으니까요.”
 50|
 51|협의지사건 경기도지사건, 오늘 이 시간부로 그게 내 여섯 살 때 장래 희망이다.
 52|
 53|“허허, 그 어린 녀석이 이렇게 훌륭히 장성하다니.”
 54|
 55|흐뭇하게 웃은 진위경이 이번엔 다른 두 사람을 향해 고개를 돌렸다.
 56|
 57|“그 자리에 자네도 있었지. 위팽, 기억나는가?”
 58|
 59|위팽이 숨도 쉬지 않고 대답했다.
 60|
 61|“그건 모르겠고, 그러고서 딱 십 년 후부터 계집질 시작한 건 기억납니다. 커서 뭐가 될 거냐고 물었더니 그때는 천하제일의 풍류남아라고 하던데요.”
 62|
 63|“영웅이라면 모름지기 풍류를 알아야지.”
 64|
 65|“무공은 쥐뿔도 모르는데 풍류만 알아서 뭐 합니까? 말씀하시는 영웅이 밤의 영웅, 기녀들의 영웅. 뭐 그런 겁니까?”
 66|
 67|“조용히 하게. 우리 막내는 어릴 때부터 싹수가 남달랐어.”
 68|
 69|“그러니까 그 싹수가…… 어후, 됐습니다. 내가 말을 말아야지.”
 70|
 71|벌컥벌컥.
 72|
 73|술을 병째로 들이붓는 위팽을 깔끔하게 무시한 진위경의 시선이 다음 주자를 향했다.
 74|
 75|“무경아. 이제 막내의 진심을 알았으니 화 풀거라.”
 76|
 77|오만상을 쓰고 있던 진무경이 입을 뗐다.
 78|
 79|“저 자식 한 대만 때리면 안 됩니까?”
 80|
 81|“어허.”
 82|
 83|“딱 한 대만. 제발.”
 84|
 85|싸늘한 목소리에 내가 재빨리 고개를 숙였다.
 86|
 87|“이 못난 아우를 용서하십시오, 둘째 형님.”
 88|
 89|“지금까지 반말 찍찍 하던 놈이 형님 같은 소리 하네.”
 90|
 91|“예? 제가요?”
 92|
 93|“그만해라. 마지막 경고다.”
 94|
 95|“아닙니다. 차라리 절 때리십시오. 그렇게라도 형님의 분이 풀리신다면 이 아우, 기꺼이 감내하겠습니다.”
 96|
 97|“야, 이 새끼야!”
 98|
 99|벌떡 일어난 진무경이 헉, 하는 신음과 함께 도로 주저앉았다. 가슴팍에 동여맨 붕대가 붉게 젖어 드는 걸 보니 상처가 벌어진 모양이다.
100|
101|“아이고 형님, 괜찮으십니까!”
102|
103|“이 자식이 또…… 커헉!”
104|
105|“의원, 의원!”
106|
107|순식간에 난장판이 되어 버린 술자리.
108|
109|묵묵히 두 번째 술병을 집어 든 위팽이 중얼거렸다.
110|
111|“가문 꼴 잘 돌아간다…….”
112|
113|얼마나 잘 돌아가는지, 무려 산서제일가다.
114|
115|
116|
117|* * *
118|
119|
120|
121|결국, 의원이 다녀가고 나서야 분위기가 수습됐다.
122|
123|나를 찢어 죽일 듯한 진무경의 시선을 외면하고 잠력단을 품에서 꺼냈다.
124|
125|“바로 이겁니다.”
126|
127|마치 피를 응축시킨 것처럼 온통 붉은 단환.
128|
129|진위경과 위팽이 잠력단을 유심히 살폈다.
130|
131|“위팽, 어떻게 생각하나?”
132|
133|“보기만 해도 피비린내가 나는군요. 흉악한 물건입니다.”
134|
135|“정말 마교 쪽에서 만든 걸까?”
136|
137|“글쎄요. 그렇다면 마기가 느껴져야 하는데…… 저로서는 확신하기 어렵습니다.”
138|
139|“그렇지? 뭔가 달라.”
140|
141|두 사람의 표정은 몹시 심각했다. 잠력단을 어디서, 누가 만들었는지 궁금한 건 나도 매한가지라 힌트를 던져 주기로 했다.
142|
143|“잠력단이라고 하던데요.”
144|
145|“잠력단?”
146|
147|“네, 풍양의 입으로 직접 들었어요.”
148|
149|진무경이 불쑥 끼어들었다.
150|
151|“풍양이? 도대체 언제?”
152|
153|“너 기절해 있을 때요.”
154|
155|“……후욱. 후우욱.”
156|
157|누가 뭐라고 하든 내가 유일한 목격자고 증인이다. 본전도 못 찾은 진무경이 화를 가라앉히려 호흡을 가다듬을 때, 다른 두 사람은 미간의 골만 깊어지고 있었다.
158|
159|“잠력단이라, 위팽?”
160|
161|“저도 처음 들어 봅니다. 이 정도 효력에 마교의 물건이라면 분명 정마대전 때 쓰였을 터인데…….”
162|
163|“마교가 아닐 수도 있지 않아요?”
164|
165|두 사람의 시선이 날 향했다.
166|
167|“마교가 아니다?”
168|
169|“어찌 그렇게 생각하십니까?”
170|
171|“처음부터 단정 지을 필요는 없다 이거죠.”
172|
173|사실 마교가 만든 단환이 아니라면 다시 가져갈 수 있을까 하는 희망 사항에서 나온 말이다.
174|
175|물론 내 나름대로 달리 떠오른 생각도 있었고.
176|
177|‘대장로.’
178|
179|지난번 전쟁에서 표면적으로 드러난 적은 분명 항산검문이었지만 진정한 적은 대장로, 바로 그였다.
180|
181|이분법적인 추측보다는 제3의 세력이 있을지도 모른다는 가능성을 늘 염두에 둬야 한다는 것이 내 생각이다.
182|
183|“뭐, 그냥 갑자기 그런 생각이 들었다는 거죠.”
184|
185|내 말을 모두 들은 두 사람의 표정이 심상치 않다. 그리고 다음 순간, 위팽의 입에서 아주 작은 목소리가 흘러나왔다.
186|
187|그것은 무의식중에 신음처럼 흘러나온 한 단어였다.
188|
189|“암천…….”
190|
191|“위팽.”
192|
193|진위경의 날카로운 눈빛이 이어지는 말을 틀어막았다.
194|
195|“아, 죄송합니다. 제가 실언을.”
196|
197|황급히 얼버무리는 위팽. 하지만 이미 늦었다.
198|
199|암천이라는 두 글자가 내 뇌리에 깊게 박힌 후였으니까.
200|
201|‘암천? 그게 뭐지?’
202|
203|그때, 예상치 못한 일이 일어났다.
204|
205|띠링.
206|
207|
208|
209|- [암천]에 관한 미약한 정보를 얻었습니다.
210|
211|- [잠력단]에 관한 아이템 설명이 변경됩니다.
212|
213|
214|
215|느닷없는 시스템 알림. 나는 잠력단을 들고 있는 위팽에게 손을 내밀었다.
216|
217|“제가 잠깐 확인해 봐도 될까요?”
218|
219|“아, 물론입니다.”
220|
221|아이템 확인. 마음속으로 중얼거리자 곧장 잠력단에 관한 정보가 떴다.
222|
223|변경된 정보를 찾는 것은 쉬운 일이었다.
224|
225|
226|
227|아이템창
228|
229|
230|
231|[잠력단]
232|
233|종류 : 영단
234|
235|등급 : ???
236|
237|제한 : [절정 무인] 이상
238|
239|설명 : [암천]이 제조한 단환. 약 한 시진 동안 복용자의 잠재된 힘을 대폭 끌어 올리는 대신, 그에 대한 대가가 뒤따른다. 최악의 경우가 아니고서는 복용하지 말 것.
240|
241|효과 : 전투 관련 능력치 +100
242|
243|[공력] +15년
244|
245|[호신강기] 사용 가능
246|
247|
248|
249|
250|
251|[알 수 없는 누군가]가 사라지고 [암천]이라는 생소한 단어가 그 자리를 채웠다.
252|
253|‘문맥으로 봐서 어떤 모종의 단체인 건 확실한데…….’
254|
255|뭐, 잠력단 같은 물건을 만드는 놈들이니 마교와 비교해도 그 나물에 그 밥일 게 뻔하다.
256|
257|‘암천.’
258|
259|누가 지었는지 작명 센스 하나는 끝내준다. 두 글자만으로 자신들이 수상쩍은 놈들이라는 걸 알려 주니까.
260|
261|이 새끼들 분명히 뒤가 구린 놈들이다. 99퍼센트 확신한다.
262|
263|‘진위경과 위팽은 뭔가 알고 있는 것 같은데.’
264|
265|문제는 앞서 두 사람이 보인 반응으로 봤을 때 암천에 관한 정보 노출을 극도로 꺼릴 거라는 사실이다.
266|
267|‘그래도 한 번 찔러 볼까?’
268|
269|하지만 정작 내가 입을 열기도 전에, 진무경이 한발 빨리 물었다.
270|
271|“암천? 그게 뭡니까?”
272|
273|“그게…….”
274|
275|진위경의 얼굴 위로 곤란한 빛이 스쳤다.
276|
277|“미안하구나. 아직은 말해 줄 수 없다.”
278|
279|동생들을 끔찍이 생각하는 그의 입에서 나온 말이다.
280|
281|진위경이 이러는데 위팽에게는 물어볼 필요도 없다.
282|
283|“두 공자님께는 죄송합니다만, 보다 명확해지기 전까지는 알려 드릴 수 없습니다.”
284|
285|지금까지 보지 못했던 확고한 태도다. 나도, 진무경도 오늘은 이쯤에서 물러나야 한다는 사실을 깨달았다.
286|
287|다만 그럴수록 암천에 대한 호기심은 더더욱 커져 갔다.
288|
289|‘우리한테까지 감춰야 할 비밀이라 이거지.’
290|
291|가문의 직계라는 혈통은 둘째치더라도, 나와 진무경은 태원진가의 핵심 고수다. 진위경의 오른팔이 위팽이라면 각자 왼팔, 한쪽 다리 역할 정도는 하고도 남는다.
292|
293|‘그럼 가문 내에서도 두 사람만 아는 특급 기밀이라는 건데.’
294|
295|나도 사람인지라 궁금해지는 건 어쩔 수 없다. 게다가 항산검문 때는 잠잠하던 시스템이 반응했다는 사실도 한몫했다.
296|
297|‘암천, 잠력단, 진위경과 위팽만 아는 특급 기밀.’
298|
299|몇 가지 키워드가 머릿속을 휙휙 스쳐 지나간다.
300|
301|좋아, 결심했다.
302|
303|‘신경 끄고 살아야지.’
304|
305|과한 호기심은 명줄을 짧게 만드는 법이다. 항산검문에 우편 배달하러 갔다가 죽을 고비를 넘긴 지 며칠 되지도 않았다.
306|
307|이름부터가 불길하기 짝이 없는 수수께끼의 단체? 엮였다가는 좋은 꼴 못 볼 게 뻔하다.
308|
309|“자자, 이 얘기는 그만하고 술이나 한 잔씩들 할까?”
310|
311|진위경이 억지로 분위기를 환기시킨다.
312|
313|이미 혼자서 두 병을 아작 낸 위팽도, 부상당한 진무경도 잔을 채우는데 나라고 뺄 수 있나. 진위경이 따라 주는 술을 받아 쭉 들이켰다.
314|
315|꿀꺽, 꿀꺽.
316|
317|도수 높기로 악명이 자자한 화주(火酒)가 후끈한 열기와 함께 목을 타고 넘어갔다.
318|
319|“크으으.”
320|
321|이야, 이거 장난 아닌데?
322|
323|도수 높은 거야 알고는 있었지만 직접 마셔 보니 생각 이상이다. 이 정도면 소주, 맥주는 명함도 못 내밀 것 같다.
324|
325|몸을 부르르 떠는 나와는 달리 나머지 셋은 곧장 빈 술잔을 꽉꽉 채웠다.
326|
327|“마셔!”
328|
329|“들이부어!”
330|
331|“죽을 때까지 달려!”
332|
333|“…….”
334|
335|산서성이 화북(華北) 지방에 속하며, 화북 사내들은 하나같이 엄청난 주당이라는 사실을 안 것은 술로 밤을 꼬박 지새우고 난 후였다.
336|
337|
338|
339|* * *
340|
341|
342|
343|다음 날 정오. 상쾌한 기분으로 말에 오르는 나를 혁무진이 괴물 보듯 바라봤다.
344|
345|“속 괜찮으세요?”
346|
347|“어, 괜찮은데?”
348|
349|“혹시 어제 혼자 술 안 드신 건 아니죠? 아니면 중간에 주무셨다거나.”
350|
351|“응, 넷이서 계속 마셨어.”
352|
353|“……그걸 전부 다요?”
354|
355|녀석이 입을 딱 벌렸다.
356|
357|“그게 말이 됩니까? 사람이에요?”
358|
359|“다 들어가더라.”
360|
361|“세상에, 도대체 밤새 몇 병을 드신 겁니까?”
362|
363|단위가 잘못됐다. ‘병’이 아니라 ‘통’이다.
364|
365|무슨 해적 나오는 영화에서나 보던 거대한 술통을 끊임없이 비우고, 또 비웠다.
366|
367|“글쎄, 한 스무 통 가까이 마신 것 같은데. 열 통 넘은 후로는 안 세어 봐서 모르겠다.”
368|
369|“허, 정말 대단하십니다.”
370|
371|혁무진이 감탄하며 엄지를 추켜세우는데 갑자기 객잔의 문이 열렸다.
372|
373|그리고 세 마리의 좀비, 아니 세 명의 절정 고수가 모습을 드러낸다.
374|
375|“흐어어.”
376|
377|“우욱.”
378|
379|“허억, 허억.”
380|
381|창백한 안색, 바짝 마른 입술과 퀭한 눈동자.
382|
383|한 명의 예외도 없이 발을 질질 끌며 마차로 쏙 들어가는 모습에 호위대의 무인들이 눈을 휘둥그레 떴다.
384|
385|“갑자기 왜 마차를…….”
386|
387|“상태가 많이 안 좋으신 것 같은데?”
388|
389|“그럴 리가. 자네들 우리 대주님이랑 술 안 마셔 봤어? 주신(酒神) 위팽. 몰라?”
390|
391|“대주님 별호는 귀검 아니었습니까?”
392|
393|“모르긴 몰라도 주량으로 따지면 무신(武神)도 이길걸. 그냥 지금까지의 피로가 쌓여서 저러시는 거겠지.”
394|
395|무인들이 쑥덕거리던 그때, 마차 문이 벌컥 열리더니 한 사람이 후다닥 뛰쳐나와 허리를 숙였다.
396|
397|“꺼억, 끄우웨에에엑!”
398|
399|촤르르르륵.
400|
401|희멀건 액체만 한참 쏟아 내고 비틀비틀 마차로 복귀하는 위팽의 뒷모습에 한창 떠들던 무인이 얼떨떨한 목소리로 중얼거렸다.
402|
403|“……이럴 리가 없는데.”
404|
405|“이럴 리가 없긴. 저건 누가 봐도 숙취지. 잠도 안 주무시고 그렇게 마셔 댔으니 저러실 만도 해.”
406|
407|“그럼 삼공자님은 왜 저렇게 멀쩡하신데?”
408|
409|호위대의 시선이 내게로 쏠렸다. 전신에서 섬뜩할 정도로 풍기는 술 냄새. 하지만 그와는 반대로 상쾌하기 짝이 없는 얼굴과 편안한 호흡.
410|
411|“설마?”
412|
413|“삼공자님이 대주님을 이겼다고? 그 주신을?”
414|
415|술렁이는 장내.
416|
417|이제 혁무진은 감탄을 넘어 존경의 눈빛을 보내고 있었다.
418|
419|“아아, 역시! 허구한 날 기녀들 끼고 술 마시던 조장님 수준!”
420|
421|“…….”
422|
423|“조장님이 삼 년만 더 술을 마셨으면 본가 기둥뿌리가 뽑혔을 거라는 총관님 말씀이 생각납니다. 이래서 항상 공금을 훔칠 수밖에 없었던 거였군요!”
424|
425|“……야, 인마.”
426|
427|단둘이 있는 것도 아니고, 그딴 식으로 말하면 내 이미지가 뭐가 되냐.
428|
429|안 그래도 아까부터 사방에서 우수수 꽂혀 드는 시선에 얼굴이 따가울 지경이다.
430|
431|“커흠. 커흐흠!”
432|
433|헛기침하며 슬쩍 주위를 둘러봤는데 이게 웬걸. 시커먼 사내놈들 눈동자가 밤하늘 샛별보다 반짝거리는 중이다.
434|
435|“진정한 주신, 주신이다.”
436|
437|“태원 홍등가에서는 유명하시지. 야왕이라고 못 들어 봤나?”
438|
439|“야왕? 별호만 들어도 알겠다. 원래 술 잘 드시는 걸로 정평이 나 있으셨구먼.”
440|
441|“그게 아니라…… 그거. 그거.”
442|
443|“허억. 정말인가?”
444|
445|“나야 모르지. 본 적이 없으니까.”
446|
447|“알고 보니 진정한 사내셨구먼.”
448|
449|띠링.
450|
451|
452|
453|- 이 자리에 모인 이들이 당신의 주량과 위용에 감탄합니다!
454|
455|- 명성이 20 상승합니다!
456|
457|- 명성이 22 상승합니다!
458|
459|- 명성이 25 상승합니다!
460|
461|- 특정 소문이 퍼질 시, 관련된 칭호를 얻을 수 있습니다.
462|
463|
464|
465|“…….”
466|
467|아니 시발, 명성 쭉쭉 오르는 거 뭔데.
468|
469|그리고 관련된 칭호라니. 괜찮아, 넣어 둬. 제발 산서잠룡으로 만족하게 해 줘.
470|
471|‘그만해. 이 미친놈들아…….’
472|
473|이유 모를 수치심과 함께 고개를 돌린 나는, 내 특정 부위를 뚫어져라 바라보는 혁무진과 마주할 수 있었다.
474|
475|“……뭐 하냐, 지금?”
476|
477|“아, 잠깐 눈대중으로 재 보고 있었습니다.”
478|
479|너무 당당하게 대답해서 당황스러울 정도다. 혁무진이 해맑게 웃으며 팔뚝을 내밀었다.
480|
481|“이야, 역시 대단하십니다. 헤헤.”
482|
483|나는 팔뚝에 대한 답례로 주먹을 내밀었다.
484|
485|뻑!
```

## Assembled English

```markdown
[P1]
# Chapter 127

[P2]
It didn’t take long for the question marks to turn into exclamation points, and the exclamation points into bewilderment and rage.

[P3]
Jin Mukyung was the first to break the silence.

[P4]
“You…”

[P5]
His face was flushed red, his breathing ragged. His fist twitched as if he wanted to plant one right in my mouth.

[P6]
*Well, he’s really pissed.*

[P7]
A chill ran through me. A dagger had flown in and lodged in my chest.

[P8]
But don’t worry. I had a sturdy shield.

[P9]
“Now, now, Mukyung.”

[P10]
At the quiet voice, Jin Mukyung’s face twisted violently.

[P11]
“Eldest brother!”

[P12]
“Taekyung must have had his reasons. Isn’t that right?”

[P13]
I deliberately lowered my eyes.

[P14]
“No, eldest brother. I was shortsighted.”

[P15]
“Hm?”

[P16]
“I let my curiosity get the better of me… But after hearing what Eldest Brother said, I realized the truth. That object must never be kept—or hidden.”

[P17]
I didn’t forget to make a show of trembling my fist, as if merely thinking about it made my teeth chatter with rage.

[P18]
“The Demonic Cult! Just hearing the name of those vile bastards makes my teeth chatter with fury!”

[P19]
That part was sincere. If they were going to make something, they should’ve made it properly. Turning the user into a deranged murderer was one hell of a design flaw.

[P20]
“Good heavens.”

[P21]
Jin Wikyung looked at me with eyes full of affection.

[P22]
“I remember a small, adorable little boy who said he would grow up to become a chivalrous hero. You were six years old then. Do you remember?”

[P23]
Of course I didn’t.

[P24]
Even the year before last was already hazy. How was I supposed to know what the original owner of this body had done at age six?

[P25]
Still, I nodded solemnly.

[P26]
“I remember it clearly. It was my one and only dream.”

[P27]
Chivalrous hero, governor of Gyeonggi Province—whatever. As of this moment, that was my career aspiration at age six.

[P28]
“Ha-ha. To think that little boy would grow into such a fine man.”

[P29]
Jin Wikyung smiled with satisfaction, then turned to the other two.

[P30]
“You were there too, Wipeng. Do you remember?”

[P31]
Wipeng answered without even taking a breath.

[P32]
“I don’t remember that, but I do remember him starting to womanize exactly ten years later. When I asked what he wanted to be when he grew up, he said he’d become the greatest ladies’ man under heaven.”

[P33]
“A hero ought to know how to enjoy romance.”

[P34]
“He doesn’t know squat about martial arts, so what good is knowing about romance? Is the hero you’re talking about a hero of the night, a hero to courtesans, or something?”

[P35]
“Be quiet. Our youngest showed unusual promise from an early age.”

[P36]
“So that promise… Ah, forget it. I should just keep my mouth shut.”

[P37]
Glug, glug.

[P38]
Jin Wikyung neatly ignored Wipeng, who was pouring liquor straight from the bottle, and turned to the next man in line.

[P39]
“Mukyung. Now that you understand your little brother’s sincerity, let go of your anger.”

[P40]
Jin Mukyung, whose face was twisted into an ugly grimace, finally spoke.

[P41]
“Can’t I hit that bastard just once?”

[P42]
“Now, now.”

[P43]
“Just once. Please.”

[P44]
At the icy voice, I quickly bowed my head.

[P45]
“Please forgive this foolish little brother, Second Brother.”

[P46]
“You’ve been talking down to me this whole time, and now you’re calling me ‘brother’?”

[P47]
“Pardon? Me?”

[P48]
“That’s enough. This is your final warning.”

[P49]
“No. Hit me instead. If that would ease your anger, this little brother will gladly endure it.”

[P50]
“You little shit!”

[P51]
Jin Mukyung shot to his feet, only to sink back down with a gasp. The bandages wrapped around his chest were turning red. His wound must have reopened.

[P52]
“Oh, no! Second Brother, are you all right?”

[P53]
“This bastard, again… Guh!”

[P54]
“Doctor! Doctor!”

[P55]
The drinking party descended into chaos in an instant.

[P56]
Wipeng silently picked up his second bottle and muttered,

[P57]
“This family is really something…”

[P58]
And how something it was—the foremost family in Shanxi.

[P59]
* * *

[P60]
The atmosphere finally settled down after the physician had come and gone.

[P61]
Ignoring Jin Mukyung’s murderous glare, I took the Temporary Strength Pill from inside my robes.

[P62]
“This is it.”

[P63]
The pill was entirely red, as if blood had been condensed into a single sphere.

[P64]
Jin Wikyung and Wipeng examined it closely.

[P65]
“Wipeng, what do you think?”

[P66]
“Just looking at it, I can smell blood. It’s a vicious object.”

[P67]
“Could it really have been made by the Demonic Cult?”

[P68]
“I couldn’t say. If it were, we should be able to sense demonic qi… but I can’t be certain.”

[P69]
“Right? There’s something different about it.”

[P70]
Both of them looked extremely serious. I was just as curious about where the Temporary Strength Pill had come from and who had made it, so I decided to give them a hint.

[P71]
“They called it a Temporary Strength Pill.”

[P72]
“A Temporary Strength Pill?”

[P73]
“Yes. I heard it directly from Pung Yang’s own mouth.”

[P74]
Jin Mukyung abruptly cut in.

[P75]
“Pung Yang? When?”

[P76]
“While you were unconscious.”

[P77]
“…Hoo. Hoo…”

[P78]
No matter what anyone said, I was the sole eyewitness and witness. While Jin Mukyung steadied his breathing to calm himself after getting nowhere, the furrows between the other two men’s brows only deepened.

[P79]
“A Temporary Strength Pill, Wipeng?”

[P80]
“I’ve never heard the name either. If something this potent belonged to the Demonic Cult, it must have been used during the Great Faction War…”

[P81]
“What if the Demonic Cult didn’t make it?”

[P82]
Their gazes turned toward me.

[P83]
“Not the Demonic Cult?”

[P84]
“What makes you think that?”

[P85]
“I’m just saying there’s no need to jump to conclusions.”

[P86]
In truth, I had said it out of hope that I might be able to take the pill back if it hadn’t been made by the Demonic Cult.

[P87]
Of course, I had another thought as well.

[P88]
*The Head Elder.*

[P89]
On the surface, the enemy in the last battle had clearly been the Mount Heng Sword Sect. But the true enemy had been the Head Elder himself.

[P90]
Rather than making a simple either-or assumption, I believed we always had to keep open the possibility that there might be a third faction involved.

[P91]
“Well, it just suddenly occurred to me.”

[P92]
After hearing me out, the other two men’s expressions grew strange. Then, in the next moment, a very quiet voice escaped Wipeng’s lips.

[P93]
It was a single word that slipped out unconsciously, like a groan.

[P94]
“Dark Heaven…”

[P95]
“Wipeng.”

[P96]
Jin Wikyung’s sharp gaze cut off whatever he had been about to say.

[P97]
“Ah, I apologize. I misspoke.”

[P98]
Wipeng hurriedly tried to cover it up.

[P99]
But it was already too late.

[P100]
The two words *Dark Heaven* had been deeply etched into my mind.

[P101]
*Dark Heaven? What’s that?*

[P102]
Then something unexpected happened.

[P103]
> **System**
>
> You have obtained a small amount of information about **Dark Heaven**.
>
> The item description for the **Temporary Strength Pill** will be updated.

[P104]
The System notification had come out of nowhere. I held out my hand toward Wipeng, who was holding the Temporary Strength Pill.

[P105]
“May I take a quick look?”

[P106]
“Of course.”

[P107]
*Item check.*

[P108]
The moment I muttered the command in my head, the information on the Temporary Strength Pill appeared.

[P109]
The change was easy to spot.

[P110]
> **System**
>
> **Item Window**
>
> **Temporary Strength Pill**
>
> **Type:** Elixir  
> **Grade:** ???  
> **Restriction:** Peak martial artist or higher  
> **Description:** A pill manufactured by **Dark Heaven**. For approximately one shichen, it dramatically raises the user’s latent power, but a price follows. Do not take it except in the worst-case scenario.  
> **Effect:** Combat-related stats +100  
> **Internal energy:** +15 years  
> **Body-Protecting Qi:** Available

[P111]
The phrase *Someone Unknown* had disappeared, replaced by the unfamiliar term *Dark Heaven*.

[P112]
*Judging by the context, it’s definitely some kind of organization…*

[P113]
Well, anyone capable of making something like the Temporary Strength Pill was bound to be no better than the Demonic Cult. Same rotten lot, different name.

[P114]
*Dark Heaven.*

[P115]
Whoever had named them had one hell of a gift. Those two words alone announced that they were shady bastards.

[P116]
*These fuckers definitely have something rotten going on behind the scenes. I’m ninety-nine percent sure.*

[P117]
*Jin Wikyung and Wipeng seem to know something.*

[P118]
The problem was that, judging by their reactions, they were extremely reluctant to reveal anything about Dark Heaven.

[P119]
*Should I poke at them once?*

[P120]
But before I could open my mouth, Jin Mukyung beat me to it.

[P121]
“Dark Heaven? What is that?”

[P122]
“Well…”

[P123]
A troubled look crossed Jin Wikyung’s face.

[P124]
“I’m sorry. I can’t tell you yet.”

[P125]
Those words came from a man who cared deeply for his younger brothers.

[P126]
If even Jin Wikyung refused to speak, there was no point asking Wipeng.

[P127]
“I apologize, Young Masters, but I cannot tell you until the matter becomes clearer.”

[P128]
His attitude was firmer than I had ever seen it. Jin Mukyung and I both realized that we had to withdraw for today.

[P129]
But the more they tried to hide it, the more curious I became about Dark Heaven.

[P130]
*So it’s a secret they have to keep even from us.*

[P131]
Setting aside the fact that Mukyung and I were direct descendants, we were both core masters of the Jin Family of Taiyuan. If Wipeng was Jin Wikyung’s right arm, either of us could more than qualify as his left arm—or at least one of his legs.

[P132]
*Then it must be top-secret information known only to those two, even within the family.*

[P133]
I was only human, so I couldn’t help being curious. The fact that the System had reacted this time, despite remaining silent during the Mount Heng Sword Sect incident, also played a part.

[P134]
*Dark Heaven. The Temporary Strength Pill. A top-secret matter known only to Jin Wikyung and Wipeng.*

[P135]
Several keywords flashed through my mind.

[P136]
All right. I’d made up my mind.

[P137]
*I’ll ignore it and go on living.*

[P138]
Too much curiosity had a way of shortening your life. It had only been a few days since I’d gone to deliver the mail to the Mount Heng Sword Sect and nearly died.

[P139]
A mysterious organization whose very name was ominous? If I got involved with them, it was obvious things wouldn’t end well.

[P140]
“Come now, let’s stop talking about this and have another drink.”

[P141]
Jin Wikyung forced the mood back to normal.

[P142]
Wipeng had already demolished two bottles by himself, and even the injured Mukyung was filling his glass. How could I be the only one to sit out? I accepted the liquor Jin Wikyung poured and downed it in one gulp.

[P143]
Gulp, gulp.

[P144]
The notoriously potent fire liquor burned down my throat in a rush of heat.

[P145]
“Guhhh.”

[P146]
Wow. This was no joke.

[P147]
I knew it was strong, but drinking it myself, it was far more potent than I’d expected. At this strength, soju and beer couldn’t even hold a candle to it.

[P148]
Unlike me, who shuddered from head to toe, the other three immediately filled their empty glasses to the brim.

[P149]
“Drink!”

[P150]
“Pour it down!”

[P151]
“Keep going till we drop!”

[P152]
“….”

[P153]
It wasn’t until we had drunk through the entire night that I learned Shanxi Province was part of North China—and that every man from North China was an incredible drinker.

[P154]
* * *

[P155]
At noon the next day, I mounted my horse in a perfectly refreshed mood, and Hyuk Mujin stared at me as if I were a monster.

[P156]
“Is your stomach all right?”

[P157]
“Yeah. It’s fine.”

[P158]
“Don’t tell me you were the only one who didn’t drink last night. Or did you fall asleep halfway through?”

[P159]
“No. The four of us kept drinking.”

[P160]
“…All of it?”

[P161]
His mouth fell open.

[P162]
“How is that possible? Are you even human?”

[P163]
“It all went down.”

[P164]
“Good heavens. How many bottles did you drink through the night?”

[P165]
He had the wrong unit.

[P166]
Not bottles. Barrels.

[P167]
We kept emptying massive casks of liquor—the kind I’d only ever seen in pirate movies—and then emptying more.

[P168]
“I think it was close to twenty barrels. I stopped counting after ten, so I’m not sure.”

[P169]
“Wow. That’s incredible.”

[P170]
Hyuk Mujin raised his thumb in admiration. Just then, the inn door swung open.

[P171]
And three zombies—or rather, three Peak masters—emerged.

[P172]
“Uuugh.”

[P173]
“Urk.”

[P174]
“Huff, huff.”

[P175]
Pale faces, parched lips, and hollow eyes.

[P176]
Every last one of them dragged his feet straight into the carriage. The martial artists of the escort force stared wide-eyed.

[P177]
“Why are they suddenly getting into the carriage…?”

[P178]
“They look really unwell.”

[P179]
“That can’t be right. Haven’t you ever drunk with our Commander? Wipeng, the God of Drinking? Never heard of him?”

[P180]
“Wasn’t the Commander’s epithet Ghost Sword?”

[P181]
“Whatever else you might say, when it comes to drinking, he could probably beat even the Martial God. They’re probably just like this because all the fatigue they’ve accumulated finally caught up with them.”

[P182]
As the martial artists whispered among themselves, the carriage door suddenly flew open, and one person hurriedly dashed out and bent over.

[P183]
“Urrp, buuurrgh!”

[P184]
Splaaarsh.

[P185]
Wipeng spent a good while spewing nothing but pale liquid, then staggered back into the carriage. One of the martial artists who had been talking animatedly muttered in a dazed voice,

[P186]
“…This can’t be.”

[P187]
“It absolutely can. Anyone can see that’s a hangover. They drank like that all night without sleeping. Of course they’d end up like that.”

[P188]
“Then why is the Third Young Master so perfectly fine?”

[P189]
Every eye in the escort force turned toward me.

[P190]
The smell of liquor radiating from my entire body was strong enough to send chills down the spine. But in complete contrast, my face looked unbelievably refreshed, and my breathing was calm.

[P191]
“No way…”

[P192]
“The Third Young Master beat the Commander? That God of Drinking?”

[P193]
The courtyard buzzed with excitement.

[P194]
Hyuk Mujin’s look of admiration had gone beyond admiration and become outright reverence.

[P195]
“Ah, I knew it! That’s our Captain—the man who used to drink with courtesans every damn day!”

[P196]
“….”

[P197]
“I remember what the Chief Steward said. If Captain had kept drinking for three more years, he would have uprooted our family’s entire foundation. So that’s why you always had to steal from the family coffers!”

[P198]
“…Hey, you punk.”

[P199]
We weren’t alone. What did he think would happen to my image if he talked like that?

[P200]
As if the stares pouring in from every direction hadn’t already made my face feel hot enough.

[P201]
“Ahem. Ahem!”

[P202]
I cleared my throat and glanced around. And what do you know? The eyes of all those rough-looking men were sparkling brighter than stars in the night sky.

[P203]
“The true God of Drinking. That’s him.”

[P204]
“He’s famous in Taiyuan’s red-light district. Haven’t you heard of the Night King?”

[P205]
“The Night King? The epithet says it all. So he was already renowned for his drinking.”

[P206]
“No, not that… You know. That.”

[P207]
“Gasp. Is it true?”

[P208]
“How would I know? I’ve never seen it.”

[P209]
“Turns out he’s a true man among men.”

[P210]
> **System**
>
> Everyone gathered here is impressed by your drinking capacity and imposing presence!
>
> **Fame** rises by 20!
>
> **Fame** rises by 22!
>
> **Fame** rises by 25!
>
> If a particular rumor spreads, you may obtain a related **Title**.

[P211]
“….”

[P212]
Why the fuck was my Fame shooting up?

[P213]
And what was this about a related Title? No, thanks. Put it away. Please, just let me be satisfied with the Sleeping Dragon of Shanxi.

[P214]
*Stop it, you lunatics…*

[P215]
I turned away in inexplicable shame—only to find Hyuk Mujin staring intently at a certain part of my body.

[P216]
“…What are you doing?”

[P217]
“Oh, I was just measuring it by eye.”

[P218]
He answered so matter-of-factly that I was almost thrown off. Hyuk Mujin held out his forearm with an innocent smile.

[P219]
“Wow. As expected, you’re amazing. Hehe.”

[P220]
In return for his forearm, I offered him my fist.

[P221]
Thwack!
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
# Chapter 127

[P2]
It didn’t take long for the question marks to turn into exclamation points, and the exclamation points to turn into bewilderment and rage.

[P3]
Jin Mukyung was the first to break the silence.

[P4]
“You…”

[P5]
His face was flushed red, and his breathing was rough. His fist twitched as if he wanted to plant one right in my mouth.

[P6]
*Well, he’s really pissed.*

[P7]
It was chilling. A dagger had flown straight into my chest.

[P8]
But don’t worry. I had a sturdy shield.

[P9]
“Now, now, Mukyung.”

[P10]
At the quiet voice, Jin Mukyung’s face twisted violently.

[P11]
“Eldest brother!”

[P12]
“Taekyung must have had his reasons. Isn’t that right?”

[P13]
I deliberately lowered my eyes.

[P14]
“No, eldest brother. I was short-sighted.”

[P15]
“Hm?”

[P16]
“I let my curiosity get the better of me… But after hearing what Eldest Brother said, I realized something. It’s an object that should never be kept—or hidden.”

[P17]
I didn’t forget to make a show of trembling my fist, as if merely thinking about it made my teeth chatter with rage.

[P18]
“The Demonic Cult! Just hearing the name of those vile bastards makes me tremble with fury!”

[P19]
This part was sincere. If you’re going to make something, make it properly. Why did it have such a serious defect that it turned people into deranged murderers?

[P20]
“Good heavens.”

[P21]
Jin Wikyung looked at me with eyes full of affection.

[P22]
“I remember a small, adorable little boy who said he would grow up to become a chivalrous hero. You were six years old then. Do you remember?”

[P23]
Of course I didn’t.

[P24]
The events of the year before last were already hazy. How was I supposed to know what the original owner of this body had done at age six?

[P25]
Still, I nodded solemnly.

[P26]
“I remember it clearly. It was my only dream.”

[P27]
Whether it was a chivalrous hero or the governor of Gyeonggi Province, as of this moment, that was my career aspiration at age six.

[P28]
“Ha-ha. To think that little boy would grow up so splendidly.”

[P29]
After laughing with satisfaction, Jin Wikyung turned toward the other two people.

[P30]
“You were there too, Wipeng. Do you remember?”

[P31]
Wipeng answered without even taking a breath.

[P32]
“I don’t remember that, but I do remember him starting to womanize exactly ten years later. When I asked what he wanted to be when he grew up, he said he’d become the greatest ladies’ man under heaven.”

[P33]
“A hero ought to know how to enjoy romance.”

[P34]
“He doesn’t know squat about martial arts, so what good is knowing about romance? Is the hero you’re talking about a hero of the night, a hero to courtesans, or something?”

[P35]
“Be quiet. Our youngest showed unusual promise from an early age.”

[P36]
“So that promise… Ah, never mind. I should just stop talking.”

[P37]
Glug, glug.

[P38]
Jin Wikyung completely ignored Wipeng, who was pouring liquor straight from the bottle, and turned his attention to the next man in line.

[P39]
“Mukyung. Now that you understand your little brother’s sincerity, let go of your anger.”

[P40]
Jin Mukyung, who had been making a face like he’d swallowed something foul, finally spoke.

[P41]
“Can’t I hit that bastard just once?”

[P42]
“Now, now.”

[P43]
“Just once. Please.”

[P44]
At the icy voice, I quickly lowered my head.

[P45]
“Please forgive this foolish little brother, Second Brother.”

[P46]
“The bastard who’s been speaking casually to me this whole time is suddenly calling me ‘brother.’”

[P47]
“Pardon? I am?”

[P48]
“That’s enough. This is your final warning.”

[P49]
“No. Hit me instead. If that would ease your anger, this little brother will gladly endure it.”

[P50]
“You little shit!”

[P51]
Jin Mukyung shot to his feet, then sank back down with a gasp. The bandages tied around his chest were turning red. It seemed his wound had reopened.

[P52]
“Oh, no! Second Brother, are you all right?”

[P53]
“This bastard, again… Guh!”

[P54]
“Doctor! Doctor!”

[P55]
The drinking party became a complete disaster in an instant.

[P56]
Wipeng quietly picked up his second bottle and muttered,

[P57]
“This family is really something…”

[P58]
And how something it was—the foremost family in Shanxi.

[P59]
* * *

[P60]
The atmosphere finally settled down after the physician had come and gone.

[P61]
I ignored Jin Mukyung’s murderous glare and took the Temporary Strength Pill from inside my robes.

[P62]
“This is it.”

[P63]
The pill was entirely red, as if blood had been condensed into a single sphere.

[P64]
Jin Wikyung and Wipeng examined it closely.

[P65]
“Wipeng, what do you think?”

[P66]
“Just looking at it makes me smell blood. It’s a vicious object.”

[P67]
“Could it really have been made by the Demonic Cult?”

[P68]
“I couldn’t say. If it were, we should be able to sense demonic qi… but I can’t be certain.”

[P69]
“Right? There’s something different about it.”

[P70]
Both of them looked extremely serious. I was just as curious about where the Temporary Strength Pill had come from and who had made it, so I decided to give them a hint.

[P71]
“They called it a Temporary Strength Pill.”

[P72]
“A Temporary Strength Pill?”

[P73]
“Yes. I heard it directly from Pung Yang.”

[P74]
Jin Mukyung suddenly cut in.

[P75]
“Pung Yang? When did you hear that?”

[P76]
“While you were unconscious.”

[P77]
“…Hoo. Hoo…”

[P78]
I was the only eyewitness and witness, no matter what anyone said. As Jin Mukyung, who had gotten nowhere with his interruption, steadied his breathing to calm himself, the furrows between the other two men’s brows only deepened.

[P79]
“A Temporary Strength Pill, Wipeng?”

[P80]
“I’ve never heard of it either. If an object with this level of efficacy belonged to the Demonic Cult, it must have been used during the Great Faction War…”

[P81]
“Could it not be the Demonic Cult?”

[P82]
Their gazes turned toward me.

[P83]
“Not the Demonic Cult?”

[P84]
“What makes you think that?”

[P85]
“I’m saying there’s no need to decide that from the start.”

[P86]
In truth, I had said it out of hope that I might be able to take the pill back if it hadn’t been made by the Demonic Cult.

[P87]
Of course, I had another thought as well.

[P88]
*The Head Elder.*

[P89]
The Mount Heng Sword Sect had certainly been the enemy that appeared on the surface during the last battle, but the true enemy had been the Head Elder himself.

[P90]
Rather than making a simple either-or assumption, I believed we always had to keep open the possibility that there might be a third faction involved.

[P91]
“Well, it just suddenly occurred to me.”

[P92]
After hearing me out, the other two men’s expressions grew strange. Then, in the next moment, a very quiet voice escaped Wipeng’s lips.

[P93]
It was a single word that slipped out unconsciously, like a groan.

[P94]
“Dark Heaven…”

[P95]
“Wipeng.”

[P96]
Jin Wikyung’s sharp gaze cut off whatever he had been about to say.

[P97]
“Ah, I apologize. I misspoke.”

[P98]
Wipeng hurriedly tried to cover it up.

[P99]
But it was already too late.

[P100]
The two words *Dark Heaven* had been deeply etched into my mind.

[P101]
*Dark Heaven? What is that?*

[P102]
Then something unexpected happened.

[P103]
> **System**
>
> You have obtained a small amount of information about **Dark Heaven**.
>
> The item description for the **Temporary Strength Pill** will be updated.

[P104]
It was a completely sudden System notification. I held out my hand toward Wipeng, who was holding the Temporary Strength Pill.

[P105]
“May I take a quick look?”

[P106]
“Of course.”

[P107]
*Item check.*

[P108]
As soon as I muttered the words in my mind, information about the Temporary Strength Pill appeared.

[P109]
Finding the changed information was easy.

[P110]
> **System**
>
> **Item Window**
>
> **Temporary Strength Pill**
>
> **Type:** Elixir  
> **Grade:** ???  
> **Restriction:** Peak martial artist or higher  
> **Description:** A pill manufactured by **Dark Heaven**. For approximately one shichen, it dramatically raises the user’s latent power, but a price follows. Do not take it except in the worst circumstances.  
> **Effects:** Combat-related stats +100  
> Internal energy +15 years  
> Body-Protecting Qi available

[P111]
The phrase *Someone Unknown* had disappeared, replaced by the unfamiliar term *Dark Heaven*.

[P112]
*Judging by the context, it’s definitely some kind of organization…*

[P113]
Well, anyone capable of making something like the Temporary Strength Pill was bound to be no better than the Demonic Cult. Same rotten lot, different name.

[P114]
*Dark Heaven.*

[P115]
Whoever came up with the name had incredible instincts. Two words were enough to tell everyone they were suspicious bastards.

[P116]
*These guys definitely have something rotten going on behind the scenes. Ninety-nine percent sure.*

[P117]
*Jin Wikyung and Wipeng seem to know something.*

[P118]
The problem was that, judging by their reactions, they were extremely reluctant to reveal anything about Dark Heaven.

[P119]
*Should I poke at them once?*

[P120]
But before I could open my mouth, Jin Mukyung beat me to it.

[P121]
“Dark Heaven? What is that?”

[P122]
“Well…”

[P123]
A troubled look crossed Jin Wikyung’s face.

[P124]
“I’m sorry. I can’t tell you yet.”

[P125]
Those words came from a man who cared deeply for his younger brothers.

[P126]
If Jin Wikyung was unwilling to speak, there was no need to ask Wipeng.

[P127]
“I apologize, Young Masters, but I cannot tell you until the matter becomes clearer.”

[P128]
His attitude was firmer than anything I had seen from him before. Both Jin Mukyung and I realized that we had to withdraw for today.

[P129]
But the more they tried to hide it, the more curious I became about Dark Heaven.

[P130]
*So it’s a secret they have to keep hidden even from us.*

[P131]
Even putting aside the fact that Mukyung and I were direct descendants of the family, we were core masters of the Jin Family of Taiyuan. If Wipeng was Jin Wikyung’s right arm, the two of us were each more than qualified to serve as his left arm or one of his legs.

[P132]
*Then it must be a top-secret matter known only to those two, even within the family.*

[P133]
I was only human, so I couldn’t help being curious. The fact that the System had reacted this time, despite remaining silent during the Mount Heng Sword Sect incident, also played a part.

[P134]
*Dark Heaven. The Temporary Strength Pill. A top-secret matter known only to Jin Wikyung and Wipeng.*

[P135]
Several keywords flashed through my mind.

[P136]
All right. I’d made up my mind.

[P137]
*I’ll ignore it and go on living.*

[P138]
Excessive curiosity had a way of shortening one’s life. It had only been a few days since I’d gone to deliver the mail to the Mount Heng Sword Sect and nearly died.

[P139]
A mysterious organization whose very name was ominous? If I got involved with them, it was obvious things wouldn’t end well.

[P140]
“Well, let’s stop talking about this and have another drink.”

[P141]
Jin Wikyung forced the mood back to normal.

[P142]
Wipeng, who had already demolished two bottles by himself, was filling his glass, and so was the injured Mukyung. How could I be the only one to sit out? I accepted the liquor Jin Wikyung poured and downed it in one gulp.

[P143]
Gulp, gulp.

[P144]
The notorious fire liquor burned its way down my throat with a fierce heat.

[P145]
“Guhhh.”

[P146]
Wow. This was no joke.

[P147]
I knew it was strong, but drinking it myself, it was far more potent than I’d expected. At this strength, soju and beer couldn’t even hold a candle to it.

[P148]
Unlike me, who shuddered from head to toe, the other three immediately filled their empty glasses to the brim.

[P149]
“Drink!”

[P150]
“Down it!”

[P151]
“Let’s keep going until we drop!”

[P152]
“….”

[P153]
I didn’t learn that Shanxi Province belonged to North China, or that every man from North China was an incredible drinker, until after we spent the entire night drinking.

[P154]
* * *

[P155]
The next day at noon, Hyuk Mujin stared at me as if I were a monster when I mounted my horse in a perfectly refreshed mood.

[P156]
“Is your stomach all right?”

[P157]
“Yeah. Why wouldn’t it be?”

[P158]
“Don’t tell me you were the only one who didn’t drink yesterday. Or did you fall asleep halfway through?”

[P159]
“No. The four of us kept drinking.”

[P160]
“…All of it?”

[P161]
His mouth fell open.

[P162]
“Is that even possible? Are you human?”

[P163]
“It all fit.”

[P164]
“My goodness. How many bottles did you drink through the night?”

[P165]
He had the wrong unit.

[P166]
It wasn’t bottles. It was barrels.

[P167]
We kept emptying massive casks of liquor—the kind I’d only ever seen in pirate movies—and then emptying more.

[P168]
“I think it was close to twenty barrels. I stopped counting after ten, so I’m not sure.”

[P169]
“Wow. That’s incredible.”

[P170]
Hyuk Mujin raised his thumb in admiration when the inn door suddenly opened.

[P171]
And three zombies—or rather, three Peak masters—appeared.

[P172]
“Uuugh.”

[P173]
“Urk.”

[P174]
“Huff, huff.”

[P175]
Their faces were pale, their lips parched, and their eyes sunken.

[P176]
Without a single exception, they dragged their feet and climbed straight into the carriage. The martial artists of the escort force stared at them with their eyes wide.

[P177]
“Why are they suddenly getting into the carriage…?”

[P178]
“They look really unwell.”

[P179]
“That can’t be. Haven’t you ever drunk with our Commander? Wipeng, the God of Drinking? You don’t know?”

[P180]
“Wasn’t the Commander’s epithet Ghost Sword?”

[P181]
“Whatever else you might say, when it comes to drinking, he could probably beat even the Martial God. They’re probably just like this because all the fatigue they’ve accumulated finally caught up with them.”

[P182]
As the martial artists whispered among themselves, the carriage door suddenly flew open, and one person hurriedly dashed out and bent over.

[P183]
“Urrp, buuurrgh!”

[P184]
Splaaarsh.

[P185]
After pouring out a pale liquid for quite some time, Wipeng staggered back into the carriage. One of the martial artists who had been talking animatedly muttered in a dazed voice,

[P186]
“…This can’t be.”

[P187]
“It absolutely can. Anyone can see that’s a hangover. They drank all night without sleeping. Of course they’d end up like that.”

[P188]
“Then why is the Third Young Master so perfectly fine?”

[P189]
The escort force’s gazes all turned toward me.

[P190]
The smell of liquor radiating from my entire body was strong enough to send chills down the spine. But in complete contrast, my face looked unbelievably refreshed, and my breathing was calm.

[P191]
“No way…”

[P192]
“The Third Young Master beat the Commander? That God of Drinking?”

[P193]
The courtyard buzzed with excitement.

[P194]
Hyuk Mujin’s look of admiration had gone beyond admiration and become outright reverence.

[P195]
“Ah, I knew it! That’s our Captain—the man who used to drink with courtesans every damn day!”

[P196]
“….”

[P197]
“I remember what the Chief Steward said. If Captain had kept drinking for three more years, he would have uprooted the family’s entire foundation. So this is why you always had to steal from the family coffers!”

[P198]
“…Hey, you punk.”

[P199]
It wasn’t as if we were alone. If he talked like that, what would happen to my image?

[P200]
As if the stares pouring in from every direction hadn’t already made my face feel hot enough.

[P201]
“Ahem. Ahem!”

[P202]
I cleared my throat and glanced around. And what do you know? The eyes of all those rough-looking men were sparkling brighter than stars in the night sky.

[P203]
“A true God of Drinking. He really is.”

[P204]
“He’s famous in Taiyuan’s red-light district. Haven’t you heard of the Night King?”

[P205]
“The Night King? I can tell just from the epithet. So he was already renowned for his drinking.”

[P206]
“No, not that… The other thing. That.”

[P207]
“Gasp. Is it true?”

[P208]
“How would I know? I’ve never seen it.”

[P209]
“Turns out he really is a man among men.”

[P210]
> **System**
>
> Everyone gathered here is impressed by your drinking capacity and imposing presence!
>
> **Fame** rises by 20!
>
> **Fame** rises by 22!
>
> **Fame** rises by 25!
>
> If a particular rumor spreads, you may obtain a related **Title**.

[P211]
“….”

[P212]
What the fuck was with my Fame shooting up like that?

[P213]
And what did it mean, a related Title? No, it was fine. Put that away. Please, just let me be satisfied with the Sleeping Dragon of Shanxi.

[P214]
*Stop it, you lunatics…*

[P215]
With a mysterious sense of shame, I turned my head—and came face-to-face with Hyuk Mujin, who was staring intently at a certain part of me.

[P216]
“…What are you doing?”

[P217]
“Oh, I was just taking a rough measurement with my eyes.”

[P218]
His answer was so straightforward that I was almost thrown off. Hyuk Mujin cheerfully extended his forearm.

[P219]
“Wow. As expected, you’re amazing. Hehe.”

[P220]
In return for the forearm, I offered him my fist.

[P221]
Thwack!
```


## Exact glossary matches

These English spellings are binding for the matched Korean keys.

| 진위경    | **Jin Wikyung**    |
| 진무경    | **Jin Mukyung**    |
| 위팽     | **Wipeng**         |
| 혁무진    | **Hyuk Mujin**     |
| 산서잠룡   | **Sleeping Dragon of Shanxi** | Jin Taekyung   |
| 무신     | **Martial God**               | —              |
| 태원진가   | **Jin Family of Taiyuan**        |
| 항산검문   | **Mount Heng Sword Sect**        |
| 암천     | **Dark Heaven**                  |
| 절정     | **Peak**          |
| 무인     | **martial artist**                               | Default term                                          |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 마교     | **Demonic Cult**                                 |                                                       |
| 기녀     | **courtesan**                                    |                                                       |
| 장로     | **Elder**                                    |
| 대장로    | **Head Elder**                               |
| 대주     | **Squad Leader** / **Commander**             |
| 큰형     | **eldest brother**                           |
| 시스템              | **System**                     |
| 상태               | **Status**                     |
| 명성               | **Fame**                       |
| 칭호               | **Title**                      |
| 등급               | **Grade**                      | System/UI field for quest, item, and martial-art classifications; do not use “Rank” here |
| 아이템              | **Item**                       |
| 산서     | **Shanxi**             |
| 태원     | **Taiyuan**            |
| 항산     | **Mount Heng**         |
| 정마대전   | **Great Faction War**         |
| 본가      | **our family / this family**                                    |
| 귀가      | **your family**                                                 |
| 공자      | **Young Master**                                                |
| 풍양 | **Pung Yang** | Personal name of the Red Wind Band Leader. |
| 삼공자 | **Third Young Master** | Title used for Jin Taekyung. |
| 귀검 | **Ghost Sword** | Wipeng's epithet. |
| 잠력단 | **Temporary Strength Pill** | Rare pill that temporarily enhances strength; Pung Yang has only three and uses one against Cheol Mubaek and another during the battle. |
| 호신강기 | **Body-Protecting Qi** | Powerful defensive qi barrier that shields Pung Yang. |
| 산서성 | **Shanxi Province** | Province containing the Lower District Sect branches. |
| 조장 | **Captain** | Hyuk Mujin's address for Taekyung as squad leader. |
| 갑자 | **jiazi** | Traditional sixty-year cycle. |
| 시진 | **shichen** | Traditional time unit of approximately two hours. |
| 아이템창 | **Item Window** | System window displaying an item's details. |
| 마기 | **demonic qi** | Demonic energy discussed as a possible effect of the pill. |
| 주신 | **God of Drinking** | Wipeng's drinking epithet. |
| 야왕 | **Night King** | Rumored epithet for Jin Taekyung in Taiyuan's red-light district. |
| 화북 | **North China** | Regional designation used when discussing Shanxi drinking culture. |
| 산서제일가 | **foremost family in Shanxi** | Description of the Jin Family of Taiyuan's standing. |
| 가지 | **Go** | Song associated with Won Myunghoon. |

## Deterministic QA

```json
{
  "version": 1,
  "chapter": 127,
  "passed": true,
  "metrics": {
    "source_characters": 6884,
    "translation_characters": 15298,
    "length_ratio": 2.222,
    "source_paragraphs": 230,
    "translation_paragraphs": 221
  },
  "errors": [],
  "warnings": [
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
        "korean": "귀가",
        "preferred": "your family"
      }
    },
    {
      "code": "terminology",
      "message": "matched preferred term is absent",
      "details": {
        "korean": "갑자",
        "preferred": "jiazi"
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
