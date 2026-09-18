<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0387.txt",
      "sha256": "027b3f02abdb7e83b2ae6bb9cd2f61b9ba8132439e2cf03e0283c76757518183",
      "bytes": 13996
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "3de7f714b38702a7d81f8113ffc57983cd5eda668e851676548f8832ba61a744",
      "bytes": 3942
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "e624c1a27f5f8a896bce426e1f41773adca3f1f660fa708733b95c585296ec64",
      "bytes": 134201
    },
    {
      "path": "characters/Lee Jungryong.md",
      "sha256": "ef494de0cc1bfefb46cba77d8c04f6bc8ffd94e36789721f3bc5f48bd212c2ce",
      "bytes": 1396
    },
    {
      "path": "characters/Wu Heixing.md",
      "sha256": "f5aafc76f5e336a3c3d07152391e83c6396e60e8187de1745bd19d13ce5796c5",
      "bytes": 562
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "908c68b1f003c3584b707856c0bc2bbdf69088b53766c02aa14cc191decd4d63",
      "bytes": 109463
    }
  ],
  "estimated_tokens": 10097
}
-->

# Durable State Update — Chapter 387

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 387. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 387. Profile updates may replace only one
complete line in Aliases, Role, Personality, Voice, or Relationships. Do not
return Safe through updates; the controller sets that field automatically.
Each profile field should be one concise sentence; never append semicolon-separated
chapter history.
`names` contains only newly required Korean-to-English rows that are absent from
Exact glossary matches; Korean keys must occur in the source. Do not repeat
glossary matches. The controller drops rows already in the names ledger.
`address_pairs` contains only newly required speaker→addressee rows that are
absent from Matched address pairs. Speaker and addressee must be Hangul source
spellings such as 진태경 or 혁무진, never English names. Arabic digits are
allowed in titles such as 1팀장. At least one endpoint must occur in the source.
The controller drops pairs already in the address ledger. Do not invent
risk-register rows. Beat plot paragraphs are plain strings; continuity and
translation decisions are concise list items.
Return this exact shape:

{
  "chapter": 387,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 387,
    "continuity_sources": [387],
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

## Prior durable context

```json
{
  "active_continuity": [
    "Jin Taekyung is Level 121, has the Undead Hunter Title, and keeps the strengthened Skeleton Warlord in his Inventory under the mocking name Bones.",
    "Jin Taekyung has crossed the wall into true mastery, while Choi Minwoo has become substantially stronger and more refined.",
    "The Arch Lich's three incomplete Liches were destroyed at Chengdu International Airport, and their testimony identified the Arch Lich as responsible for the undead army's actions.",
    "Wei Fenghu is China's Minister of National Defense under the Central Military Commission, a four-star general, and the current Chairman's right-hand man; he raised Lei Fei as his own son and asked Jin to bring him back if found.",
    "Sichuan Province remains in a wartime emergency involving magical communications interference, flying-monster attacks, and a Monster Wave that has caused at least hundreds of thousands of casualties; the dead may have been raised as undead.",
    "China has concealed at least one of its S-rank Hunters, Lei Fei, who disappeared with his department's Hunters when the first Monster Wave began and remains unconfirmed dead or alive.",
    "The temporary operations headquarters is at Mount Qingcheng, where international S-rank Hunters are gathered, including Magic Johnson and Faye Chen.",
    "Shao Yang is Chairman of the People's Republic of China, Chairman of the Chinese Communist Party's Central Military Commission, and General Secretary; he retains authority over China's crisis response while asking Hunters to prioritize human lives.",
    "Faye Chen is an older S-rank Hunter and Great Cataclysm hero with a former film career, a low media profile, and a playful but composed manner toward Jin.",
    "Wu Heixing is an S-rank Hunter whose arrogance and hostility toward Jin have escalated into a public confrontation; he nearly drew his sword before the interruption.",
    "Prince Felix Alexander Louis is a British royal third in line to the throne who patronizes Jin as lowborn while claiming that all people are equal beneath God.",
    "Lee Jungryong is the de facto head of the Ares Guild and one of the world's three strongest S-rank Hunters; he has recognized Jin's breakthrough and is visibly unsettled by it, while the six S-rank Hunters prepare for deployment in six directions."
  ],
  "continuity_sources": [
    386,
    385
  ],
  "open_questions": [
    "Who is the Arch Lich, and what will happen after Jin Taekyung destroys its three servants?",
    "What happened to Lei Fei and the Hunters who disappeared with him?",
    "What happened to the Second Fiend assigned to the Qingcheng attack?",
    "Who is the unidentified person directing Aehyang, and what are they planning?",
    "Who used Sound Transmission to summon Jin Taekyung after the war council, and why?"
  ],
  "safe_through": 386,
  "temporary_decisions": [
    "Render 열화신룡 as Blazing Flame Divine Dragon, distinct from Huashan Divine Dragon; use Mimi and Mimi-chan for 미미 and 미미쨩, and Third Fiend and Three Fiends for 삼괴.",
    "Render 진인 as Perfected One, 도우 as Fellow Daoist, 신니 as Venerable Nun, 환영진 as illusion formation, and 이동진 as Moving Formation; use Archmage and War Mage for 대마법사 and 워 메이지.",
    "Render 독룡각 as Poison Dragon Pavilion, 가주 대행 as Acting Family Head, 화룡갑 as Fire Dragon Armor, and 공안무력부 as Public Security Armed Forces Department.",
    "Render 사기 as death energy, 의념 as conveyed thoughts, 데스나이트 as Death Knight, 골골 as Bones, and 아크 리치 as Arch Lich.",
    "Render 시벌좌 as Lord Fuck, 반도의 빵즈 as peninsula bangzi, 짱깨 as chink, 주석 동지 as Chairman Comrade, and 전하 as His Highness; preserve Jin's vulgar historical and cultural jokes, and use General Liao, Crown Prince Party, and Shanghai Gang for this chapter."
  ],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 이정룡    | **Lee Jungryong** |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 내공     | **internal energy**                              |                                                       |
| 열양지기   | **Scorching Yang Qi**                            | Fire-aligned qi                                       |
| 심법     | **cultivation technique**                        | Especially internal cultivation                       |
| 검법     | **sword technique**                              |                                                       |
| 전음     | **Sound Transmission**                           | Fixed skill terminology; preserve the internal-energy mechanism when the source explains it, but do not add an explanation where it does not |
| 장비               | **Equipment**                  |
| 습득               | **Acquired**                   |
| 매력               | **Charm**                      |
| 헌터      | **Hunter**            |
| 레이드     | **raid**              |
| 길드      | **Guild**             |
| 팀장      | **Team Leader**       |
| 마법사     | **mage**              |
| 대격변     | **Great Cataclysm**   |
| 사천     | **Sichuan**            |
| 공자      | **Young Master**                                                |
| 우헤이싱 | **Wu Heixing** | Chinese S-rank Hunter who provokes Jin and nearly draws his sword. |
| 아레스 | **Ares Guild** | The leading Guild in Korea; formerly employed Team Leader Choi and Song Song. |
| 아줌마 | **ajumma** | Familiar term for a middle-aged or married woman, used for Kim Jeonghee |
| 검강 | **Sword Force** | Higher manifestation than Sword Energy; Pung Yang's is explicitly imperfect because of insufficient enlightenment. |
| 주신 | **God of Drinking** | Wipeng's drinking epithet. |
| 전하 | **His Highness** | Formal royal address for the resident prince; the official insists on this form instead of king. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 권각술 | **fist-and-foot martial arts** | Unlearned martial-arts category referenced by the System. |
| 마도 | **Demonic Path** | Term raised for martial power that appears to defy common principles. |
| 존슨 | **Johnson** | Co-host of the American talk show that replays Taekyung's viral interview. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 마법사 | 이정룡 | Ares Guild mage subordinate to Vice Guild Master | Vice Guild Master | formal-deferential | Lee's five direct A-rank mages greet him and receive instructions for concealing the battle. |
| 우헤이싱 | 이정룡 | younger S-rank Hunter to senior Ares Guild authority | Mr. Lee | formal and deferential | Wu addresses Lee respectfully despite his usual hostility toward Koreans. |
| 필릭스 | 이정룡 | British prince to senior S-rank Hunter | Jungryong Lee | formal through a translation device | Felix permits Lee to omit His Highness and gives his own preferred form of address. |

## Listed compact profiles

### Lee Jungryong.md

# Lee Jungryong (이정룡)

- **Safe through:** Chapter 386
- **Aliases:** None
- **Role:** Vice Guild Master of Ares Guild; one of Korea's two S-rank Hunters; effective wielder of Ares Guild's authority in place of its Guild Master; Supreme Peak-level martial artist; gave Park Jihoon his initial orders and is Jihoon's master; visited the Peace Guild's hospital after Taekyung demanded an apology, brought compensation, and demanded the captives after negotiations.
- **Personality:** Outwardly genial, calm, and humorous; calculating, manipulative, coercive, and ruthless when challenged
- **Voice:** Smooth, good-natured, and indirect, using teasing conversation and veiled threats before becoming openly furious
- **Relationships:** Master of Park Jihoon and Go Jun (Team Leader Seok), whom he personally selected and trained; longtime Great Cataclysm acquaintance of Park Tae Seop; adversary of Jin Taekyung; knew Team Leader Choi from childhood; has an antagonistic history with Kim Hwajong, who saved his life at the collapse of Mapo Bridge eighteen years earlier; was visibly shaken by learning that Choi is Cheon Taemin's maternal grandson; regards Cheon Taemin as an older brother despite no blood relation and has long held him in respect and fear; operates as Ares Guild's senior authority beneath its Guild Master

### Wu Heixing.md

# Wu Heixing (우헤이싱)

- **Safe through:** Chapter 386
- **Aliases:** None
- **Role:** Wu Heixing is a Chinese S-rank Hunter known for frequent media exposure and a reputation for scandal.
- **Personality:** Arrogant, status-conscious, abusive, and quick to anger when humiliated.
- **Voice:** Loud, insulting, entitled, and dependent on national and political status.
- **Relationships:** He is openly hostile toward Jin Taekyung and resents Jin receiving Chairman Shao Yang's attention.

## Korean source

```text
＃387화



지하 벙커를 빠져나왔을 때는 이미 깊은 밤이었다.

크게 숨을 들이쉬자 차가운 공기가 폐부로 스며든다. 저 어딘가에 있을 무림의 사천을 떠올리며 별이 총총히 박힌 밤하늘을 바라보고 있는데, 자그마한 손이 어깨를 톡 건드렸다.

「따라올래? 가볍게 한잔할 생각인데.」

“지금요?”

「응. 우리끼리.」

파이 첸이다. 그녀의 등 뒤에는 ‘우리’에 속한 두 사람이 서 있었다.

그중 하나가 기품이 넘쳐흐르는 말투로 입을 열었다.

「동양의 귀부인이여, 혹 함께 마실 술 중에 로마네콩티가 있는가?」

「귀부인은 아닌데, 당연히 있지. 술 좋아해, 왕자?」

필릭스 왕자가 못마땅한 얼굴로 대답했다.

「왕자가 아니라 필릭스 전하라고 부르라니까. 그리고 술은 적당히 즐기는 편이다. 특히 로마네콩티 45년 산을.」

「45년 산은 없는데.」

「그럼 거절하지. 난 이만.」

저거 진짜 미친놈인가.

필릭스 왕자가 수행원들을 이끌고 사라지자 파이 첸이 남은 한 사람을 향해 고개를 돌렸다.

「당신은 갈 거지. 존슨?」

매직 존슨이 새하얀 이빨을 드러내며 웃었다.

「미안하군. 아쉽지만 다음으로 미뤄야 할 것 같아.」

「왜?」

「당장 내일 전선에 투입될지도 모르는데, 메모라이즈(Memorize) 정도는 해 둬야 마음이 편할 것 같아서.」

역시 대마법사. 대격변의 영웅은 괜히 되는 게 아니구나.

매직 존슨의 마음가짐에 깊은 감명을 받은 내가 입술을 뗐다.

“저도 지금은 안 될 것 같은데요.”

「안 돼.」

“왜요?”

「넌 왕자도 아니고, 대마법사도 아니잖아.」

“……아니, 그런 게 어딨어요.”

어이가 없네. 말도 안 되는 강짜를 놓는 건 둘째치고 이런 판국에 술을 마시자는 저 아줌마도 정말 어지간하다.

「너, 방금 속으로 내 욕했지? 이런 상황에서 술이나 마시는 생각 없는 아줌마라고.」

“……어떻게 알았어요?”

「어머, 얘 쓸데없이 솔직한 것 좀 봐라?」

파이 첸이 긴 손가락으로 내 코끝을 쿡 찔렀다. 외관만 보면 20대 초반의 미인인데, 실상은 어머니보다 나이 많은 사람이라 그런지 기분이 묘하다.

“다른 사람 찾아보시는 게 어때요? 이정룡 씨라거나…….”

「리(Lee)?」

파이 첸의 고개가 살짝 기울어졌다. 이정룡은 이미 자신이 데려온 아레스 길드원들과 사라진 지 오래였다.

「흠. 뭔가 어려운 사람이라서. 대격변 때만 해도 저 정도는 아니었는데 능구렁이가 다 됐어. 무슨 생각을 하는지 알 수가 없다니까.」

사람 보는 눈이 상당히 정확한데.

파이 첸은 저 멀리 사라지는 또 다른 후보를 힐끗 곁눈질하며 말을 이었다.

「우헤이싱. 쟤는 너무 예의가 없고. 같이 마시면 술맛 떨어져.」

나는 인적 드문 숲속으로 향하는 우헤이싱의 뒷모습을 물끄러미 바라보며 대답했다.

“어쩔 수 없네요. 다음에 드시는 수밖에.”

「아니. 술은 이런 날에 마시는 거란다.」

“……?”

「마지막이 될지도 모르잖니.」

“아.”

파이 첸이 왜 술을 찾는지, 어느 정도 알 것 같았다.

전쟁은 사람을 지치게 만든다. 동시에 죽음이라는 방식으로 예측하지 못한 이별이 찾아오기도 한다.

대격변을 통해 수많은 동료를 잃었던 그녀만의 전야제(前夜祭)인 셈이다.

당장 이번 사태가 마무리되었을 때, 우리 중 누군가는 영영 돌아올 수 없는 강을 건넜을 수도 있으니까.

「뭐, 어쨌건 이렇게 된 이상 표적을 바꾸는 수밖에 없네. 안 그래, 거기 잘생긴 총각?」

“저 안 간다니까요.”

파이 첸이 어처구니없는 표정으로 나를 바라봤다.

「양심이 없니? 너 말고 저 청년 말이야.」

파이 첸에게 지목당한 잘생긴 총각, 최 팀장은 내 예상과 다르게 흔쾌히 고개를 끄덕였다.

“불러 주신다면 저야 영광입니다.”

“어, 팀장님. 진짜 가시게요?”

“가야죠. 파이 첸과 함께 술자리를 가질 기회가 언제 또 오겠습니까. 궁금한 것도 많고요.”

파이 첸이 까르르 웃었다.

「잘생긴 줄만 알았는데 말도 예쁘게 하네. 그래, 뭐가 그렇게 궁금하니?」

“혹시 지금 착용하고 계신 장비. 어디서 구매하신 겁니까?”

「……그게 질문이야?」

“예.”

「얘도 만만치 않네.」

한숨을 푹 내쉬는 파이 첸을 보며 매직 존슨이 호탕한 웃음을 터트렸다.

「하하. 미스 첸, 그럼 이제 다 같이 한잔하러 갈까?」

「다 같이? 존슨 당신 안 간다고 하지 않았어?」

「그랬지. 여자랑 단둘이 술 마시는 취미는 없거든. 하지만 여기 있는 미스터 최처럼 매력적인 남자가 동석한다면 이야기는 달라지지.」

「…….」

「난 남자가 좋아. 특히 동양인 남자.」

「그, 그래. 가자.」

역시 타임지가 선정한 세상에서 가장 영향력 있는 성소수자 1위답다.

나는 바짝 굳은 채 끌려가는 최 팀장에게 전음을 날렸다.

- 무슨 일 생기면 연락해요.

도살장에 끌려가는 소처럼 슬픈 눈으로 나를 바라본 최 팀장이 두 S급 헌터와 함께 사라지고, 주위를 둘러본 나는 발걸음을 옮겼다.

‘이 방향이었지.’

사람들의 눈을 피해 어두컴컴한 오솔길을 얼마나 걸었을까. 컴컴한 어둠 속에 멈추어 서서 입을 열었다.

“나와.”

잠깐의 침묵 후, 누군가의 목소리가 흘러나왔다.

「……제법이군.」

부스럭.

인기척과 함께 나타난 한 사람, 우헤이싱이 나를 위아래로 훑었다.

「어떻게 알았지?」

저걸 말이라고. 나는 심드렁하게 대꾸했다.

“차라리 일 더 하기 일이 뭐냐고 물어봐라. 그게 더 어렵겠다.”

「음. 생각보다 실력 있는 놈이었군.」

“이제 와서 칭찬하는 척하지마. 개수작 부리려는 거 뻔히 보이니까.”

「……!」

정곡을 찔린 우헤이싱의 얼굴이 붉게 달아올랐다.

어떤 의미에서는 참 다루기 쉬운 놈이다. 서른 중반이 넘은 나이로 알고 있는데 저렇게 단순하기도 힘들다.

「그, 그게 아니라 나는 진심으로…….」

“진심으로 빵즈라고 생각하겠지. 아직 정식 S급 헌터도 아닌 웬 한국놈이 너 대신 주목받으니까 짜증 났을 거고. 특유의 일차원적인 행동으로 시비부터 걸고 봤는데, 이게 영 반응도 안 좋고 저 빵즈 놈도 생각 외로 만만치가 않네?”

나는 대꾸할 틈도 주지 않고 속사포처럼 말을 이었다.

“그래서 괜히 마음에도 없는 칭찬 몇 번 날려 주고, 우호적인 제스처 취하면서 뭔가 수작을 부리려는 것 같은데…… 아, 혹시 지금까지 내가 말한 것 중에 틀린 부분 있냐?”

「…….」

“그래, 너 같은 놈 많이 봤다. 뒤통수를 하도 처맞았더니 안 돌아가던 머리가 휙휙 돌아가더라.”

한심한 눈빛으로 바라보자, 얼굴이 벌겋게 달아올라 있던 우헤이싱이 더듬더듬 입을 열었다.

「다른 수작을 부리려던 건 아니었다.」

“아니면? 혹시 나랑 친해질 생각이면 곱게 접어서 넣어 둬라. 똥 옆에 있으면 나한테까지 냄새 배니까.”

「……!」

“그런데 너 지금 뭐 하냐?”

내 나직한 한마디에, 검파를 향해 움직이던 놈의 손이 우뚝 멈췄다.

“뽑지 마라. 다친다.”

갈등 어린 눈빛으로 날 바라보던 우헤이싱이 불쑥 입을 열었다.

「어차피 다 알고 있었으면서…… 왜 순순히 따라온 거지?」

“물어볼 게 있어서.”

「뭐?」

난 우헤이싱의 눈동자를 똑바로 직시하며 입을 열었다.

“전음(傳音). 맞지?”

「……!」

딱딱하게 굳은 얼굴이 곧 대답이다. 설마 했는데, 나는 뒷머리를 긁적이며 중얼거렸다.

“맞나 보네. 하긴, 본토니까 여러 가지 무공이 남아 있을 수도 있겠지. 내공심법이라던가.”

「무, 무슨 소리! 그건 메시지 마법…….」

“얼씨구.”

황급히 변명을 늘어놓는 녀석의 모습에 실소가 흘러나왔다.

무공을 접하지 못한 다른 사람들은 차이점을 구분할 수 없겠지만, 나까지 속일 수는 없다.



‘잠깐 나 좀 보지.’



회의가 끝날 무렵 귓가에 닿은 것은 분명 전음이었다.

무시할 수도 있었던 제의에 응했던 이유는, 전음을 보낸 장본인이 바로 우헤이싱이었기 때문이다.

「네, 네놈이 그걸 어떻게.」

“왜, 아무도 모르는 비밀이었어?”

나는 당황하는 우헤이싱을 물끄러미 바라보며 입을 열었다.

“어느 정도 가능성은 있다고 생각하긴 했는데, 확실히 신기하긴 하네. 너희 문화 대혁명이다, 뭐다 해서 무술인들 싹 다 조져 놓지 않았었냐? 그 와중에도 용케 무공이 남아 있었네.”

「주둥이 닥쳐!」

“아, 너 집안 빵빵하다고 했었지. 그럼 공산당 최고위층이 직위를 이용해서 슬쩍 빼돌린 건가?”

「…….」

순식간에 착 가라앉은 표정을 보니 맞는 것 같다.

엄연한 외국인인 나로서는 이게 얼마나 큰 문제인지는 잘 모르겠지만, 내공심법. 즉 현대에 이르러 마나 연공법이라 불리는 이것의 가치가 어느 정도인지 알고 있다.

‘이곳이 무림이었다면, 한바탕 피바람이 일었겠지.’

그렇게 몰래 빼돌린 금송아지를 들켰으니, 놈의 반응이 좋지 않은 것은 당연했다.

「방금 했던 말, 두 번 다시 발설하지 않는 것이 좋을 거다.」

“딱히 할 생각은 없었는데, 말투가 상당히 띠껍네.”

우헤이싱이 표독스러운 눈빛으로 나를 노려보았다.

「내 아버지가 누군지 안 후에도 네놈이 이런 식으로 나올 수 있을까?」

“네 아버지가 누군진 모르겠고, 홍위병 출신이었을 것 같긴 한데.”

「……!」

“소싯적에 오함마 들고 공자 묘 때려 부순 게 너희 아버지 아니냐?”

「이 빵즈 새끼가-!」

파팟!

분기탱천한 고함과 함께 놈의 신형이 쏘아졌다.

어느새 검집에서 뽑혀 나온 직검(直劍)에서 솟구친 오러 블레이드, 아니 검강이 내 목을 노리고 날아든다.

쉬이이이잉!

시원한 바람에 머리카락이 흩날렸다. 바닥에 닿을 만큼 허리를 젖혀 검강을 피해 낸 나는, 몸을 튕기듯 일어나며 무릎으로 놈의 턱을 쳐올렸다.

콰직!

허공으로 솟구치는 치아와 핏물. 순간 비틀거리는 놈의 두 팔을 움켜잡고 귓가에 속삭였다.

“그 검. 뽑지 말랬지.”

치이이익, 우두둑!

「크아아아악!」

양손에 실린 강대한 열양지기가 갑옷을 부수고 살을 태운다.

우헤이싱의 입술 사이로 뛰쳐나온 비명은 내가 펼쳐 놓은 기막(氣幕)에 가로막혀 나아가지 못했다.

「노옴!」

후우우웅!

이놈, 권각술(拳脚術)까지 익혔다. 허접한 검법과는 달리 이건 제법 예리하다.

물론…….

‘무림이랑 비교하면 무공의 질이 훨씬 떨어져.’

나는 약간의 실망을 느끼며 손을 뻗었다.

꽈앙!

공력과 공력의 격돌.

내 허리를 향해 채찍처럼 휘둘러진 놈의 다리는 더 이상 나아가지 못했다.

우헤이싱의 눈동자가 충격과 경악으로 파르르 떨렸다.

「어, 어떻게?」

“잘.”

발목을 덥석 붙잡은 나는 땅을 향해 있는 힘껏 놈을 패대기쳤다.

후우웅, 콰앙!

한 번 더.

후우우웅, 쾅!

더, 더, 더.

쾅! 쾅! 콰과광!

땅이 뒤집히고 바위와 나무가 뽑혀 나간다.

잠시 후 생체 곡괭이질이 멈췄을 때는, 혼이 빠져나간 듯한 우헤이싱이 커다란 크레이터 안에 대자로 뻗어 있었다.

“그래도 몸은 튼튼해서 별로 안 다쳤네.”

「흐, 흐어…….」

“야, 우냐?”

「흐어어어…….」

아주 정신이 나갔군.

혀를 차며 허리를 굽힌 나는 놈의 주머니를 뒤졌다.

공간 확장 마법이 걸린 주머니를 얼마나 헤집었을까, 마침내 원하던 물건을 찾을 수 있었다.

“아, 여기 있네. 상급 포션.”

띠링.



- [최상급 포션]을 습득하셨습니다!



“……이 아니라. 최상급 포션? 뭐야, 이 새끼.”

나는 놀란 눈으로 뻗어 있는 우헤이싱을 바라봤다. 아무리 S급 헌터라지만 이런 물건을 들고 다니다니.

상급 포션도 희귀하지만, 최상급 포션은 일 년에 한두 개 나올까 말까 하는 물건이다.

현실감조차 들지 않는 가격은 둘째치고, 희소성이 너무 높은 탓에 돈이 있어도 못 구한다.

‘인터넷에서나 보던 걸 여기서 보네.’

잠시 고민하던 나는 최상급 포션을 슬쩍 인벤토리에 집어넣었다. 그리고 놈의 주머니를 뒤져 상급 포션 하나를 찾아내 부어 주었다.

“합의금 챙겼으니까 이쯤에서 봐준다. 너도 켕기는 거 많으니까 오늘 일 어디 가서 떠들면…… 알지?”

「흐으, 흐으으으…….」

“오케이. 우리 합의 본 거야.”

깔끔하게 사태를 마무리한 그때, 주머니에 넣어 둔 휴대폰이 부르르 몸을 떨었다.

최 팀장으로부터 짤막한 문자 한 통이 와 있었다.



〈 최 팀장님



최 팀장님

지ㄴ태경시제발빠ㄹ리 와주세요



“…….”

안 돼, 존슨.
```

## Final English reading copy

```markdown
# Chapter 387

It was already deep into the night by the time we left the underground bunker.

I drew in a deep breath, and cold air seeped into my lungs. As I gazed up at the star-filled night sky, thinking of Sichuan in the Murim somewhere out there, a small hand tapped me on the shoulder.

“Coming with me? I’m thinking of having a light drink.”

“Now?”

“Yeah. Just us.”

It was Faye Chen. Two of the people included in that “us” stood behind her.

One of them spoke in a voice overflowing with dignity.

“Lady of the East, might there be any Romanée-Conti among the wine we shall share?”

“I’m no noblewoman, but of course I have some. Do you like wine, Prince?”

Prince Felix answered with a displeased expression.

“I told you to call me His Highness Felix, not Prince. And I enjoy wine in moderation. Especially the 1945 Romanée-Conti.”

“I don’t have the 1945 vintage.”

“Then I must decline. I shall be leaving.”

Was this guy actually insane?

As Prince Felix disappeared with his attendants, Faye Chen turned toward the one person left behind.

“You’re coming, right, Johnson?”

Magic Johnson grinned, baring his snow-white teeth.

“I’m sorry. Unfortunately, I think I’ll have to put it off until next time.”

“Why?”

“I might be deployed to the front tomorrow, so I’d feel more at ease if I at least prepared my spells with Memorize.”

As expected of an Archmage. Heroes of the Great Cataclysm didn’t become heroes for no reason.

Deeply impressed by Magic Johnson’s attitude, I opened my mouth.

“I don’t think I can go right now either.”

“No.”

“Why not?”

“You’re neither a prince nor an Archmage.”

“……That’s not how this works.”

Unbelievable. Leaving aside the fact that she was throwing around such unreasonable demands, that ajumma was something else for wanting to drink in a situation like this.

“You just cursed me in your head, didn’t you? You called me a clueless ajumma who only thinks about drinking in a situation like this.”

“……How did you know?”

“Oh my, look at how pointlessly honest this boy is.”

Faye Chen poked me on the tip of the nose with one long finger. She looked like a beautiful woman in her early twenties, but in reality, she was older than my mother, which gave me a strange feeling.

“How about you find someone else? Mr. Lee, perhaps……”

“Lee?”

Faye Chen tilted her head slightly. Lee Jungryong had disappeared a long time ago with the Ares Guild members he had brought with him.

“Hmm. He’s a difficult person somehow. He wasn’t like that during the Great Cataclysm, but he’s become such a slippery snake. You can never tell what he’s thinking.”

She had an excellent eye for people.

Faye Chen cast a sidelong glance at another candidate disappearing in the distance before continuing.

“Wu Heixing. He’s far too rude. Drinking with him would ruin the taste.”

I gazed blankly at Wu Heixing’s back as he headed into the secluded forest and answered.

“Nothing we can do, then. You’ll have to drink another time.”

“No. These are exactly the days you drink.”

“……?”

“It might be our last chance.”

“Ah.”

I thought I understood, at least somewhat, why Faye Chen was looking for a drink.

War exhausted people. At the same time, it brought unexpected farewells in the form of death.

This was her own eve-of-battle ritual, after losing countless comrades during the Great Cataclysm.

Once this crisis was over, one of us might have crossed the river from which no one ever returned.

“Well, since things have turned out this way, I have no choice but to change my target. Right, handsome young man?”

“I told you I’m not going.”

Faye Chen stared at me with an incredulous expression.

“Do you have no conscience? I mean the young man over there, not you.”

The handsome young man Faye Chen pointed out—Team Leader Choi—nodded readily, contrary to my expectations.

“If you would invite me, it would be my honor.”

“Uh, Team Leader. You’re really going?”

“Of course. When will I ever have another chance to share a drink with Faye Chen? Besides, there are a lot of things I’m curious about.”

Faye Chen giggled.

“I thought you were only handsome, but you speak sweetly, too. So, what are you so curious about?”

“The Equipment you’re wearing right now. Where did you buy it?”

“……That’s your question?”

“Yes.”

“He’s no pushover either.”

Magic Johnson burst into hearty laughter as he watched Faye Chen sigh deeply.

“Ha ha. Miss Chen, shall we all go have a drink together, then?”

“All together? Johnson, didn’t you say you weren’t coming?”

“I did. I have no interest in drinking alone with a woman. But if an attractive man like Mr. Choi here joins us, that changes things.”

“……”

“I like men. East Asian men in particular.”

“R-right. Let’s go.”

As expected of Time magazine’s choice for the world’s most influential LGBT person.

I sent Sound Transmission to Team Leader Choi, who was dragged away with his body stiff as a board.

“Call me if anything happens.”

Team Leader Choi looked back at me with sad eyes, like a cow being led to the slaughterhouse, then disappeared with the two S-rank Hunters.

I looked around before setting off.

*This was the direction.*

How long had I walked along the dark path, avoiding people’s eyes? I stopped in the pitch-black darkness and opened my mouth.

“Come out.”

After a brief silence, someone’s voice drifted out.

“……Not bad.”

Rustle.

Wu Heixing appeared amid the sound of movement and looked me up and down.

“How did you know?”

What kind of question was that? I answered flatly.

“You might as well ask me what one plus one is. That would be harder.”

“Hmm. So you were more capable than I expected.”

“Don’t pretend to praise me now. It’s obvious you’re trying to pull some cheap trick.”

“……!”

I had hit the nail on the head. Wu Heixing’s face flushed bright red.

In a way, he was remarkably easy to handle. I knew he was well into his thirties, but it was hard to believe anyone could be this simple-minded at that age.

“It wasn’t like that. I sincerely……”

“You sincerely think I’m a bangzi. You were annoyed because some Korean who isn’t even an official S-rank Hunter yet was getting more attention than you. You picked a fight first with your usual one-dimensional behavior, but the reaction wasn’t good, and that bangzi turned out to be less of a pushover than you expected, right?”

I continued firing off words like a machine gun without giving him a chance to answer.

“So now you’re throwing out a few compliments you don’t mean and making friendly gestures, trying to pull some kind of trick…… Wait. Is any part of what I just said wrong?”

“……”

“Yeah, I’ve seen plenty of people like you. After getting hit in the back of the head so many times, even the brain that wouldn’t work started spinning.”

I gave him a contemptuous look, and the red-faced Wu Heixing began to stammer.

“I wasn’t trying to pull some other trick.”

“Then what? If you’re thinking of becoming friends with me, fold that idea up neatly and put it away. If you stand next to shit, the smell gets on me too.”

“……!”

“But what are you doing right now?”

At my quiet question, the hand moving toward his sword hilt stopped abruptly.

“Don’t draw it. You’ll get hurt.”

Wu Heixing looked at me with conflicted eyes before suddenly speaking.

“You already knew everything…… So why did you come along so willingly?”

“Because I had something to ask.”

“What?”

I looked straight into Wu Heixing’s eyes and opened my mouth.

“Sound Transmission. Right?”

“……!”

His stiffened face was answer enough. I had wondered if it was possible, but apparently it was. I scratched the back of my head and muttered.

“I guess it is. Well, this is the mainland, so I suppose various martial arts could have survived here. An internal-energy cultivation technique, for example.”

“W-what are you talking about? That was message magic……”

“Well, look at you.”

A snort escaped me at the sight of him hurriedly making excuses.

Other people who had never encountered martial arts might not be able to tell the difference, but he couldn’t fool me.

*Take a look at me for a moment.*

What had reached my ear near the end of the meeting had unquestionably been Sound Transmission.

I had responded to an invitation I could have ignored because Wu Heixing himself had been the one to send it.

“H-how did you know that?”

“Why? Was it a secret no one else knew?”

I stared at the flustered Wu Heixing and continued.

“I thought it was possible, but it’s still fascinating. Didn’t you wipe out all the martial artists during that whole Cultural Revolution business? Somehow, martial arts survived even through that.”

“Shut your mouth!”

“Oh, right. You said your family was powerful. Did the highest-ranking Communist Party officials quietly smuggle it out by abusing their positions?”

“……”

His expression sank instantly. I must have been right.

As a foreigner, I didn’t know how serious a problem this was, but I understood the value of internal-energy cultivation techniques—in other words, what was called mana cultivation in the modern era.

*If this had been the Murim, there would have been a river of blood.*

He had been caught hiding away a golden calf like that. Naturally, Wu Heixing wasn’t reacting well.

“It would be wise never to speak of what you just said again.”

“I had no particular intention of doing so, but your tone is pretty damn offensive.”

Wu Heixing glared at me with vicious eyes.

“Would you still act like this after learning who my father is?”

“I don’t know who your father is, but he sounds like he might have been a former Red Guard.”

“……!”

“Wasn’t your father the one who went around with a sledgehammer in his youth, smashing Confucius’s tomb?”

“You fucking bangzi bastard!”

Flash!

With a furious shout, his body shot forward.

The Aura Blade surging from the straight sword already drawn from its sheath—no, the Sword Force—flew toward my throat.

Whoosh!

The cool wind scattered my hair. I bent backward until my waist nearly touched the ground and avoided the Sword Force, then sprang up and drove my knee into his chin.

Crack!

Teeth and blood flew into the air. As Wu Heixing staggered, I seized both his arms and whispered into his ear.

“I told you not to draw that sword.”

Sizzle. Crack!

“Aaaaaaargh!”

The powerful Scorching Yang Qi in both hands shattered his armor and burned his flesh.

Wu Heixing’s scream was blocked by the qi barrier I had spread out and failed to travel any farther.

“You bastard!”

Whoosh!

This guy had even learned fist-and-foot martial arts. Unlike his shoddy sword technique, this was fairly sharp.

Of course……

*Compared to the Murim, the quality of the martial arts is far lower.*

I felt a slight sense of disappointment as I reached out.

Boom!

Internal energy collided with internal energy.

His leg, swung like a whip toward my waist, could go no farther.

Wu Heixing’s eyes trembled with shock and disbelief.

“H-how?”

“I’m good.”

I grabbed his ankle and slammed him into the ground with all my strength.

Whoosh! Boom!

Once more.

Whoosh! Boom!

Again. And again. And again.

Boom! Boom! Craaash!

The ground overturned, while rocks and trees were ripped out.

When the living pickaxe work finally stopped, Wu Heixing lay spread-eagled inside a huge crater, looking as though his soul had left his body.

“Still, you’ve got a sturdy body, so you’re not hurt that badly.”

“Urgh…… ugh……”

“Hey, are you crying?”

“Uuuugh……”

He was completely out of it.

Clicking my tongue, I bent over and searched his pockets.

After rummaging through the pouch enchanted with spatial expansion magic for a while, I finally found what I was looking for.

“Ah, here it is. A high-grade potion.”

> **System**
>
> **Acquired:** **Top-Grade Potion**

“……No, wait. A top-grade potion? What the hell, you bastard?”

I stared at the sprawled-out Wu Heixing with startled eyes. Even if he was an S-rank Hunter, carrying something like this around was absurd.

High-grade potions were rare enough, but top-grade potions were items that appeared maybe once or twice a year.

Leaving aside their almost unreal price, they were so scarce that even people with money couldn’t obtain them.

*I’m seeing one here after only ever seeing them online.*

After a moment’s hesitation, I slipped the top-grade potion into my Inventory. Then I searched through his pouch again, found a high-grade potion, and poured it over him.

“I’ve got my settlement payment, so I’ll let you off here. You’ve got plenty to be worried about yourself, so if you go around telling people about what happened today…… You know what’ll happen, right?”

“Ugh…… uuuugh……”

“Okay. We’ve reached a settlement.”

Just as I was wrapping things up neatly, the phone in my pocket began to vibrate.

A short text from Team Leader Choi was waiting for me.

> Team Leader Choi
>
> Team Leader Choi
>
> Mr. Ji nTaekyung, pl ease come quickly.

“……”

*No, Johnson.*
```
