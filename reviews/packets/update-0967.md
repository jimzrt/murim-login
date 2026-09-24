<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0967.txt",
      "sha256": "2981cacd23d35df103a076c745e500e5f5a768a307984171b46d4324413ec6dc",
      "bytes": 13970
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "8ba7e519f03a3ed5a002ed7c26ab07eb6017c567083d3291dd2a64824d23797f",
      "bytes": 2162
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "b40e329f8ccc2725c247f21e7d735563c277525366768cd3625d9f3f4a508cda",
      "bytes": 235410
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "5d8a25644c570e75bb97604a6bd052661b86f534a4df09ea8443e64bfcdc9373",
      "bytes": 759
    },
    {
      "path": "characters/Jeok Cheongang.md",
      "sha256": "5ba04f13b101fbf8ef90ac93996fae6709da1bf76ef946b881ead77bb47e4fdc",
      "bytes": 1204
    },
    {
      "path": "characters/Peng Cheolhu.md",
      "sha256": "854289499f9ecffe43afdacc9298cf34dccb6cfcd3fc15aa3363ce49a14f62a3",
      "bytes": 707
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "37e19e0467234b45cbbaae5d189b109838afbd345811992a7e017233f86ec98d",
      "bytes": 269308
    }
  ],
  "estimated_tokens": 10494
}
-->

# Durable State Update — Chapter 967

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

For each matched character, check whether this chapter adds clear, durable
evidence that improves Role, Personality, Voice, or Relationships. Update a
field when it corrects or meaningfully sharpens the existing profile; otherwise
leave it unchanged. Voice guidance should capture observable register, cadence,
word choice, or address habits that help distinguish the character in English.
Do not infer a stable voice from one situational line or generic personality
adjectives. Keep “Not established” only when this chapter provides no reliable
voice evidence; never replace it with unsupported specificity.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 967. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 967. Profile updates may replace only one
complete line in Aliases, Role, Personality, Voice, or Relationships. Do not
return Safe through updates; the controller sets that field automatically.
Each profile field should be one concise sentence; never append semicolon-separated
chapter history. For a new profile, describe voice only when the chapter supports
a useful, stable distinction; otherwise say “Not established”.
`names` contains only newly required Korean-to-English rows that are absent from
Exact glossary matches; Korean keys must occur in the source. Do not repeat
glossary matches. The controller drops rows already in the names ledger.
`address_pairs` contains only newly required speaker→addressee rows that
are absent from Matched address pairs. Speaker and addressee must be Hangul source
spellings such as 진태경 or 혁무진, never English names. Arabic digits are
allowed in titles such as 1팀장. At least one endpoint must occur in the source.
Before returning JSON, verify every `speaker` and `addressee` value contains at
least one Hangul character; use the Korean source spelling even when the same
person's English name appears in the reading copy. If no valid new pair exists,
return `"address_pairs": []`.
The controller drops pairs already in the address ledger. Do not invent
risk-register rows. Beat plot paragraphs are plain strings; continuity and
translation decisions are concise list items.
Return this exact shape:

{
  "chapter": 967,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 967,
    "continuity_sources": [967],
    "active_continuity": ["active fact"],
    "open_questions": ["unresolved question"],
    "temporary_decisions": ["temporary translation decision"]
  },
  "names": [
    {"korean": "source spelling", "english": "English rendering", "notes": "brief note"}
  ],
  "address_pairs": [
    {
      "speaker": "진태경",
      "addressee": "문경",
      "kinship": "kinship or role relation",
      "normal_address": "established English address",
      "speech_level": "speech level",
      "notes": "brief note"
    }
  ],
  "profile_updates": [
    {
      "path": "characters/Listed Profile.md",
      "current": "- **Role:** exact current full line",
      "replacement": "- **Role:** finished replacement full line"
    }
  ],
  "profile_creations": [
    {
      "filename": "English Name.md",
      "korean": "source name",
      "english": "English Name",
      "aliases": [],
      "role": "stable role",
      "personality": "stable traits",
      "voice": "stable voice",
      "relationships": "stable relationships"
    }
  ]
}

Use empty arrays when no name, address-pair, or profile change is required.
`profile_creations` is only for characters with no existing `characters/` file.
If the person already appears under Listed compact profiles, use `profile_updates`.

## Prior durable context

```json
{
  "active_continuity": [
    "Mukyung is alive but grievously internally injured; he has risen again near the battle at the gorge’s center.",
    "Cheolhu and Jamukha continue their duel in the gorge; Cheolhu now knows Jamukha is stronger and more perceptive than expected.",
    "Wikyung leads Shanxi fighters toward the gorge’s center, believing their current momentum is temporary.",
    "The Hebei Peng Family fights the steppe army in the basin while outnumbered by more than ten to one; Cheolhu has gone to the gorge with some of its elite.",
    "Jamukha ordered his Keshik centurions not to use an unnamed weapon without his permission because more battles lie ahead.",
    "Jamukha anticipated allied forces would come to the Jin Family’s aid; an unidentified force has appeared beyond the basin and fired thousands of arrows.",
    "The Emperor remains gravely ill with Blood Soul Gu; the treatment requiring him to die once remains unresolved.",
    "The improved Temporary Strength Pill’s source and effects remain unknown; Jang Sam remains unconscious.",
    "The Martial God’s identity and connection to the chosen one and the Bow Saint remain unknown.",
    "The Eastern Heaven Demon Lord’s papers and silk pouch remain unexplained.",
    "Taekyung intends to keep the pocket watch for half a month before deciding whether to give it to Mujin.",
    "Taekyung resolved to trust his allies rather than bear every burden alone."
  ],
  "continuity_sources": [
    966
  ],
  "open_questions": [
    "Who is the newly arrived force, and what will its arrows do to the battle?",
    "What is the unnamed weapon the Keshik centurions were ordered not to use?",
    "How will the duel between Jamukha and Cheolhu, and the fighting in the gorge, unfold?",
    "Who gave Jang Sam the silk pouch, and what are the improved pill’s effects and distribution?",
    "What is the Martial God’s identity and connection to the chosen one and the Bow Saint?"
  ],
  "safe_through": 966,
  "temporary_decisions": [
    "Taekyung intends to keep the pocket watch for half a month before deciding whether to give it to Mujin."
  ],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 적천강    | **Jeok Cheongang** |
| 팽철후    | **Peng Cheolhu**   |
| 화왕     | **Fire King**                 | Jeok Cheongang |
| 벽력도왕   | **Thunderbolt Saber King**    | Peng Cheolhu   |
| 십왕     | **Ten Kings**       |
| 하북팽가   | **Hebei Peng Family**            |
| 무인     | **martial artist**                               | Default term                                          |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 경지     | **realm** / **realm stage**                      | Especially power level                                |
| 내공     | **internal energy**                              |                                                       |
| 심법     | **cultivation technique**                        | Especially internal cultivation                       |
| 보법     | **manoeuvre technique** / **footwork technique** | Named Jin technique uses “Manoeuvre”                  |
| 검법     | **sword technique**                              |                                                       |
| 구결     | **formula**                                      | Mnemonic/oral formula for a martial art               |
| 깨달음    | **enlightenment** / **insight**                  | Martial enlightenment                                 |
| 생사결    | **life-and-death duel**                          | Explicitly lethal                                     |
| 중원     | **Central Plains**                               |                                                       |
| 강호     | **martial world**                                | Prefer “Murim” where the setting itself is meant      |
| 가주     | **Family Head**                              |
| 소가주    | **Lesser Family Head**                       |
| 명성               | **Fame**                       |
| 정마대전   | **Great Faction War**         |
| 노부      | **this old man / I**                                            |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 평화 | **Peace Guild** | Guild name. |
| 내상 | **Internal Injury** | System condition label for internal injury. |
| 오대세가 | **Five Great Families** | Major Murim grouping. |
| 하북 | **Hebei** | Province where Hyuk Family Textile Shop has a branch. |
| 전하 | **His Highness** | Formal royal address for the resident prince; the official insists on this form instead of king. |
| 고자 | **eunuch** | Castrated man; Hong Jin openly identifies himself by this term. |
| 세가 | **great family** | Murim category Jin Wikyung hopes the Jin Family will attain. |
| 대초원 | **Great Steppe** | The steppe region from which Temur and Chinggen come. |
| 게르 | **ger** | Traditional nomadic dwelling contrasted with Central Plains wooden buildings. |
| 인내 | **Endurance** | System attribute replacing Toughness. |
| 리치 | **Lich** | Named Monster; fallen archmage and apex undead monster. |
| 강기 | **Force** | Generic manifestation of concentrated martial energy; distinct from Sword Force. |
| 낭중지추 | **needle in a bag** | Idiom meaning exceptional talent eventually reveals itself. |
| 일원 | **One Origin** | Named Tang Clan organizational unit in Tang Sadok's mobilization order. |
| 오대 | **Five Squads** | Named Tang Clan organizational group in Tang Sadok's mobilization order. |
| 장성 | **Great Wall** | Wall used in the discussion of the Outer Lands. |
| 모용세가 | **Murong Family** | One of the Five Great Families, based in Liaoning. |
| 이전 | **Two Halls** | Top-level Murim Alliance organizational grouping. |
| 대전쟁 | **Great War** | The long war that ended after the Great Cataclysm. |
| 사냥개 | **hunting dog** | Jin's demeaning metaphor for Ares personnel who obey Go Jun. |
| 동문 | **East Gate** | One of the Nanman Beast Palace's gates. |
| 균열 | **rift** | The dark rift opening in the cliff behind the Inner Palace. |
| 육부 | **Six Ministries** | The central government ministries. |
| 자무카 | **Jamukha** | Khan of the western grasslands and the steppe army’s practical leader. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 적천강 | 벽력도왕 | rival_martial_master_to_rival_martial_master | Virility Saber King | insulting and taunting | Jeok coins 정력도왕 as a taunting replacement for the established title. |
| 벽력도왕 | 적천강 | rival_martial_master_to_rival_martial_master | Jeok Cheongang | boisterous and hostile-teasing | The Thunderbolt Saber King calls Jeok by name before their argument escalates. |
| 적천강 | 신의 | senior_martial_master_to_physician | Divine Physician | blunt and familiar | Uses 신의 while recognizing Dong Feng’s medical identity. |
| 신의 | 적천강 | physician_to_legendary_martial_master | Sir Jeok | formal-deferential | Uses 적 대협 while thanking and counseling Jeok. |

## Listed compact profiles

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 965
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** He is devoted to medicine and the lives he could not save, yet remains composed and self-effacing under mortal danger.
- **Voice:** He speaks in calm, respectful, self-effacing language, framing mortality through quiet philosophical reflections.
- **Relationships:** Mungyeong is the Divine Physician's true identity, the Slaughter Saint was his Master, and Dong Feng is his Disciple.

### Jeok Cheongang.md

# Jeok Cheongang (적천강)

- **Safe through:** Chapter 955
- **Aliases:** Fire King; eighteenth Sect Leader of the Fire Gate Clan
- **Role:** Jeok Cheongang is the Fire Gate Clan’s current Sect Leader, a legendary martial master who has surpassed the Three Saints, Jin Taekyung’s Master and intended heir’s mentor, and a trusted confidant who occupies the chief seat of the Murim Alliance’s Five Kings Hall.
- **Personality:** Secretive, sharp-eyed, gruff, dryly teasing, and pathologically afraid of water; believes there is no absolute justice and hopes to make good choices while protecting those he still has.
- **Voice:** Sharp and ringing when calling out; otherwise gruff, dryly teasing, blunt, and threatening during interrogation or confrontation.
- **Relationships:** He considers Jin Taekyung his one and only Disciple and says they have shared everything since he accepted him; he warmly regards Ju Hwaran, sees Mae Jonghak as a kindred spirit, recognizes Cheongpung as Mae's grandson and successor, was close to Hong Dao, accepted Jangcheon as a Disciple before he became Jopil, and remains Peng Cheolhu's rival.

### Peng Cheolhu.md

# Peng Cheolhu (벽력도왕)

- **Safe through:** Chapter 966
- **Aliases:** Thunderbolt Saber King
- **Role:** Peng Cheolhu is the Thunderbolt Saber King, a Ten Kings master and Great Hero of the Hebei Peng Family.
- **Personality:** Boisterous, hot-tempered, argumentative, and protective toward those connected to his close friend Hong Dao.
- **Voice:** Loud, blunt, confrontational, and prone to disguising embarrassment or retreat as serious martial instruction.
- **Relationships:** Long-standing rival and friend of Jeok Cheongang; close friend of Hong Dao; protective toward Hong Dao's Disciple Unnamed; father of Peng Cheolyeong.

## Korean source

```text
＃967화



무림인에게 있어 무공이란 저마다 다른 모양을 지닌 지문(指紋)과도 같다.

같은 스승 아래에서 동문수학하며 같은 무공을 사사하고, 정해진 구결에 따라 움직임을 펼치더라도 그 사람의 성향과 신체적 특징에 따라 달라진다.

죽음을 두려워하지 않는 자는 정해진 것 이상으로 과감한 검법을 펼치고, 팔다리의 길이가 짧은 이가 보폭을 넓혀 보법을 펼치는 것처럼.

그리고 그런 의미에서, 지금 이 순간 벽력도왕 팽철후는 묘한 기시감을 느끼고 있었다.

쾅! 쾅! 콰아앙!

맹렬한 충돌음과 함께 쉴 새 없이 뒤섞이는 두 개의 도신.

그 너머로 보이는 침착한 자무카의 얼굴이, 그 움직임 하나하나가 벽력도왕에게는 볼수록 낯설지 않았다.

‘뭐지?’

경지에 오른 무인에게 있어, 생사결(生死決) 도중에 잡념을 떠올리는 것은 해서는 안 되는 금기.

하지만 벽력도왕은 그러한 금기를 범하면서까지 자무카를 주시했고, 마침내 케케묵은 기억 속에 파묻혀 있던 과거의 한 장면을 떠올릴 수 있었다.

‘설마?’

불현듯 크게 뜨여진 두 눈동자.

벽력도왕이 보인 그 찰나의 빈틈을 놓치지 않고, 자무카는 전력을 다해 신월도를 내리그었다.

쾅! 카가가각!

보도(寶刀)라 부르기에 부족함이 없는 두 자루의 도가 맞물리며 섬광을 흩뿌린다.

한 치의 양보도 없는 힘겨루기 속, 벽력도왕은 도신 너머로 비치는 자무카의 얼굴을 깊게 가라앉은 눈빛으로 응시했다.

“어디서 이런 오랑캐 놈이 튀어나왔나 했는데……. 이제 보니 구면이었구먼.”

잠시 침묵하던 자무카가 입을 열었다.

중원과는 한참 동떨어진 서부 초원의 유목민이라면 구사할 수 없는, 능숙하기 그지없는 한어로.

“이제야 기억하는 걸 보니 여전히 머리가 나쁜 모양이군. 벽력도(霹靂刀) 팽철후.”

“벽력도라. 분명 그렇게 불리던 시절이 있었지.”

벽력도왕은 혼잣말처럼 뇌까렸다.

지금의 별호와는 고작 한 글자 차이지만, 그 안에 담겨 있는 세월은 실로 장구한 것이었다.

두 사람이 처음으로 맞닥트린 것은 정마대전이라는 유례없는 대전쟁이 일어나기도 전, 팽철후가 하북팽가의 소가주였던 시절의 일이었으니.

‘설마 했는데, 놈이 그때의 그 오랑캐였다니.’

벽력도왕은 새삼스러운 눈빛으로 자무카를 바라보았다.

자그마치 반세기도 넘게 흘러간, 오래된 기억의 한 조각.

그럼에도 불구하고 현재에 이르러 그 자그마한 조각을 노쇠한 머릿속에서 끄집어 올릴 수 있었던 이유는, 극심한 부상을 입은 와중에도 한 마리의 늑대처럼 날뛰던 젊은 유목민의 모습이 그만큼 인상 깊어서였기 때문이리라.

‘그래, 그랬었지.’

장성을 넘어 국경을 침탈하는 유목민들.

그리고 재물과 고향을 지키기 위해 유목민들에 맞서 싸우는 이들.

이는 대초원과 인접한 변방에서는 늘 있는 일이었고, 팽가라는 거목이 버티고 있는 하북 또한 예외는 아니었다.

다만 두 사람의 만남이 조금 더 특별할 수 있었던 이유는, 혼란스럽던 동부 초원의 실력자로 급부상한 어느 젊은 부족장이 무려 수천에 달하는 전사를 거느린 채 하북을 노렸기 때문이었다.

약탈과 방어가 반복되던 변방에서도 결코 흔치 않았던.

아니, 당시로서도 십여 년 만에 일어난 대규모 침략.

소가주였던 팽철후는 와병(臥病) 중이던 가주를 대신하여 가문을 이끌었고, 사태의 심각성을 인지한 모용세가에서도 자신들의 소가주를 비롯한 정예 일천을 보내어 도왔다.

각각 천하 오대세가의 한 자리씩을 차지한 하북팽가와 모용세가.

거기에 더해 당대 최고의 신진 고수로 떠오르던 두 가문의 소가주들이 이끄는 정예들까지.

정마대전 이전까지만 하더라도 북방의 패자 자리를 놓고 반목하던 두 가문의 극적인 연합은, 그에 걸맞은 결실을 얻어 내기에 충분했다.

한 치의 군더더기도 없던 완승(完勝).

혹은 위대한 대승(大勝).

천하의 그 누구도 이러한 표현을 쓰는 것에 의문을 제기하지 않았다.

그만큼 그들이 거둔 승리는 완벽했고, 팽철후가 이끈 하북팽가에 의해 일패도지(一敗塗地)한 동부 초원의 젊은 부족장은 때맞춰 도착한 모용세가의 추격마저 아슬아슬하게 뿌리치며 사라졌다.

자신을 따르던 수많은 전사들의 핏물만을 남긴 채.

그렇게 영영 자취를 감추었다.

벽력도왕을 비롯한 모든 이가 그렇게 생각했다.

오늘 이 자리에서 다시 맞닥트리기 전까지는.

“지금까지도 살아 있었을 줄이야. 명줄 한번 질긴 놈이로고.”

낭중지추(囊中之錐)라고 했다.

날카로운 송곳 같은 자들은 결국 반드시 튀어나오게 되어 있다.

그 장소가 주머니 안이 아니라 광활한 초원이라 해도.

그러나 끓어오르는 야욕과 그만한 실력을 갖추었던 젊은 부족장은 장장 반세기가 넘도록 모습을 드러내지 않았고, 유목민들은 두 번 다시 하북을 침범하지 않았다.

그것이 벽력도왕이 오랫동안 자무카를 잊고 있었던 이유였다.

제아무리 오랑캐라고는 하나, 그 정도의 실력자가 재기하지 못한 것에는 그만한 사정이 있다고 생각했으니까.

분명 그날에 자신이 입혔던 부상으로 죽음에 이르렀거나, 또 다른 초원의 분란에 휘말려 희생당했을 거라 짐작했다.

그 이유가 무엇이던, 결론은 죽음이었다.

분명 그렇게 생각했었다.

“그때 무슨 수를 써서라도 네놈을, 화근(禍根)을 뿌리 뽑았어야 했는데.”

팽팽하게 맞물린 도신 너머로 나직이 탄식하는 벽력도왕의 모습이, 안광으로 번뜩이는 자무카의 두 눈동자에 고스란히 비쳤다.

“죽을 수 없었다. 묵은 빚을 갚기 전까지는.”

자무카는 씹어뱉듯이 뇌까렸다.

어찌 잊었겠는가. 그 뼈저린 과거를.

패장이 되어 돌아온 그는 살아남은 부족민들과 함께 동부 초원을 떠났고, 수천 리가 넘는 행군 끝에 저 멀리 서쪽 끝자락에 다다라 자신만의 게르를 세웠다.

증오스러운 하북팽가의 깃발이 보이지 않는 곳.

그가 몰락하기만을 기다리던 이리떼의 이빨을 피할 수 있는 그곳에 새롭게 정착하여 재기의 때만을 노렸다.

그렇게 강물처럼 흘려보낸 오십여 년.

실로 많은 것이 바뀌었다.

혹시 모를 추격을 피하고자 얻은 자무카라는 새로운 이름은 어느새 서부 초원의 권위이자 상징이 되었고, 휘하에는 뛰어난 준마와 사냥개 같은 전사들이 우글거렸으며, 수십에 불과했던 게르는 수만 호(戶)로 늘어났으니까.

하지만, 초원의 왕이나 다름없어진 상황에서도 자무카는 잊지 않았다.

자신의 몸뚱어리를 벼락처럼 가로지르던 팽철후의 일도(一刀)를.

치욕스러운 패배를 겪어야 했던 그 날의 기억을.

우우우웅.

대기를 떨어 울리며, 더욱더 몸집을 부풀려 가는 신월도의 녹색 강기.

지금 이 순간 벽력도왕을 향한 자무카의 시선에는, 아직 씻지 못한 과거가 담겨 있었다.

“벽력도. 아니, 벽력도왕 팽철후.”

선조들의 위업을 다시 이루겠다는 야욕을 품었던 젊은 부족장은 초원의 절대자가 되어 대군세(大軍勢)와 함께 돌아왔고, 그의 모든 것을 빼앗아 갔던 하북팽가의 소가주는 정마대전을 거쳐 십왕(十王)의 일인으로, 천하 무림을 지탱하는 거목으로 우뚝 섰다.

그러나 변치 않은 것이 있다면 그건 바로 해묵은 원한이다.

“아직도 모르겠느냐.”

크그그극.

휘황한 녹색 강기에 휩싸인 신월도가 대도(大刀)를 짓누른다.

부르르 떨리는 도신 너머로 침음성을 흘리는 벽력도왕의 모습에 자무카의 입매가 비틀렸다.

“기다렸다. 네놈이, 하북팽가가 이곳에 나타나기만을.”

“……!”

생각지도 못한 한 마디에 벽력도왕이 눈을 부릅뜬 그 순간.

꽈앙!

하늘이 쪼개지는 듯한 굉음과 함께, 거대한 벽과도 같았던 대도가 신월도의 힘을 이기지 못하고 밀려났다.

콰아아아!

광풍이 휘몰아친다.

끔찍한 압력을 이기지 못한 암벽의 일부가 갈라지고 터져나간다.

그러나 사방을 휘감으며 소용돌이치는 먼지구름 속에서도, 자무카의 움직임은 정확하면서도 쾌속했다.

슈확!

궤적을 따라 갈라지는 공간.

초승달처럼 휘어진 신월도를 따라 줄기줄기 뻗어 나온 녹빛 강기가 뒷걸음질 치는 벽력도왕을 향해 쇄도했다.

쾅! 콰앙!

두 자루의 도가 맞부딪히며 터져 나오는 소음은 이미 강철의 영역을 넘어섰다.

시종일관 깊게 가라앉아 있던 자무카의 눈빛은, 입술 사이로 흘러나오는 그의 목소리는 어느새 용암처럼 끓어오르고 있었다.

마치.

“죽여 주마, 모조리!”

뼈아픈 패배로 모든 것을 잃고 떠나야 했던, 과거의 어느 젊은 부족장처럼.

화아아아악!

모든 힘을 다해, 폭발하듯 넘쳐흐르는 녹빛 강기.

마치 이른 시간에 찾아온 서광(曙光)처럼 협곡 내부를 밝히는 그 화려하면서도 강대한 빛줄기가 벽력도왕을 향해 비스듬히 내리그어졌다.

서걱!

번뜩이는 섬광 속에서 울려 퍼진 서늘하기 그지없는 한 줄기 절삭음.

“쿨럭.”

투두둑.

비틀거리며 뒷걸음질 친 벽력도왕이 한 움큼의 핏물을 뱉어내며 자무카를 바라보았다.

한껏 일그러진 주름진 미간은 내상으로 인한 고통의 흔적이었다.

“……대단하군. 진정 대단해.”

비아냥이나 거짓이 아닌, 말 그대로의 진심.

지금 이 순간, 벽력도왕은 한 사람의 무인이자 팽가의 명맥을 이은 투사(鬪士)로서 감탄하고 있었다.

패배를 설욕하기 위해 그토록 기나긴 세월을 버텨 온 자무카의 인내심에. 그 놀라운 무위에.

그리고…….

복수의 완성을 코앞에 두고서도, 마지막까지 이성의 끈을 놓지 않았던 자무카라는 한 인간에 대해.

“어떻게 물러설 생각을 했나? 분명 자네에게는 완벽한 기회였을 텐데.”

찬사받을 만한 용맹과 투지를 선보인 자라면, 설령 그 상대가 적이라 해도 합당한 예의를 갖춰야 하는 법.

그러나 그런 벽력도왕의 물음에 자무카는 대답하지 않았다.

아니, 대답할 수 없었다.

쩌적.

귀를 기울여야만 들을 수 있을, 아주 미세한 균열음과 함께 그의 신월도가 부르르 떨린 다음 순간.

콰앙!

산산조각 나며 허물어지는 강철의 파편 위로, 자무카의 어깻죽지에서 뿜어져 나온 피 분수가 떨어져 내렸다.

푸화악! 투두두둑!

살갗 사이로 터져 나온 핏물은 붉었고, 깊게 베인 어깻죽지와 오장육부에서 치밀어오르는 통증은 벼락처럼, 불길처럼 뜨겁다.

그리고 마치 타들어 가는 듯한 고통 속, 자무카는 비틀거리는 신형을 다잡으며 입을 열었다.

“쿨럭. 어떻, 어떻게…….”

자무카는 좀처럼 이해할 수 없었다.

하북팽가의 무공은 패도(霸道), 그 자체다.

팽가의 일원은 수련을 통해 단련된 힘과 폭발적인 내공심법을 바탕으로 대대로 천하에 명성을 떨쳤고, 그것이 유일한 한계이기도 했다.

그렇기에, 자무카는 오직 극쾌(極快)를 좇았다.

벽력도왕을 쓰러트리기 위해 지난 오십여 년간 극쾌의 도법을 수련했고 그의 무공에 대해 분석했다.

자신이 완성한 쾌속함이, 하북팽가의 패력함을 꺾으리라는 믿음을 가진 채.

하지만.

“왜, 어째서……!”

내상을 추스르며 다가오는 벽력도왕을 향해, 자무카는 핏물이 끓어오르는 목소리로 부르짖었다.

그리고 앞선 질문에 대답하지 못했던 자무카와 달리 벽력도왕은 담담한 얼굴로 입을 열었다.

“정마대전. 그 빌어먹을 전장에서 깨달았지. 세상에는 노부보다 더한 괴물이 많다는 것을.”

깨달음에는 끝이 없다.

발전하는 것은 젊은이들만의 특권이 아니었다.

특히 벽력도왕이라는 별호를 지닌 노강호(老强豪)에게는.

“그중에서도 웬 미친 늙은이가 노부를 농락하며 비웃지 뭔가. 덩치는 곰 같고, 하는 짓은 느려터졌다고.”

화왕(火王) 적천강.

언젠가 그 정신 나간 노괴를 넘어서기 위해, 그는 평화가 찾아온 후에도 수련을 멈추지 않았다.

지난 세월 동안 단 하루도.

“아직도 모르겠나?”

반쯤 잘려나간 어깨를 부여잡은 채 신음하는 자무카를 바라보며, 벽력도왕은 거대한 대도를 곧추세웠다.

“벽력도 팽철후가, 어찌하여 벽력도왕이 될 수 있었는지.”

고작 한 글자 차이.

그러나 이 광활한 천하에서 왕(王)이라 불릴 자격을 얻은 것은, 끝없이 펼쳐진 하늘과 세 개의 별 아래에 우뚝 선 열 명의 위대한 무인뿐이다.

“자네가 왕이라 불릴 수 있는 곳은, 저 초원뿐이야.”

눈을 부릅뜬 자무카를 바라보며, 벽력도왕 팽철후는 소리내어 웃었다.
```

## Final English reading copy

```markdown
# Chapter 967

To a martial artist, martial arts are like fingerprints: no two are quite alike.

Even when disciples study under the same master, learn the same martial arts, and perform the same movements according to the same formulas, their styles differ according to their temperaments and physical traits.

A man who doesn’t fear death might use a sword technique more boldly than prescribed. Someone with short arms and legs might widen their stride when using a footwork technique.

And in that sense, at this very moment, Peng Cheolhu, the Thunderbolt Saber King, was feeling a strange sense of déjà vu.

*BOOM! BOOM! KRAAA-BOOM!*

The two saber blades clashed without pause, accompanied by a barrage of fierce impacts.

Beyond them, Jamukha’s calm face—and each and every one of his movements—seemed more familiar to the Thunderbolt Saber King the longer he watched.

*What is it?*

For a martial artist who had reached a high realm, letting his mind wander during a life-and-death duel was a taboo.

Yet the Thunderbolt Saber King kept his eyes on Jamukha, violating that taboo, until at last he recalled a scene buried deep in the dusty recesses of his memory.

*Could it be?*

His eyes suddenly flew wide.

Jamukha didn’t miss the instant opening the Thunderbolt Saber King showed. He swung his crescent saber down with all his might.

*BOOM! KRRRACK!*

Two sabers worthy of being called treasured blades met, scattering flashes of light.

As their blades strained against each other without giving an inch, the Thunderbolt Saber King looked past them at Jamukha, his gaze sinking deep.

“I wondered where a barbarian like you had come from… Now I see we’ve met before.”

Jamukha fell silent for a moment, then spoke.

His Central Plains language was so fluent that no nomad from the western steppe, so far removed from the Central Plains, should have been able to speak it.

“Now that you finally remember, I see your head’s still as thick as ever, Thunderbolt Saber Peng Cheolhu.”

“Thunderbolt Saber. There was a time when they called me that.”

The Thunderbolt Saber King murmured as if to himself.

It was only one character different from his current title, but the years contained in that difference were vast indeed.

The first time the two had crossed paths was before the unprecedented Great War called the Great Faction War, back when Peng Cheolhu was the Lesser Family Head of the Hebei Peng Family.

*I suspected as much. He’s that barbarian from back then.*

The Thunderbolt Saber King looked at Jamukha with fresh eyes.

It was a fragment of a memory from more than half a century ago.

And yet he could still dredge up that tiny fragment from his aging mind because the young nomad, who had rampaged like a wolf despite his terrible injuries, had left such a powerful impression on him.

*Right. That’s how it was.*

Nomads crossed the Great Wall and invaded the borders.

People stood against them to protect their homes and possessions.

Such things happened all the time along the frontier near the Great Steppe. Hebei, adjacent to the vast grasslands and home to the great tree that was the Peng Family, was no exception.

But what made the two men’s encounter unusual was that a young chieftain, rising to prominence amid the turmoil of the eastern steppe, had led thousands of warriors to attack Hebei.

Even along the frontier, where raids and defenses came in endless cycles, such a thing was far from common.

No—in those days, it was the first large-scale invasion in over a decade.

Peng Cheolhu, then the Lesser Family Head, led his family in place of its ailing Family Head. The Murong Family, recognizing the gravity of the situation, sent a thousand elite fighters, including their own Lesser Family Head, to help.

The Hebei Peng Family and the Murong Family, each occupying a place among the Five Great Families.

And on top of that, the elite forces led by the two families’ Lesser Family Heads, who were emerging as the greatest young masters of their generation.

Before the Great Faction War, the two families had been at odds over supremacy in the north. Their dramatic alliance proved enough to secure a fitting reward.

A flawless victory, without a single misstep.

Or perhaps a glorious triumph.

No one in the world questioned the use of those words.

Their victory had been that complete. The young chieftain of the eastern steppe, thoroughly defeated by the Hebei Peng Family led by Peng Cheolhu, barely evaded the pursuing Murong Family, which had arrived in time, and disappeared.

Leaving behind only the blood of the countless warriors who had followed him.

Just like that, he vanished without a trace.

That was what everyone had believed, including the Thunderbolt Saber King.

Until they met again here today.

“I never thought you’d still be alive. You sure have a stubborn hold on life.”

They said a needle in a bag would eventually poke through.

Those as sharp as needles would inevitably reveal themselves.

Even if the bag wasn’t a bag at all, but the vast steppe.

Yet the young chieftain, with ambition to match his skill, had not shown himself for more than half a century. The nomads never invaded Hebei again.

That was why the Thunderbolt Saber King had forgotten Jamukha for so long.

Barbarian though he was, the man had been skilled enough that there must have been some reason he hadn’t risen again.

The Thunderbolt Saber King had assumed that his injuries from that day had killed him, or that he had fallen victim to another conflict on the steppe.

Whatever the reason, the conclusion was the same: he was dead.

That was what he had believed.

“I should’ve done whatever it took to root you out back then—to tear out the source of this trouble.”

Beyond their locked blades, the Thunderbolt Saber King let out a quiet sigh. His figure was reflected in Jamukha’s gleaming eyes.

“I couldn’t die. Not before I repaid an old debt.”

Jamukha spat the words out.

How could he forget that bitter past?

Defeated, he had left the eastern steppe with the surviving members of his tribe. After marching for thousands of li, he reached the distant western edge and raised a ger of his own.

A place where he couldn’t see the hated banners of the Hebei Peng Family.

A place where he could escape the wolves waiting to tear him apart if he fell—and where he could settle anew and wait for his chance to rise again.

Fifty years had flowed by like a river.

So much had changed.

The new name he had taken to avoid a possible pursuit—Jamukha—had become a symbol of authority across the western steppe. His ranks teemed with fine steeds and warriors like hunting dogs. The few dozen gers he had started with had grown into tens of thousands of households.

But even after he had become all but the king of the steppe, Jamukha had never forgotten.

Peng Cheolhu’s saber, which had torn through his body like a bolt of lightning.

The memory of the day he had suffered that humiliating defeat.

*Wooooom.*

The green Force of the crescent saber vibrated through the air as it swelled larger and larger.

At this moment, Jamukha’s gaze on the Thunderbolt Saber King held the past, still unavenged.

“Thunderbolt Saber. No—Thunderbolt Saber King Peng Cheolhu.”

The young chieftain, once driven by the ambition to restore his ancestors’ achievements, had returned as the absolute ruler of the steppe, leading a mighty army. The Lesser Family Head of the Hebei Peng Family, who had taken everything from him, had risen through the Great Faction War to become one of the Ten Kings, a great tree that held up the martial world.

But one thing had never changed: their old grudge.

“Do you still not understand?”

*Krrrrk.*

The crescent saber, engulfed in radiant green Force, pressed down on the great saber.

The Thunderbolt Saber King groaned as his blade trembled. Jamukha’s lips twisted.

“I waited. I waited for you—for the Hebei Peng Family—to show up here.”

“……!”

The Thunderbolt Saber King’s eyes flew wide at the unexpected words.

*KA-BOOM!*

With a thunderclap that seemed to split the sky, the great saber—until then like a colossal wall—was forced back, unable to withstand the crescent saber’s power.

*KRAAAASH!*

A gale swept through.

Part of the rocky cliff cracked and burst apart under the terrible pressure.

Yet even amid the dust clouds swirling all around him, Jamukha moved with precision and speed.

*Shwaa!*

Space split along the saber’s path.

Green Force streamed from the crescent-shaped blade and surged toward the Thunderbolt Saber King as he retreated.

*BOOM! BOOM!*

The roar of the two sabers colliding had already gone beyond the realm of steel.

Jamukha’s gaze, which had been so deeply composed throughout, and his voice, slipping between his lips, were now boiling like lava.

Just like—

“I’ll kill every last one of you!”

—some young chieftain from long ago, forced to leave after losing everything in a bitter defeat.

*FWOOOSH!*

Green Force erupted in a burst, overflowing with all his strength.

Like the first light of dawn arriving early, that dazzling, mighty beam illuminated the gorge as it slashed diagonally toward the Thunderbolt Saber King.

*Shhk!*

Amid the brilliant flash, a single, chilling sound of a blade cutting through flesh rang out.

“Cough.”

*Thud, thud.*

The Thunderbolt Saber King stumbled backward, spat out a mouthful of blood, and looked at Jamukha.

His deeply furrowed brow was twisted with pain from his internal injuries.

“…Impressive. Truly impressive.”

There was no sarcasm or pretense in his words. He meant them.

At this moment, the Thunderbolt Saber King was admiring him as a martial artist, and as a warrior who had carried on the Peng Family’s legacy.

Jamukha’s patience, which had endured such a long stretch of time in order to avenge his defeat.

His astonishing martial prowess.

And…

Jamukha himself—a man who had held on to his reason until the very end, even with revenge almost within reach.

“How did you think to pull back? You had the perfect chance.”

Even an enemy deserved proper respect if he had shown courage and fighting spirit worthy of praise.

But Jamukha didn’t answer the Thunderbolt Saber King’s question.

No—he couldn’t answer.

*Crack.*

A faint fracture, so slight it could only be heard if you listened closely. The crescent saber trembled, and in the next instant—

*KA-BOOM!*

—his crescent saber shattered into pieces. Blood spraying from Jamukha’s shoulder blade rained onto the steel fragments.

*FWASH! THUD-THUD-THUD!*

The blood that burst through his skin was red. The pain from his deeply cut shoulder and his internal organs surged up like lightning, hot as fire.

Amid that searing agony, Jamukha steadied his staggering body and spoke.

“Cough. How—how did you…”

Jamukha couldn’t understand.

The martial arts of the Hebei Peng Family were the very embodiment of domineering power.

For generations, the family had made its name throughout the world through strength honed by training and cultivation techniques that produced explosive internal energy. That reliance was also its one limitation.

That was why Jamukha had pursued only speed.

For the past fifty years, he had trained in saber techniques of the utmost speed and analyzed the Thunderbolt Saber King’s martial arts, all to bring him down.

He had believed that the speed he perfected would overcome the Hebei Peng Family’s overwhelming strength.

But…

“Why? How…!”

As the Thunderbolt Saber King approached, steadying himself despite his internal injuries, Jamukha cried out, his voice thick with blood.

Unlike Jamukha, who couldn’t answer the question he’d been asked earlier, the Thunderbolt Saber King replied with a calm expression.

“The Great Faction War. I realized it on that damn battlefield. There are plenty of monsters in this world even worse than this old man.”

There was no end to enlightenment.

Progress wasn’t a privilege reserved for the young.

Especially not for an old master like the Thunderbolt Saber King.

“Among them, there was this crazy old man who toyed with me and laughed at me. Said I was built like a bear and moved like molasses.”

The Fire King, Jeok Cheongang.

To surpass that deranged old monster someday, he had never stopped training—even after peace returned.

Not for a single day in all those years.

“Still don’t understand?”

The Thunderbolt Saber King straightened his massive great saber as he looked at Jamukha, clutching his half-severed shoulder and groaning.

“How Peng Cheolhu, the Thunderbolt Saber, became the Thunderbolt Saber King?”

It was the difference of only one character.

But in this vast world, only ten great martial artists had earned the right to be called kings—standing tall beneath the endless sky and three stars.

“The only place you can be called a king is out there on the steppe.”

Looking at Jamukha, whose eyes were wide with shock, Peng Cheolhu, the Thunderbolt Saber King, laughed aloud.
```
