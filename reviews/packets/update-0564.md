<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0564.txt",
      "sha256": "9ffe09b86db0ac16dc6665c6618efab9495f8da4a0c762e5d523a370b7b0f66f",
      "bytes": 14882
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "6c3eadef4d7b3b0f4c7551ab1b0ae11d8ea679ad72c9c895bb5a252a590b83a6",
      "bytes": 4979
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "2ea39b8929290a63980b44f3fae36ba096fdf1a01f9d8e7a19d37a682e05906a",
      "bytes": 178851
    },
    {
      "path": "characters/Baek Hanseong.md",
      "sha256": "f8a349bb2c3c6595be819ed7b6a1b3c76a059da6e9a5749bbf26fa758a13131e",
      "bytes": 741
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "f05e3e9827aaa544c5302b5a22ad89980a5f42a2ab526ebe551f67f4f6563634",
      "bytes": 553
    },
    {
      "path": "characters/Go Jun.md",
      "sha256": "d9db01f8c9ce9f12c65b2417fdf3e8f4a361fa7ef75bdc1a32d809280c182422",
      "bytes": 798
    },
    {
      "path": "characters/Im Kkeokjeong.md",
      "sha256": "1c5ea0fc27c9b700d86ab6484c4ccd68c359c603467044c164773d4a7759874f",
      "bytes": 1774
    },
    {
      "path": "characters/Lee Jungryong.md",
      "sha256": "4ebbaccbeadc5894cdaa2a3cfb88fbf2e0caa3864157ef831aa7bc9126547140",
      "bytes": 1182
    },
    {
      "path": "characters/Song Song.md",
      "sha256": "a6ce65d6c3a4c88399b75b1a0f1657b075acf122419b7e9351875905bf65c35d",
      "bytes": 939
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "3b96bf7c262cc59c1e7f47871b7225460f314fe9b03f8c4d46f69bd96de6280c",
      "bytes": 172963
    }
  ],
  "estimated_tokens": 11854
}
-->

# Durable State Update — Chapter 564

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 564. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 564. Profile updates may replace only one
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
  "chapter": 564,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 564,
    "continuity_sources": [564],
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
    "Magic Johnson's information records at least thirty-two Mutated Gates in the United States during one week, and the true number is likely higher.",
    "The Peace Guild has risen as the only apparent counterweight to Ares Guild; Team Leader Choi is gathering political, business, and Guild allies to strengthen Peace and weaken Ares, with Magic Johnson and the Wizard Guild supporting him.",
    "Team Leader Choi has confirmed that his blood descends from Cheon Taemin, whose legacy gives him exceptional political and social leverage.",
    "The Fire Dragon Pavilion's six-member first mission is entering Nanman through the Journey to Nanman Quest, whose reward is a linked quest and whose failure penalty is the Title Can't Go to Nanman; the party secretly departed Henan.",
    "Taekyung is a Supreme Peak master with Three Flowers Gather at the Crown, advanced Qi Sense, exceptional resistance to monster Fear, public S-rank-level recognition while retaining an A-rank license, leadership of the Fire Dragon Pavilion's first mission to Nanman, and the Peace Guild's modern-world patronage.",
    "Mungyeong ended Taekyung's direct training and assigned him the final task of incorporating martial principles into his learned martial arts; Cheongpung accompanies Mungyeong and learns through observation.",
    "Mungyeong considers Nanman a plausible site for Dark Heaven's second rift, while Dark Heaven remains a monster-like threat capable of causing rifts and creating mutants; the mechanism behind Jang Sam's transformation remains unresolved.",
    "The Mount Song Resolution restored the Murim Alliance with Mae Jonghak as Alliance Leader and Jeok Cheongang heading the Five Kings Hall; Zhuge Feng's Demon-Sealing Formation still blocks mana from the exposed Gate while Jang Taebo processes the Water God Dragon's remains.",
    "The Southern Heaven Demon Empress is believed to be moving toward the suspected next target, while Song Ho's dispatch there has received no reply for more than seven days.",
    "Im Kkeokjeong's arms have been reattached, his rehabilitation is nearly complete, and he intends to remain a Hunter and Peace Guild member while spending time with his wife and children.",
    "Taekyung is in the modern world in early 2047, has entered the Yeokgok Mutated Gate, and has just killed its Orc Lord to rescue an Ares raid team.",
    "Go Jun is Ares Guild's Vice Guild Master and Lee Jungryong's disciple; Jin Taekyung's public exposure of a major Guild's Gate negligence has intensified the threat to Ares, and Go Jun has vowed to kill Jin."
  ],
  "continuity_sources": [
    563,
    562
  ],
  "open_questions": [
    "What is the Lord of Heaven's identity, how is he connected to the dangerous force Taekyung associates with his original world, and how can Dark Heaven open Gates?",
    "What will Taekyung's party find in Nanman, and what does the Southern Heaven Demon Empress intend there?",
    "What is the outcome of the duel between Jeok Cheongang and Nangong Cheon, and why did Ju Hwaran and Sama Pyo's political engagement end?",
    "What process created Jang Sam's mutant form, whether Dark Heaven's mutants can absorb human energy, and whether it relates to the Mutated Gate?",
    "How many additional Gate disasters are being concealed, and what consequences will the investigation into Ares's Gate negligence and Go Jun's threat against Jin produce?"
  ],
  "safe_through": 563,
  "temporary_decisions": [
    "Render 건량 as dry rations, 광서 as Guangxi, 대별산 as Mount Daebyeol, 만리행 as Ten-Thousand-Li Journey, and 고잉메리호 as Going Merry.",
    "Render 반 시진 as half a shichen and retain Nanman, Nanman Beast Palace, Fire Dragon Pavilion, Great Hero, and Young Lady Ju.",
    "Render 남만행 as Journey to Nanman, 남만을 못 가 as Can't Go to Nanman, 면구 as disguise mask, 역용술 as disguise technique, 각주님 as Pavilion Master, 로그아웃 as Logout, and 동기화 as Synchronization.",
    "Render 일기당천 as One Against a Thousand, 거인의 포효 as Giant's Roar, 타락한 엔트 as Corrupted Ent, 붉은 눈 as Red Eye, 치코리타 as Chikorita, 대마도사 as Grand Mage, 순간이동 as Teleportation, 텔레포트 as Teleport, 변이 게이트 as Mutated Gate, and 몬스터 웨이브 as Monster Wave.",
    "Render 모하비 사막 as Mojave Desert, 애리조나주 as Arizona, 대의 as greater cause, 순수혈통 as pureblood, 국부 as Founding Father, 위저드(Wizard) 길드 as Wizard Guild, 조셉 바이든 as Joseph Biden, 펠릭스 왕자 as Prince Felix, 곽한구 as Gwak Hangu, 역곡 as Yeokgok, 오크의 황무지 as Orc Wasteland, 오크 로드 as Orc Lord, 국회의사당 as National Assembly, 고세원 as Go Se-won, 경호팀장 as Head of Security, A구역 as Section A, 신성불가침 as sacrosanct, 바티칸 as Vatican, 영구 임대 as permanent lease, and 혈안 as bloodshot."
  ],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 송송이    | **Song Song**     |
| 이정룡    | **Lee Jungryong** |
| 화산파    | **Huashan**                      |
| 심법     | **cultivation technique**                        | Especially internal cultivation                       |
| 돌파     | **break through** / **breakthrough**             | Realm advancement                                     |
| 장문인    | **Sect Leader**                              |
| 진가심법   | **Jin Family's Cultivation Technique** |
| 일격     | **One Strike**                         |
| 시스템              | **System**                     |
| 헌터      | **Hunter**            |
| 게이트     | **Gate**              |
| 길드      | **Guild**             |
| 길드장     | **Guild Master**      |
| 부길드장    | **Vice Guild Master** |
| 팀장      | **Team Leader**       |
| 탱커      | **tank**              |
| 마법사     | **mage**              |
| 대격변     | **Great Cataclysm**   |
| 화산     | **Huashan**            |
| 도사      | **Daoist**                                                      |
| 대사      | **Master** for a senior Buddhist monk                           |
| 백한성 | **Baek Hanseong** | Twenty-seventh President of Korea and youngest president elected in Korean history. |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 고준 | **Go Jun** | Personal name of Team Leader Seok; Lee Jungryong's prized Disciple. |
| 임꺽정 | **Im Kkeokjeong** |
| 평화 | **Peace Guild** | Guild name. |
| 대한민국 | **Korea** | Country reference. |
| 아레스 | **Ares Guild** | The leading Guild in Korea; formerly employed Team Leader Choi and Song Song. |
| 대리 | **Assistant Manager** | Corporate title used by Kim Seonhee |
| 송이 | **Song-i** | Short form used for Song Song; Taekyung's love interest. |
| 갑자 | **jiazi** | Traditional sixty-year cycle. |
| 개방 | **Beggars' Sect** | Murim organization counted among the Nine Sects and One Gang. |
| 오우거 | **ogre** | B-rank monster species emerging from the Gate. |
| 청와대 | **Blue House** | Presidential office mentioned in an online comment about proposed legislation. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 마도 | **Demonic Path** | Term raised for martial power that appears to defy common principles. |
| 준이 | **Jun** | Family nickname used in the form Jun's dad. |
| 석고준 | **Go Jun** | Source full-name form for the established Go Jun, also known as Team Leader Seok. |
| 경호팀장 | **Head of Security** | Go Jun's security-team office under Lee Jungryong. |
| 존슨 | **Johnson** | Co-host of the American talk show that replays Taekyung's viral interview. |
| 미국 | **United States** | Country associated with the talk show and CNM. |
| 대통령 | **President** | Title for Korea's head of state. |
| 성도 | **Chengdu** | Sichuan destination of Taekyung's party. |
| 시리 | **City** | Second word in one of the necromantic chants. |
| 꺽정 | **Kkeokjeong** | Jin's injured ally, addressed as Uncle Kkeokjeong. |
| 의지 | **Will** | System attribute that replaces Endurance after its dramatic increase. |
| 마법 | **Magic** | Taekyung's explanation for Dark Heaven's anomalous abilities. |
| 성하 | **Seongha** | Hunter named during the cave battle. |
| 대마도사 | **Grand Mage** | Title used for Magic Johnson. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 송송이 | 임꺽정 | younger_guild_member_to_older_guild_member | Uncle | casual-polite | Song Song uses 아저씨 while asking Im Kkeokjeong to agree that Changsoo is nasty. |
| 이정룡 | 고준 | Master to Disciple | Go Jun | familiar and testing | Lee switches from Seok's office title to his personal name while considering whether he can defeat Taekyung. |
| 고준 | 이정룡 | Disciple to Master | Master | deferential | Go Jun responds to Lee's personal-name address as 스승님. |
| 마법사 | 이정룡 | Ares Guild mage subordinate to Vice Guild Master | Vice Guild Master | formal-deferential | Lee's five direct A-rank mages greet him and receive instructions for concealing the battle. |
| 이정룡 | 백한성 | Ares authority to national head of state | Mr. President | formal-polite | Uses 대통령 각하 while greeting Baek Hanseong. |
| 백한성 | 이정룡 | President to Ares Guild Vice Guild Master | Vice Guild Master Lee | formal-polite | Uses 이정룡 부길드장님 while discussing the Chinese proposal. |

## Listed compact profiles

### Baek Hanseong.md

# Baek Hanseong (백한성)

- **Safe through:** Chapter 563
- **Aliases:** None
- **Role:** Twenty-seventh President of Korea and the youngest president elected in Korean history; leads the government's public response to the Mutated Gate crisis and supports Jin Taekyung in public appearances.
- **Personality:** Confident, politically shrewd, composed, and willing to needle Lee Jungryong while advancing his anti-Ares stance.
- **Voice:** Polite, self-assured, calm, and lightly teasing.
- **Relationships:** Political counterpart to Lee Jungryong; cooperates with Ares Guild over the Chinese crisis while allowing the Peace Guild to participate at Xiao Yang's request.

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 562
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** Publicly reputed to be selfless and devoted to treating patients in the lowest places.
- **Voice:** Not established.
- **Relationships:** Mungyeong is the Divine Physician's true identity, and Dong Feng is his Disciple.

### Go Jun.md

# Go Jun (고준)

- **Safe through:** Chapter 563
- **Aliases:** Team Leader Seok
- **Role:** Go Jun is Ares Guild's Vice Guild Master, Lee Jungryong's disciple and former security-team leader, and the de facto successor to Lee's Ares legacy.
- **Personality:** Disciplined and controlled under ordinary pressure, fiercely loyal to Lee Jungryong, but consumed by humiliation and rage when Ares Guild's authority is challenged.
- **Voice:** Dry, controlled, and formal with subordinates; deferential when addressing his Master.
- **Relationships:** Disciple and direct protégé of Lee Jungryong, Go Jun inherited Lee's Ares Guild legacy after his death and regards Jin Taekyung and Choi Minwoo as enemies seeking to take it away.

### Im Kkeokjeong.md

# Im Kkeokjeong (임꺽정)

- **Safe through:** Chapter 561
- **Aliases:** Im Hyeokjun; Kkeokjeong hyung; Uncle Kkeokjeong
- **Role:** D-rank Hunter and veteran tank in the Peace Guild; after recovering from the Black Hunters’ attack and having both arms reattached, he continues as a Hunter while nearing the end of rehabilitation.
- **Personality:** Good-natured, sociable, modest about his family, and shamelessly confident about their age difference
- **Voice:** Hearty, casual, teasing, and quick to laugh
- **Relationships:** An old acquaintance of Jin Taekyung from the Ilsan manpower office; calls Taekyung his little brother, recommends him to Team Leader Choi, and remembers that Taekyung protected him during an E-Rank Gate attack; married with two children

### Lee Jungryong.md

# Lee Jungryong (이정룡)

- **Safe through:** Chapter 563
- **Aliases:** None
- **Role:** Former Vice Guild Master of Ares Guild, one of Korea's two S-rank Hunters, and a Supreme Peak-level martial artist who was killed by Jin Taekyung.
- **Personality:** Outwardly genial, calm, and humorous; calculating, opportunistic, manipulative, coercive, and ruthless when challenged
- **Voice:** Smooth, good-natured, and indirect, using teasing conversation and veiled threats before becoming openly furious
- **Relationships:** Master of Park Jihoon and Go Jun (Team Leader Seok), whom he personally selected and trained; longtime Great Cataclysm acquaintance of Park Tae Seop; adversary of Jin Taekyung; knew Team Leader Choi from childhood; has an antagonistic history with Kim Hwajong, who saved his life at the collapse of Mapo Bridge eighteen years earlier; was visibly shaken by learning that Choi is Cheon Taemin's maternal grandson; regards Cheon Taemin as an older brother despite no blood relation and has long held him in respect and fear; operates as Ares Guild's senior authority beneath its Guild Master

### Song Song.md

# Song Song (송송이)

- **Safe through:** Chapter 561
- **Aliases:** Miss Song
- **Role:** Founding member of the Peace Guild; B-rank healer whose buff magic is powerful enough to be mistaken for an A-rank healer's; Healer Team Leader and temporary head of the Peace Guild's emergency rescue team, which is piloting free public-safety rescues for medium- and low-grade Gates in the capital region.
- **Personality:** Calm, practical, capable, and attentive; speaks briefly and handles domestic work with practiced skill
- **Voice:** Calm, concise, polite, and capable of devastatingly blunt candor
- **Relationships:** Works alongside Team Leader Choi, Butler Kim, Im Kkeokjeong, and Jin Taekyung as a member of the Peace Guild; Jin recruited her to help run its emergency rescue team, while she remains his same-age friend and guildmate after rejecting his confession.

## Korean source

```text
＃564화



회사가 성장하면 가장 먼저 해야 할 것은 무엇인가.

사람에 따라 각자의 대답은 다르겠지만, CEO라면 누구나 가슴 한구석에 간직한 꿈이 있다.

바로 사옥 건축이다.

‘아니, 이 경우에는 증축이라고 해야 하나?’

길드 하우스 내부를 걷고 있던 나는, 문득 걸음을 멈추고 복도 아래에서 펼쳐지는 광경을 내려다보았다.

“거, 여기 중력 마법으로 자재 좀 올려 줘요!”

“자자, 주목. 탱커 출신 손.”

“저요.”

“여기도 있습니다. 그런데 왜요?”

“왜긴, 일 시키려고 그러지. 알아들었으면 이쪽으로 F급 다섯만 붙어. E급도 한두 명 끼워서.”

드드득. 쿵!

반질반질한 대리석이 허공을 오르내리고, 근육질의 거한들이 오함마를 휘두를 때마다 단단한 콘크리트 벽이 박살 난다.

부지런히 움직이는 백여 명의 인부들. 다들 각성자 출신이라 그런지 작업 속도가 장난 아니다.

물론 그만큼 급여도 비쌌지만, 주머니 두둑한 어느 젊은 대부호에게는 푼돈이나 다름없었다.



‘사람이 많아지니, 길드 하우스가 좁아졌네요.’



며칠 전 그 한마디를 툭 던진 최 팀장은 즉각 행동에 나섰다.

듣기로는 인근 부지를 웃돈까지 줘 가며 전부 매입해서 대대적인 중축에 착수했다고 하는데, 나야 뭐 그러려니 할 뿐이다.

‘어차피 내 돈 들어가는 것도 아니고.’

그리고 내 돈이 들어갈 구석은 따로 있다.

세금 한 푼 떼지 않은 50조의 자산은 용도에 따라 조금씩 줄어들고 있지만, 남은 돈에 비하면 새 발의 피에 불과하다.

‘50조라니…….’

다시 한번 생각해도 비현실적인 액수다. 마치 복도 너머에서부터 점점 가까워지는 한 사람의 모습처럼.

스으윽.

유령처럼 허공을 미끄러져 온 거구의 사내가 불쑥 입을 열었다.

「헤이, 기자회견 잘 봤어.」

“……?”

아니, 형이 거기서 왜 나와.

황당한 눈빛으로 매직 존슨을 바라보던 나는 간신히 입을 뗐다.

“뭡니까?”

「왜?」

“왜냐뇨. 그건 제가 드리고 싶은 말씀인데요. 왜 오늘도 여기 계세요?”

「잠깐 볼일이 있어서.」

“화장실 때문에 온 건 아니죠?”

「당연히 아니지. 최에게 전달해 줄 게 있어서 왔어. 겸사겸사 진도 보고.」

“이메일은 시리얼에 넣어서 먹습니까?”

「설마 내가 있어서 불편한 건 아니지?」

“설마 아니라고 생각하신 건 아니죠?”

칼 같이 받아치는 대답에 매직 존슨이 한숨을 푹 내쉬었다.

「헤이, 진. 나처럼 여린 사람은 그렇게 심한 말을 들으면 상처 입는다고.」

“……상처요?”

나는 그의 두꺼운 목과 강철같은 구릿빛 팔뚝을 바라보며 생각했다.

‘칼도 안 들어가게 생겼는데.’

흑형 근질 보소.

저 정도 피지컬이라면 지금 당장 마법사에서 근접 헌터로 이직해도 된다.

심지어 그냥 하는 말이 아닌 것이, 당장 인터넷에 ‘매직 존슨 스태프’를 검색해도 관련 영상이 주르륵 뜬다.

마법 쓰라고 만든 스태프로 오우거 골통을 일격에 빠갰다는 이야기는 이미 모르는 사람이 없을 정도이며, 헬스 커뮤니티에서는 도대체 저 스태프 중량이 어느 정도인지 의견이 분분할 지경이다.

‘그런 인간이 여리긴 개뿔이.’

내 그윽한 눈빛에 담긴 뜻을 알아챈 매직 존슨이 고개를 절레절레 내저었다.

「몸이 아니라 마음. 마음이 중요한 거야, 진.」

“마음이 여린 사람은 대격변을 버티지도 못해요. 강하니까 지금까지 살아남아서 영웅으로 불리는 거죠.”

「흐음. 칭찬인지 욕인지 헷갈리는데.」

“칭찬이라고 생각하세요.”

수상쩍다는 눈빛을 흘린 매직 존슨이 말을 이었다.

「어쨌든, 기자회견 잘 봤어. 상당히 의미심장하던걸.」

기자회견이라…….

나는 민망함에 뒤통수를 긁적였다.

대통령의 부탁으로 함께한 청와대 공식 기자회견은 엄청난 반향을 불러왔다.

듣기로는 국내 시청률만 70%를 돌파하고 외신에서도 크게 화제가 되었다던가.

이틀이 지난 지금도 관련 검색어가 실시간 검색어 상위권을 굳건히 지키고 있을 정도다. 그리고 아마 일주일 뒤에도 마찬가지겠지.

“방송 사고의 영향도 있고, 시청률이 좀 잘 나오긴 했죠. 존슨도 봤을 줄은 몰랐네요.”

「진의 행보는 미국에서도 늘 화제니까. 특히 몇몇 사람들에게는 프레지던트 백의 마지막 말이 의미심장하게 들렸을 거야. 물론 나도 그중 하나고.」

“아, 그거요.”

「미스터 리를 왜 그렇게 띄워 주나 했더니, 한 방 제대로 먹였군. 안 그래?」

“뭐. 제가 먹인 건 아니긴 한데…… 석고준 입장에서는 꼴 좀 받긴 했겠죠.”

지금이 춘추 전국시대는 아니지만, 그래도 거대한 집단을 물려받기 위해 정통성은 언제나 필요하다.

그리고 그런 측면에서 보자면 아레스 길드의 새로운 부길드장으로 취임한 석고준은 상당히 정통성이 떨어지는 편이었다.

「아레스 길드는 거대한 제국이야. 유언장에 따라 지분을 물려받았다 해도 미스터 리의 영향력까지 전부 이어받지는 못하지. 같은 핏줄이라면 아시아의 정서상 어느 정도 조건은 갖췄겠지만, 그것도 아니잖아?」

“이정룡 슬하에 아들이 있긴 했는데, 일찍 요절했다고 하더라고요. 각성하지 않은 일반인이라 지금까지 살아 있더라도 이정룡의 뒤를 잇지는 못했겠지만.”

현대의 길드는 무림 문파와 같다. 백면서생이 화산파 장문인이 될 수 없는 것처럼, 헌터로서의 힘과 권위를 지닌 이들이 길드장이 될 수 있는 것이다.

그 사실을 모를 리 없는 매직 존슨이 고개를 끄덕였다.

「맞는 말이지. 반면에 썩코춘 그 친구는 인격적인 결함과는 반대로 실력 하나는 좋으니까. 이번에 S급 헌터 자격 심사도 엄청난 점수로 통과했다더군. 물론 요즘 연달아 터지는 다른 이슈들 때문에 금방 묻히긴 했지만 말이야.」

“썩코춘이 아니라 석고준이요. 그리고 뭐, 그 자식은 어쨌든 이정룡 경호팀장이었잖아요.”

「그 정도로는 턱없이 부족해. 지금의 아레스 길드를 있게 만든 또 다른 개국 공신들의 지지가 필요하지. 하지만…….」

“시간이 부족했죠.”

「맞아. 시간. 아마 미스터 리는 만일의 상황을 대비해 유언장을 작성하면서도 자신이 그리 쉽게 죽을 거라곤 생각 못 했겠지.」

하지만 그는 결국 죽었고, 석고준은 후계자의 위치를 공고히 다지기도 전에 왕관을 물려받았다.

경호팀장이라는 직책은 최측근이었다는 증거지만, 아레스 길드라는 거대 집단을 모두 물려받기에는 여러 가지 애로사항이 많았다.

이정룡의 유언장이 있다고는 해도 나이 지긋한 원로들이 30대의 새파란 청년을 상관으로 깍듯하게 모시기란 쉽지 않다.

더군다나 석고준조차 이정룡 사후부터 급격히 무너진 모습을 보인 상황.

‘그런 와중에 시청률 70%짜리 청와대 공식 기자회견에서 대놓고 정통성을 부정당했으니…….’

백한성 대통령이 던진 한마디는 교묘하면서도 날카로웠다.

이번 변이 게이트에 관련된 아레스 길드를 돌려 깎기 식으로 비판함과 동시에, 이정룡의 생전 업적을 띄우며 내가 그의 유지를 잇는다고 포장해 버린 것이다.

‘완전히 짜고 치는 판이었지.’

이번 기자회견은 국회의원 시절부터 반(反) 아레스 성향을 띠고 있던 백한성 대통령과 최 팀장의 합작품이었다.

기자들을 포섭하고, 질문지를 던져 준 다음 원하는 방향으로 이야기를 이끈 것이다.

처음부터 끝까지 철저하게 준비된 대사와 배우.

만약 이정룡이 살아 있었다면 이번 시나리오는 폐기되었겠지만, 석고준에게는 새로운 언더독(Underdog)의 반란을 잠재울 만한 힘이 없었고 덕분에 우리는 무사히 촬영을 끝마쳤다.

국내 시청률 70%라는 훌륭한 흥행 성적과 외신의 스포트라이트를 한껏 받으며.

「어쨌든 또 한 번의 작은 승리로군. 이럴 때 샴페인이라도 한잔해야 하는데. 최는 어디 있지?」

“전에도 그랬지만, 요즘은 특히 눈코 뜰 새 없이 바쁘죠. 운 좋으면 지금쯤 본인 사무실에 있을 수도 있겠네요.”

「없어.」

매직 존슨이 어깨를 으쓱하며 덧붙였다.

「지금 막 들렀다 오는 길이거든.」

“아하. 무슨 일이 또 생기신 모양이네.”

새삼스러운 일도 아니다. 말이 팀장이지, 처음부터 최 팀장은 실질적인 길드장이나 다름없었고 지금에 이르러서는 세간의 인식도 그랬다.

아마 지금의 그는 대한민국을 통틀어 가장 바쁜 사람 중 하나일 것이다.

「헤이, 진. 같이 좀 걸을까?」

“좋죠. 으슥한 곳만 피하면요.”

「농담이 늘었군.」

“…….”

「……농담이라고 해 줘.」

나는 말 없이 걷는 속도를 올렸다. 부유하듯 허공을 밟으며 뒤따라온 매직 존슨이 투덜거렸다.

「진, 왜 자꾸 날 이상한 사람으로 만드는 거야?」

“자꾸 이상한 말씀을 하시니까 그렇죠.”

「그거야 당연히 장난이지. 그리고 나도 취향이라는 게 있는 사람이야. 진은 해당 사항 없다고. 저기 저 친구라면 모를까.」

매직 존슨의 시선을 따라간 곳에는, 훤칠하게 잘생긴 남자가 지나가고 있었다.

「못 보던 얼굴인데. 이번에 새로 들어온 길드원인가?」

“……누가 들으면 존슨도 우리 길드원인 줄 알겠어요. 아는 얼굴이 몇이나 된다고.”

「말도 안 되는 소리! 내가 저런 미남을 기억 못 할 리가 없지!」

“…….”

쓸데없이 단호한 거 뭔데.

이 방면으로는 귀신이네, 진짜. 작게 한숨을 내쉰 내가 대답했다.

“저도 이름은 잘 모르는데, 신입은 맞아요. 아마 C급이랬나?”

「전 길드장이 누군지는 모르겠지만 피눈물을 흘렸겠군. 저 정도 외모면 화제성도 충분한데. 스타 헌터로도 잘나갈걸?」

“말씀하신 전 길드장은 다른 일 때문에 피눈물 흘리고 있을걸요. 기자회견 때 워낙 개망신을 당해서.”

「아, 그럼 혹시?」

“예. 저 친구, 아레스 길드 소속이었어요.”

아레스 길드를 나와 평화 길드로 옮겼다는 것은, 단순히 이적을 의미하는 것이 아니다.

대강의 상황을 짐작한 매직 존슨이 중얼거렸다.

「철옹성이 흔들리고 있다는 산증인이군. 지금까지 아레스에서 몇 명이나 옮겼지?」

“숫자는 적어요. 열 명 남짓.”

「숫자가 중요한 게 아니지. 틈이 벌어지고 있다는 증거니까.」

나는 작게 고개를 끄덕였다. 외부의 시선으로 보일 정도라면 내부에서는 더 큰 균열이 일어나고 있을 것이다.

‘물론 석고준이 의도적으로 보낸 첩자일 확률도 무시할 수는 없지만.’

그렇기에 철저한 검증 과정을 통해 받아들였고, 조금씩 실전에 투입시킬 예정이라고 들었다.

시스템이 있는 나로서도 사람 속마음까지 꿰뚫어 볼 수는 없으니, 이 부분에 관해서는 최 팀장이 지닌 정보력이 큰 힘을 발휘할 것이다.

「그런데 저곳은 어디지? 보안이 상당히 철저해 보이는데.」

생각에 잠겨 말없이 걷고 있던 나는 문득 고개를 들었다.

매직 존슨의 손가락이 가리키는 방향에는 티타늄 합금으로 제작된 출입문이 있었다.

“아, 저거요. 훈련장입니다.”

「훈련장? 트레이닝 룸?」

“네.”

「맙소사. 무슨 트레이닝 룸이 저렇게 보안이 철저해?」

매직 존슨이 실소를 흘리며 물었다.

「중첩 마법만 다섯 개라니. 물론 훈련 과정을 남에게 보여 주기 싫을 수도 있지만…… 길드 하우스 내부라는 걸 감안하면 과하지 않나?」

“글쎄요.”

나는 말을 아꼈다. 어차피 저 트레이닝 룸은 극소수의 사람들만을 위해 마련된 공간이다.

이를테면…….

‘진가심법을 수련하는 사람들에 한해서지.’

이건 아직 매직 존슨에게도 말하지 않은 비밀이다. 최 팀장과 김 집사, 그리고 송송이와 임꺽정에게만 허락한 영역이기도 했다.

「보안 수준을 보아하니, 길드원 모두에게 개방된 공간은 아닌 듯싶은데.」

그의 예리한 지적에 내가 고개를 끄덕였다.

“정확합니다. 저를 포함한 길드 초기 멤버들 전용이에요.”

「으흠. 비밀이란 말이지. 그렇게 말하니까 마법사로서의 탐구 정신이 깨어나는 것 같은데.」

“다시 재우세요.”

「정말 너무하는군. 잠깐 구경하는 것도 안 되나?」

순간 멈칫한 내가 손을 내저었다.

“안 됩니다. 안에 사람 있어요.”

「누구? 혹시, 최?」

“아뇨.”

갑자기 씁쓸해지는 기분을 느끼며, 나는 말을 이었다.

“누구보다 수련이 간절한 사람이요.”

「……?」

“있습니다. 그런 사람이.”

지금 당장은 눈으로 보지 못하지만, 머릿속에서는 선명한 이미지가 떠오른다.

비 오듯 땀을 흘리며 훈련을 거듭하는 어느 중년 헌터의 모습이.

누구보다 괜찮은 척하지만, 무참히 꺾여버린 마음으로 다시 일어서려는 그의 의지가.

‘슬슬…… 그걸 시작해 봐야 하나.’

순간 내 머릿속을 스친 어떤 생각은, 뒤이어 흘러나온 매직 존슨의 말을 들으며 서서히 실체를 갖춰 갔다.

「어쩔 수 없군. 최를 만나면 전해 줘.」

“네? 뭘요?”

「이거.」

스으윽.

미세한 기의 흐름과 함께 품 안을 파고드는 자그마한 물체.

칩의 존재를 확인하고 고개를 든 나는 볼 수 있었다. 심각하게 굳어진 대마도사의 얼굴을.

「한국과 미국뿐만이 아니야. 전 세계에서 마력 수치가 폭등하고 있어. 전년도 대비 7% 상승. 행운의 숫자가 이렇게 불길하게 느껴지는 건 처음이군.」

“……!”
```

## Final English reading copy

```markdown
# Chapter 564

When a company grows, what is the first thing it should do?

Everyone would have a different answer, but every CEO has a dream tucked away somewhere in their heart.

Building their own headquarters.

*Or should I call it an expansion in this case?*

I was walking through the Guild House when I suddenly stopped and looked down at the scene unfolding below in the hallway.

“Hey, could you use gravity magic to lift some of these materials?”

“All right, listen up. Any former tanks here?”

“Me.”

“I’m one, too. Why?”

“Why do you think? To put you to work. If you understand, five F-ranks get over here. Add one or two E-ranks, too.”

*Grrrind. Boom!*

Smooth marble rose and fell through the air, while every swing of the muscle-bound giants’ sledgehammers smashed apart the solid concrete walls.

More than a hundred workers moved busily about. Maybe it was because they were all Awakened, but they worked at an incredible pace.

Of course, their wages were just as expensive. But to a young tycoon with deep pockets, it was little more than pocket change.



*Now that there are more people, the Guild House has gotten cramped.*

Team Leader Choi had casually tossed out that one remark a few days ago, then immediately taken action.

I heard he had bought up all the nearby plots of land, even paying above market value, and begun a massive expansion. As for me, I could only shrug.

*It’s not like any of my money is going into it.*

And there were other places where my money would be going.

My fifty trillion in assets, not a penny of which had been taken in taxes, was slowly shrinking depending on how I used it. But compared to what remained, the amount spent was barely a drop in the ocean.

*Fifty trillion…*

Even thinking about it again, it was an absurd amount of money. Like the figure of a man gradually approaching from beyond the corridor.

*Swoosh.*

A huge man glided through the air like a ghost before suddenly speaking.

“Hey, I watched the press conference.”

“……”

*Wait. What are you doing here, hyung?*

I stared at Magic Johnson in disbelief, then finally managed to open my mouth.

“What is it?”

“Why?”

“Why? That’s what I want to ask you. Why are you here again today?”

“I had something to take care of.”

“You didn’t come because you needed to use the bathroom, did you?”

“Of course not. I came to give Choi something. I figured I’d check on the progress while I was here.”

“Do you put emails in cereal and eat them?”

“Surely you’re not uncomfortable because I’m here?”

“Surely you didn’t think I was comfortable?”

Magic Johnson sighed deeply at my immediate retort.

“Hey, Jin. Sensitive people like me get hurt when they hear such harsh words.”

“…Hurt?”

I looked at his thick neck and iron-hard, bronze-colored arms.

*He looks like a knife couldn’t even get through him.*

*Damn, that Black dude is jacked.*

With a physique like that, he could quit being a mage and switch to being a melee Hunter right now.

And I wasn’t just saying that. Even if you searched for “Magic Johnson’s staff” on the internet right now, page after page of related videos would come up.

Practically everyone had heard the story about how he had smashed an ogre’s skull with a single blow using a staff designed for casting magic. Even the fitness community was divided over exactly how heavy that staff was.

*That man is calling himself sensitive? Give me a break.*

Magic Johnson realized what my deep stare meant and shook his head.

“It’s not the body. It’s the heart. The heart is what matters, Jin.”

“A sensitive person couldn’t survive the Great Cataclysm. You survived this long and became a hero because you’re strong.”

“Hmm. I can’t tell whether that was a compliment or an insult.”

“Take it as a compliment.”

Magic Johnson gave me a suspicious look before continuing.

“Anyway, I watched the press conference. It was quite meaningful.”

The press conference…

I scratched the back of my head, embarrassed.

The official Blue House press conference I had attended at the President’s request had caused an enormous stir.

I heard domestic viewership had broken seventy percent, while it had also become a major topic in the foreign press.

Even two days later, the related search terms were still firmly near the top of the real-time rankings. They probably would be a week from now, too.

“The broadcasting accident probably helped, and the ratings did turn out pretty well. I didn’t know you had watched it, Johnson.”

“Jin’s every move is always a topic of conversation in the United States. For some people in particular, President Baek’s final words must have sounded quite meaningful. I was one of them, of course.”

“Oh, that.”

“I was wondering why he was praising Mr. Lee so much. Then he landed one hell of a blow, didn’t he?”

“Well, I wasn’t the one who landed it exactly… But I’m sure it really got under Go Jun’s skin.”

The world was no longer in the Warring States period, but legitimacy was still necessary for anyone who wanted to inherit a massive organization.

And in that respect, Go Jun, who had taken office as Ares Guild’s new Vice Guild Master, had very little legitimacy.

“Ares Guild is a vast empire. Even if he inherited the shares according to the will, he didn’t inherit all of Mr. Lee’s influence. If they had shared blood, he would at least have met certain expectations in Asian society. But he doesn’t, does he?”

“Lee Jungryong did have a son, but I heard he died young. Even if he had still been alive, he wouldn’t have inherited Lee Jungryong’s position, since he was an ordinary person who never Awakened.”

Modern Guilds were like Murim sects. Just as a bookish scholar could not become the Sect Leader of Huashan, only those with the power and authority of a Hunter could become a Guild Master.

Magic Johnson knew that as well as anyone and nodded.

“That’s right. On the other hand, that Sseokkochoon fellow has plenty of skill despite his character flaws. I heard he passed the S-rank Hunter qualification assessment with an incredible score this time. Of course, all the other issues erupting in succession these days quickly buried the news.”

“His name is Go Jun, not Sseokkochoon. And anyway, that bastard was Lee Jungryong’s Head of Security.”

“That’s nowhere near enough. He needs the support of the other founding heroes who made Ares Guild what it is today. But…”

“He didn’t have enough time.”

“Exactly. Time. Even while preparing a will in case of the worst, Mr. Lee probably never imagined that he would die so easily.”

But he had died in the end, and Go Jun had inherited the crown before he could firmly establish himself as the successor.

Being Head of Security was proof that he had been one of Lee Jungryong’s closest aides, but there were many difficulties involved in inheriting an enormous organization like Ares Guild.

Even with Lee Jungryong’s will, it would not be easy for elderly veterans to respectfully serve a fresh-faced man in his thirties as their superior.

And on top of that, Go Jun himself had visibly begun to crumble after Lee Jungryong’s death.

*And in the middle of all that, his legitimacy was openly denied during an official Blue House press conference with seventy percent viewership…*

President Baek Hanseong’s single remark had been subtle and sharp.

He had indirectly criticized Ares Guild over the Mutated Gate while praising Lee Jungryong’s achievements and presenting me as the man who would carry on his legacy.

*The whole thing was rigged from start to finish.*

The press conference had been a joint production by President Baek Hanseong, who had shown an anti-Ares stance since his days as a lawmaker, and Team Leader Choi.

They had won over the reporters, handed them questions, and led the conversation in the direction they wanted.

A script and cast prepared with absolute thoroughness from beginning to end.

If Lee Jungryong had still been alive, the scenario would have been scrapped. But Go Jun did not have the power to suppress the rebellion of a new underdog, so we had managed to finish the shoot without incident.

With the excellent domestic rating of seventy percent and the full glare of the foreign press upon us.

“Either way, it’s another small victory. This would be the time to celebrate with a glass of champagne. Where’s Choi?”

“He was busy before, but these days he’s especially swamped. If we’re lucky, he might be in his office right now.”

“He’s not.”

Magic Johnson shrugged and added,

“I just stopped by there on my way here.”

“Ah. So something else must have come up.”

It was hardly surprising. Team Leader Choi might have been called a team leader, but he had effectively been the Guild Master from the beginning, and by now, that was how the public saw him, too.

He was probably one of the busiest people in all of Korea.

“Hey, Jin. Want to walk together?”

“Sure. As long as we avoid secluded places.”

“You’ve gotten funnier.”

“……”

“Tell me that was a joke.”

I silently increased my walking speed. Magic Johnson followed behind, stepping through the air as though he were floating, and grumbled.

“Jin, why do you keep making me seem like a strange person?”

“Because you keep saying strange things.”

“Obviously, I’m joking. And I have preferences, too, you know. You’re not my type. That guy over there might be, though.”

Following Magic Johnson’s gaze, I saw a tall, handsome man walking past.

“I haven’t seen that face before. Is he a new Guild member?”

“Who would hear you and not think you were a Guild member? How many people here do you even know?”

“That’s ridiculous! There’s no way I could fail to remember a handsome man like that!”

“……”

*Why was he so needlessly adamant about that?*

When it came to this sort of thing, his instincts were downright uncanny.

I let out a small sigh before answering.

“I don’t know his name very well either, but he’s definitely new. I think he’s C-rank.”

“I don’t know who the former Guild Master was, but he must be crying tears of blood. Someone that handsome would have plenty of publicity value. He could make a name for himself as a star Hunter, too.”

“The former Guild Master you mentioned is probably crying blood over something else. He was humiliated pretty badly during the press conference.”

“Oh. Then, could it be…?”

“Yes. That guy used to belong to Ares Guild.”

Leaving Ares Guild and transferring to Peace Guild did not simply mean changing jobs.

Magic Johnson seemed to guess the general situation and muttered,

“He’s living proof that an iron fortress is beginning to shake. How many people have transferred from Ares so far?”

“Not many. Around ten.”

“The number isn’t important. It’s proof that a crack has opened.”

I nodded faintly. If the fracture was visible to outsiders, then an even larger crack must have formed on the inside.

*Of course, we can’t rule out the possibility that Go Jun sent him deliberately as a spy.*

That was why he had been accepted only after a thorough verification process, and I heard they planned to deploy him in actual operations little by little.

Even with the System, I couldn’t see straight through people’s hearts. In that regard, Team Leader Choi’s intelligence network would be a tremendous asset.

“But what’s that place? The security looks pretty serious.”

I had been walking in silence, lost in thought, when I suddenly looked up.

In the direction Magic Johnson pointed stood a door made of titanium alloy.

“Oh, that? It’s the training room.”

“The training room? A training room?”

“Yes.”

“My goodness. What kind of training room needs security that intense?”

Magic Johnson gave a short, incredulous laugh.

“Five overlapping spells? I can understand not wanting other people to see your training, but isn’t that excessive considering it’s inside the Guild House?”

“Who knows?”

I kept my answer brief. That training room had been prepared for only a handful of people.

More specifically…

*For those training the Jin Family’s Cultivation Technique.*

It was a secret I had not even told Magic Johnson yet. It was an area permitted only to Team Leader Choi, Butler Kim, Song Song, and Im Kkeokjeong.

“Judging by the security, it doesn’t seem like a space open to every Guild member.”

His sharp observation made me nod.

“That’s exactly right. It’s for the Guild’s founding members, including me.”

“Hmm. So it’s a secret. Hearing you say that makes my spirit of inquiry as a mage awaken.”

“Put it back to sleep.”

“You’re really too much. I can’t even take a quick look?”

I hesitated for a moment, then waved my hand.

“No. There’s someone inside.”

“Who? Is it Choi?”

“No.”

A sudden bitterness welled up inside me as I continued.

“Someone more desperate to train than anyone else.”

“……”

“There is such a person.”

I couldn’t see him with my own eyes at the moment, but a vivid image rose in my mind.

A middle-aged Hunter training again and again, sweat pouring from him like rain.

A man who tried harder than anyone to pretend he was fine, yet willed himself to stand again after his spirit had been brutally crushed.

*Should I start that soon…?*

A thought flashed through my mind. Then, as I listened to Magic Johnson’s next words, it slowly began to take shape.

“Well, it can’t be helped. Give this to Choi when you see him.”

“Give him what?”

“This.”

*Swoosh.*

A small object slipped into my clothes on a faint current of energy.

I confirmed the presence of the chip and looked up.

The Grand Mage’s face had hardened into grim seriousness.

“It’s not only Korea and the United States. Mana levels are skyrocketing all over the world. They’re up seven percent compared to last year. This is the first time a lucky number has felt so ominous.”
```
