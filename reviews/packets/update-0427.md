<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0427.txt",
      "sha256": "9b4428e00778311ee0de52cc28b0ee61263792f94a696021d7f60d153b578242",
      "bytes": 13836
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "0f8248326672c2f1e9471c2c5d83ab7c3024492a69ecb5d1d5ea89272cc5ba3f",
      "bytes": 1745
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "d7e0788e810ee3578a703bd7e4aeaa3c1062be624a2fae8640786ee3b65ca3fb",
      "bytes": 141048
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "4a373afa751eb1b2f6a7df2abe6afd46a7bf35cf4752e9a30fc4bea8ecacc42d",
      "bytes": 533
    },
    {
      "path": "characters/Felix.md",
      "sha256": "4f66db9750506c2ffe7c79c9262f6a822de31d8d69baf7a9feb13365ad74cf49",
      "bytes": 464
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "bf2a4503d8e1bf291e2e241be001402213d8ae88ac3ff759beb07f44e16b2e5f",
      "bytes": 1286
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "84e4ba348e823f2d1f29cdb25d6c91fde3a61511739210e1d23eba23e844cd60",
      "bytes": 622
    },
    {
      "path": "characters/Lee Jungryong.md",
      "sha256": "6dd7ac0bda1efb4c41556a236227433cf5850a7861d3a418398f3f71541bb3d2",
      "bytes": 1182
    },
    {
      "path": "characters/Team Leader Choi.md",
      "sha256": "ff1de68bb66878ba92627ef151e5105fcfbc08aaecd61b7983c7b31b300e1316",
      "bytes": 575
    },
    {
      "path": "characters/Wu Heixing.md",
      "sha256": "5754ef900d4536dd87efb007c66c7b51446ac44caad28a2b4c1bd6c4d85d3ecc",
      "bytes": 795
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "7b376808cb65ab14dd4b344534eed1342e8fed53811e057916ec3345836c7699",
      "bytes": 130845
    }
  ],
  "estimated_tokens": 11082
}
-->

# Durable State Update — Chapter 427

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 427. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 427. Profile updates may replace only one
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
  "chapter": 427,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 427,
    "continuity_sources": [427],
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
    "One Annihilation destroyed the Arch Lich's manifested body, the unfinished Gate, and the surrounding city structures.",
    "The Arch Lich's remaining soul fragment was erased by the golden soul within Hero's Soul; the soul was identified as a remnant of Lei Fei's will.",
    "Jin exhausted all his strength and fell unconscious after the attack.",
    "The Skeleton King caught Jin, retrieved Hero's Soul, and remains Jin's ally.",
    "The Skeleton King sensed that Hero's Soul had lost its former mystical quality after its golden light pursued the Arch Lich's black energy, then stored the sword between its pelvic bones.",
    "The hidden elite Death Knights, Liches, and Wyverns attacked the main battlefield after the S-rank Hunters departed, but the monster army was reduced to ash and the war ended.",
    "The Quest One Who Returned from Death remains active, keeping Login unavailable until the Quest ends."
  ],
  "continuity_sources": [
    426,
    425
  ],
  "open_questions": [
    "What is Hero's Soul's current condition after its golden light pursued and erased the Arch Lich's soul fragment?",
    "When will Jin regain consciousness, and what condition will he be in?",
    "What caused the mass ashfall that destroyed the monsters on the main battlefield?",
    "What is Asmodeus's current status and location?"
  ],
  "safe_through": 426,
  "temporary_decisions": [
    "Render 스켈레톤 킹 as Skeleton King and 골골이 as Bones.",
    "Render 영웅의 혼 as Hero's Soul and 치유의 빛 as the light of healing.",
    "Render 라이프 포스 베슬 as Life Force Vessel.",
    "Preserve the Arch Lich's archaic, contemptuous register and Jin's profanity."
  ],
  "version": 1
}
```

## Exact glossary matches

| 진태경    | **Jin Taekyung**   |
| 최민우    | **Choi Minwoo**   |
| 이정룡    | **Lee Jungryong** |
| 상태               | **Status**                     |
| 헌터      | **Hunter**            |
| 게이트     | **Gate**              |
| 몬스터     | **monster**           |
| 길드      | **Guild**             |
| 길드장     | **Guild Master**      |
| 힐러      | **healer**            |
| 대격변     | **Great Cataclysm**   |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 필릭스 | **Felix** | British prince and S-rank Hunter. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 우헤이싱 | **Wu Heixing** | Chinese S-rank Hunter who provokes Jin and nearly draws his sword. |
| 평화 | **Peace Guild** | Guild name. |
| 아레스 | **Ares Guild** | The leading Guild in Korea; formerly employed Team Leader Choi and Song Song. |
| 대리 | **Assistant Manager** | Corporate title used by Kim Seonhee |
| 주신 | **God of Drinking** | Wipeng's drinking epithet. |
| 태자 | **Crown Prince** | Title of the Emperor's older brother who was reportedly assassinated. |
| 대위 | **captain** | Military rank held by Yoo Sijin. |
| 고려일보 | **Goryeo Daily** | Daily newspaper carrying a feature on Taekyung. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 꼬리 | **the “tail”** | Codename for the Black Hunter traced by Butler Kim. |
| 미국 | **United States** | Country associated with the talk show and CNM. |
| 영국 | **United Kingdom** | Country associated with BCC. |
| 중국 | **China** | Country from which Team Leader Choi’s video originates. |
| 리치 | **Lich** | Named Monster; fallen archmage and apex undead monster. |
| 쓰촨성 | **Sichuan Province** | Source spelling variant of the established Sichuan location. |
| 주석 | **Chairman** | Political title used for Xiao Yang. |
| 화타 | **Hua Tuo** | Historical physician invoked in Taekyung's comparison for Mungyeong's future medical skill. |
| 중화 | **Zhonghua** | Patriotic term used in Shao Shen’s rallying speech. |
| 태자당 | **Crown Prince Party** | The faction associated with General Liao. |
| 소멸 | **Erasure** | Jin's term for the Skeleton Warlord's destruction by the Arch Lich's mana. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 상인 | 청년 | stranger_to_stranger | Young Brother | formal-polite | A merchant uses 소형제 after noticing the young man's sword, and the young man approves of the address. |
| 청년 | 상인 | stranger_to_stranger | friend | casual and shameless | The young man declares that they should be friends after drinking their Yeoahong. |
| 이정룡 | 진태경 | senior S-rank Hunter to younger Hunter and adversary | Young man | polished, teasing, and veiled-threatening | Uses a genial tone and indirect threats while trying to make Taekyung release the captives. |
| 진태경 | 이정룡 | younger Hunter to senior S-rank Hunter and adversary | you | polite but mocking and defiant | Taekyung answers Lee's soft threats with the wolf-and-tiger metaphor and refuses to yield. |
| 신의 | 진태경 | physician_to_benefactor | Young Master Jin | formal-polite | The Divine Physician addresses Taekyung as 진 공자 while expressing concern for his injuries. |
| 우헤이싱 | 진태경 | hostile S-rank Hunter to foreign Hunter and provocation target | peninsula bangzi | insulting and confrontational | Wu repeatedly addresses Jin with anti-Korean slurs. |
| 우헤이싱 | 이정룡 | younger S-rank Hunter to senior Ares Guild authority | Mr. Lee | formal and deferential | Wu addresses Lee respectfully despite his usual hostility toward Koreans. |
| 필릭스 | 이정룡 | British prince to senior S-rank Hunter | Jungryong Lee | formal through a translation device | Felix permits Lee to omit His Highness and gives his own preferred form of address. |
| 진태경 | 필릭스 | Korean S-rank Hunter addressing a British prince | His Highness | mock-formal and sarcastic | Felix demands formal address, and Jin complies by calling him His Highness while continuing to mock him. |
| 진태경 | 청년 | celebrated Hunter to younger fellow Hunter | young man | casual, teasing, and profane | Jin addresses the young Hunter after overhearing his criticism and deliberately switches to casual speech. |
| 청년 | 진태경 | frightened junior Hunter to celebrated senior Hunter | you | fearful and deferential | The young Hunter uses 당신 while asking whether Jin is really the person he recognizes from the media. |
| 진태경 | 우헤이싱 | adversarial S-rank Hunters | you idiot | insulting-casual | Mocks Wu's cowardice and orders him to stop complaining. |
| 이정룡 | 우헤이싱 | senior S-rank Hunter to younger allied S-rank Hunter | Mr. Wu | polished and formally coaxing | Lee publicly draws Wu into agreement with the suicide-squad plan. |
| 최민우 | 진태경 | trusted allied team leader to younger allied Hunter | Mr. Jin | formal-polite and concerned | Choi warns Jin about the danger of the operation and affirms his deep trust. |
| 진태경 | 최민우 | younger allied Hunter to allied team leader | Team Leader Choi | polite, familiar, and teasing | Jin jokes with Choi while acknowledging and dismissing his concern. |
| 필릭스 | 진태경 | British prince and S-rank Hunter to allied Korean S-rank Hunter | Jin | lofty and aristocratic | Felix addresses Jin while discussing royal duty and their teleport. |

## Listed compact profiles

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 426
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who has sworn never to kill again.
- **Personality:** Publicly reputed to be selfless and devoted to treating patients in the lowest places.
- **Voice:** Not established.
- **Relationships:** Mungyeong is the Divine Physician's true identity, and Dong Feng is his Disciple.

### Felix.md

# Felix (필릭스)

- **Safe through:** Chapter 415
- **Aliases:** Prince Felix
- **Role:** British prince and S-rank Hunter who joins the reinforcement force against the Arch Lich.
- **Personality:** Haughty, self-important, and conscious of royal duty.
- **Voice:** Formal, lofty, and aristocratic.
- **Relationships:** Travels with Faye Chen and Magic Johnson and is allied with Jin Taekyung.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 426
- **Aliases:** Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan, Jeok Cheongang's publicly acknowledged Disciple and the Fire Gate Clan's nineteenth successor, and a Supreme Peak master who has manifested Force, opened his Middle Dantian, and crossed the wall into true mastery.
- **Personality:** Hungry, self-aware, dryly observant, pragmatic under pressure, and willing to risk himself for people he has accepted as real. Treats impossible situations like games until their human cost becomes undeniable.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, Jeok Cheongang is his Master, Cheongpung is his trusted companion and only true martial rival, Choi Minwoo is his subordinate and student, his mother and sister Hayeon are among those he protects, and the Skeleton King is his friend and ally.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 426
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Lee Jungryong.md

# Lee Jungryong (이정룡)

- **Safe through:** Chapter 425
- **Aliases:** None
- **Role:** Former Vice Guild Master of Ares Guild, one of Korea's two S-rank Hunters, and a Supreme Peak-level martial artist who was killed by Jin Taekyung.
- **Personality:** Outwardly genial, calm, and humorous; calculating, opportunistic, manipulative, coercive, and ruthless when challenged
- **Voice:** Smooth, good-natured, and indirect, using teasing conversation and veiled threats before becoming openly furious
- **Relationships:** Master of Park Jihoon and Go Jun (Team Leader Seok), whom he personally selected and trained; longtime Great Cataclysm acquaintance of Park Tae Seop; adversary of Jin Taekyung; knew Team Leader Choi from childhood; has an antagonistic history with Kim Hwajong, who saved his life at the collapse of Mapo Bridge eighteen years earlier; was visibly shaken by learning that Choi is Cheon Taemin's maternal grandson; regards Cheon Taemin as an older brother despite no blood relation and has long held him in respect and fear; operates as Ares Guild's senior authority beneath its Guild Master

### Team Leader Choi.md

# Team Leader Choi

- **Safe through:** Chapter 420
- **Aliases:** Choi Minwoo (최민우)
- **Role:** Allied team leader and Hunter who analyzes battlefield conditions during the Arch Lich operation.
- **Personality:** Calm, analytical, and steady under extreme battlefield pressure.
- **Voice:** Measured and logical, using clear tactical explanations.
- **Relationships:** Works alongside Jin Taekyung and the coalition opposing the Arch Lich, trusts Jin deeply, and leads allied fighters in battle.

### Wu Heixing.md

# Wu Heixing (우헤이싱)

- **Safe through:** Chapter 420
- **Aliases:** None
- **Role:** Wu Heixing was a Chinese S-rank Hunter known for frequent media exposure and scandal who secretly practiced martial arts, including an internal-energy cultivation technique and fist-and-foot martial arts, before Jin Taekyung killed him.
- **Personality:** Arrogant, status-conscious, abusive, and fiercely proud of his power, he responds to humiliation with anger and protects himself even while his allies die.
- **Voice:** Loud, insulting, entitled, and dependent on national and political status.
- **Relationships:** He is openly hostile toward Jin Taekyung and Faye Chen, and resents Jin receiving Chairman Shao Yang's attention.

## Korean source

```text
＃427화



눈이 펑펑 쏟아지던 12월의 겨울밤이었다.

분명 평소보다 맑은 날씨일 거라는 일기예보를 믿고 거리를 바삐 오가던 사람들은 어리둥절했고, 기상청은 당황했다.

“뭐야. 뭐가 문제야?”

“분석 중입니다. 분명 이럴 리가 없는데.”

“우박만 한 눈이 쏟아지는데 이럴 리가 없기는, 흰소리 늘어놓지 말고 자료를 가져와. 실시간 관측 현황 있을 거 아냐!”

“지, 지금 살펴보는 중인데…… 아, 중국 쓰촨 지역에서 마나 급등으로 이상 현상이 생긴 것 같습니다. 예상 적설량이 장난 아니에요.”

“쓰촨? 빌어먹을. 아크 리치라는 놈이 이제는 날씨까지 조종하나?”

대격변 이후 각종 마법을 도입하여 예언에 가까운 일기예보를 내보내던 기상청이었다.

그리고 부랴부랴 재관측에 들어간 지 한 시간 뒤, 기상청은 전국에 대설주의보를 발령했다. 약 30년 만의 기록적인 폭설이 내릴 거라는 게 그들의 결론이었다.

하지만 집으로 걸음을 재촉하던 사람들은 얼마 지나지 않아 걸음을 멈출 수밖에 없었다.

어디에나 있는 번화가. 그 중심부에 설치된 대형 스크린에서 흘러나온 한마디 때문이었다.

- 오늘 같은 날. 이와 같은 소식을 전해드리게 되어 기쁘고 감격스럽습니다.

스크린에 등장한 것은 늙은 동양인 남성이었다.

그의 뒤로 유엔 안전 보장 이사회에 속한 각국의 지도자들이 앉아 있었고, 중화 인민공화국의 주석은 붉어진 눈가와 축축한 목소리로 수많은 마이크를 향해 입술을 뗐다.

- 아크 리치가 소멸했습니다. 우리는…… 승리했습니다.

승리.

그 한 단어로 족했다. 약 한 달. 정확히는 34일 동안 이어진 사상 초유의 몬스터 웨이브.

쓰촨성을 넘어 세계를 불안에 떨게 했던 대전쟁이 막을 내렸다는 소식에 사람들은 멍하니 입을 벌렸고, 이내 거대한 환호성을 내질렀다.

“와아아아아!”

“잠깐! 잠깐만요. 저 못 들었어요. 방금 뭐라고 한 거예요?”

“……났대요!”

“예?”

“자막! 자막 보세요!”

“아크 리치 소멸…… 어어, 진짜네! 으와아아아악! 시발 예비군 끌려가는 줄 알았는데!”

삼십 분에 걸친 샤오 양 주석의 발표도, 이후 마이크를 이어받은 유엔 안전 보장 이사회 대변인의 추가 설명도 그들에게는 들리지 않았다.

아크 리치가 소멸함으로써 수많은 언데드 군단 역시 힘을 잃고 궤멸 되었고, 마침내 모두가 바라던 평화가 찾아온 것이다.

“엄마, 난데. 어어. 뉴스 봤어? 안 봤어? 빨리 봐 봐. 응, 응!”

“안 되겠다. 김 대리, 우리 3차 가자!”

“3차요? 내일 서버 업데이트 날인데요. 노 과장님이 지랄할 텐데.”

“노 과장도 온대. 법카 들고.”

“하, 그 인간 얼굴 보기 싫은데. 좋습니다. 일단 가시죠.”

“단결. 예, 대대장님. 저 대위 이준범입니다. 저 휴가 하루만 더 연장할…… 아닙니다. 죄송합니다.”

애써 불안함을 무시하며 밖을 오가던 사람들은 환호와 함께 술집으로 달려갔고, 제2의 대격변을 예견하며 집에 있던 이들도 거리로 쏟아져 나와 축제 분위기에 동참했다.

자정이 지나도 환호는 가라앉지 않았다.

다음 날도, 또 그다음 날도…….

이 기념비적인 승전보에 전 세계는 숯불 위 가마솥처럼 들끓었고, 연일 각국의 언어로 새로운 기사를 쏟아냈다.

오죽했으면 사흘 내내 한국에 내렸던 폭설보다 이번 승리에 관한 뉴스와 기사가 더 많다는 말이 나올 정도였다.

그리고…… 이 모든 기사에서 빠지지 않고 등장하는 한 사람의 이름이 있었다.



[미국 뉴욕 타임즈, ‘위대한 승리, 새로운 영웅.’]

[영국 더 타임즈, ‘새롭게 떠오른 동방의 별. 필릭스 왕자와의 친분?’]

[일본 아사히 신문, ‘진태경은 아시아의 자랑. 하지만 일본의 1군 헌터들이라면 그를 뛰어넘을 수 있다!’]

[중국 인민 일보, ‘수많은 인민을 구한 한국의 젊은 협객. 그리고 중화가 낳은 천재 우헤이싱의 비통한 죽음.’]

[중국 청년 소식지, ‘진태경은 명나라 장수 진린(陳璘)의 후손. 그에게는 틀림없는 중화의 핏줄이 흐르니 머지않아 귀화할 것,’]

[한국 고려일보, ‘아레스 부 길드장, 이정룡 헌터(68세). 사망 유력…….’]

[한국 다스 패치 관계자, ‘몇 달 전부터 진태경에 대해 총력을 기울여 조사했지만 어떤 것도 알아낼 수 없었다. 그의 여자관계는 놀랍도록 깨끗했다.’ 많은 연애를 했음에도 깔끔하게 헤어진 거냐 묻는 기자의 질문에, ‘아니. 그게 아니라 모태솔로라고.’ 일축.]



각종 언론 매체에 있어 진태경의 존재는 그야말로 크리스마스 선물이나 다름없었다.

모든 스포트라이트가 쏠렸고 그에 관한 온갖 이야기가 흘러나왔다.

소재는 무궁무진했다. 이른바 ‘겨울 전쟁’이라 명명된 이번 몬스터 웨이브에 관련된 것은 말할 것도 없었고, 지금의 위치에 오르기까지 있었던 과거 행적과 사소한 사생활까지 뉴스 거리였다.

평소였다면 기레기라며 욕을 한 바가지씩 처먹었을 찌라시성 기사도 흥미를 끌었다.

그만큼 전 세계의 관심은 이 위대한 승리를 견인한 새로운 영웅에게 쏠려 있었다.

하지만 그 모든 관심이 긍정적인 것만은 아니었다.

철통같은 내부 보안에서 조금씩 새어 나간 정보들에 의해 의문을 제기하는 이들이 나타난 것이다.



[종전 후 4일. 그날, 위대한 승리의 뒷면에는 무엇이 감춰져 있었을까. 진태경을 둘러싼 의문점들.]

[이정룡 사망 추정. 우헤이싱의 미심쩍은 죽음. 두 S급 헌터의 죽음과 새로운 영웅의 비상.]

[당신 현장에 있던 연합군 수뇌부 비밀리에 증언, ‘치열한 전투라고 하기에는 발견 당시 진태경의 신체는 별다른 상처가 보이지 않았다. 포션 사용 여부에 대해서는 조사 중. 그가 의식을 회복한다면 모든 정황이 확실해질 것.’]



비록 극소수에 불과했지만, 조금씩 등장하는 음모론에 인터넷에서는 치열한 갑론을박이 펼쳐졌다.

이와 같은 찌라시성 기사는 악플과 신고 세례를 견디지 못하고 금방 사라졌으나 몇몇 대중들에게 의문을 심어 주었고, 마침내 사람들의 이목은 한 가지에 집중되었다.

진태경.

과연 그가 언제쯤 모습을 드러낼 것인지에 대해서.



* * *



삐빅. 삑.

최신식 의료기기가 기계음을 토해 냈다.

극소수만이 드나들 수 있는 병실의 한 자리를 차지한 사람들은, 산소호흡기를 착용한 채 누워 있는 진태경을 근심 어린 표정으로 바라보았다.

「진 선생의 상태는 어떻소?」

샤오 양 주석의 물음에 최민우가 대답했다.

「항상 같습니다. 모든 것이 지극히 정상인데, 이상하게 정신을 차리지 못하고 있다더군요.」

「두 사람 모두 그렇게 말했소?」

「예. 원인을 모르겠답니다.」

「허어. 그렇다면 틀림없을 터인데…… 도대체 어째서 의식을 회복하지 못하는 건지.」

샤오 양 주석은 한숨을 내쉬었다.

그가 앞서 말한 두 사람이란 치료 분야에서 최고를 달리고 있는 이들이다.

한 사람은 화타의 현신이라 불리는 민간 의사고, 또 다른 한 사람은 세계에서 손꼽히는 탑 클래스의 힐러였다.

진태경의 임시 주치의로 초빙해 온 두 사람이 그리 말했다면 틀림없었다.

「가족분들께서 와 계시다고 들었소만.」

「저희 평화 길드 측에서 잘 모시고 있습니다. 다행히 안정을 찾고 계십니다.」

「그렇구려. 혹 잠시라도 뵐 수 있겠소?」

「음. 여쭤보긴 하겠지만 가족분들의 의사가 가장 중요한지라…….」

「이해하오. 피가 섞인 가족이 의식을 회복하지 못하고 있는데 누군들 다르겠소. 그저 늙은이의 주책이라 생각해 주면 고맙겠소.」

「아닙니다. 주석님. 그리 생각해 주신 것만으로도 감사합니다.」

「감사하다니, 그런 말씀 마시오. 진 선생이 아니었다면 더 큰 참사가 일어났을 터. 내 비록 살날이 얼마 남지 않은 늙은이지만, 이 감사함은 무덤까지 갖고 가겠소.」

샤오 양 주석의 말은 진심이었다.

그날로부터 4일이 흐른 지금, 전 세계의 수많은 전문가가 참가한 조사단은 아크 리치의 본거지였던 도시를 샅샅이 수색했고 게이트 발생의 흔적을 찾아냈다.

그리고 엄청난 마력의 잔재와 함께 유추해 낸 게이트의 예상 규모는 그야말로 재앙에 가까웠다.

「그날 진 선생이 아크 리치를 막지 못했더라면, 본국은 물론이고 아시아 전체가 전쟁터가 되었을 거요. 아니, 어쩌면 전 세계가 되었을 수도 있었겠지.」

「충분히 가능성 있는 일이지요.」

약간의 과장은 있을지언정 대부분은 사실이었다.

그래서 최민우는 굳이 부정하지 않고 고개를 끄덕여 인정했다.

어차피 자신을 향한 공치사도 아니니 부끄러워할 필요도 없었고, 10억이 넘는 인구를 지닌 한 나라의 지도자가 가진 고마움을 깎아내릴 필요도 느끼지 못했다.

상대방이 가진 마음의 빚은 더 큰 선물이 되어 돌아오는 법이니까.

「그런데 주석님. 근래 들어 진태경 씨에 관한 안 좋은 소문들이 들려오는 것 같던데…… 혹시 알고 계셨습니까?」

「안의 일이오, 아니면 밖의 일이오?」

「안의 일입니다. 공산당 수뇌부, 아니 태자당 쪽이라고 하는 것이 더 정확하겠군요.」

샤오 양 주석은 고개를 끄덕였다.

「그 이야기에 대해서는 충분히 인지하고 있소.」

우헤이싱의 죽음에 관련된 문제다.

조사단이 발견한 그의 시신은 심각하게 훼손되어 있었는데, 이에 관한 음모론이 안팎으로 조금씩 퍼져 나가는 상황이었다.

「진태경 씨를 의심하는 이들이 있습니다. 처음 우헤이싱과 마주한 회의 자리에서 약간의 언쟁이 있었던 점. 그리고 처음 진태경 씨를 발견했을 당시 별다른 상처가 없었던 점에 대해서요.」

이 부정적인 추측에 대한 의견은 두 가지로 나뉘었다.

첫째, 평소 우헤이싱에게 좋지 않은 감정을 품었던 진태경이 그를 죽인 뒤 아크 리치의 소행으로 위장했다는 것.

둘째, 실종, 혹은 사망으로 추정되는 이정룡과 함께 우헤이싱을 방패막이로 내세우고, 그 틈을 타 아크 리치를 처치했다는 것.

이에 관한 이야기는 샤오 양 주석 역시 알고 있었고, 이미 결론을 내린 상태였다.

늙은 정객은 최민우를 향해 단호한 어조로 말했다.

「터무니없는 비방과 음모론일 뿐이오.」

「믿어 주시니 감사합니다만…….」

좋은 반응이지만, 이것으로는 부족하다.

최민우는 천천히 말을 이었다.

「태자당의 영수(領袖)는 주석님과 생각이 달라 보여서 말입니다.」

중국 내부에서도 나라 망신시키지 말라며 욕먹는 음모론이지만, 자식을 잃은 아비에게는 신빙성 있는 가설로 들렸다.

우헤이싱의 부친은 중국 공산당의 절반을 차지하고 있는 태자당의 우두머리다.

주석과 비견되는 정치 거물인 그는 본격적으로 소문을 확산. 그에 그치지 않고 단독 조사단을 꾸려 일을 파헤치고 있었다.

「어차피 진태경 씨가 의식을 회복한다면 진실이 밝혀질 겁니다. 그런데 그런 말도 안 되는 음모론을 퍼트리는 것에 고위 정치인이 앞장선다는 건…….」

말꼬리를 흐리는 최민우를 향해, 샤오 양 주석이 희미하게 웃었다.

‘거리낌 없군.’

아무리 큰 전공을 세웠다고 해도 자신과는 살아온 인생과 위치가 다르다.

하지만 눈앞의 청년은 완급 조절까지 해 가며 자신의 뜻을 적극적으로 피력하고 있었다.

‘그 이야기가 사실이었나.’

문득 최민우의 신상정보를 떠올렸던 샤오 양 주석은 의자 팔걸이를 두드렸다.

「좋소. 내 설명이 부족했던 듯싶으니 다시 말하리다.」

「듣고 있습니다.」

「나와 내 동지들은 이미 그에 관한 모든 것들을 알고 있으며, 만반의 준비를 끝내 두었소.」

「만반의 준비라면……?」

「아들의 죽음에 대해 호소하기 전에, 재판을 받게 될 것이라는 이야기요.」

이번 전쟁에서 쓰러진 것은 아크 리치뿐만이 아니다.

천문학적인 액수의 비리, 부패가 드러났고 그걸 감당하려면 태자당은 기둥뿌리를 뽑아야 한다.

최민우는 그제야 잔잔한 미소를 입가에 띄웠다.

「대답이 되었소?」

「충분합니다.」

오늘의 대화는 이 정도로 충분하다.

잠시 후, 몇 마디 대화를 나눈 샤오 양 주석이 자리를 뜨자, 홀로 남겨진 최민우가 불쑥 입을 열었다.

“그렇다는군요.”

그리고 한 사람이 번쩍 눈을 떴다.

“어휴, 시벌. 답답해서 죽는 줄 알았네.”
```

## Final English reading copy

```markdown
# Chapter 427

It was a winter night in December, and snow was pouring down in thick flurries.

People who had hurried through the streets trusting the weather forecast—which had confidently predicted clearer weather than usual—were bewildered, and the Meteorological Agency was thrown into confusion.

“What the hell? What’s going on?”

“We’re analyzing it now. This definitely shouldn’t be happening.”

“With snow the size of hailstones pouring down, don’t tell me this shouldn’t be happening. Stop spouting nonsense and bring me the data. There should be real-time observations!”

“We’re looking into it right now, but… Ah, it looks like an abnormal phenomenon caused by a sudden surge in mana in China’s Sichuan region. The expected snowfall is no joke.”

“Sichuan? Damn it. Is that Arch Lich bastard controlling the weather now, too?”

After the Great Cataclysm, the Meteorological Agency had introduced various types of magic and begun issuing weather forecasts that bordered on prophecy.

One hour after hastily beginning a second round of observations, the agency issued a heavy-snow advisory across the country. Their conclusion was that record-breaking snowfall, the heaviest in roughly thirty years, was on its way.

But before long, the people hurrying home had no choice but to stop in their tracks.

It was because of a single sentence that rang out from a massive screen installed in the center of one of the countless busy commercial districts.

—On a day like today, it is both my pleasure and my honor to bring you this news.

An elderly East Asian man appeared on the screen.

Behind him sat the leaders of the nations belonging to the United Nations Security Council. The Chairman of the People’s Republic of China began speaking into the countless microphones, his eyes red and his voice thick with emotion.

—The Arch Lich has been erased. We… have won.

Victory.

That single word was enough.

For roughly a month—thirty-four days, to be exact—an unprecedented monster wave had continued without pause.

The news that the great war, which had spread unease throughout the world beyond Sichuan Province, had finally come to an end left people standing there with their mouths hanging open.

Then they erupted into thunderous cheers.

“Waaaaaaah!”

“Wait! Hold on! I couldn’t hear that. What did he just say?”

“...It’s over!”

“What?”

“Look at the subtitles! Look at the subtitles!”

“‘The Arch Lich has been erased’… Oh, shit, it’s true! Waaaaaaah! I thought I was going to get called up for reserve duty!”

They heard neither Chairman Xiao Yang’s thirty-minute announcement nor the additional explanation given afterward by the spokesperson for the United Nations Security Council.

With the Arch Lich erased, countless undead legions had lost their power and been annihilated as well. At last, the peace everyone had prayed for had arrived.

“Mom, it’s me. Yeah. Did you see the news? You didn’t? Turn it on right now. Yeah, yeah!”

“We have to celebrate. Assistant Manager Kim, let’s go for a third round!”

“A third round? The server update is tomorrow. Manager Noh is going to lose his shit.”

“Manager Noh is coming, too. He has the corporate card.”

“Ugh, I don’t want to see that bastard’s face. Fine. Let’s go.”

“Unity! Yes, Battalion Commander. This is Captain Lee Junbeom. Could I extend my leave by just one more day—? No, sir. I’m sorry, sir.”

People who had been going back and forth outside while desperately ignoring their unease ran to the bars amid the cheers. Even those who had stayed home, anticipating a second Great Cataclysm, poured into the streets and joined the festive atmosphere.

The cheers did not die down even after midnight.

Nor the next day, or the day after that…

The entire world boiled like a cauldron over a charcoal brazier at this monumental victory, pouring out new articles day after day in every language.

There were even jokes that more news and articles had been published about the victory than about the heavy snow that had fallen over Korea for three straight days.

And… there was one name that appeared without fail in every one of those articles.

[The New York Times, United States: “A Great Victory, a New Hero.”]

[The Times, United Kingdom: “A New Star Rising in the East. Is He Close to Prince Felix?”]

[Asahi Shimbun, Japan: “Jin Taekyung Is Asia’s Pride. But Japan’s First-String Hunters Could Surpass Him!”]

[People’s Daily, China: “The Young Korean Knight-Errant Who Saved Countless People. And the Tragic Death of Zhonghua’s Genius, Wu Heixing.”]

[China Youth News: “Jin Taekyung Is a Descendant of Chen Lin, a Ming Dynasty General. The Blood of Zhonghua Unmistakably Flows Through Him, and He Will Surely Become a Chinese Citizen Before Long.”]

[Goryeo Daily, Korea: “Ares Guild Vice Guild Master, Hunter Lee Jungryong, Age 68. Presumed Dead…”]

[Das Patch Korea official: “We have devoted every effort to investigating Jin Taekyung for several months, but we could not uncover a single thing. His romantic history is astonishingly clean.” When a reporter asked whether that meant he had dated many women but parted with each of them amicably, the official cut him off: “No. I mean he’s never dated anyone in his life.”]

To the various media outlets, Jin Taekyung’s existence was nothing short of a Christmas present.

Every spotlight turned toward him, and all kinds of stories about him came pouring out.

The material was endless. Needless to say, there was plenty to cover about the monster wave now known as the “Winter War,” but his past actions on the way to his current position and even the most trivial details of his private life were considered newsworthy.

Even the trashy articles that would normally have been cursed out as gutter journalism attracted interest.

That was how much the attention of the entire world had turned toward the new hero who had led them to this great victory.

But not all that attention was positive.

Information had begun leaking out bit by bit from behind the ironclad internal security, and people began raising questions.

[Four Days After the War. What Was Hidden Behind the Great Victory That Day? The Questions Surrounding Jin Taekyung.]

[Lee Jungryong Presumed Dead. Wu Heixing’s Suspicious Death. The Deaths of Two S-Rank Hunters and the Rise of a New Hero.]

[Secret Testimony from Coalition Commanders Who Were at the Scene: “Despite the battle’s ferocity, no significant injuries were visible on Jin Taekyung’s body when he was discovered. We are investigating whether he used potions. If he regains consciousness, the entire situation will become clear.”]

Although they were few in number, conspiracy theories began to appear, and the internet erupted into fierce arguments.

Articles like these, unable to withstand waves of malicious comments and reports, vanished almost immediately. But they planted doubts in the minds of some members of the public, and eventually everyone’s attention focused on one thing.

Jin Taekyung.

When, exactly, would he show himself?

* * *

Beep. Beep.

State-of-the-art medical equipment emitted mechanical sounds.

The people gathered in one part of the hospital room, which only a select few were permitted to enter, gazed worriedly at Jin Taekyung as he lay there wearing an oxygen mask.

“How is Mr. Jin’s condition?”

Choi Minwoo answered Chairman Shao Yang’s question.

“It’s always the same. Everything is perfectly normal, but for some reason, he still hasn’t regained consciousness.”

“Did both of them say that?”

“Yes. They said they don’t know the cause.”

“Hmm. If both of them said so, there can be no doubt… Then why on earth hasn’t he regained consciousness?”

Chairman Shao Yang sighed.

The two people he had mentioned were both at the very top of their fields.

One was a civilian physician known as the reincarnation of Hua Tuo, while the other was a top-class healer renowned throughout the world.

If the two people invited as Jin Taekyung’s temporary attending physicians had said so, there could be no doubt about it.

“I heard his family is here.”

“The Peace Guild is taking good care of them. Fortunately, they’ve regained their composure.”

“I see. Would it be possible for me to see them, even briefly?”

“I can ask, but their wishes are the most important thing, so…”

“I understand. Who could feel differently when a blood relative has yet to regain consciousness? I would appreciate it if you simply considered this the foolishness of an old man.”

“No, Chairman. We’re grateful that you even thought of it.”

“Don’t say that you’re grateful. If not for Mr. Jin, an even greater catastrophe would have occurred. Though I am an old man with little time left to live, I will carry this gratitude with me to the grave.”

Chairman Shao Yang was sincere.

Four days had passed since that day. During that time, an investigation team made up of countless experts from around the world had combed through the city that had served as the Arch Lich’s base and discovered traces of the Gate.

And the projected scale of the Gate, inferred from the enormous residue of mana, was nothing short of catastrophic.

“If Mr. Jin had failed to stop the Arch Lich that day, not only our country but all of Asia would have become a battlefield. No… Perhaps the entire world could have become one.”

“It was certainly possible.”

There might have been some exaggeration, but most of it was true.

That was why Choi Minwoo did not bother to deny it. He simply nodded in acknowledgment.

There was no need to feel embarrassed, since the praise was not directed at him in the first place. Nor did he feel the need to diminish the gratitude of the leader of a nation with a population of more than a billion.

A debt of gratitude in someone’s heart had a way of returning as an even greater gift.

“But Chairman. I’ve been hearing some unfavorable rumors about Jin Taekyung lately… Were you aware of them?”

“Do you mean something inside the country or outside it?”

“Inside. The leadership of the Communist Party—or, more precisely, the Crown Prince Party.”

Chairman Shao Yang nodded.

“I am fully aware of the matter.”

It concerned Wu Heixing’s death.

The investigation team had found his body in a severely mutilated state, and conspiracy theories about it were slowly spreading both inside and outside the country.

“There are people who suspect Mr. Jin. They point to the fact that he had a minor argument with Wu Heixing during their first meeting, as well as the fact that Mr. Jin had no notable injuries when he was first discovered.”

There were two negative theories about what had happened.

The first was that Jin Taekyung, who had harbored ill feelings toward Wu Heixing for some time, had killed him and disguised it as the work of the Arch Lich.

The second was that, together with Lee Jungryong, who was presumed missing or dead, he had used Wu Heixing as a shield and taken advantage of the opportunity to kill the Arch Lich.

Chairman Shao Yang knew about these theories as well, and he had already reached his own conclusion.

The old statesman spoke to Choi Minwoo in a firm tone.

“They are nothing more than absurd slander and conspiracy theories.”

“Thank you for believing him, but…”

It was a good response, but it was not enough.

Choi Minwoo continued slowly.

“The leader of the Crown Prince Party doesn’t seem to share your view, Chairman.”

It was a conspiracy theory that even people inside China condemned as an embarrassment to the country. But to a father who had lost his son, it sounded like a credible hypothesis.

Wu Heixing’s father was the head of the Crown Prince Party, which made up half of the Chinese Communist Party.

A political giant comparable to the Chairman, he had begun spreading the rumors in earnest. He had gone even further and formed an independent investigation team to dig into the matter.

“If Mr. Jin regains consciousness, the truth will come to light anyway. But for a high-ranking politician to take the lead in spreading such an absurd conspiracy theory…”

Choi Minwoo let his voice trail off, and Chairman Shao Yang smiled faintly.

*He has no qualms at all.*

No matter how great a feat he had accomplished, the young man before him had lived a very different life and stood in a very different position from his own.

And yet, the young man was actively making his position known, even carefully modulating his pace and tone.

*Was that information true?*

As Chairman Shao Yang suddenly recalled Choi Minwoo’s personal information, he tapped the armrest of his chair.

“Very well. It seems my explanation was insufficient, so let me say it again.”

“I’m listening.”

“My comrades and I already know everything about the matter, and we have made all the necessary preparations.”

“All the necessary preparations…?”

“Before he can appeal to anyone about his son’s death, he will be standing trial.”

The Arch Lich was not the only one to fall in this war.

Corruption and embezzlement involving astronomical sums had been uncovered, and to contain the fallout, the Crown Prince Party would have to sacrifice its very pillars.

Only then did Choi Minwoo allow a gentle smile to spread across his lips.

“Does that answer your question?”

“It’s more than enough.”

That was sufficient for today’s conversation.

A short while later, after exchanging a few more words, Chairman Shao Yang left the room. Choi Minwoo, now alone, suddenly opened his mouth.

“That’s what he says.”

And then one person’s eyes snapped open.

“Oh, fuck. I thought I was going to die from how stifling this was.”
```
