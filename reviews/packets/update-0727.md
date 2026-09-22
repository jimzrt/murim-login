<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0727.txt",
      "sha256": "ec2c9c682ec0ef0b47a44f7bb4145ddeddd5438fb00913a4296c18b5e6f3b673",
      "bytes": 14556
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "4f343bc95e3a54346ee607a48cf517b0212c0eccb71bebf1cb4adae552b56483",
      "bytes": 2351
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "486a1773ee71815ccbd62d2095050d2d392a02e240be917d0430b0fe106b71d7",
      "bytes": 209842
    },
    {
      "path": "characters/Cheon Taemin.md",
      "sha256": "2b2020c7ff155f1a65403ee5c46be2d9083626471fc98fb880891285232f2688",
      "bytes": 752
    },
    {
      "path": "characters/Jeok Cheongang.md",
      "sha256": "6fefacc1c715a7b75fc286d56231771e212838fbde13e20fbcfe98ec522be4ca",
      "bytes": 1848
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "396b344b62febd61e7dbd647a017e82ed39e439d66d181b4d3d7a1fbb27c81d5",
      "bytes": 2011
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "4b002a1172feb03c153543314fbf9b6eef76983287cb0499cc4784a555b64cdd",
      "bytes": 622
    },
    {
      "path": "characters/Team Leader Choi.md",
      "sha256": "315c870013f9330cf37dc7342a308bbfab73df9f99f74fac69bb77423d19484f",
      "bytes": 967
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "77a1af6702369bd34848af1d07d41d67810d45567369af3d54b0fca4f77a12b4",
      "bytes": 220286
    }
  ],
  "estimated_tokens": 11745
}
-->

# Durable State Update — Chapter 727

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 727. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 727. Profile updates may replace only one
complete line in Aliases, Role, Personality, Voice, or Relationships. Do not
return Safe through updates; the controller sets that field automatically.
Each profile field should be one concise sentence; never append semicolon-separated
chapter history.
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
  "chapter": 727,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 727,
    "continuity_sources": [727],
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
    "Nanman is unified under the Beast Miao King's authority and has joined the Murim Alliance as the Nanman Beast Palace.",
    "Yayul Mok is committed to defending Nanman and its allies with his life after learning humanity from Jin Taekyung.",
    "The Sacred Rain is fading after healing Jin Taekyung's companions.",
    "The prelude to the Great War has begun, with Nanman's beasts and people mobilizing and the White Tiger present above them.",
    "Dark Heaven's full strength remains unrevealed, and its servants regard the Lord of Heaven as a living god.",
    "The Lord of Heaven has taken an unexplained personal interest in Jin Taekyung.",
    "Jin Taekyung has disclosed his cross-world origin and Dark Heaven's attempts to capture or kill him to Jeok Cheongang.",
    "Jeok Cheongang accepts Jin Taekyung as himself rather than as a Little Immortal from the realm of immortals.",
    "Choi Minwoo is now the Peace Guild's Guild Master and remains Jin Taekyung's trusted subordinate and manager.",
    "Jin Taekyung created the beginner-accessible Smiling Mana Cultivation Method.",
    "The Dharma King foresaw a vast war and identified a young man as the Master of Morning Star, leading Jeok Cheongang to make that youth the Fire Gate Clan's successor."
  ],
  "continuity_sources": [
    726
  ],
  "open_questions": [
    "What does the Lord of Heaven know about Jin Taekyung's hidden secrets, and what does he intend?",
    "What is the nature of the other world resembling the realm of immortals, and how does Jin travel between it and Murim?",
    "Why has Dark Heaven withheld its full strength, and what is its larger plan?",
    "How will the Great War unfold now that Nanman has joined the Murim Alliance?",
    "What will happen to Nanman and the Sacred Rain after the rain ends?"
  ],
  "safe_through": 726,
  "temporary_decisions": [
    "Render 싱글벙글 마나 연공법 as The Smiling Mana Cultivation Method.",
    "Render 전고 as war drums, 신강 as Xinjiang, and 신께서 원하신다! as God wills it!.",
    "Preserve the established Lord of Heaven rendering for 천주.",
    "Render 선계 as realm of immortals and 소신선 as Little Immortal.",
    "Preserve the chapter's profane comic banter, including poop for 똥 and civet cat for 사향 고양이."
  ],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 진태경    | **Jin Taekyung**   |
| 적천강    | **Jeok Cheongang** |
| 최민우    | **Choi Minwoo**   |
| 천태민    | **Cheon Taemin**  |
| 절정     | **Peak**          |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 심법     | **cultivation technique**                        | Especially internal cultivation                       |
| 검법     | **sword technique**                              |                                                       |
| 진가심법   | **Jin Family's Cultivation Technique** |
| 등급               | **Grade**                      | System/UI field for quest, item, and martial-art classifications; do not use “Rank” here |
| 로그아웃             | **Logout**                     |
| 민첩               | **Agility**                    |
| 헌터      | **Hunter**            |
| 게이트     | **Gate**              |
| 몬스터     | **monster**           |
| 레이드     | **raid**              |
| 길드      | **Guild**             |
| 길드장     | **Guild Master**      |
| 팀장      | **Team Leader**       |
| 마정석     | **Magic Gem**         |
| 귀가      | **your family**                                                 |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 삼재검법 | **Three Calamities Sword Technique** | Sword technique Mukyung assumes Taekyung is pretending to use. |
| 아스모데우스 | **Asmodeus** | Demon King referenced in Taekyung's sarcastic comparison; does not appear directly. |
| 평화 | **Peace Guild** | Guild name. |
| 대한민국 | **Korea** | Country reference. |
| 아레스 | **Ares Guild** | The leading Guild in Korea; formerly employed Team Leader Choi and Song Song. |
| 갑자 | **jiazi** | Traditional sixty-year cycle. |
| 주신 | **God of Drinking** | Wipeng's drinking epithet. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 마도 | **Demonic Path** | Term raised for martial power that appears to defy common principles. |
| 준이 | **Jun** | Family nickname used in the form Jun's dad. |
| 마왕 | **Demon King** | The being Cheon Taemin killed. |
| 스켈레톤 | **Skeleton** | Undead monster species. |
| 존슨 | **Johnson** | Co-host of the American talk show that replays Taekyung's viral interview. |
| 미국 | **United States** | Country associated with the talk show and CNM. |
| 대통령 | **President** | Title for Korea's head of state. |
| 도람프 | **Doramp** | Parodic name for the U.S. president in a forum headline. |
| 소하 | **Xiao He** | Historical civil official invoked in the same exchange. |
| 천지창조 | **The Creation (The Genesis)** | The painting title used for the Sistine Chapel ceiling frescoes. |
| 펜타곤 | **Pentagon** | Headquarters of the United States Department of Defense and source of intelligence about terrorist experiments. |
| 변이 | **mutation** | The transformation threatening the humans and beasts in the Inner Palace. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 적천강 | 진태경 | overwhelming stranger to interrogated young martial artist | you; you bastard | blunt, threatening, and taunting | Uses 너, 네놈, and 이놈 while demanding Taekyung explain Qi Sense and the System. |
| 진태경 | 적천강 | frightened young martial artist to overwhelming elder | elder | polite and fearful | Uses the honorific 어르신 while explaining that the System may have felt like a cheat. |
| 상인 | 적천강 | merchant_to_legendary_martial_master | Great Hero Jeok | deferential and flattering | Praises Jeok Cheongang while presenting the Poison-Averting Ring and requesting help. |
| 적천강 | 상인 | legendary_guest_to_merchant | you | blunt and transactional | Cuts off the merchant’s praise, asks his identity and origin, and accepts the gift without committing to the requested favor. |
| 진태경 | 기장 | strangers | Captain | casual and commanding | Taekyung directly asks the captain for permission to open the aircraft door before cutting it open. |
| 최민우 | 진태경 | trusted allied team leader to younger allied Hunter | Mr. Jin | formal-polite and concerned | Choi warns Jin about the danger of the operation and affirms his deep trust. |
| 진태경 | 최민우 | younger allied Hunter to allied team leader | Team Leader Choi | polite, familiar, and teasing | Jin jokes with Choi while acknowledging and dismissing his concern. |
| 진태경 | 존슨 | Allied Hunter to Grand Mage | Johnson | polite and familiar | Jin repeatedly addresses Magic Johnson directly while requesting explanations and permission to visit the site. |
| 진태경 | 대통령 | Hunter_to_President | Mr. President | formal-polite | Taekyung addresses the President respectfully during their airport greeting. |
| 대통령 | 진태경 | President_to_Hunter | Mr. Jin Taekyung | formal-polite | The President addresses Taekyung by name at the airport photo line. |

## Listed compact profiles

### Cheon Taemin.md

# Cheon Taemin (천태민)

- **Safe through:** Chapter 647
- **Aliases:** Slayer; Sky (the American epithet used for him)
- **Role:** Cheon Taemin is Ares Guild Master and the world's greatest Hunter, known as the Slayer for killing the Demon King and creating the first Mana Cultivation Method during the Great Cataclysm, and he remains unconscious after more than twenty years in a wired mechanical capsule at his former mansion.
- **Personality:** Not established.
- **Voice:** Not established.
- **Relationships:** Maternal grandfather of Team Leader Choi and Jin Taekyung and father of Soyeong; regarded by Lee Jungryong as an older brother despite their lack of blood relation.

### Jeok Cheongang.md

# Jeok Cheongang (적천강)

- **Safe through:** Chapter 726
- **Aliases:** Fire King; eighteenth Sect Leader of the Fire Gate Clan
- **Role:** Jeok Cheongang is the current Sect Leader of the Fire Gate Clan, a legendary wandering martial master who has achieved Five Qi Returning to Origin, Furnace Fire Pure Blue, and Returned to Youth, Jin Taekyung's Master who has broken free of his Heart Demon and entered a new realm, the occupant of the chief seat of the Murim Alliance's Five Kings Hall, and a trusted confidant who accepts Jin as himself despite knowing that he travels between Murim and another world resembling the realm of immortals.
- **Personality:** Secretive, cryptic, sharp-eyed, gruff, dryly teasing, casually threatening or violent when dissatisfied, pathologically afraid of water, and more deeply trusting of Taekyung than anyone else despite responding to his impossible claims with mockery and violence.
- **Voice:** Sharp and ringing when calling out; otherwise gruff, dryly teasing, blunt, and threatening during interrogation or confrontation.
- **Relationships:** Jin Taekyung is his publicly acknowledged Disciple and intended heir to the Fire Gate Clan; Jeok recognizes Taekyung's Heavenly Martial Physique and has invested heavily in his growth. Jeok regards Mae Jonghak, the Sword Saint, as a kindred spirit and recognizes Cheongpung as Mae's grandson and successor. He was a close friend of Hong Dao, Shaolin's Abbot and Dharma King, whose death left him determined to act against the forces responsible. He rescued Jangcheon during an Anhui epidemic, accepted him as a Disciple, and regarded him as an only son and grandson despite Jangcheon becoming the murderer Jopil. Jeok is a long-standing rival of Peng Cheolhu, the Thunderbolt Saber King.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 726
- **Aliases:** Blazing Flame Divine Dragon; Apostle of the Earth Mother Goddess; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan, Jeok Cheongang's publicly acknowledged Disciple, the Fire Gate Clan's nineteenth successor, and the Pavilion Master of the Fire Dragon Pavilion within the Murim Alliance, a Supreme Peak master with the Heavenly Martial Physique and Force, a publicly recognized S-rank-level Hunter who formally retains an A-rank license, a traveler between Murim and another world resembling the realm of immortals, and the creator of the beginner-accessible Smiling Mana Cultivation Method.
- **Personality:** Hungry, self-aware, dryly observant, pragmatic under pressure, and willing to risk himself for people he has accepted as real. Treats impossible situations like games until their human cost becomes undeniable.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, Jeok Cheongang is his Master, Mungyeong was his recent instructor, Cheongpung is his trusted companion and only true martial rival, Choi Minwoo is his subordinate, trusted manager of media and official arrangements, and now the Peace Guild's Guild Master, Ju Hwaran is a trusted Fire Dragon Pavilion member who followed him to Nanman, Chuck Hagel is an American operative allied with him in the covert anti-terror campaign, his mother and sister Hayeon are among those he protects, the Skeleton King is his friend and ally, Xiao Shen regards him as an older brother after Jin saved him, and Jin-ho is his older friend and trusted confidant.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 726
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Team Leader Choi.md

# Team Leader Choi

- **Safe through:** Chapter 613
- **Aliases:** Choi Minwoo (최민우)
- **Role:** Team Leader Choi is Cheon Taemin's only living blood relative, a formidable aura-wielding swordsman who wields Hero's Soul, and the current Guild Master of the Peace Guild and Vice Guild Master of Ares Guild after a unanimous board vote.
- **Personality:** Strategic, candid, controlled, and possessive of the power and influence he intends to inherit.
- **Voice:** Dry, formal, and direct, with calm candor and carefully chosen metaphors.
- **Relationships:** Choi Minwoo is Cheon Taemin's maternal grandson and only living blood relative, was kept out of public knowledge by Lee Jungryong, is closely integrated with Jin Taekyung's family, seeks to acquire the Ares Guild intact, knows that Song Cheonwoo and Lee concealed Taemin's collapse and purged aides, and is Kim Hwajong's grandson.

## Korean source

```text
＃727화



찢을까, 말까.

얼굴 위로 생각이 고스란히 드러난 진태경을 바라보며, 최민우는 내심 어이없는 실소를 흘렸다.

‘도무지 알 수가 없단 말이지.’

평소 보이는 언행도, 생각도 단순하기 그지없다.

하지만 가끔 진태경이 보여 주는 어떤 면모는, 놀랍다 못해 경악스러울 정도였다.

‘더 놀라는 것도 이상하지만, 그래도 이건 정말이지…….’

최민우의 시선이 테이블 위에 머물렀다.

[싱글벙글 마나 연공법]

어린아이가 쓴 것처럼 삐뚤빼뚤한 글씨체와 우습기 그지없는 제목.

그러나 저 열 장 남짓한 A4용지에 담긴 내용은, 제목과 달리 결코 우습지 않았다.

‘아예 새로운 마나 연공법을 만들다니.’

앞서 최민우가 악필까지 지적해 가며 진태경은 골려 준 이유는 간단했다.

이처럼 말도 안 되는 물건을 갑작스럽게, 그것도 한마디 말도 없이 전한 것에 대한 소소한 복수,

몇 시간 전, 최민우가 느꼈던 충격은 그만큼 엄청난 것이었다.

‘어떻게 이럴 수 있지?’

지금껏 본 적 없는 간단명료한 설명과 방식. 더없이 안정적이며, 기본기에 충실한 마나 연공법.

그리고 어느덧 무림의 절정 고수와 비교해도 뒤떨어지지 않는 실력자가 된 최민우는, 이 새로운 마나 연공법의 진가를 즉각 알아차릴 수 있었다.

더불어 불과 얼마 전, 세상의 이목을 끌었던 일련의 사건이 진태경에게 어떤 의미였는지도.

“심판의 일주일.”

짧은 침묵을 깨트린 최민우가 진태경을 응시하며 말을 이었다.

“마치 신께서 일주일에 걸쳐 천지를 창조했던 것처럼, 전 세계의 테러리스트들은 심판의 일주일을 보냈다. 며칠 전 도람프 주니어 미 대통령이 백악관 기자회견에서 한 말입니다.”

다른 누구도 아닌 미국 대통령이 공식 석상에서 한 발언이다.

당연하게도 그의 파격적인 언행은 불과 한 시간이 지나기도 전에 일파만파 퍼져 나갔고, 어느 정도 시간이 흐른 지금은 대한민국에서도 모르는 사람이 없다.

아마도 한 사람을 제외한다면.

“그 양반이 그런 말을 했어요?”

줄곧 트레이닝 룸에만 처박혀 있던 진태경의 물음에, 최민우가 고개를 끄덕였다.

“한 나라의, 그것도 미국 대통령의 발언치고는 꽤 과격했습니다. 테러리스트들을 일부러 자극한다는 비판도 있었고요.”

“흠. 뭘 또 거창하게 천지창조씩이나. 그래서 보복성 테러는요?”

“없었습니다. 단 한 건도.”

“단 한 건도?”

“네. 오히려 말을 아끼기까지 하더군요.”

아직도 뚱해 있던 진태경의 표정이 살짝 풀렸다.

“열심히 두들겨 팬 보람이 있네.”

바로 그 순간이었다.

진태경을 물끄러미 바라보던 최민우가 불쑥 입을 연 것은.

“그래서였군요.”

“뭐가요?”

“두 가지에 대해 생각해 봤습니다. 갑자기 테러리스트를 진압하신 이유. 또 이 새로운 마나 연공법을 제게 주신 의미에 대해서.”

그리고 답이 나왔다.

[싱글벙글 마나 연공법].

도무지 성의라고는 찾아볼 수 없는 호치케스 한 방으로 묶인 그것을 들어 올리며, 최민우가 말을 이었다.

“모든 사람들에게 공개할 생각이시군요. 이 마나 연공법을.”

진태경이 씩 웃었다.

“우리 최 팀장님, 역시 똑똑하시다니까.”



* * *



지금 이 순간, 나를 바라보는 최 팀장의 표정은 오묘했다.

감탄하는 것 같기도 하고, 한편으로는 여러모로 생각이 많아진 것 같기도 했다.

“왜요, 무슨 문제라도?”

“글쎄요.”

최 팀장이 헝클어진 머리를 매만졌다.

“너무 많은 문제가 있어서 뭐부터 말씀드려야 할지 모르겠습니다.”

“제가 만든 마나 연공법에는 문제가 없으니, 현실적인 부분이겠네요.”

“……예, 안타깝게도 그렇습니다.”

“그중에서 어떤 게 가장 큰 문젭니까?”

잠시 생각하던 최 팀장이 입을 열었다.

“우선 이 마나 연공법을 공개한다는 것만으로도 첫 번째 문제가 되겠죠.”

“계속 말씀하세요.”

“마나 연공법은 상위 헌터들 중에서도 극소수만이 보유한, 일종의 노하우이자 비전이라는 사실은 진태경 씨도 잘 알고 계실 겁니다. 그들이 얼마나 폐쇄적인지, 또 그들이 속한 세계가 여타의 헌터들과는 얼마나 다른지에 대해서도요.”

“알죠. 이 바닥에서 구른 게 몇 년인데. 물론 F급 헌터 시절에는 마나 연공법에 대해 들어 본 적도 없지만.”

세상에 존재하는 어떤 직업보다 격차가 심한 것이 헌터다.

일반적인 사회인들이 학력과 집안, 외모로 서로를 구별한다면, 헌터는 오직 등급에 따라 귀천(貴賤)이 갈린다.

얼마나 많은 마나를 부여받았는지. 얼마나 민첩하고 힘이 강한지. 그런 원초적인 기준에 따라 선별되고 곧 도축당할 소처럼 등급이 매겨지는 거다.

‘괜히 F급 헌터를 노비라고 부르는 게 아니지.’

반면 상위 헌터들은 그야말로 구름 위의 존재나 다름없다.

그들은 어지간한 헌터가 평생 일해도 벌 수 없는 금액을 레이드 한 번으로 벌어들이고, 부러움이 담긴 시선과 스포트라이트 속에서 살아간다.

아마 그래서일 것이다.

과거 귀족들이 성을 짓고 살아가던 것처럼, 그들 역시 자신들만을 위한 벽을 지었다.

상위 헌터가 아니라면 누구도 넘을 수 없는 벽.

설령 운이 좋은 누군가가 높은 등급을 받았더라도, 자신들의 허락이 있어야만 열리는 문까지.

그렇게 보이지 않는 끈으로 연결된 상위 헌터들은 전 세계에 퍼져 있고, 그들은 저마다 속한 거대 길드들의 비호를 받는다.

“이건 단지 국내에만 한정된 문제가 아닙니다. 이 마나 연공법을 세상에 공개하면, 예상하는 것 이상으로 엄청난 반발이 일어날 겁니다.”

“우리 쪽에서 마나 연공법을 까면, 자신들이 지닌 가치가 떨어진다고 생각할 테니까?”

“그것도 그렇지만, 한 가지 이유가 더 있습니다.”

“뭔데요?”

“바로 ‘우리’라서 문제인 겁니다.”

“……!”

짤막한 대답이었지만, 나는 그 말이 뜻하는 바를 즉각 깨달았다.

‘그간 너무 튀었나.’

문득 로그아웃하기 직전 적천강과 나누었던 대화가 생각난다.

원했든, 원치 않았든 이미 필요 이상으로 많은 주목을 받았다는 그의 한 마디가.

스포트라이트는 밝다. 하지만 그 주위는 어둡다.

학창 시절 좋아하던 어느 소설에서 읽었던 그 글귀가 맞았다. 내가 밝아지는 만큼, 나를 둘러싼 어둠 역시 짙어지고 있었다.

무림에서도. 그리고 현대에서도.

“최 팀장님, 혹시?”

내가 무엇을 묻는지 알아차린 최 팀장이 고개를 저었다.

“아직 큰 문제는 없습니다만…… 보이지 않는 압박이 들어오고 있습니다. 그래서 해외 지사의 추가 설립도 잠시 보류하고 있고요.”

“그 정도예요?”

“당장 전 세계의 모든 거대 길드가 우리를 주시하고 있습니다. 꼭 무력시위가 아니더라도 그들이 어떻게든 손을 쓴다면, 저희로서도 상황이 쉽지 않습니다.”

“아니, 왜 말씀 안 하셨어요?”

최 팀장이 정색하며 대답했다.

“말할 틈이나 줬습니까?”

“……그건 그러네.”

그나저나 이 동네도 개판이구만.

본래 가진 것이 많은 이들은 세상이 변화하는 것을 꺼린다.

독자적인 마나 연공법을 익힌 극소수의 헌터들 역시 그 범주를 벗어나지 못한다.

‘아니, 사실 이쯤 되면 헌터보다는 권력자라고 하는 게 맞겠지.’

어쩌면 한 나라를 주무를 수 있는 권력자들.

막대한 부와 명예, 그리고 압도적인 힘으로 상식마저 뒤엎는 그들은 더 이상의 변화도. 자신들과 비견할 만한 또 다른 권력자의 등장도 원치 않는다.

이를테면, 나나 최 팀장이라든지.

‘아무리 그래도 그렇지. 이 새끼들은 무림 문파보다 한술 더 뜨는 것 같은데.’

독문 무공이 유출되면 눈에 불을 켜고 쫓아가 뚝배기를 깨 버리는 곳이 무림이라지만, 적어도 시장에서 삼재검법을 파는 상인한테 지랄발광을 떨지는 않는다.

그런데 가진 것도 많은 놈들이, 소소하게 마나 연공법 하나 풀려고 하니까 지랄하려고 하네?

어? 열 받네?

“이 마나 연공법 까면, 걔들 난리나겠죠?”

“네. 저희도 난리 나고요.”

“그럼 제가 걔들을 까면요?”

“네?”

“생각해 보니까 좆 같잖아요. 그냥 무지성으로 마나 연공법부터 까 보고, 그 후에 지랄하는 새끼들도 까면 조용해질…….”

“안 돼! 하지 마! 절대!”

늘 낮고 침착한 최 팀장의 목소리가 이 정도 데시벨을 낸다는 것은, ‘차라리 내 시체를 밟고 가라, 이 미친 새끼야.’라는 뜻이다.

하지만 이번만큼은 나도 쉽게 수긍할 수 없었다.

“최 팀장님 뜻은 알겠는데, 이건 공개해야 합니다. 일기장처럼 혼자 간직하려고 만든 거 아니에요.”

이미 전 세계적으로 마력이 증가했다. 아니, 지금 이 순간에도 증가하고 있다.

그로 인해 변이 게이트가 속출하고 이제는 몬스터 웨이브까지 일어나는 판국이었다.

“마력이 증가하는 만큼 몬스터도 강해지고 있습니다. 팀장님도 아시잖아요. 하지만 현재 상황에서 이 마나 연공법이 사람들에게 알려진다면…….”

“헌터들의 전체적인 수준이 높아지겠죠. 최하급 헌터도 무리 없이 익힐 수 있을 만큼 안정성이 뛰어나니까요.”

최 팀장이 굳은 얼굴로 말을 이었다.

“진태경 씨께서 무슨 생각이신지는 압니다. 애초부터 여러 반군 집단과 테러리스트들을 진압하신 이유도, 마나 연공법이 악용될 가능성을 최대한 줄이기 위해서가 아닙니까?”

“네. 제가 만든 무기의 예리함보다는, 우선 누구의 손에 들어갈 것인지를 따져 봐야 했으니까.”

현대의 시간으로 약 2주 전, 미국 텍사스에서 벌어진 한 가지 사건은 내게 경각심을 심어 주었다.

다름 아닌 마정석을 이용한 테러.

다행히 테러범의 시도는 수포로 돌아갔고 어떠한 사상자도 발생하지 않았지만, 나는 그 사건으로 인해 확실히 깨달았다.

“제가 생각하고 있는 ‘모두’라는 단어에는, 온갖 범죄자와 미치광이들까지 포함되어 있더라고요.”

이후 매직 존슨을 따라간 펜타곤에서 미 대통령의 묵인하에 놈들에 관한 정보를 얻었고, 함께하는 이들과 함께 사막을 피로 물들이며 위험이 될 만한 요소들을 잘라 냈다.

납치한 아이들에게 사격 훈련을 시키는 반군 집단. 자살 테러까지 불사하는 광신도 테러리스트들…….

앞을 막아서는 놈은 죽였고, 그렇게 죽은 놈들은 스켈레톤 킹의 언데드 군단에 복속되어 도망치는 놈들을 쫓았다.

동시에 멀리 있는 놈들은 포로로 잡은 수뇌부를 통해 거짓 명령을 내렸다.

반군 집단에게는 테러 단체를, 테러 단체에게는 반군 집단을 공격하라는 거짓 명령을.

그건 개새끼와 씹새끼의 전쟁이었고, 거짓 명령에 속아 서로를 향해 총공세를 펼친 대가는 양패구상(兩敗俱傷)이라 부를 만한 막대한 전력 손실로 돌아왔다.

“최 팀장님도 아시다시피 놈들을 완전히 뿌리 뽑는 건 이번뿐만 아니라 앞으로도 불가능하겠지만…… 현재 상황만으로도 이미 목적은 달성했습니다. 그 새끼들이 이 마나 연공법을 익힌다고 해도, 전만큼 위협이 되지는 못할 테니까요.”

내가 만든 마나 연공법으로 강해지는 건 놈들뿐만이 아니다.

마력 증강 현상으로 강해진 몬스터에게 대응할 수 있을 만큼 헌터들의 수준이 전체적으로 향상될 테고, 이것으로 균형을 유지할 수 있을 것이다.

‘만약 지금보다도 상황이 훨씬 악화된다면…….’

그때는 최 팀장을 비롯한 극소수의 인물들에게만 알려 주었던 진가심법(進家心法)까지도 공개할 생각이었다.

마나 연공법이라고는 쥐뿔도 모르는 하급 헌터들은 지금 당장 진가심법을 던져 줘도 응용할 수 없겠지만, 한번 방법을 터득한 후라면 혼자서라도 익힐 수 있을 테니까.

나는 최 팀장을 똑바로 응시하며 입을 열었다.

“공개해야 합니다, 어떻게든.”

“…….”

“다행히 아직 늦지 않았어요. 최 팀장님이나 저를 향한 대중들의 평가나 관심도 괜찮은 편이고요.”

사실 괜찮은 수준을 넘어 열광적이다.

나는 새로운 시대가 낳은 젊은 영웅으로 불리는 중이었고, 최 팀장은 세상을 떠난 김 집사의 뒤를 이어 평화 길드장에 취임. 막 만들어진 따끈따끈한 명패가 식기도 전에 아레스 길드까지 접수했다.

게다가 그에게는 누구보다 화려한 후광(後光)이 있다.

마왕 아스모데우스로부터 인류를 구한 구세주. 천태민의 하나뿐인 혈육이자 후계자라는 후광이.

덥석.

“최 팀장님.”

힘주어 붙잡은 손. 내 뜨거운 눈빛을 마주한 최 팀장이 불에 덴 것처럼 몸을 움찔 떨었다.

“가, 갑자기 왜 이러십니까.”

흡사 어두운 밤 골목길에서 매직 존슨이라도 마주친 듯한 반응. 그러나 나는 굴하지 않고 꿋꿋하게 말을 이어 갔다.

“정 그렇게 걱정되면, 우리 다른 방법으로 가 봅시다. 응?”

“말씀하시는 그 방법이란 게……?”

“외할아버지 이름 한 번만 팔아 줘.”

“네?”

“우리, 이참에 구세주 코인 한 번만 타자.”

“……!”
```

## Final English reading copy

```markdown
# Chapter 727

Should I tear it up or not?

Looking at Jin Taekyung, whose thoughts were written plainly across his face, Choi Minwoo let out a faint, incredulous laugh inwardly.

*I really can’t figure him out.*

Everything about his usual words, actions, and thoughts was absurdly simple.

But some of the sides Jin Taekyung occasionally showed were astonishing—so astonishing they bordered on shocking.

*It would be strange to be surprised by him anymore, but even so, this is really…*

Choi Minwoo’s gaze settled on the table.

**[The Smiling Mana Cultivation Method]**

The crooked handwriting looked like it had been written by a child, and the title was downright ridiculous.

But unlike its title, the contents of those roughly ten sheets of A4 paper were anything but ridiculous.

*He actually created an entirely new mana cultivation method.*

There was a simple reason Choi Minwoo had teased Jin Taekyung earlier, even going so far as to point out his terrible handwriting.

It was a small act of revenge for suddenly handing over something this absurd without saying a word.

The shock Choi Minwoo had experienced a few hours ago had been that immense.

*How is this even possible?*

The explanations and methods were simpler and clearer than anything he had ever seen. The mana cultivation method was exceptionally stable and faithful to the fundamentals.

And Choi Minwoo, who had by now become someone whose skill was not inferior even when compared to a Peak master of Murim, had immediately recognized the true value of this new mana cultivation method.

He also understood what the series of events that had drawn the world’s attention only a short while ago had meant to Jin Taekyung.

“The Week of Judgment.”

Breaking the brief silence, Choi Minwoo continued while staring at Jin Taekyung.

“‘Just as God created heaven and earth over the course of a week, terrorists around the world went through a Week of Judgment.’ That’s what President Doramp Jr. said during a White House press conference a few days ago.”

It had been said publicly by none other than the President of the United States.

Naturally, his outrageous words and actions had spread far and wide in less than an hour. Now that some time had passed, there was no one in Korea who did not know about them.

Probably with one exception.

“That guy said that?”

At Jin Taekyung’s question—he had been holed up in the training room the entire time—Choi Minwoo nodded.

“It was quite an aggressive statement for the president of a country, especially the United States. Some people criticized him for deliberately provoking the terrorists.”

“Hm. Why bring up something as grand as creating heaven and earth? What about retaliatory terrorism?”

“None. Not a single incident.”

“Not a single one?”

“Yes. If anything, they’ve even been keeping their mouths shut.”

The sullen expression that had remained on Jin Taekyung’s face softened slightly.

“Looks like beating the crap out of them was worth it.”

It was at that exact moment that Choi Minwoo, who had been gazing pensively at Jin Taekyung, suddenly spoke.

“So that was why.”

“Why what?”

“I thought about two things. Why you suddenly suppressed the terrorists. And what it meant that you gave me this new mana cultivation method.”

And then the answer appeared.

**[The Smiling Mana Cultivation Method]**

Lifting the papers bound together with a single staple—an object in which not even the slightest trace of effort could be found—Choi Minwoo continued.

“You intend to make this mana cultivation method public. To everyone.”

Jin Taekyung grinned.

“Our Team Leader Choi really is sharp.”

* * *

At that moment, Team Leader Choi’s expression as he looked at me was strange.

He seemed impressed, but at the same time, he also seemed to have a lot on his mind.

“Why? Is there a problem?”

“Well…”

Team Leader Choi ran a hand through his disheveled hair.

“There are too many problems. I don’t even know which one to mention first.”

“There’s nothing wrong with the mana cultivation method I made, so I assume you mean practical problems.”

“…Yes. Unfortunately, that’s right.”

“Which one is the biggest problem?”

After thinking for a moment, Team Leader Choi opened his mouth.

“To begin with, making this mana cultivation method public would itself be the first problem.”

“Go on.”

“You know very well that mana cultivation methods are a kind of know-how and secret art possessed by only a tiny minority of high-ranking Hunters. You also know how closed-off they are, and how different the world they belong to is from that of ordinary Hunters.”

“I know. I’ve been in this business for years. Of course, back when I was an F-rank Hunter, I’d never even heard of mana cultivation methods.”

No profession in the world had a wider gap between its members than that of a Hunter.

If ordinary people in society distinguished one another based on education, family background, and appearance, Hunters were divided into high and low solely according to rank.

How much mana they had been granted. How agile and strong they were. They were selected according to such primitive standards, then assigned ranks like cattle being marked for slaughter.

*There’s a reason they call F-rank Hunters slaves.*

High-ranking Hunters, on the other hand, were practically beings who lived above the clouds.

They made more money from a single raid than most Hunters could earn in a lifetime, and lived beneath envious gazes and the glare of the spotlight.

That was probably why.

Just as the nobles of the past had built castles and lived inside them, high-ranking Hunters had built walls meant only for themselves.

Walls no one but another high-ranking Hunter could cross.

Even if someone was lucky enough to receive a high rank, the door would open only with their permission.

Connected by invisible threads, those high-ranking Hunters were scattered across the world, each receiving the protection of the giant Guilds they belonged to.

“This isn’t a problem limited to Korea. If you reveal this mana cultivation method to the world, there will be far greater opposition than you expect.”

“Because they’ll think that if we release a mana cultivation method, the value of the ones they possess will drop?”

“That’s part of it, but there’s another reason.”

“What is it?”

“The problem is that it’s *us*.”

“……!”

It was a short answer, but I immediately understood what he meant.

*Have we stood out too much all this time?*

I suddenly remembered the conversation I’d had with Jeok Cheongang just before Logout.

His words about how, whether I had wanted it or not, I had already drawn far more attention than necessary.

The spotlight was bright. But everything around it was dark.

The line I had read in a novel I liked back in school had been right. The brighter I became, the deeper the darkness surrounding me grew.

In Murim. And in the modern world.

“Team Leader Choi, by any chance…?”

Realizing what I was asking, Team Leader Choi shook his head.

“There’s no major problem yet, but… invisible pressure is being brought to bear on us. That’s why we’ve temporarily put the establishment of additional overseas branches on hold.”

“That serious?”

“Every major Guild in the world is watching us right now. Even if they don’t stage a show of force, if they make a move somehow, the situation won’t be easy for us either.”

“Then why didn’t you tell me?”

Team Leader Choi answered with a stern expression.

“Did you give me a chance to tell you?”

“…That’s fair.”

Still, this place was a complete mess too.

People who already possessed a great deal naturally disliked seeing the world change.

The tiny minority of Hunters who had learned their own mana cultivation methods were no exception.

*No. At this point, it would be more accurate to call them power brokers than Hunters.*

Power brokers who might even be able to manipulate an entire country.

With their enormous wealth, fame, and overwhelming strength, they overturned even common sense. They wanted no further change. They did not want another power to appear that could stand alongside them.

People like me and Team Leader Choi, for example.

*Even so, these bastards seem worse than the Murim sects.*

They said that Murim sects would chase someone down with murder in their eyes and smash his head if their unique martial arts were leaked, but at least they wouldn’t throw a fit at a merchant for selling the Three Calamities Sword Technique in a marketplace.

But these bastards already had more than enough, and they were still ready to cause a scene because we wanted to release one little mana cultivation method?

*Huh? Now I’m pissed.*

“If we release this mana cultivation method, they’ll make a huge fuss, right?”

“Yes. And it’ll be chaos for us too.”

“Then what if I go after them?”

“What?”

“Now that I think about it, it’s fucking ridiculous. Let’s just release the mana cultivation method without overthinking it, and then go after the assholes who start making trouble. That should shut them up…”

“No! Don’t! Absolutely not!”

For Team Leader Choi’s normally low, composed voice to reach that many decibels meant one thing:

*You’ll have to walk over my corpse first, you lunatic.*

But this time, I couldn’t easily agree with him.

“I understand what you mean, Team Leader Choi, but we have to make this public. I didn’t create it so I could keep it to myself like a diary.”

The world’s mana had already increased. No—it was continuing to increase even at this very moment.

As a result, mutation Gates were appearing one after another, and now even monster waves were occurring.

“Monsters are growing stronger as the mana increases. You know that too, Team Leader. But if people learn about this mana cultivation method under the current circumstances…”

“The overall level of Hunters will rise. It’s stable enough that even the lowest-grade Hunters can learn it without difficulty.”

Team Leader Choi continued with a solemn expression.

“I understand what you’re thinking, Mr. Jin. Wasn’t that why you suppressed the various rebel groups and terrorists in the first place—to reduce the possibility of the mana cultivation method being misused as much as possible?”

“Yes. I had to consider whose hands the weapon I created would fall into before considering how sharp it was.”

About two weeks ago by modern-world time, an incident in Texas, United States, had given me a serious warning.

A terrorist attack using a Magic Gem.

Fortunately, the terrorists’ attempt had ended in failure, and there had been no casualties. But that incident had made me realize something for certain.

“When I said *everyone*, I realized that I was including all kinds of criminals and lunatics.”

Afterward, I followed Magic Johnson to the Pentagon and obtained information about them with the tacit approval of the President of the United States. Alongside the people who had come with me, I dyed the desert red with blood and cut away every element that might become a threat.

Rebel groups that trained kidnapped children in firearms. Fanatical terrorists who were willing to commit even suicide attacks…

I killed anyone who stood in the way, and the dead were bound to the Skeleton King’s undead army, which chased after those who fled.

At the same time, I issued false orders to those in distant locations through their captured leaders.

I ordered the rebel groups to attack the terrorist organizations, and the terrorist organizations to attack the rebel groups.

It was a war between bastards and motherfuckers, and after being duped by those false orders into launching all-out attacks against each other, both sides paid the price in massive losses—enough to leave them grievously wounded.

“As you know, Team Leader Choi, completely uprooting them won’t be possible this time or in the future, but we’ve already achieved our objective under the current circumstances. Even if those bastards learn this mana cultivation method, they won’t be as much of a threat as before.”

The only ones who would grow stronger through the mana cultivation method I created were not those bastards.

The overall level of Hunters would rise enough for them to respond to the monsters strengthened by the increase in mana, and that would allow us to maintain the balance.

*If the situation gets much worse than it is now…*

At that point, I intended to reveal even the Jin Family’s Cultivation Technique, which I had so far shared with only a tiny handful of people, including Team Leader Choi.

The low-ranking Hunters who knew absolutely nothing about mana cultivation methods would not be able to apply the Jin Family’s Cultivation Technique even if I handed it to them right now. But once they had learned the method, they would be able to cultivate it on their own.

I looked straight at Team Leader Choi and opened my mouth.

“We have to make it public, one way or another.”

“……”

“Fortunately, it isn’t too late yet. Public opinion and interest toward you and me are still fairly favorable.”

In fact, they were more than favorable. They were fervent.

I was being called a young hero born from the new age, while Team Leader Choi had succeeded Butler Kim, who had passed away, and taken over as Guild Master of the Peace Guild. Before the freshly made plaque had even had time to cool, he had also taken control of the Ares Guild.

On top of that, he had a more glorious halo than anyone else’s.

He was the sole blood relative and heir of Cheon Taemin, the savior who had rescued humanity from the Demon King Asmodeus.

Grab.

“Team Leader Choi.”

My hand tightened around his. When Team Leader Choi met my burning gaze, he flinched as though he had been burned.

“W-Why are you suddenly doing this?”

His reaction was almost as if he had run into Magic Johnson in a dark alley at night. But I didn’t back down and continued speaking firmly.

“If you’re really that worried, let’s try another way. Okay?”

“And what way would that be…?”

“Put your maternal grandfather’s name to work for us just this once.”

“What?”

“Come on. Let’s ride the Savior coin just once while we’re at it.”

“……!”
```
