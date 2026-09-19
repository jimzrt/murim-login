<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0509.txt",
      "sha256": "10c5e8628de37667fc35d69d0ef0146cb891a2eb26362e84392b163460be1d14",
      "bytes": 15114
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "0cdb74cf7faa52cd45d958a424718aaba977f990dae7ff6d8737d3aec8b0ce42",
      "bytes": 3976
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "3ef9b0673389b8351220efe4cf11c40a39bbe8956ced9bd42dfee2c53e9b5076",
      "bytes": 162641
    },
    {
      "path": "characters/Mungyeong.md",
      "sha256": "d3215679d431e377f7ce70185bb2709e6cb5515f2dcbc20acdd9ca596ed13fb8",
      "bytes": 985
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "d55e1b559aab842913d6859ee4f86aff71a3a23ad89553d949f27b82a0965ae8",
      "bytes": 154523
    }
  ],
  "estimated_tokens": 10372
}
-->

# Durable State Update — Chapter 509

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 509. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 509. Profile updates may replace only one
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
  "chapter": 509,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 509,
    "continuity_sources": [509],
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
    "Jeok Cheongang's Heart Demon and the dark memories binding him have been expelled; he has entered a new realm and achieved Returned to Youth.",
    "Mungyeong is the Slaughter Saint and former Divine Physician, a Returned to Youth Supreme Peak master and the greatest assassin in history; Mu Song and five Water Dragon Stronghold subordinates now know he is an exceptionally powerful master but not that he is the Slaughter Saint.",
    "Zhuge Feng's Demon-Sealing Formation blocks all mana from the exposed Gate by drawing in natural qi, but whether it is permanent and repeatable remains unresolved.",
    "Jang Taebo is the Jin Family of Taiyuan's Master of Ironcraft Hall and is summoning renowned artisans to process the Water God Dragon's remains.",
    "War has begun and the New Murim Alliance is being formed at Mount Song; Taekyung believes Dark Heaven planned the Gate incident, while Jin Wikyung's Hubei arrangement was designed to create an opening among rival unorthodox factions.",
    "Around one hundred Level 5 Mutated Minnows, locally called Blood Fish, were captured in the Gate's entrance waterways; the remaining population is unknown, and the fish kill one another.",
    "The Southern Heaven Demon Empress is traveling toward Yunnan and expects to cause further deaths.",
    "Jin Mukyung remains secluded in the training hall after losing to Cheongpung, refusing to emerge until he achieves a great accomplishment.",
    "Jin Taekyung's party is traveling by ship along the Yangtze toward Xixia in southwestern Henan and will continue overland after leaving the river.",
    "Mu Song wants to aid the Murim Alliance, but the Seafaring King alone decides the Yangtze River Channel League's major matters; the League and Green Forest Alliance may become rear threats.",
    "The North Sea Ice Palace remains isolationist, while Jeok Cheongang believes the Nanman Beast Palace will probably support orthodox Murim because of its historical goodwill toward the Fire Gate Clan.",
    "The Wudang pursuit party has brought back remains attributed to the Killing Ghost, but their nature is neither beast nor human."
  ],
  "continuity_sources": [
    508,
    507
  ],
  "open_questions": [
    "Will the Demon-Sealing Formation remain effective permanently, and can equivalent formations be installed repeatedly if more Gates appear?",
    "What is the Lord of Heaven's identity, and how is he connected to the dangerous force Taekyung associates with his original world?",
    "Where is the Southern Heaven Demon Empress ultimately headed, and what does she intend to do in Yunnan?",
    "Will the Nanman Beast Palace, North Sea Ice Palace, Yangtze River Channel League, and Green Forest Alliance support, ignore, or oppose the New Murim Alliance?",
    "What does Mungyeong's Linked Quest Fake Murim Martial Artist—Stage 2 require Taekyung to do?"
  ],
  "safe_through": 508,
  "temporary_decisions": [
    "Render 새외무림 as Outer Murim, 새외 as Outer Lands, 북해빙궁 as North Sea Ice Palace, 야수묘왕 as Beast Miao King, and retain Nanman Beast Palace for 남만야수궁.",
    "Render 소뢰음사 as Small Thunderclap Temple, 광풍사 as Mad Wind Society, 포달랍궁 as Potala Palace, 오독문 as Five Poisons Sect, 독곡 as Poison Valley, 천축 as India, and 갠지스강 as Ganges River.",
    "Render 파사국 as Persia, 회교도 as Muslims, 영웅건 as hero headband, 대막 as great desert, 귀염권 as Ghost Flame Fist, and 장성 as Great Wall.",
    "Retain established renderings including Energy-Dispersing Poison, Seven-Step Soul-Chasing Powder, Blood Fish, Mutated Minnow, innate qi, true-origin qi, Heart Demon, Returned to Youth, Demon-Sealing Formation, and New Murim Alliance.",
    "Render 궁예 as Gung Ye with an explanatory footnote, and render 연계 퀘스트 as Linked Quest and 가짜 무림인-2단계 as Fake Murim Martial Artist—Stage 2."
  ],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 열화문    | **Fire Gate Clan**               |
| 장강수로맹  | **Yangtze River Channel League** |
| 절정     | **Peak**          |
| 초절정    | **Supreme Peak**  |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 경지     | **realm** / **realm stage**                      | Especially power level                                |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 심법     | **cultivation technique**                        | Especially internal cultivation                       |
| 신법     | **movement technique**                           |                                                       |
| 깨달음    | **enlightenment** / **insight**                  | Martial enlightenment                                 |
| 비무     | **duel** / **spar**                              | Formal non-lethal martial contest                     |
| 생도     | **cadet**                                    |
| 시스템              | **System**                     |
| 상태               | **Status**                     |
| 퀘스트              | **Quest**                      |
| 하남     | **Henan**              |
| 본좌      | **I / this lord** only when deliberately grandiose              |
| 노부      | **this old man / I**                                            |
| 문경 | **Mungyeong** | Young medical apprentice and newly introduced passenger. |
| 교관 | **Instructor** | Kim Hwajong's former Hunter Training Center role and address. |
| 화시 | **fire arrow** | Flaming arrow Lee Seowol fires to signal Cheol Mubaek. |
| 시진 | **shichen** | Traditional time unit of approximately two hours. |
| 열화신공 | **Fire Gate Divine Technique** | Secret internal cultivation technique of the Fire Gate Clan, preserved through one-person succession without leakage. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 초절 | **supreme mastery** | Realm beyond Peak described as accessible only to the greatest martial artists. |
| 열화 | **Blazing Flame** | Lineage term in Taekyung's declaration as the Fire King's successor. |
| 호북 | **Hubei** | Province on Ju Gongsan's route from Guangdong to Henan. |
| 장강 | **Yangtze** | The river controlled by the Yangtze River Channel League. |
| 등평도수 | **Rising on Duckweed, Crossing Water** | Comparable movement feat for walking across water. |
| 동정호 | **Dongting Lake** | Lake under which Dangyang and Honghu Strongholds operated. |
| 쾌조선 | **swift ship** | Fast vessel operated by the Yangtze River Channel League. |
| 호북성 | **Hubei Province** | Province where the chapter’s Dark Heaven incidents occurred. |
| 소하 | **Xiao He** | Historical civil official invoked in the same exchange. |
| 촌각 | **moments** | Short intervals disappearing from Jeok's day. |

## Matched address pairs

(No matching address pairs.)

## Listed compact profiles

### Mungyeong.md

# Mungyeong (문경)

- **Safe through:** Chapter 508
- **Aliases:** Killing Ghost
- **Role:** Mungyeong is the legendary physician known as the former Divine Physician and Slaughter Saint, a Returned to Youth Supreme Peak master and the greatest assassin in history who passed the Divine Physician title to his Disciple.
- **Personality:** Compassionate, resolute, resourceful, and calm under extreme pressure.
- **Voice:** His Mungyeong persona is timid, deferential, and cheerful, while his Slaughter Saint voice is dry, impassive, and blunt.
- **Relationships:** Dong Feng is his Disciple, Jeok Cheongang is an old acquaintance whom Mungyeong helped break free of his Heart Demon, Mungyeong was asked to look after and instruct Jin Taekyung after testing his basics, and Mu Song plus five Water Dragon Stronghold subordinates now know he is an exceptionally powerful master but not that he is the Slaughter Saint.

## Korean source

```text
＃509화



띠링.



- 연계 퀘스트, [가짜 무림인 - 2단계]가 시작되었습니다!

- 해당 퀘스트는 수락 여부에 관계 없이 강제 진행됩니다!

- 퀘스트가 강제 수락되었습니다!



“……?”

뭐여, 시벌.

생각이 표정으로 고스란히 드러난 모양이다. 나를 바라보던 문경의 눈썹이 꿈틀거렸다.

“분명 다음 수련이 있다고 말했을 텐데, 설마 잊고 있었나?”

“예?”

아니, 잊긴 뭘 잊어. 지금 나랑 장난하나.

어이가 없어진 나는 문경을 바라보며 되물었다.

“그동안 제가 피똥을 몇 번을 쌌는데, 그걸 어떻게 잊습니까? 지금 생각해도 똥꼬가 움찔거립니다.”

“……알겠으니 거기까지 해라. 더럽다.”

“하, 진짜.”

머리는 잊어도 똥꼬, 아니 몸은 기억하는 법.

지금도 눈만 감으면 낮과 밤을 가리지 않고 피똥 싸던 기억이 새록새록 떠오른다.

과장 좀 보태서, 지난 칠주야 동안 내가 쏟아 낸 핏물을 통에 담으면 호북성에 존재하는 모든 모기 새끼들이 모여 잔치를 벌일 수 있을 거다.

‘끔찍했지.’

그런 기억들은 잊으려고 해도 지워 지지가 않는다.

문경과의 마지막 비무가 있던 날, 시스템 알림이 알려 주었던 연계 퀘스트도 마찬가지다.

애초에 얼마 되지도 않은, 그리고 그만큼 중요한 일을 잊는다면 제정신이 아니지.

“어쨌건 안 까먹고 똑똑히 기억하고 있습니다. 그때 하셨던 말씀 전부 다.”

“그래?”

문경이 나를 물끄러미 응시하며 물었다.

“네놈의 말대로면 지금 보이는 반응이 더욱 이해가 안 되는군. 미리 알려 주기까지 했는데, 왜 뒤통수라도 한 대 맞은 표정이냐?”

“……어.”

진짜 뒤통수 맞은 기분이라 그렇지.

다음 수련이 예정되어 있다는 건 알고 있었지만, 적어도 지금은 아닐 거라고 확신했다.

일반적인 선박보다도 협소한 이 쾌조선에서 가르칠 수 있는 거라고 해 봐야 지극히 한정되어 있으니까.

‘기껏해야 심법 정도?’

하지만 무공과 공력의 근간이 되는 심법은 부품처럼 손쉽게 갈아 끼울 수 있는 것이 아니다.

‘나 같은 경우에는 더더욱 그렇고.’

열화신공은 그야말로 열화문의 뿌리다.

공력의 성질을 화기(火氣)로 변화시키고, 그 힘을 증대화하는 것에 중점을 두어서 여타의 문파보다 심법이 차지하는 비중이 훨씬 높다고 할 수 있었다.

다른 사람도 아니고 문경씩이나 되는 고수가 그 사실을 모를 리 없을 텐데…….

나는 혹시나 하는 마음으로 물었다.

“저기, 설마 심법 가르쳐 주시려고 하는 건 아니죠?”

쉭, 촤악!

바람 소리와 함께 고개를 틀자, 빛살처럼 쏘아진 비도(飛刀) 한 자루가 아슬아슬하게 목을 스쳐 지나가 등 뒤의 강물을 갈랐다.

“……대답 잘 들었습니다.”

“그따위 헛소리로 내 시간을 뺏지 마라.”

“어휴, 그럼요. 저도 그냥 혹시나 해서 물어본 겁니다.”

그럼 뭐지. 설마 또 독 시음회인가.

불길함과 호기심이 동시에 엄습했지만, 지금 당장은 접어 두기로 했다.

별다른 이유가 있어서가 아니라, 어느새 부쩍 멀어진 문경의 모습 때문이었다.

촤아아아악.

딱 좋은 바람과 뱃일에는 이골이 난 수적들의 존재도 영향이 있겠지만, 쾌조선이 나아가는 속도는 확실히 일반적인 선박보다 몇 수 위에 있었다.

대화 몇 마디 나누지도 않았는데 벌써 저기까지 간 걸 보면 장강수로맹 놈들이 모터를 달아 놨는지 의심이 될 정도다.

‘거, 더럽게 빠르네.’

전교 1등을 밥 먹듯이 하는 우등생도 취약한 과목 하나쯤은 있기 마련이다. 내게는 경신법이 유독 그랬다.

명색이 초절정 고수인만큼 등평도수(登萍渡水)의 수법으로 계속 따라가고는 있는데, 익숙하지 않을뿐더러 공력 소모도 상당했다.

그렇다고 지난번 동정호에서처럼 밟고 다닐 만한 뭔가가 있는 것도 아니고.

“우선 올라가서 듣겠습니다. 이 상태로 계속 있을 수는 없잖아요.”

문경이 선선히 고개를 끄덕였다.

“그렇게 해라.”

“혹시 깜짝 선물로 암기 날리시는 건 아니죠?”

“알겠으니 헛소리 그만하고 올라오기나 해라.”

“옙.”

나는 끌어올린 공력을 발끝에 집중시켰다.

열화신공의 가장 큰 장점은 폭발적인 힘을 끌어낼 수 있다는 거다. 단 한 번의 도약이면 다시 쾌조선으로 들어가기에 차고 넘쳤다.

하나, 둘.

‘지금.’

파앙!

발끝에서 발출된 공력이 수면을 후려쳤다. 충격파로 강물이 거대한 벽처럼 솟구쳤고, 맹렬한 바람이 전신을 스쳤다.

촌각이라고 할 수도 없을 만큼 짧은 순간에 십여 장의 거리를 지워 낸 나는 쾌조선의 선미(船尾)에 착륙…….

빡!

뭐여, 시벌.

처음 거리를 좁혔을 때보다 더 빠른 속도로 튕겨 나간 나는, 황급히 공력을 발바닥으로 흘려보냄과 동시에 신형을 뒤집었다.

수면을 향해 곤두박질치던 신형이 중심을 되찾으며 간신히 수면 위에 설 수 있었다.

‘뭐지, 데자뷰인가.’

나는 떨떠름한 눈빛으로 선미에 우뚝 선 문경을 바라보았다.

“방금 뭡니까?”

“뭐가 말이냐.”

“손에 들고 계신 그거요. 그걸로 저 때리셨잖아요.”

“아, 이거.”

문경이 손에 들고 있던 커다란 무언가를 흔들었다.

“이건 노라는 물건이다. 주로 배를 저을 때 쓰지.”

“그걸 몰라서 여쭤본 게 아닌데요.”

“그걸 몰라서 여쭤본 줄 알았다.”

“이상한 짓 안 하기로 약속하지 않으셨습니까?”

“정확히는 암기를 날리지 않겠다고 했지. 이건 암기가 아니다.”

“아하, 그렇구나. 암기 대신 흉기를 사용하셨구나.”

“그런 셈이지.”

미친놈인가, 진짜.

할 말을 잃어버린 나를 문경이 심유한 눈빛으로 응시했다. 아니, 정확히는 나를 중심으로 출렁이는 수면이다.

“여전히 장강의 강물은 잔잔한데, 네놈의 발이 닿는 곳마다 난리통이로군.”

“계속 이런 장난치시면 저 난리납니다, 진짜.”

“왜 네놈만 유독 그러는지, 그 이유를 알고 있느냐?”

“그건 모르겠고, 이러시는 이유가 뭡니까?”

문경은 들은 척도 하지 않고 말을 이었다.

“움직임이 투박하고 거칠기 때문이 아니다.”

“성격 거칠어지게 만드시네.”

“일정한 경지에 오른 고수의 움직임에는 저마다의 이유와 의미가 있다. 그리고 네놈의 경우에는 공력 자체가 폭급하기 때문이라고 할 수 있겠지. 이는 열화문의 무공이 가진 고질적인 문제점 중 하나다.”

“아, 열 받네. 우선 다시 올라갈 테니까 손에 들고 계신 노부터 내려놓고…….”

말을 이어 가던 나는 순간 멈칫했다.

이게 단순한 심술이나 장난이 아니라는 사실을 깨달았기 때문이었다.

“잠깐, 지금 뭐라고요?”

“이제야 귓구멍이 뚫린 모양이로군. 물 위에서 네 움직임이 거친 이유가, 열화문의 무공이 가진 고질적인 문제라고 했다.”

고질적인 문제라…….

이건 가볍게 흘려들을 수 있는 이야기가 아니다.

잠시 생각하던 나는 재차 입을 열었다.

“그게 등평도수와 무슨 연관이 있습니까? 그냥 익숙하지 않아서 서툰 것뿐인데, 너무 쉽게 판단하시는 것 아니에요?”

“멍청한 놈. 그리 단순한 문제가 아니다.”

“그 말씀은…….”

“공력의 안정성, 그리고 세밀함이지.”

“안정성과 세밀함…….”

“등평도수는 그 두 가지를 판단하는 척도 중 하나일 뿐이다. 공력의 움직임이 안정적이고 세밀한 자일수록 등평도수를 자유롭게 펼칠 수 있지. 비록 상승의 경신법이라고는 하나, 절정 고수 중에서도 조예가 깊은 자라면 그리 큰 어려움 없이 펼칠 수 있다.”

막힘없이 말을 이어 간 문경이 돌연 선미에서 훌쩍 뛰어내렸다.

평범한 사람이라면 얼굴 생김새조차 제대로 분간 못 할 만한 거리였지만, 극도로 예리한 감각의 소유자인 나는 똑똑히 보고, 들을 수 있었다.

스윽.

공기처럼 가볍게 수면에 착지한 문경의 모습을. 그리고 마치 아무 일도 없다는 듯, 잔물결 하나 일어나지 않는 수면을.

문경의 건조한 눈빛이 나를 향했다.

“반면 네놈은 어떠하냐?”

“……!”

나는 반사적으로 고개를 숙여 발아래를 내려다보았다. 그러나 결국 보나 마나 한 일이었다.

내가 쾌조선을 쫓아 달려온 길은 또 다른 배가 지나간 것처럼 하얀 포말이 가득했으니까.

촤악.

신중하게 내디딘 걸음을 중심으로, 수십 개의 파문이 겹겹이 일어났다. 비교 대상이 문경이라 해도 너무 극심한 차이였다.

“대답은 이미 스스로도 알고 있는 모양이군.”

차라리 한심함과 비웃음이 담겨 있었다면 덜 부끄러웠을 거다.

마치 ‘그래, 넌 그 정도지.’라고 말하는 듯한 문경의 고저 없는 목소리를 듣자 얼굴이 확 달아올랐다.

“이제 내가 한 말의 뜻을 알겠느냐?”

“……어느 정도는 알 것도 같습니다.”

앞서 문경이 했던 말처럼 등평도수는 공력의 안정성과 세밀함을 볼 수 있는 중요한 척도였다.

얼마나 힘을 잘 분배하고 제어하느냐에 따라 발걸음이 향하는 수면 위가 폭풍우라도 만난 것처럼 요동칠 수도, 인적 드문 호숫가처럼 잔잔할 수도 있다.

“그럼 이를 통해 무엇을 얻어야 할지. 네놈의 입으로 직접 말해 봐라.”

“음. 공력을 보다 효율적으로 다룰 수 있겠네요.”

“답변이 마음에 들지 않는다.”

“안정성과 세밀함은 물론이고, 같은 힘을 내면서도 공력의 소모를 줄일 수 있습니다.”

“조금 나아졌군. 하지만 아직 부족하다.”

1초가 1분처럼 느껴지는 시간 속, 곰곰이 생각에 잠겨 있던 나는 문득 입술을 뗐다.

“증폭.”

“더 자세히.”

“앞서 말한 것들은 원하는 때에 적재적소의 힘을 발휘할 수 있는 조건이죠. 그리고 그만큼 공력을 세밀하게 조절할 수 있다면…… 지금보다 더욱 강하게 공력을 증폭시킬 수 있다는 뜻도 됩니다.”

“그래서?”

“단순히 안정성과 세밀함만을 추구하는 게 아니라, 제가 익힌 무공의 위력이 더욱 강력해진다. 맞습니까?”

아무런 말 없이 나를 응시하던 문경이 한 마디를 툭 내뱉었다.

“……아주 천치는 아니로군.”

됐다. 정답이다.

하지만 내가 묘한 희열을 느끼는 이유는, 사소하게나마 문경의 인정을 받았기 때문이 아니었다.

‘만약 이번 수련을 성공적으로 해낸다면…… 지금보다 더 강해질 수 있다.’

현재 나는 일종의 답보(踏步) 상태에 빠져 있었다. 너무 빠르게 성장했기 때문일까, 쭉쭉 앞으로 나아가던 무공은 어느 순간부터 정체되었고 나는 앞을 가로막은 높은 벽을 느끼고 있었다.

하지만 이 방법이라면, 어떤 깨달음을 얻지 못한다 하더라도 기술적인 부분에서 진일보할 수 있을 것이다.

‘깨달음 없이도 성장할 여지가 충분히 남아있었구나.’

언제부터였을까, 나는 잘못된 생각을 하고 있었다.

남은 것을 채워 넣을 생각은 하지 못하고, 더 새롭고 대단한 것을 원했다.

‘멍청한 짓이지.’

이건 마치 1테라 용량의 외장 하드를 갖고 있으면서도, 500기가의 야동만 채운 채 부족하다고 징징대는 꼴이었다.

문경은 바로 그 사실을 내게 알려주었다.

너에게는 아직 500기가의 야동, 아니 더 채워 넣을 수 있는 부분이 있다고. 용량이 남았는데도 새로운 외장 하드를 추가 구입할 필요는 없다고 말이다.

‘아아, 문 본좌시여.’

문경의 어깨너머에서 후광이 비추는 것 같다.

그런 마음이 가득 담긴 내 눈빛에, 문경이 입을 열었다.

“눈 똑바로 떠라. 파 버리기 전에.”

“……아, 예.”

“어쨌건 이제야 얼추 감을 잡은 모양이군.”

“네. 알 것 같네요.”

“그럼 지금부터 어떤 수련을 해야 할지도 감을 잡았겠지?”

그야 물론이다. 나는 예상하고 있던 그것을 말했다.

“등평도수. 맞습니까?”

“그렇다. 백 번을 듣고 생각하는 것보다는 직접 몸으로 겪는 것이 제일이지. 때마침 장강이라 장소도 안성맞춤이니, 지금 즉시 시작해라.”

왜 다짜고짜 물에 빠트리나 했더니, 처음부터 이럴 생각이었던 것이 분명하다.

하지만 짜증이 나거나 억울하지는 않았다.

아무런 대가 없이 얻을 수 있는 것은 존재하지 않으니까.

‘온통 강이라 그런지 조금 막막하긴 한데, 그래도 하다 보면 익숙해지겠지.’

생각을 끝마친 나는 일말의 망설임도 없이 대답했다.

“알겠습니다.”

“생각했던 것보다 고분고분하군. 앞으로도 그 자세 쭉 유지하도록.”

“예.”

지금보다 강해질 수만 있다면 뭘 못 하겠나.

그리고 문경을 향해 고개를 꾸벅 숙인 나는, 다음 순간 가장 중요한 질문을 빠트렸다는 것을 깨달았다.

“저, 그런데.”

“음?”

“이거, 얼마 동안 해야 합니까?”

“멍청한 질문이군.”

문경이 뭘 그런 걸 묻냐는 표정으로 양손을 폈다.

별이 열 개……가 아니라, 열 시진?

“자, 잠깐만요. 아무리 저라고 해도 열 시진은 무린데요. 아시다시피 등평도수로 쾌조선을 따라가야 하는데, 그렇게 하면 공력 소모가…….”

“무슨 소리냐? 열흘인데.”

“예?”

“열 시진이 아니라, 열흘이다. 하남에 도착할 때까지 쭉 따라와라.”

“……예?”

내가 돌처럼 굳어 버린 그 순간, 익숙한 알림이 귓가를 파고들었다.

띠링.



- [가짜 무림인-2단계]의 수련방식이 새롭게 설정되었습니다!

- 훈육 교관이 수련 기한을 [10일]로 설정했습니다! 해당 기한은 목적지에 도착하는 시간에 따라 짧아지거나 길어질 수 있습니다!

- 지금부터 카운트를 시작합니다! 힘내십시오, 악!

- 제한 시간 : 9일 23시간 59분 59초.



“…….”

씨바, 할 말을 잃었습니다.
```

## Final English reading copy

```markdown
# Chapter 509

Ding.

> **System**
>
> - Linked Quest **Fake Murim Martial Artist—Stage 2** has begun!
> - This Quest will proceed forcibly regardless of whether it is accepted!
> - Quest forcibly accepted!

“……?”

*What the fuck?*

It seemed my thoughts had shown plainly on my face. Mungyeong’s eyebrows twitched as he looked at me.

“I clearly told you there would be another training session. Don’t tell me you forgot?”

“Excuse me?”

*Forgot what? Is he messing with me right now?*

Dumbfounded, I looked back at Mungyeong.

“How could I forget after shitting blood so many times? Even thinking about it makes my asshole twitch.”

“……I understand, so stop there. You’re disgusting.”

“Ha. Seriously.”

The head might forget, but the asshole—no, the body—remembered.

Even now, whenever I closed my eyes, memories of shitting blood day and night came flooding back.

To exaggerate a little, if all the bloody liquid I’d passed over the past seven days and nights were collected in a tub, every mosquito in Hubei Province could gather for a feast.

*It was horrible.*

No matter how hard I tried to forget those memories, they refused to disappear.

The same went for the Linked Quest the System had announced on the day of my last duel with Mungyeong.

It had not been long ago, and it was far too important to forget. If I had forgotten it, I would have had to question my sanity.

“Anyway, I haven’t forgotten. I remember every single thing you said back then.”

“Is that so?”

Mungyeong stared at me intently.

“Then your reaction makes even less sense. I even warned you in advance. Why do you look as though someone just hit you in the back of the head?”

“……Uh.”

*Because it really does feel like I was hit in the back of the head.*

I knew another training session was coming, but I had been certain that it would not happen right now.

There was only so much he could teach me aboard this swift ship, which was even narrower than an ordinary vessel.

*At most, a cultivation technique?*

But a cultivation technique, the foundation of martial arts and internal energy, was not something that could be swapped out as easily as a machine part.

*Especially not in my case.*

The Fire Gate Divine Technique was the very root of the Fire Gate Clan.

Because it focused on transforming the nature of internal energy into fire qi and amplifying its power, the cultivation technique played a far greater role in the Fire Gate Clan’s martial arts than it did in those of other sects.

Mungyeong of all people could not possibly be unaware of that fact.

I asked, just in case.

“Um, you’re not planning to teach me a cultivation technique, are you?”

Whoosh! Slash!

I turned my head at the sound of the wind. A throwing blade shot past like a streak of light, missing my neck by a hair before slicing through the river behind me.

“……I heard your answer loud and clear.”

“Don’t waste my time with that kind of nonsense.”

“Of course. I was just asking on the off chance.”

*Then what is it? Another poison-tasting session?*

A sense of foreboding and curiosity struck me at the same time, but I decided to put it aside for now.

Not for any particular reason. Mungyeong had simply grown much farther away before I knew it.

Whoosh!

The favorable wind and the presence of waterway men who were thoroughly accustomed to sailing certainly helped, but the swift ship was unquestionably several notches faster than an ordinary vessel.

We had barely exchanged a few words, yet he had already gotten that far. I almost wondered whether the bastards from the Yangtze River Channel League had installed a motor.

*Damn, it’s fast.*

Even a model student who routinely came first in the entire school was bound to have at least one weak subject.

For me, it was movement techniques.

As befitted a Supreme Peak master, I was able to keep following him using Rising on Duckweed, Crossing Water, but I was not accustomed to it, and it consumed a considerable amount of internal energy.

Besides, unlike Dongting Lake last time, there was nothing here I could step on as I moved.

“I’ll climb aboard first and listen. I can’t keep staying like this.”

Mungyeong readily nodded.

“Do that.”

“You’re not going to throw a hidden weapon at me as a surprise, are you?”

“Stop talking nonsense and come up.”

“Yes, sir.”

I gathered the internal energy I had drawn up and concentrated it in my toes.

The greatest advantage of the Fire Gate Divine Technique was its ability to draw out explosive force. A single leap would be more than enough to get me back onto the swift ship.

*One, two.*

*Now.*

Bang!

The internal energy released from my toes slammed into the water. The river surged upward like a massive wall from the shockwave, and a fierce wind swept across my entire body.

In a moment so brief it could not even be called an instant, I covered over a hundred feet and landed on the stern of the swift ship—

Thwack!

*What the fuck?*

I was sent flying at a speed even greater than when I had first closed the distance. I hurriedly sent internal energy through the soles of my feet and flipped my body around.

As my body plunged headfirst toward the water, I regained my balance and barely managed to stand on the surface.

*What is this? Déjà vu?*

I looked at Mungyeong, who stood tall on the stern, with a thoroughly displeased expression.

“What was that just now?”

“What was what?”

“That thing in your hand. You hit me with it.”

“Oh, this.”

Mungyeong shook the large object in his hand.

“This is an oar. It is mainly used to row a boat.”

“I wasn’t asking because I didn’t know that.”

“I thought you were.”

“Didn’t you promise not to do anything strange?”

“To be precise, I said I wouldn’t throw a hidden weapon. This is not a hidden weapon.”

“Oh, I see. You used a lethal weapon instead of a hidden weapon.”

“Something like that.”

*Is he insane? Seriously.*

Mungyeong stared at me with a profound gaze. No—with a profound gaze at the water rippling around me.

“The Yangtze River is still calm, yet chaos breaks out wherever your feet touch.”

“If you keep pulling stunts like this, I’ll be the one making a scene. Seriously.”

“Do you know why this happens only to you?”

“I don’t know that, but why are you doing this?”

Mungyeong ignored my question and continued.

“It is not because your movements are clumsy and rough.”

“You’re making my personality rough.”

“The movements of a master who has reached a certain realm each have their own reason and meaning. In your case, the cause is that your internal energy itself is too violent. That is one of the chronic problems of the Fire Gate Clan’s martial arts.”

“Ah, now I’m pissed. I’ll climb aboard again, so put down that oar first and—”

I stopped halfway through my sentence.

I had realized this was not merely a case of Mungyeong being spiteful or playing a prank.

“Wait. What did you just say?”

“At last, your ears seem to have opened. I said that the reason your movements are rough on the water is a chronic problem with the Fire Gate Clan’s martial arts.”

*A chronic problem…*

This was not something I could casually dismiss.

After thinking for a moment, I opened my mouth again.

“What does that have to do with Rising on Duckweed, Crossing Water? I’m simply clumsy because I’m not accustomed to it. Aren’t you judging too quickly?”

“You fool. It is not that simple.”

“You mean…”

“The stability and precision of your internal energy.”

“Stability and precision…”

“Rising on Duckweed, Crossing Water is merely one measure of those two qualities. The more stable and precise a person’s internal energy is, the more freely they can perform it. Though it is an advanced movement technique, even among Peak masters, those with deep attainment can perform it without much difficulty.”

Mungyeong continued without pause, then suddenly leaped down from the stern.

The distance was great enough that an ordinary person would not have been able to distinguish his features properly. But with my extremely keen senses, I could see and hear him clearly.

I saw Mungyeong land on the surface of the water as lightly as air.

I heard no splash.

Not even a ripple rose from the water, as though nothing had happened.

Mungyeong’s dry gaze turned toward me.

“What about you?”

“……!”

I instinctively lowered my head and looked at the water beneath my feet.

But there was no point. The path I had taken while chasing the swift ship was covered in white foam, as though another ship had passed through it.

Splash.

Dozens of ripples overlapped one another around the cautious step I took.

Even with Mungyeong as the comparison, the difference was simply too extreme.

“You seem to know the answer yourself.”

I would have been less embarrassed if his voice had contained disdain or mockery.

But when I heard Mungyeong’s toneless voice, which seemed to say, *Yes. That is about your level,* my face heated up.

“Do you understand the meaning of what I said now?”

“……I think I understand it to some extent.”

As Mungyeong had said, Rising on Duckweed, Crossing Water was an important measure of the stability and precision of one’s internal energy.

Depending on how well a person distributed and controlled their power, the water beneath their feet could churn as though caught in a storm or remain as still as an unfrequented lakeshore.

“Then tell me, in your own words, what you should gain from this.”

“Hmm. I’ll be able to handle my internal energy more efficiently.”

“I do not like that answer.”

“Besides stability and precision, I’ll be able to reduce my internal energy consumption while producing the same amount of force.”

“That is a little better. But it is still lacking.”

With one second stretching into a minute, I thought hard. Then, suddenly, I parted my lips.

“Amplification.”

“Explain further.”

“What I said earlier describes the conditions needed to produce the right amount of force in the right place at the right time. And if I can control my internal energy that precisely… it also means I can amplify it more powerfully than I do now.”

“So?”

“Rather than simply pursuing stability and precision, the power of the martial arts I’ve learned will become even stronger. Is that right?”

Mungyeong stared at me in silence before tossing out a single remark.

“……You are not a complete idiot.”

*That’s it. I got the answer right.*

But the reason I felt a strange thrill was not because I had received a small measure of Mungyeong’s approval.

*If I can complete this training successfully, I can become stronger than I am now.*

At present, I was in a kind of stagnant state.

Perhaps it was because I had grown too quickly. The martial arts that had once advanced by leaps and bounds had stagnated at some point, and I could feel a tall wall blocking my path.

But with this method, I could make technical progress even without gaining some new enlightenment.

*So there was still plenty of room for me to grow without enlightenment.*

When had I begun thinking incorrectly?

I had failed to consider filling in what I already had and instead kept wanting something newer and greater.

*What a stupid thing to do.*

It was like owning a one-terabyte external hard drive, filling only five hundred gigabytes of it with porn, then whining that the storage was insufficient.

Mungyeong had shown me exactly that.

*You still have another five hundred gigabytes of porn—no, another five hundred gigabytes left to fill. There’s no reason to buy another external hard drive when you still have capacity.*

*Ah, Great Lord Mun.*

A halo seemed to shine over Mungyeong’s shoulder.

At the sight of my eyes brimming with those feelings, Mungyeong opened his mouth.

“Watch where you’re looking before I gouge your eyes out.”

“……Ah, yes.”

“Anyway, you seem to have finally grasped the general idea.”

“Yes. I think I understand.”

“Then you have also figured out what kind of training you should do from now on, correct?”

Of course I had. I gave the answer I had expected.

“Rising on Duckweed, Crossing Water. Am I right?”

“That is correct. Experiencing something directly with your body is better than hearing and thinking about it a hundred times. And the Yangtze is the perfect place, so begin immediately.”

So that was why he had knocked me into the water without warning. He must have been planning this from the beginning.

But I was not annoyed or indignant.

Nothing could be gained without paying a price.

*It’s a little daunting with nothing but river all around me, but I’ll get used to it if I keep practicing.*

Having finished my thoughts, I answered without the slightest hesitation.

“Understood.”

“You are more obedient than I expected. Keep that attitude from now on.”

“Yes.”

If it meant becoming stronger than I was now, what wouldn’t I do?

I bowed my head toward Mungyeong, then realized I had forgotten the most important question.

“Um, by the way.”

“Hmm?”

“How long do I have to do this?”

“What a foolish question.”

Mungyeong spread both hands, looking as though he could not understand why I would ask something so obvious.

*Ten stars… no, ten shichen?*

“W-wait a minute. Even for me, ten shichen is impossible. As you know, I have to follow the swift ship using Rising on Duckweed, Crossing Water, and if I do that, the internal energy consumption will—”

“What are you talking about? Ten days.”

“Excuse me?”

“Not ten shichen. Ten days. Follow me the entire way until we reach Henan.”

“……Excuse me?”

The instant I froze like a stone, a familiar notification pierced my ears.

Ding.

> **System**
>
> - The training method for **Fake Murim Martial Artist—Stage 2** has been newly established!
> - The Instructor has set the training period to **10 days**! This period may become shorter or longer depending on how long it takes to reach the destination!
> - The countdown begins now! Hang in there—argh!
> - **Time limit:** 9 days 23 hours 59 minutes 59 seconds.

“……”

*Fuck. I have no words.*
```
