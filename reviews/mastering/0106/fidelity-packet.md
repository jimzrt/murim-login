# Fidelity Gate — Chapter 106

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
  1|＃106화
  2|
  3|
  4|
  5|“같이 가요. 항산검문.”
  6|
  7|“네?”
  8|
  9|“진 공자가 들은 그대로예요. 나도 항산검문에 볼일이 있거든.”
 10|
 11|“무슨 일로요?”
 12|
 13|“그건 말 못 할 것 같은데? 나도 공과 사가 뚜렷한 편이라서.”
 14|
 15|되로 주고 말로 받았군.
 16|
 17|방금 내 입으로 한 말이 고스란히 돌아온다. 머쓱해하는 나를 보는 월화의 미소가 짙어졌다.
 18|
 19|“장난이에요. 마침 항산검문 쪽에 받을 게 있거든요. 정확히는 태원진가에서 받기로 한 거지만.”
 20|
 21|“무슨…… 아.”
 22|
 23|문득 떠오르는 기억이 있다. 항산검문과의 전쟁이 한창 진행되고 있을 무렵, 태원진가와 하오문이 맺었던 밀약.
 24|
 25|‘정보를 제공하는 대신 항산검문이 소유한 부지 등에 대한 소유권을 받기로 약속했던가?’
 26|
 27|하오문은, 아니 월화는 약속을 지켰다. 개전 초기 항산검문의 선봉대를 궤멸시킬 수 있었던 것도 그녀의 도움이 있었기 때문이다.
 28|
 29|태원진가는 그 후에도 하오문에게 여러 도움을 받았고 마침내 전쟁에서 승리했지만, 문제는 그 후였다.
 30|
 31|“진 공자도 알다시피 우리 입장이 좀 묘하게 됐어요. 전쟁에선 이겼는데 전리품에 손을 못 대고 있는 상황이라.”
 32|
 33|약육강식. 강자가 약자를 집어삼키는 건 무림의 법칙이다.
 34|
 35|그러나 대장로의 등장이 모든 걸 망쳤다. 태원진가와 항산검문이 그의 농간에 놀아났다는 사실이 밝혀진 순간부터 전리품을 취할 명분이 희미해진 거다.
 36|
 37|‘그래서 합병을 진행하는 거고.’
 38|
 39|지금은 검을 거두고 붓으로 대화를 나눠야 할 때다. 세상 사람들이 욕하지 않는 범위 안에서 조용히, 원만하게 흡수하는 것이 진위경이 그리는 그림이다.
 40|
 41|월화는 그 전에 보상을 받기를 원하는 거고.
 42|
 43|“항산검문 측이 우리의 제안을 받아들인다면 그때 보상을 요구해도 될 텐데요.”
 44|
 45|“그건 태원진가가 산서성의 맹주(盟主)가 아닌 패자(霸者)일 때나 가능한 이야기예요. 지금 상황에서 섣불리 뺏으려 하다가는 다른 중소 문파들도 발을 빼겠죠. 더군다나…….”
 46|
 47|순간 나를 의미심장한 눈빛으로 바라본 그녀가 고개를 저었다.
 48|
 49|도대체 뭐지?
 50|
 51|“더군다나, 뭐요?”
 52|
 53|“아니에요. 뭐, 아무튼 소가주님께도 제안을 받긴 했어요.”
 54|
 55|월화가 곰방대를 뻐끔거리며 말을 이었다.
 56|
 57|“약속했던 것에 상응하는 재물, 혹은 태원진가가 관리하는 구역을 양도해 주시겠다고 하더군요.”
 58|
 59|그 정도면 괜찮은 거 아닌가 싶지만 개인이 아닌, 한 단체를 이끄는 수장의 입장에서 생각해 보면 다르다.
 60|
 61|‘활동 영역을 확대하고 싶은 거겠지.’
 62|
 63|월화의 본질은 기녀도, 객잔의 주인도 아닌 정보 상인.
 64|
 65|이번 기회에 항산검문의 차단으로 비교적 약세였던 산서성 북부까지 하오문의 영향력을 넓히고 싶어 하는 게 분명했다.
 66|
 67|‘진위경이야 당연히 태원진가가 산서성 전역을 아울렀으면 하는 마음일 거고.’
 68|
 69|이미 오래전부터 산서성 중남부에 막대한 영향력을 행사해 왔던 태원진가다. 알짜배기 구역을 몇 개 넘겨준다고 해서 지금까지 쌓아 올린 영향력이 줄어들지는 않는다.
 70|
 71|‘이거 딱 그거네. 재개발 구역.’
 72|
 73|북부를 꽉 잡고 외부 세력의 유입을 막던 항산검문이 무너지고 있다. 그린벨트가 해제되고 재개발 구역이 되니 진위경과 월화 간의 밀고 당기기가 시작된 거다.
 74|
 75|‘둘 다 장난 아니네.’
 76|
 77|어제의 동맹이 오늘의 경쟁자가 됐다.
 78|
 79|사람은 보이는 게 전부가 아니라는 사실을 오늘 다시 한번 느낀다.
 80|
 81|“그래서 우리 귀여운 신임 문주님도 뵙고, 빚 독촉도 할 겸 항산검문까지 동행하려고 하는데…… 어때요?”
 82|
 83|더 생각할 것도 없이 대답했다.
 84|
 85|“거절하겠습니다.”
 86|
 87|“와, 너무 단호한 거 아니에요? 거래 조건도 듣기 전에 칼같이 잘라 버리네.”
 88|
 89|“아우가 돼서 형님 앞길에 똥물 뿌릴 순 없죠.”
 90|
 91|피 한 방울 안 섞인 형제지만 이미 마음 한구석에서는 그의 존재를, 이 무림을 받아들인 지 오래다.
 92|
 93|“흐음.”
 94|
 95|나를 지그시 바라보던 월화가 곰방대를 탁 내려놨다.
 96|
 97|“그렇게 해요, 그럼.”
 98|
 99|“아, 예.”
100|
101|몇 번 더 꼬드길 줄 알았는데 바로 포기하네.
102|
103|뭐, 나로서는 이야기가 빨리 끝나서 마음 편하다.
104|
105|“그럼 이만.”
106|
107|아직도 입을 봉인한 채 앉아 있는 혁무진을 툭 치며 자리에서 일어났다. 그때 월화가 묘한 웃음을 짓곤 말했다.
108|
109|“아, 진 소협한테 전해 줄래요? 후원에 있는 노송(老松), 그거 비싼 거니까 수련 좀 조심히 해 달라고.”
110|
111|산서성 제일의 정보 상인이 운영하는 객잔이다. 이곳에 들어온 후부터 내부 장기까지 훤히 읽히고 있는 거나 마찬가지겠지.
112|
113|“그러죠.”
114|
115|“필요한 거 있으면 말씀하시고. 우리 진 공자님 부탁인데 뭐든 다 구해 드려야지.”
116|
117|눈을 찡긋거리는 그녀를 일별하고 방을 나오자마자 잠시 잊고 있던 일이 생각났다.
118|
119|“무진아, 넌 왜 그렇게 주둥이를 함부로 놀리니?”
120|
121|빡! 빡! 빡!
122|
123|“악, 악, 악!”
124|
125|한 명은 때리고, 한 명은 맞고.
126|
127|그렇게 돌아온 별채에서는 반듯하게 잘려 나간 노송 몇 그루와 흡족한 얼굴의 진무경이 기다리고 있었다.
128|
129|“베는 맛이 있군.”
130|
131|“…….”
132|
133|“…….”
134|
135|언젠가 저놈을 베어 버리고 싶다.
136|
137|
138|
139|* * *
140|
141|
142|
143|고요해진 객실. 한동안 곰방대만 피워 물던 월화가 입을 연 것은 진태경이 떠나고 한참 후였다.
144|
145|“내가 일전에 지시한 거, 알아봤어?”
146|
147|객실 밖에서 대기하고 있던 하오문도가 낮은 목소리로 대답했다.
148|
149|“나흘 전에 확인하신 것이 전부입니다. 추가 정보를 수집하고는 있습니다만…….”
150|
151|“더 나올 게 없다?”
152|
153|“예, 희박합니다.”
154|
155|“희박? 그럼 가능성이 없진 않네? 계속 파. 시간 넉넉하게 줄 테니까 서두르지 말고. 지금 태원진가 건드렸다가는 우리도 좋은 꼴 못 보는 거 알지?”
156|
157|“존명.”
158|
159|물러가려는 하오문도를 붙잡은 건 이어지는 월화의 한마디였다.
160|
161|“삼류 망나니가 불과 두 달도 안 돼서 산서잠룡이 됐어. 네 생각은 어때?”
162|
163|“가능합니다. 소문대로라면.”
164|
165|“아, 그거.”
166|
167|월화가 피식 실소를 터트렸다. 진태경이 일문일살 조필을 쓰러트린 후부터 퍼지기 시작한 소문이다.
168|
169|지금까지 진태경이 보인 모습은 모두 위장이었고, 사실은 그가 어린 시절부터 전폭적인 지원 아래 무공을 익혔다는 소문.
170|
171|이제는 산서성 전역에 모르는 사람이 없을 정도로 퍼진 이야기다.
172|
173|“그걸 믿니?”
174|
175|“황당무계한 헛소문이죠. 하지만…….”
176|
177|“사람들은 믿지. 멍청해서가 아니라, 믿을 수밖에 없으니까. 하지만 우리는 아니야.”
178|
179|산서는 이미 중원에서 취급도 안 해 주는 변방이지만 하오문은 끊임없이 정보를 모아 왔다.
180|
181|산서성의 유력가인 태원진가의 직계에 대해서는 말할 것도 없다. 유일한 실수라고는 혼란스러웠던 전란(戰亂)의 시기에 활동했던 대장로를 정확히 파악하지 못했다는 것뿐.
182|
183|그러나 진태경에 관한 정보는 완벽에 가깝다.
184|
185|“술, 여자, 도박. 어린 시절부터 나태했고 노는 것에만 정신이 팔려 있었지. 태원진가 역사에 저런 자가 있었나 싶을 정도로.”
186|
187|“이 년 전, 지부장님께서 부임하시자마자 내린 첫 지시도 그것이었죠.”
188|
189|“맞아. 산서 전체 동향 파악. 그리고 진태경 집중 조사.”
190|
191|본디 재능은 대물림되는 법이다. 태원진가의 직계는 대대로 뛰어난 무재(武才)의 소유자들이었고 기인이라 평가받는 현 가주와 두 아들도 예외는 아니었다.
192|
193|그 사이에서 진태경의 존재는 이질적일 만큼 눈에 띄었고, 그래서 하오문은 조사에 착수했다.
194|
195|“결과는 허무했지.”
196|
197|“정말 보이는 그대로 나왔습니다.”
198|
199|가문의 핏줄 덕분인지 근골과 근맥이 약간 뛰어나다는 것 빼고는 특별할 것도 없었다.
200|
201|“그때 뭔가 놓쳤던 걸까?”
202|
203|“이틀에 한 번꼴로 기루에서 자고 가던 놈입니다. 잠을 줄여 가며 익혀도 부족한 것이 무공이지 않습니까?”
204|
205|“알지, 잘 알지.”
206|
207|월화는 일류 중에서도 제법 완숙한 경지까지 무공을 익힌 사람이다. 그에 대해 모를 리 없었다.
208|
209|답답함에 연신 곰방대만 빨아들이던 그녀가 긴 숨을 토했다.
210|
211|“결국 답은 하나뿐이네.”
212|
213|“그렇습니다.”
214|
215|진태경이 두 달 남짓한 시간 동안 삼류에서 초일류의 고수가 되었다는 것. 월화는 스스로 내린 결론에 기가 찼지만 어쩔 도리가 없었다.
216|
217|“아까 내린 지시는 없던 걸로 해. 그에 대해서는 더 이상 묻지도, 알려고 하지도 마. 혹여나 입에 올리는 일 없도록 함구령 내리고.”
218|
219|“존명. 단단히 일러두겠습니다.”
220|
221|“아, 그리고 하나 더. 내일 일찍 떠날 테니까 준비해 둬.”
222|
223|“누구를 데려가실 생각인지.”
224|
225|“나 혼자.”
226|
227|“지부장님, 그건…….”
228|
229|“명령이야.”
230|
231|“……존명.”
232|
233|수하가 물러나자 객실에는 적막이 내리깔렸다. 월화는 까맣게 타 버린 담뱃잎을 털며 생각했다.
234|
235|‘진태경이라.’
236|
237|지금까지의 행보가 모두 사실이라면, 항산검문에게서 얻어 내야 할 북부 이권 따위는 아무것도 아니다.
238|
239|‘고금을 통틀어 이 정도로 빠르게 성장한 이가 있었을까?’
240|
241|진태경이 앉아 있던 자리를 바라보는 그녀의 눈빛이 깊게 가라앉았다.
242|
243|
244|
245|* * *
246|
247|
248|
249|다음 날 아침.
250|
251|문제가 터졌다고 느낀 건 별채를 담당하는 책임자를 만난 후부터였다.
252|
253|“숙박비 스물다섯 냥, 음식값 다섯 냥, 그리고 기물 파손비로 오십 냥. 총합 은자 여든 냥입니다.”
254|
255|어제 마적 놈들을 주머니를 털었다며 희희낙락하던 혁무진이 입을 딱 벌렸다.
256|
257|“기물 파손? 은자 오십 냥?”
258|
259|“후원에 가 보니 노송 다섯 그루가 쓰러져 있더군요.”
260|
261|월화가 비싸다고 했던 그 나무다.
262|
263|나와 혁무진이 동시에 고개를 돌렸다. 시선이 마주친 진무경이 움찔하더니 입을 열었다.
264|
265|“검을 펼치다 보니 흥에 취했다.”
266|
267|“……아니, 시바. 흥에 취하면 걸리는 거 다 잘라도 되는 거야? 어?”
268|
269|“후우우.”
270|
271|혁무진은 뭐라 말은 못 하고 분노의 한숨만 푹푹 내쉬었다.
272|
273|척 보아하니 내야 할 돈이 경비를 초과한 게 분명하다. 그래도 약간 정도라면 잘 말해서 협의점을 찾을 수도…….
274|
275|“무진아, 지금 얼마 있냐?”
276|
277|“사십 냥이요.”
278|
279|협의점은 염병. 턱도 없네.
280|
281|“혹시 외상 됩니까?”
282|
283|별채 책임자의 입가에 맺혀 있던 상냥한 미소가 사라진 그 순간이었다.
284|
285|“진 공자, 여기서 뭐 해요?”
286|
287|이쪽을 향해 다가오는 하늘하늘한 궁장 차림의 미녀.
288|
289|지금의 우리에게 있어 월화의 등장은 구명줄이나 다름없었다.
290|
291|어젯밤 그녀의 제안을 단호하게 제안한 게 마음에 걸리지만, 이것저것 가릴 때가 아니다.
292|
293|“아니, 그게요…….”
294|
295|사정을 설명하자 월화가 눈을 동그랗게 떴다.
296|
297|“여든 냥? 그럴 리가 없는데.”
298|
299|“그렇죠? 좀 잘못된 것 같다니까요.”
300|
301|“그거 이리 줘 봐.”
302|
303|책임자가 들고 있던 죽간을 건네받아 읽기 시작하는 그녀.
304|
305|점점 눈살을 찌푸리는 걸 보니 계산이 단단히 틀어진 것이 분명했다.
306|
307|‘그럼 그렇지.’
308|
309|이윽고 죽간을 모두 읽은 월화의 입술 사이로 싸늘한 목소리가 흘러나왔다.
310|
311|“일 똑바로 안 해?”
312|
313|“죄, 죄송합니다.”
314|
315|“이분들이 어떤 분들이신데 감히 이따위 짓거리를…… 가격 똑바로 적어.”
316|
317|혁무진이 작은 목소리로 소곤거렸다.
318|
319|“천만다행이네요.”
320|
321|“그러게. 접시 닦고 갈 뻔했네.”
322|
323|“이공자님 때문에 뭔 고생입니까, 이게.”
324|
325|“저 인간 얘기는 꺼내지도 마. 듣기만 해도 암 걸려.”
326|
327|“암이 뭔데요?”
328|
329|“……있어, 안 좋은 거.”
330|
331|그사이 진땀을 흘려 가며 가격을 고친 책임자가 허리를 푹 숙이며 우리에게 사과했다.
332|
333|“죄송합니다. 제가 생각이 짧아서 결례를 저질렀습니다.”
334|
335|혁무진이 거만한 태도로 인사를 받았다.
336|
337|“다음부턴 그러지 마쇼. 상대를 봐 가면서 장난을 쳐야지. 그래서 얼마요?”
338|
339|“은자 백오 냥 하고도 철전 이십삼 냥입니다.”
340|
341|“……?”
342|
343|“……?”
344|
345|뭐야, 이거. 꿈인가?
346|
347|고개가 저절로 월화를 향해 돌아간다.
348|
349|“무슨 소리예요, 저게?”
350|
351|“내 지인이라고 멋대로 가격을 깎았더라고요. 감히 대태원진가의 자제분들을 뭘로 보고. 다시 한번 사과드려.”
352|
353|“몰라뵈어서 죄송합니다!”
354|
355|“그…….”
356|
357|나는 잔뜩 목멘 목소리로 물었다.
358|
359|“외상은 되죠? 당연히.”
360|
361|“안 되죠. 당연히. 이 년 동안 단 한 번도 없었어요.”
362|
363|“이번 기회에 선례를 남기는 건 어떨까요?”
364|
365|“아직은 그럴 생각이 없어서. 다음 기회를 노려 봐야죠.”
366|
367|월화가 화사한 웃음과 함께 덧붙였다.
368|
369|“더 하실 말씀이라도?”
370|
371|“……하, 항산.”
372|
373|“뭐라고요?”
374|
375|나는 눈을 질끈 감고 말을 이었다.
376|
377|“항산검문까지 같이 가실래요?”
378|
379|“와아, 저야 좋죠.”
380|
381|저 가증스러운 웃음이라니. 월화의 손짓에 책임자가 죽간을 들고 빛의 속도로 사라진다.
382|
383|“앞으로 여비 걱정은 없겠네요.”
384|
385|혁무진처럼 현실을 받아들이는 사람이 있는 반면에, 결사반대를 외치는 사람도 있었다.
386|
387|“헛소리! 가문의 임무를 수행하는 길에 어찌 여인을 데려간단 말이냐!”
388|
389|“그럼 여기서 그릇 닦고 오든가.”
390|
391|“…….”
392|
393|“이 중에서 노송 자른 사람 손?”
394|
395|진무경은 손을 들지 않았고, 월화는 그에게 치맛자락을 살짝 들어 올리며 인사했다.
396|
397|“잘 부탁드려요. 진 소협.”
```

## Assembled English

```markdown
[P1]
# Chapter 106

[P2]
“Let’s go together. To the Mount Heng Sword Sect.”

[P3]
“What?”

[P4]
“You heard me, Young Master Jin. I have business at the Mount Heng Sword Sect too.”

[P5]
“What kind of business?”

[P6]
“I don’t think I can tell you that. I’m rather clear about keeping business and personal matters separate myself.”

[P7]
*Talk about getting paid back tenfold.*

[P8]
My own words had come straight back to bite me. Wolhwa’s smile deepened as she watched me grow awkward.

[P9]
“I’m only joking. I happen to have something to collect from the Mount Heng Sword Sect. More precisely, something I’m supposed to receive from the Jin Family of Taiyuan.”

[P10]
“What… Oh.”

[P11]
A memory suddenly came to me. Back when the war with the Mount Heng Sword Sect was in full swing, the Jin Family of Taiyuan and the Lower District Sect had made a secret pact.

[P12]
*Hadn’t we promised them ownership of the Mount Heng Sword Sect’s properties and other holdings in exchange for information?*

[P13]
The Lower District Sect—or rather, Wolhwa—had kept her promise. It was thanks to her help that we had been able to annihilate the Mount Heng Sword Sect’s vanguard early in the war.

[P14]
The Jin Family of Taiyuan had continued receiving help from the Lower District Sect afterward and eventually won the war, but that was when the trouble began.

[P15]
“As you know, Young Master Jin, our position has become rather awkward. We won the war, but we can’t lay our hands on the spoils.”

[P16]
The strong devouring the weak. That was the law of Murim.

[P17]
But the appearance of the Head Elder had ruined everything. The moment it came to light that the Jin Family of Taiyuan and the Mount Heng Sword Sect had both been manipulated by him, the justification for claiming the spoils had grown faint.

[P18]
*So that’s why we’re pursuing a merger.*

[P19]
Now was the time to sheathe our swords and negotiate with a brush. Jin Wikyung’s vision was to quietly and amicably absorb the Mount Heng Sword Sect within limits that would keep the world from condemning us.

[P20]
Wolhwa wanted her reward before that happened.

[P21]
“If the Mount Heng Sword Sect accepts our proposal, couldn’t you demand your reward then?”

[P22]
“That would only be possible if the Jin Family of Taiyuan were Shanxi’s hegemon rather than its Alliance Leader. If you tried to seize anything rashly in the current situation, the other small and mid-sized sects would pull out too. Besides…”

[P23]
For a moment, she gave me a meaningful look, then shook her head.

[P24]
*What was that supposed to mean?*

[P25]
“Besides what?”

[P26]
“No, it’s nothing. Anyway, I did receive a proposal from the Lesser Family Head.”

[P27]
Wolhwa took a puff from her long-stemmed tobacco pipe before continuing.

[P28]
“He said he would transfer wealth equivalent to what he had promised, or hand over some of the areas managed by the Jin Family of Taiyuan.”

[P29]
That sounded reasonable enough, but it looked different from the perspective of someone leading an organization rather than acting as an individual.

[P30]
*She wants to expand her territory.*

[P31]
Wolhwa was neither a courtesan nor an innkeeper at heart. She was an information merchant.

[P32]
She clearly wanted to use this opportunity to expand the Lower District Sect’s influence into northern Shanxi, where the Mount Heng Sword Sect’s blockade had kept it relatively weak.

[P33]
*Jin Wikyung, naturally, wants the Jin Family of Taiyuan to encompass all of Shanxi.*

[P34]
The Jin Family of Taiyuan had already wielded enormous influence over central and southern Shanxi for a long time. Handing over a few prime territories wouldn’t diminish what they had built.

[P35]
*This is exactly like a redevelopment zone.*

[P36]
The Mount Heng Sword Sect, which had held the north in an iron grip and blocked outside forces from entering, was collapsing. The greenbelt had been lifted and the area opened for redevelopment, kicking off a tug-of-war between Jin Wikyung and Wolhwa.

[P37]
*They’re both something else.*

[P38]
Yesterday’s ally had become today’s competitor.

[P39]
Once again, I was reminded that there was always more to people than met the eye.

[P40]
“So I thought I’d meet our adorable new Sect Leader and collect what I’m owed while I was at it. How about we travel to the Mount Heng Sword Sect together?”

[P41]
I answered without another thought.

[P42]
“I’ll have to decline.”

[P43]
“Wow, aren’t you being a little too decisive? You cut me off without even hearing the terms.”

[P44]
“As his younger brother, I can’t go around splashing filth on my hyung’s path.”

[P45]
We might not have shared a drop of blood, but I had long since accepted his existence—and this Murim—as my own.

[P46]
“Hmm.”

[P47]
Wolhwa stared at me for a moment before setting her pipe down with a sharp tap.

[P48]
“All right, then.”

[P49]
“Ah. Yes.”

[P50]
I had expected her to tempt me a few more times, but she gave up right away.

[P51]
Well, I was glad the conversation had ended quickly. That made things easier for me.

[P52]
“Then we’ll be going.”

[P53]
I gave Hyuk Mujin, who was still sitting there with his mouth sealed shut, a light tap and rose from my seat. That was when Wolhwa smiled strangely and spoke.

[P54]
“Oh, could you tell Young Hero Jin something for me? The old pines in the rear courtyard are expensive, so please ask him to be careful while training.”

[P55]
This was an inn run by the greatest information merchant in Shanxi. Ever since we entered this place, she had probably seen right through us, down to our innards.

[P56]
“Sure.”

[P57]
“And tell me if you need anything. It’s a request from our Young Master Jin, so I have to procure anything you might need.”

[P58]
She winked. I glanced at her and left the room, only to remember something I had momentarily forgotten.

[P59]
“Mujin, why do you run your mouth so carelessly?”

[P60]
Whack! Whack! Whack!

[P61]
“Argh! Argh! Argh!”

[P62]
One of us hit, and the other took the hits.

[P63]
When we returned to the private residence, several old pine trees stood neatly severed, with Jin Mukyung waiting beside them looking thoroughly satisfied.

[P64]
“There’s a certain satisfaction to cutting.”

[P65]
“……”

[P66]
“……”

[P67]
*One day, I really want to cut that bastard down.*

[P68]
* * *

[P69]
The guest room fell quiet. Wolhwa smoked her long-stemmed tobacco pipe for a long while, and it was only well after Jin Taekyung had left that she finally spoke.

[P70]
“Did you look into what I instructed you to investigate?”

[P71]
A member of the Lower District Sect who had been waiting outside the room answered in a low voice.

[P72]
“What you confirmed four days ago is all we have. We’re still gathering additional information, but…”

[P73]
“Nothing else is going to turn up?”

[P74]
“It’s unlikely.”

[P75]
“Unlikely? Then there’s still a chance. Keep digging. I’ll give you plenty of time, so don’t rush. You know we won’t come out of it well either if we provoke the Jin Family of Taiyuan right now.”

[P76]
“Yes, Branch Leader.”

[P77]
The Lower District Sect member was about to withdraw when Wolhwa stopped him with one more question.

[P78]
“A Third Rate wastrel became the Sleeping Dragon of Shanxi in less than two months. What do you think?”

[P79]
“It’s possible, if the rumors are true.”

[P80]
“Ah, that.”

[P81]
Wolhwa let out a short, incredulous laugh. The rumor had begun spreading after Jin Taekyung defeated Jopil, One Question, One Kill.

[P82]
According to the rumor, everything Jin Taekyung had shown until then had been an act. In truth, he had trained in martial arts from childhood with the family’s full support.

[P83]
By now, the story had spread so widely that there was hardly anyone in Shanxi who hadn’t heard it.

[P84]
“Do you believe it?”

[P85]
“It’s ridiculous nonsense. But…”

[P86]
“People believe it. Not because they’re stupid, but because they have no choice but to believe it. But we’re different.”

[P87]
Shanxi was a remote frontier the Central Plains barely even acknowledged, but the Lower District Sect had never stopped gathering information there.

[P88]
That went without saying when it came to the direct descendants of the Jin Family of Taiyuan, one of Shanxi’s most powerful families. Their only mistake had been failing to accurately assess the Head Elder, who had been active during the chaotic period of war.

[P89]
But their information on Jin Taekyung was nearly perfect.

[P90]
“Alcohol, women, gambling. He was lazy from childhood and cared about nothing but having fun. He was so out of place that you had to wonder whether anyone like him had ever existed in the history of the Jin Family of Taiyuan.”

[P91]
“That was the first order you gave after taking office as Branch Leader two years ago.”

[P92]
“That’s right. Monitor the entire situation in Shanxi. And investigate Jin Taekyung in depth.”

[P93]
Talent tended to run in families. The direct descendants of the Jin Family of Taiyuan had possessed exceptional martial talent for generations, and the current Family Head and his two sons, all regarded as eccentrics, were no exception.

[P94]
Jin Taekyung stood out among them as something almost alien. That was why the Lower District Sect had begun its investigation.

[P95]
“The result was anticlimactic.”

[P96]
“He was exactly what he appeared to be.”

[P97]
Other than slightly superior bones, sinews, and meridians—perhaps thanks to his bloodline—there was nothing special about him.

[P98]
“Did we miss something back then?”

[P99]
“He was the kind of bastard who spent every other night at a pleasure house. Martial arts take more time than anyone has, even if they cut back on sleep.”

[P100]
“I know. I know very well.”

[P101]
Wolhwa had cultivated her martial arts to a fairly mature stage even within the First Rate realm. There was no way she didn’t understand that.

[P102]
She drew repeatedly on her pipe in frustration, then released a long breath.

[P103]
“In the end, there’s only one answer.”

[P104]
“That’s right.”

[P105]
Jin Taekyung had gone from Third Rate to a master beyond First Rate in a little over two months. Wolhwa was dumbfounded by the conclusion she had reached herself, but there was nothing she could do about it.

[P106]
“Forget the order I gave earlier. Don’t ask about him anymore, and don’t try to learn anything else. Issue a gag order and make sure no one even mentions this.”

[P107]
“Yes, Branch Leader. I’ll make sure they understand.”

[P108]
“Oh, and one more thing. I’ll be leaving early tomorrow, so make the preparations.”

[P109]
“Who are you planning to take with you?”

[P110]
“No one. I’ll go alone.”

[P111]
“Branch Leader, that…”

[P112]
“It’s an order.”

[P113]
“Understood.”

[P114]
Once her subordinate withdrew, silence settled over the guest room. Wolhwa tapped the blackened tobacco leaves from her pipe and thought.

[P115]
*Jin Taekyung.*

[P116]
If everything he had done until now was true, then the northern interests she needed to extract from the Mount Heng Sword Sect were nothing.

[P117]
*Has anyone in all history ever grown this quickly?*

[P118]
Her gaze darkened as she stared at the place where Jin Taekyung had been sitting.

[P119]
* * *

[P120]
The next morning.

[P121]
I began to feel that something had gone wrong after meeting the person in charge of the private residence.

[P122]
“The lodging fee is twenty-five nyang, the food comes to five nyang, and the property damage fee is fifty nyang. The total is eighty silver nyang.”

[P123]
Hyuk Mujin, who had been celebrating yesterday after emptying those mounted bandits’ pockets, gaped.

[P124]
“Property damage? Fifty silver nyang?”

[P125]
“When I went to the rear courtyard, I found that five old pine trees had fallen.”

[P126]
They were the trees Wolhwa had said were expensive.

[P127]
Hyuk Mujin and I turned our heads at the same time. Jin Mukyung, whose eyes met ours, flinched before opening his mouth.

[P128]
“I got carried away while practicing my swordsmanship.”

[P129]
“……No, fuck. If you get carried away, does that mean you can cut down anything in your way? Huh?”

[P130]
“Hoooo.”

[P131]
Hyuk Mujin couldn’t say anything. He merely let out one furious sigh after another.

[P132]
One look told me the bill exceeded the money we had left. If it had only been a little over, maybe we could have talked it out and found some middle ground…

[P133]
“Mujin, how much do you have right now?”

[P134]
“Forty nyang.”

[P135]
*Middle ground, my ass. We’re nowhere close.*

[P136]
“Could we put it on credit?”

[P137]
That was the exact moment the kind smile around the private-residence manager’s lips disappeared.

[P138]
“Young Master Jin, what are you doing here?”

[P139]
A beautiful woman in a light, flowing palace-style dress was approaching us.

[P140]
Right now, Wolhwa’s appearance was nothing short of a lifeline.

[P141]
I felt bad about turning down her proposal so decisively the night before, but this was no time to be picky.

[P142]
“Well, you see…”

[P143]
When I explained the situation, Wolhwa’s eyes grew round.

[P144]
“Eighty nyang? That can’t be right.”

[P145]
“Exactly. I knew something was wrong.”

[P146]
“Give me that.”

[P147]
She took the bamboo slip from the manager and began to read.

[P148]
The deeper her frown grew, the clearer it seemed that the arithmetic had been badly botched.

[P149]
*Knew it.*

[P150]
At last, Wolhwa finished reading the bamboo slip. A chill entered her voice.

[P151]
“Are you not doing your job properly?”

[P152]
“I-I’m sorry.”

[P153]
“Do you have any idea who these gentlemen are? How dare you pull this kind of stunt? Write down the correct prices.”

[P154]
Hyuk Mujin whispered to me.

[P155]
“What a relief.”

[P156]
“Yeah. We almost had to wash dishes before leaving.”

[P157]
“Why do we have to suffer because of the Second Young Master?”

[P158]
“Don’t even mention that man. Just hearing about him gives me cancer.”

[P159]
“What’s cancer?”

[P160]
“……Something bad.”

[P161]
Meanwhile, the manager revised the prices, sweating profusely. Then he bowed deeply and apologized to us.

[P162]
“I’m sorry. I acted thoughtlessly and committed a grave discourtesy.”

[P163]
Hyuk Mujin accepted the apology with an arrogant air.

[P164]
“Don’t do that again. You have to know who you’re dealing with before pulling a prank. So how much is it?”

[P165]
“One hundred and five silver nyang and twenty-three iron coins.”

[P166]
“……?”

[P167]
“……?”

[P168]
*What the hell? Is this a dream?*

[P169]
My head turned toward Wolhwa of its own accord.

[P170]
“What is that supposed to mean?”

[P171]
“He arbitrarily lowered the prices because you were my acquaintances. How dare he look down on the young masters of the great Jin Family of Taiyuan? Apologize again.”

[P172]
“I’m sorry for failing to recognize your identities!”

[P173]
“But…”

[P174]
I asked in a thoroughly choked voice.

[P175]
“We can put it on credit, right? Of course.”

[P176]
“No, you can’t. Of course not. We haven’t allowed that even once in the past two years.”

[P177]
“How about making an exception and setting a precedent this time?”

[P178]
“I don’t have any plans to do that yet. You’ll have to aim for the next opportunity.”

[P179]
Wolhwa added with a radiant smile,

[P180]
“Was there something else you wanted to say?”

[P181]
“……M-Mount Heng.”

[P182]
“What was that?”

[P183]
I squeezed my eyes shut and continued.

[P184]
“Would you like to come with us to the Mount Heng Sword Sect?”

[P185]
“Wow, I’d love to.”

[P186]
*That hateful smile.*

[P187]
At Wolhwa’s gesture, the manager snatched up the bamboo slip and vanished at the speed of light.

[P188]
“We won’t have to worry about travel expenses anymore.”

[P189]
While Hyuk Mujin was the sort of person who simply accepted reality, someone else was shouting vehement opposition.

[P190]
“Nonsense! How can you bring a woman along while carrying out a family mission?”

[P191]
“Then stay here and wash dishes.”

[P192]
“……”

[P193]
“Who here cut down the old pine trees? Raise your hand.”

[P194]
Jin Mukyung didn’t raise his hand. Wolhwa slightly lifted the hem of her skirt and greeted him.

[P195]
“Please take good care of me, Young Hero Jin.”
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
# Chapter 106

[P2]
“Let’s go together. To the Mount Heng Sword Sect.”

[P3]
“What?”

[P4]
“You heard me, Young Master Jin. I have business at the Mount Heng Sword Sect too.”

[P5]
“What kind of business?”

[P6]
“I don’t think I can tell you that. I’m rather clear about keeping business and personal matters separate.”

[P7]
*Talk about getting paid back tenfold.*

[P8]
What I had just said had come back to bite me. Wolhwa’s smile deepened as she watched me grow awkward.

[P9]
“I’m only joking. I happen to have something to collect from the Mount Heng Sword Sect. More precisely, something I’m supposed to receive from the Jin Family of Taiyuan.”

[P10]
“What… Oh.”

[P11]
A memory suddenly came to me. Back when the war with the Mount Heng Sword Sect was in full swing, the Jin Family of Taiyuan and the Lower District Sect had made a secret pact.

[P12]
*Hadn’t we promised to give them ownership of the Mount Heng Sword Sect’s properties and such in exchange for information?*

[P13]
The Lower District Sect—or rather, Wolhwa—had kept her promise. It was thanks to her help that we had been able to annihilate the Mount Heng Sword Sect’s vanguard in the early days of the war.

[P14]
The Jin Family of Taiyuan had continued receiving help from the Lower District Sect afterward and had eventually won the war, but that was when the trouble began.

[P15]
“As you know, Young Master Jin, our position has become rather awkward. We won the war, but we can’t lay our hands on the spoils.”

[P16]
The strong devouring the weak. That was the law of Murim.

[P17]
But the appearance of the Head Elder had ruined everything. The moment it came to light that the Jin Family of Taiyuan and the Mount Heng Sword Sect had both been manipulated by him, the justification for claiming the spoils had grown faint.

[P18]
*So that’s why we’re pursuing a merger.*

[P19]
Now was the time to put away our swords and negotiate with a brush. Jin Wikyung’s vision was to quietly and amicably absorb the Mount Heng Sword Sect within limits that would keep the world from condemning us.

[P20]
Wolhwa wanted to receive her reward before that happened.

[P21]
“If the Mount Heng Sword Sect accepts our proposal, couldn’t you demand your reward then?”

[P22]
“That would only be possible if the Jin Family of Taiyuan were Shanxi’s hegemon rather than its Alliance Leader. If we tried to snatch things away carelessly in the current situation, the other mid-sized and small sects would withdraw too. And on top of that…”

[P23]
For a moment, she looked at me with meaningful eyes before shaking her head.

[P24]
*What was that supposed to mean?*

[P25]
“And on top of that, what?”

[P26]
“No, it’s nothing. Anyway, I did receive a proposal from the Lesser Family Head.”

[P27]
Wolhwa took a puff from her long-stemmed tobacco pipe before continuing.

[P28]
“He said he would transfer wealth equivalent to what he had promised, or hand over some of the areas managed by the Jin Family of Taiyuan.”

[P29]
That sounded like a reasonable offer, but it looked different when viewed from the perspective of someone leading an organization rather than acting as an individual.

[P30]
*She wants to expand her territory.*

[P31]
Wolhwa’s true nature was neither that of a courtesan nor an innkeeper. She was an information merchant.

[P32]
There was no doubt that she wanted to use this opportunity to expand the Lower District Sect’s influence into northern Shanxi, where it had been relatively weak because of the Mount Heng Sword Sect’s blockade.

[P33]
*Jin Wikyung, naturally, wants the Jin Family of Taiyuan to encompass all of Shanxi.*

[P34]
The Jin Family of Taiyuan had already wielded enormous influence over central and southern Shanxi for a long time. Handing over a few prime areas wouldn’t diminish the influence they had built up until now.

[P35]
*This is exactly like a redevelopment district.*

[P36]
The Mount Heng Sword Sect, which had held a firm grip on the north and blocked outside forces from entering, was collapsing. The greenbelt had been lifted and the area had become open for redevelopment, so the tug-of-war between Jin Wikyung and Wolhwa had begun.

[P37]
*They’re both something else.*

[P38]
Yesterday’s ally had become today’s competitor.

[P39]
Once again, I felt that people were never everything they appeared to be.

[P40]
“So I thought I’d meet our adorable new Sect Leader and collect what I’m owed while I was at it. How about we travel to the Mount Heng Sword Sect together?”

[P41]
I answered without needing to think any further.

[P42]
“I’ll have to decline.”

[P43]
“Wow, aren’t you being a little too decisive? You cut me off without even hearing the terms.”

[P44]
“As his younger brother, I can’t go around splashing filth on my hyung’s path.”

[P45]
We weren’t related by blood, but I had long since accepted his existence—and this Murim—as my own.

[P46]
“Hmm.”

[P47]
Wolhwa stared at me for a moment before setting her pipe down with a sharp tap.

[P48]
“All right, then.”

[P49]
“Ah. Yes.”

[P50]
I had expected her to tempt me a few more times, but she gave up right away.

[P51]
Well, at least the conversation had ended quickly. That made things easier for me.

[P52]
“Then we’ll be going.”

[P53]
I gave Hyuk Mujin, who was still sitting there with his mouth sealed shut, a light tap and rose from my seat. That was when Wolhwa smiled strangely and spoke.

[P54]
“Oh, could you tell Young Hero Jin something for me? The old pine in the rear courtyard is expensive, so please be careful with your training.”

[P55]
This was an inn run by the greatest information merchant in Shanxi. Ever since we entered this place, she had probably seen right through us, down to our innards.

[P56]
“Sure.”

[P57]
“And tell me if you need anything. It’s a request from our Young Master Jin, so I have to procure anything you might need.”

[P58]
She gave me a wink. I merely glanced at her and left the room, only to remember something I had momentarily forgotten.

[P59]
“Mujin, why do you run your mouth so carelessly?”

[P60]
Whack! Whack! Whack!

[P61]
“Argh! Argh! Argh!”

[P62]
One of us hit, and the other took the hits.

[P63]
When we returned to the private residence, we found several old pine trees neatly cut down and Jin Mukyung waiting with a satisfied expression.

[P64]
“There’s a certain satisfaction to cutting.”

[P65]
“……”

[P66]
“……”

[P67]
*One day, I really want to cut that bastard down.*

[P68]
* * *

[P69]
The guest room had grown quiet. Wolhwa smoked her long-stemmed tobacco pipe for a long while before finally speaking, long after Jin Taekyung had left.

[P70]
“Did you look into what I instructed you to investigate?”

[P71]
A member of the Lower District Sect, who had been waiting outside the guest room, answered in a low voice.

[P72]
“What you confirmed four days ago is all we have. We’re still gathering additional information, but…”

[P73]
“Nothing else is going to turn up?”

[P74]
“It’s unlikely.”

[P75]
“Unlikely? Then there’s still a chance. Keep digging. I’ll give you plenty of time, so don’t rush. You know that if we provoke the Jin Family of Taiyuan right now, we won’t fare well either.”

[P76]
“Yes, Branch Leader.”

[P77]
The Lower District Sect member was about to withdraw when Wolhwa stopped him with one more question.

[P78]
“A Third Rate wastrel became the Sleeping Dragon of Shanxi in less than two months. What do you think?”

[P79]
“It’s possible, if the rumors are true.”

[P80]
“Ah, that.”

[P81]
Wolhwa let out a short laugh. It was a rumor that had begun spreading after Jin Taekyung defeated Jopil, One Question, One Kill.

[P82]
According to the rumor, everything Jin Taekyung had shown until now had been an act. In truth, he had learned martial arts since childhood under the full support of the family.

[P83]
By now, the story had spread throughout Shanxi to the point that there was hardly anyone who hadn’t heard it.

[P84]
“Do you believe it?”

[P85]
“It’s ridiculous nonsense. But…”

[P86]
“People believe it. Not because they’re stupid, but because they have no choice but to believe it. But we’re different.”

[P87]
Shanxi was already a frontier region that the Central Plains hardly even acknowledged, but the Lower District Sect had continued gathering information there without pause.

[P88]
When it came to the direct descendants of the Jin Family of Taiyuan, one of Shanxi’s most powerful families, there was no need to mention it. Their only mistake had been failing to accurately assess the Head Elder, who had been active during the chaotic period of war.

[P89]
But their information on Jin Taekyung was nearly perfect.

[P90]
“Alcohol, women, gambling. He had been lazy since childhood and obsessed with nothing but having fun. He was so out of place that you would have wondered whether someone like him had ever existed in the history of the Jin Family of Taiyuan.”

[P91]
“That was the first order you gave after taking office as Branch Leader two years ago.”

[P92]
“That’s right. Monitor the entire situation in Shanxi. And investigate Jin Taekyung in depth.”

[P93]
Talent was normally passed down through the generations. The direct descendants of the Jin Family of Taiyuan had possessed exceptional martial talent for generations, and the current Family Head and his two sons, all regarded as eccentrics, were no exception.

[P94]
Jin Taekyung’s existence stood out so sharply among them that he seemed almost alien. That was why the Lower District Sect had begun its investigation.

[P95]
“The result was anticlimactic.”

[P96]
“He was exactly what he appeared to be.”

[P97]
Other than having slightly superior bones and meridians, perhaps thanks to his family bloodline, there had been nothing special about him.

[P98]
“Did we miss something back then?”

[P99]
“He was the kind of bastard who spent the night at a pleasure house every other day. Martial arts already demands more time than a person has, even if they cut back on sleep.”

[P100]
“I know. I know very well.”

[P101]
Wolhwa had cultivated her martial arts to a fairly mature stage of the First Rate realm. There was no way she didn’t understand that.

[P102]
She continued drawing on her pipe, exhaling long breaths in frustration before finally letting out a deep sigh.

[P103]
“In the end, there’s only one answer.”

[P104]
“That’s right.”

[P105]
Jin Taekyung had gone from Third Rate to a master beyond First Rate in a little over two months. Wolhwa was dumbfounded by the conclusion she had reached herself, but there was nothing she could do about it.

[P106]
“Cancel the order I gave earlier. Don’t ask about him anymore, and don’t try to find out anything else. Issue a gag order so that no one even mentions him.”

[P107]
“Yes, Branch Leader. I’ll make sure they understand.”

[P108]
“Oh, and one more thing. I’ll be leaving early tomorrow, so prepare everything.”

[P109]
“Who are you planning to take with you?”

[P110]
“No one. I’ll go alone.”

[P111]
“Branch Leader, that…”

[P112]
“It’s an order.”

[P113]
“Understood.”

[P114]
Once her subordinate withdrew, silence settled over the guest room. Wolhwa shook the completely burned tobacco leaves from her pipe and thought.

[P115]
*Jin Taekyung.*

[P116]
If everything he had done until now was true, then the northern interests she was supposed to extract from the Mount Heng Sword Sect were nothing.

[P117]
*Has anyone in all history ever grown this quickly?*

[P118]
Her gaze, fixed on the place where Jin Taekyung had been sitting, sank into deep contemplation.

[P119]
* * *

[P120]
The next morning.

[P121]
I began to feel that something had gone wrong after meeting the person in charge of the private residence.

[P122]
“The lodging fee is twenty-five nyang, the food comes to five nyang, and the property damage fee is fifty nyang. The total is eighty silver nyang.”

[P123]
Hyuk Mujin, who had been rejoicing yesterday over emptying the pockets of those mounted bandits, gaped.

[P124]
“Property damage? Fifty silver nyang?”

[P125]
“When I went to the rear courtyard, I found that five old pine trees had fallen.”

[P126]
They were the trees Wolhwa had said were expensive.

[P127]
Hyuk Mujin and I turned our heads at the same time. Jin Mukyung, whose eyes met ours, flinched before opening his mouth.

[P128]
“I got carried away while practicing my swordsmanship.”

[P129]
“……No, fuck. If you get carried away, does that mean you can cut down anything in your way? Huh?”

[P130]
“Hoooo.”

[P131]
Hyuk Mujin couldn’t say anything. He merely kept letting out furious sighs.

[P132]
At a glance, it was obvious that the bill exceeded the amount we had on hand. If it had only been a little over, we might have been able to talk things out and find a compromise…

[P133]
“Mujin, how much money do you have right now?”

[P134]
“Forty nyang.”

[P135]
*To hell with a compromise. We’re nowhere close.*

[P136]
“Could we put it on credit?”

[P137]
That was the exact moment the kind smile around the private-residence manager’s lips disappeared.

[P138]
“Young Master Jin, what are you doing here?”

[P139]
A beautiful woman in a light, flowing palace-style dress was approaching us.

[P140]
Wolhwa’s appearance was nothing short of a lifeline.

[P141]
I felt bad about turning down her proposal so decisively the night before, but this was no time to be picky.

[P142]
“Well, you see…”

[P143]
When I explained the situation, Wolhwa’s eyes grew round.

[P144]
“Eighty nyang? That can’t be right.”

[P145]
“Exactly. I knew something was wrong.”

[P146]
“Give me that.”

[P147]
She took the bamboo slip from the manager and began to read.

[P148]
The deeper her frown grew, the clearer it seemed that the arithmetic had been badly botched.

[P149]
*Knew it.*

[P150]
At last, Wolhwa finished reading the bamboo slip. A chill entered her voice.

[P151]
“Are you not doing your job properly?”

[P152]
“I-I’m sorry.”

[P153]
“Who do you think these gentlemen are, to dare pull this kind of stunt? Write the prices correctly.”

[P154]
Hyuk Mujin whispered in a small voice.

[P155]
“What a relief.”

[P156]
“Yeah. We almost had to wash dishes before leaving.”

[P157]
“What kind of hardship is this because of the Second Young Master?”

[P158]
“Don’t even mention that man. Just hearing about him gives me cancer.”

[P159]
“What’s cancer?”

[P160]
“……It’s something bad.”

[P161]
Meanwhile, the manager revised the prices while sweating profusely. Then he bent deeply at the waist and apologized to us.

[P162]
“I’m sorry. I was thoughtless and committed a grave discourtesy.”

[P163]
Hyuk Mujin accepted the apology with an arrogant air.

[P164]
“Don’t do that again. You have to know who you’re dealing with before pulling a prank. So how much is it?”

[P165]
“One hundred and five nyang, along with twenty-three iron coins.”

[P166]
“……”

[P167]
“……”

[P168]
*What the hell? Is this a dream?*

[P169]
My head turned toward Wolhwa of its own accord.

[P170]
“What is that supposed to mean?”

[P171]
“He arbitrarily lowered the price because you were my acquaintances. How dare he take the young masters of the Jin Family of Taiyuan for fools? Apologize to them again.”

[P172]
“I’m sorry for failing to recognize your identities!”

[P173]
“But…”

[P174]
I asked in a thoroughly choked voice.

[P175]
“We can put it on credit, right? Of course.”

[P176]
“No, you can’t. Of course not. We haven’t allowed that even once in the past two years.”

[P177]
“How about making an exception and setting a precedent this time?”

[P178]
“I don’t have any plans to do that yet. You’ll have to aim for the next opportunity.”

[P179]
Wolhwa added with a bright smile,

[P180]
“Was there something else you wanted to say?”

[P181]
“……M-Mount Heng.”

[P182]
“What was that?”

[P183]
I squeezed my eyes shut and continued.

[P184]
“Would you like to come with us to the Mount Heng Sword Sect?”

[P185]
“Wow, I’d love to.”

[P186]
*That hateful smile.*

[P187]
At Wolhwa’s gesture, the manager snatched up the bamboo slip and vanished at the speed of light.

[P188]
“We won’t have to worry about travel expenses anymore.”

[P189]
While Hyuk Mujin was the sort of person who simply accepted reality, someone else was shouting vehement opposition.

[P190]
“Nonsense! How can you bring a woman along while carrying out a family mission?”

[P191]
“Then stay here and wash dishes.”

[P192]
“……”

[P193]
“Who here cut down the old pine trees? Raise your hand.”

[P194]
Jin Mukyung didn’t raise his hand. Wolhwa slightly lifted the hem of her skirt and greeted him.

[P195]
“Please take good care of me, Young Hero Jin.”
```


## Exact glossary matches

These English spellings are binding for the matched Korean keys.

| 무림     | **Murim**          |
| 진태경    | **Jin Taekyung**   |
| 진위경    | **Jin Wikyung**    |
| 진무경    | **Jin Mukyung**    |
| 혁무진    | **Hyuk Mujin**     |
| 조필     | **Jopil**          |
| 월화     | **Wolhwa**         |
| 산서잠룡   | **Sleeping Dragon of Shanxi** | Jin Taekyung   |
| 태원진가   | **Jin Family of Taiyuan**        |
| 항산검문   | **Mount Heng Sword Sect**        |
| 하오문    | **Lower District Sect**          |
| 삼류     | **Third Rate**    |
| 일류     | **First Rate**    |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 경지     | **realm** / **realm stage**                      | Especially power level                                |
| 중원     | **Central Plains**                               |                                                       |
| 마적     | **mounted bandits**                              |                                                       |
| 기루     | **pleasure house**                               |                                                       |
| 기녀     | **courtesan**                                    |                                                       |
| 곰방대   | **long-stemmed tobacco pipe**                    |                                                       |
| 가주     | **Family Head**                              |
| 소가주    | **Lesser Family Head**                       |
| 문주     | **Sect Leader**                              |
| 장로     | **Elder**                                    |
| 대장로    | **Head Elder**                               |
| 지부장    | **Branch Leader**                            |
| 보상               | **Reward**                     |
| 산서     | **Shanxi**             |
| 태원     | **Taiyuan**            |
| 청해     | **Qinghai**            |
| 항산     | **Mount Heng**         |
| 소협      | **Young Hero**                                                  |
| 공자      | **Young Master**                                                |
| 인도 | **Human Butcher** | Epithet of a mysterious Han Chinese mounted-bandit power commanding fifty subordinates. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 이공자 | **Second Young Master** | Title used for Jin Mukyung. |
| 맹주 | **Alliance Leader** | Leader of the regional Murim alliance. |
| 일문일살 | **One Question, One Kill** | Jopil's alias. |
| 문주님 | **Sect Leader** | Honorific title Lee Seowol orders the senior figures to use. |
| 산서성 | **Shanxi Province** | Province containing the Lower District Sect branches. |
| 은자 | **silver nyang** | Silver currency unit. |
| 철전 | **iron coins** | Lower-value coin currency used to compare the payment's value. |
| 대태원진가 | **great Jin Family of Taiyuan** | Formal exalted reference to the Jin Family of Taiyuan. |
| 근맥 | **Sinews and Meridians** | System attribute reduced by one after Taekyung's failed qi circulation. |
| 무재 | **martial talent** | Innate aptitude for learning martial arts. |
| 가지 | **Go** | Song associated with Won Myunghoon. |

## Deterministic QA

```json
{
  "version": 1,
  "chapter": 106,
  "passed": true,
  "metrics": {
    "source_characters": 6234,
    "translation_characters": 14949,
    "length_ratio": 2.398,
    "source_paragraphs": 194,
    "translation_paragraphs": 195
  },
  "errors": [],
  "warnings": [
    {
      "code": "terminology",
      "message": "matched preferred term is absent",
      "details": {
        "korean": "청해",
        "preferred": "Qinghai"
      }
    },
    {
      "code": "terminology",
      "message": "matched preferred term is absent",
      "details": {
        "korean": "인도",
        "preferred": "Human Butcher"
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
        "korean": "산서성",
        "preferred": "Shanxi Province"
      }
    },
    {
      "code": "terminology",
      "message": "matched preferred term is absent",
      "details": {
        "korean": "근맥",
        "preferred": "Sinews and Meridians"
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
