<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0805.txt",
      "sha256": "df2cbd94fd3fb807a9eb5ba4f7c9fab08d0c6920ccd37d6becc63e78b414c4ba",
      "bytes": 14479
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "ef0a743122bbf9caba3b7d9697b1c79d1355d43de03f9d375dd50d3807364900",
      "bytes": 1513
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "100f68bfda71f40b74d4770881e96f6f66cdf9d7745c21e9555d2006d308e1cf",
      "bytes": 225046
    },
    {
      "path": "characters/Hwangso.md",
      "sha256": "de4c5f868e5ac7d223e1a3ce5e97d8ea7f41dd88e46e50247e52325a8f06f69a",
      "bytes": 698
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "3b1ff7bd6d72759728ede64bf6cdc36bd4e334e099e0b0badb0e0fe5fc0c7d00",
      "bytes": 1921
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "ca89d883d95380876aba1e818c364724ba87f97dac1ace4d601513613aeb9288",
      "bytes": 622
    },
    {
      "path": "characters/Team Leader Choi.md",
      "sha256": "fc3b7ec92f95ec871d5d63a25b6aba20d2499fa55c75c5608c22b0a8036811cd",
      "bytes": 645
    },
    {
      "path": "characters/The Prophet.md",
      "sha256": "84643a8da5e946c3d82c842e5d5d228379e0499441ce5833c91c9794349834e1",
      "bytes": 707
    },
    {
      "path": "characters/Yamamoto.md",
      "sha256": "171410c05d4465d62f09d83cd805c3b5db3a398eda4ae81ddd8c6b6b38c6dd96",
      "bytes": 574
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "8bd8b3dadce9eb815c5d9dd06390882ed0e507ef0582faa521024fa16dde0508",
      "bytes": 247238
    }
  ],
  "estimated_tokens": 10906
}
-->

# Durable State Update — Chapter 805

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 805. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 805. Profile updates may replace only one
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
  "chapter": 805,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 805,
    "continuity_sources": [805],
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
    "Jin Taekyung is the World Hunter Federation’s Alliance Leader and pursues Main Quest [Cataclysm], which requires him to eliminate The Prophet within an unspecified time limit.",
    "Taekyung commands roughly one thousand Hunters against a monster force exceeding ten thousand in the Rub’ al Khali.",
    "Three S-rank monsters lead the ground force, and a Griffon leads hundreds of flying monsters.",
    "Taekyung believes The Prophet is observing the battlefield from a distance, but his location is unknown.",
    "Taekyung attacked the Scorpion King and then charged toward the S-rank monsters.",
    "Magic Johnson is following Taekyung’s orders to protect allies and counter aerial threats; Team Leader Choi is holding the front line.",
    "The Skeleton King’s undead can raise fallen monsters as soldiers, limited by the magical power he bestowed.",
    "Amir and Hamid lead desert fanatics advancing toward their promised land, believing the time foretold by The Prophet has arrived."
  ],
  "continuity_sources": [
    803,
    804
  ],
  "open_questions": [
    "Where is The Prophet, and when will he enter the battle?",
    "What are the identities and capabilities of the other S-rank monsters?",
    "How will the battle against the advancing ground and aerial forces unfold?"
  ],
  "safe_through": 804,
  "temporary_decisions": [
    "Keep magical power distinct from mana.",
    "Render 강기 as Force, distinct from Sword Force."
  ],
  "version": 1
}
```

## Exact glossary matches

| 진태경    | **Jin Taekyung**   |
| 최민우    | **Choi Minwoo**   |
| 화왕     | **Fire King**                 | Jeok Cheongang |
| 살성     | **Slaughter Saint**           | —              |
| 열양지기   | **Scorching Yang Qi**                            | Fire-aligned qi                                       |
| 깨달음    | **enlightenment** / **insight**                  | Martial enlightenment                                 |
| 제자     | **Disciple**                                 |
| 일격     | **One Strike**                         |
| 시스템              | **System**                     |
| 레벨               | **Level**                      |
| 지능               | **Intelligence**               |
| 헌터      | **Hunter**            |
| 게이트     | **Gate**              |
| 몬스터     | **monster**           |
| 도사      | **Daoist**                                                      |
| 황소 | **Hwangso** | First-generation disciple of the Gongdao Sect and a reluctant search-party member. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 선지자 | **The Prophet** | Mysterious religious leader directing the terrorist warriors. |
| 야마모토 | **Yamamoto** | Japanese S-rank Hunter named in post-Leviathan media coverage. |
| 화염신장 | **Flame Divine Palm** | Jopil's deadly palm technique, noted when Taekyung compares Jopil with Mukyung. |
| 오우거 | **ogre** | B-rank monster species emerging from the Gate. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 라이칸스로프 | **Lycanthrope** | B-rank Gate monster species. |
| 만티코어 | **Manticore** | A-Rank Gate monster and original raid target. |
| 백염 | **White Flame** | Name of Jin Taekyung's newly forged spear. |
| 멸염신권 | **Flame-Extinguishing Divine Fist** | Named fist technique Taekyung announces at the chapter's end. |
| 마도 | **Demonic Path** | Term raised for martial power that appears to defy common principles. |
| 화룡 | **fire dragon** | Fire-dragon image within Taekyung's dantian that awakens before the duel. |
| 염화일로 | **Flamefire Path** | Fire Gate Clan signature movement technique; Jeok Cheongang has reached its ninth stage. |
| 꼬리 | **the “tail”** | Codename for the Black Hunter traced by Butler Kim. |
| 그분 | **that person** | Unidentified figure whom Jihoon reveres and credits with disabling cameras and microphones. |
| 준이 | **Jun** | Family nickname used in the form Jun's dad. |
| 스켈레톤 | **Skeleton** | Undead monster species. |
| 존슨 | **Johnson** | Co-host of the American talk show that replays Taekyung's viral interview. |
| 마계어 | **Demon Realm language** | Language spoken by monsters from the Demon Realm. |
| 화룡일미 | **Fire Dragon's Single Tail** | A form of the Fire Dragon Divine Spear. |
| 천격 | **Heavenly Strike** | A Fire Dragon Divine Spear form used by Taekyung against Hwangbo Eom. |
| 겁화 | **hellfire** | Destructive fire energy used by Taekyung. |
| 화룡갑 | **Fire Dragon Armor** | Jin Taekyung's renamed bound armor, formerly the Black Dragon Armor. |
| 데스나이트 | **Death Knight** | Undead commander type serving under the Black Knight. |
| 마법 | **Magic** | Taekyung's explanation for Dark Heaven's anomalous abilities. |
| 위압 | **Intimidation** | System attribute strengthened by the achievement reward. |
| 이전 | **Two Halls** | Top-level Murim Alliance organizational grouping. |
| 대마도사 | **Grand Mage** | Title used for Magic Johnson. |
| 서리 | **seori** | Colloquial term for stealing crops or produce from a field. |
| 마력 | **magical power** | Distinct from mana; the Skeleton King's area of expertise. |
| 마계 | **Demon Realm** | Realm associated with the S-rank monsters and Leviathan. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 데스나이트 | 인간 | enemy combatants | human | contemptuous and commanding | Used in the Death Knight's warnings to Jin. |
| 데스나이트 | 로드 | subordinate to commanding lord | Lord | fearful and deferential | The Death Knight calls to the Death Knight Lord after Jin overwhelms the army. |
| 최민우 | 진태경 | trusted allied team leader to younger allied Hunter | Mr. Jin | formal-polite and concerned | Choi warns Jin about the danger of the operation and affirms his deep trust. |
| 진태경 | 최민우 | younger allied Hunter to allied team leader | Team Leader Choi | polite, familiar, and teasing | Jin jokes with Choi while acknowledging and dismissing his concern. |
| 진태경 | 존슨 | Allied Hunter to Grand Mage | Johnson | polite and familiar | Jin repeatedly addresses Magic Johnson directly while requesting explanations and permission to visit the site. |
| 진태경 | 헌터 | field commander to allied Hunters | you; Hunters | blunt and commanding | Orders the human forces to stop asking questions and kill the fleeing Minotaurs. |
| 최민우 | 존슨 | allied Hunter to allied Grand Mage | Mr. Johnson | formal-polite | Minwoo calls out to Johnson during the battle. |
| 진태경 | 야마모토 | Alliance Leader to Japanese S-rank Hunter he sent on the mission | Yamamoto | blunt and familiar | Jin quietly says Yamamoto’s name while treating him. |
| 야마모토 | 진태경 | Japanese Hunter to the Alliance Leader who rescued him | Chōsenjin | insulting | Yamamoto uses the ethnic slur as he regains the ability to speak. |

## Listed compact profiles

### Hwangso.md

# Hwangso (황소)

- **Safe through:** Chapter 728
- **Aliases:** None
- **Role:** First-generation disciple of the Gongdao Sect in Sichuan, deployed with roughly thirty second- and third-generation disciples to search for the surviving Third Fiend.
- **Personality:** Privileged, impatient, pleasure-seeking, inattentive, and dismissive of the danger surrounding the mission.
- **Voice:** Complaining and casual, with irreverent sarcasm toward his Senior Brother and the search.
- **Relationships:** His Senior Brother supervises him, and his prosperous merchant father forced him into the Murim to establish family connections.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 802
- **Aliases:** Blazing Flame Divine Dragon; Apostle of the Earth Mother Goddess; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan, Jeok Cheongang’s Disciple, the Fire Gate Clan’s nineteenth successor, Pavilion Master of the Fire Dragon Pavilion, a Supreme Peak master and publicly recognized S-rank-level Hunter with an A-rank license, a traveler between Murim and another world, and the World Hunter Federation’s Alliance Leader.
- **Personality:** Hungry, self-aware, dryly observant, pragmatic under pressure, and willing to risk himself for people he has accepted as real; treats impossible situations like games until their human cost becomes undeniable.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, Jeok Cheongang is his Master, Mungyeong was his recent instructor, Cheongpung is his trusted companion and only true martial rival, Choi Minwoo is his subordinate and trusted manager of media and official arrangements as well as the Peace Guild's Guild Master, Ju Hwaran is a trusted Fire Dragon Pavilion member who followed him to Nanman, Magic Johnson is an allied Grand Mage who supplies him with intelligence, Chuck Hagel is an American operative allied with him in the covert anti-terror campaign, his mother and sister Hayeon are among those he protects, the Skeleton King is his friend and ally, Xiao Shen regards him as an older brother after Jin saved him, and Jin-ho is his older friend and trusted confidant.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 802
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Team Leader Choi.md

# Team Leader Choi

- **Safe through:** Chapter 804
- **Aliases:** Choi Minwoo (최민우)
- **Role:** Team Leader Choi is Jin Taekyung's meticulous intelligence and operations lead, a trusted ally and natural leader capable of guiding the reestablished World Hunter Federation.
- **Personality:** Calm, pragmatic, meticulous, and emotionally steady under pressure.
- **Voice:** Measured, professional, and reassuring without minimizing responsibility.
- **Relationships:** A trusted ally and operational adviser to Jin Taekyung, and the maternal grandson of Cheon Taemin.

### The Prophet.md

# The Prophet (선지자)

- **Safe through:** Chapter 804
- **Aliases:** Muninn (무닌)
- **Role:** The Prophet is a monster posing as the leader of the revived Hasasin, whose power includes stopping transport vehicles and absorbing blood and a pale mist from the dead.
- **Personality:** Religiously fervent, commanding, and shrouded in an intentionally indistinct identity.
- **Voice:** Mysterious, genderless, and age-indeterminate, speaking in solemn religious imperatives.
- **Relationships:** The Prophet commands the ten warriors, is revered by the followers, and secretly communicates with Michael Silbert through a magic mirror.

### Yamamoto.md

# Yamamoto (야마모토)

- **Safe through:** Chapter 804
- **Aliases:** None
- **Role:** Yamamoto Genji is a Japanese S-rank Hunter and J1’s sole survivor.
- **Personality:** Prideful and easily offended, prone to self-aggrandizement and self-serving assumptions, and cowardly under mortal threat.
- **Voice:** Not established.
- **Relationships:** Jin Taekyung sent Yamamoto on the J1 mission and treated him after the attack, though Jin resents Yamamoto for arriving late during the Leviathan crisis.

## Korean source

```text
＃805화



맹수.

지금 이 순간, 모두의 눈에 비친 진태경은 그야말로 맹수 같았다. 굶주린 호랑이처럼 사납고, 사자처럼 위엄 있으며, 표범처럼 날렵한.

콰아아아!

모래과 흙이 사방을 휘감으며 솟구친다. 제자리에서 일렁거리듯 사라진 진태경의 신형이 무시무시한 속도로 쏘아졌다.

염화일로(炎火一路).

한 줄기의 화염이 공간을 가로질렀다. 그저 거칠게 들이닥칠 뿐이었던 이전과는 비교도 할 수 없을 만큼 빠르고, 동시에 절제된 움직임.

화왕(火王)과 살성(殺星)이라 불리는 두 거인이 평생에 걸쳐 이룩한 깨달음을, 이제 진태경은 조금이나마 이해할 수 있을 것 같았다.

시시각각 가까워지는 눈앞의 적들을 어떻게 쓰러트려야 하는지도.



[Lv.130 라이칸스로프 챔피언]

[Lv.140 데스나이트 군단장]

[Lv.148 만티코어 로드]



짙어진 마력 농도에 따라 더욱 높은 레벨을 지니게 된 S급 몬스터들.

그러나 레벨은 상대의 강함을 결정짓는 절대적인 척도가 아니다.

레벨이 낮아도 더 거대한 기운을 지니고 있을 수도 있고, 레벨이 높아도 육체적인 능력이 떨어질 수도 있다.

상대의 수준이 최상위권에 접어들었다면, 그때부터는 결국 타이밍과 상성의 문제라는 뜻이다.

진태경이 조금 전의 기습으로 140레벨이나 되는 스콜피온 킹을 통구이로 만들어 버렸던 것처럼.

그리고 그 상대의 힘과 상성을 가장 빠르게 파악하는 방법은 단 하나뿐이었다.

바로 직접 몸으로 부딪쳐 보는 것.

쉭.

수십여 미터의 거리가 단숨에 지워진 그 순간.

낮게 중심을 유지한 채 정면으로 달려든 진태경을 향해 세 줄기의 섬광이 떨어져 내렸다.

쏴아아악!

데스 나이트의 검과 라이칸스로프의 도끼. 마지막으로 만티코어의 발톱까지.

공간을 일그러트리는 듯한 착각마저 불러일으키는 검붉은 마력이 진태경의 몸뚱어리를 관통했다.

아니, 적어도 세 마리의 S급 몬스터는 그러리라 믿어 의심치 않았다.

콰앙!

굉음과 함께 땅거죽이 뒤집힌 그때, 머리 위로 어두운 그림자가 드리워지기 전까지는.

- ……!

머릿속 경고등과 함께 타고난 본능이 깨어난다.

단순한 괴물이라 치부할 수 없을 만큼 뛰어난 지능을 갖춘 S급 몬스터들은 곧장 상황을 깨달았고, 한편으로는 도무지 이해할 수 없는 눈앞의 현실을 받아들여야 했다.

한없이 작고 나약한 저 인간의 몸뚱어리에, 그들을 뛰어넘는 힘과 기운이 들끓고 있다는 사실을.

그리고 그 순간.

‘천격(天格).’

지면을 향해 내리꽂히는 진태경의 신형과 함께, 백염의 창날을 타고 쏟아진 청백색의 겁화가 사방을 휩쓸었다.

화륵, 콰아아아아!

대마도사가 펼치는 파이어 월(Fire Wall) 마법만큼이나 광범위하고, 그보다 뜨거운 열기를 머금은 초고온의 화염이 몬스터 군단의 선두를 집어삼켰다.

보는 이로 하여금 몸서리칠 정도로 탐욕스럽고, 그 어떤 맹수보다 광포하게.

- 끄아아아아아!

- 끼이잇!

띠링. 띠링. 띠링.

생애 마지막으로 내지르는 단말마와 시스템 알림이 뒤섞인다.

그러나 까맣게 물든 잿더미의 중심에서 몸을 일으키는 진태경을 기다리고 있던 것은 비단 그뿐만이 아니었다.

- 네. 놈. 이. 감. 히!

라이칸스로프 챔피언.

영원한 달의 저주에 갇혀 버린 최강의 반인반수(半人半獸)가 포효와 함께 거대한 도끼를 휘둘렀다.

후우웅!

휘몰아치는 검붉은 마력이 공간을 가르고, 바람을 지웠다,

그리고 눈앞의 인간을 단숨에 반으로 쪼개 버리려던 그때. 화염을 머금은 백염의 창날이 섬광처럼 솟구쳤다.

쩌엉!

날카로운 울림. 동시에 단단하기 그지없는 도끼날이 폭발하듯 터져나갔다.

콰득, 퍼엉!

산산이 부서진 도끼가 사방으로 비산한다.

수백 개가 넘는 무수한 파편이 자신들의 지휘관을 구하기 위해 달려오던 몬스터들을 덮쳤다.

푸푸푸푹!

- 크아아악!

비명과 핏물이 솟구치고, 시체 위에 또 다른 시체가 쌓인다.

샛노란 눈동자를 부릅뜬 채 굳어 버린 라이칸스로프 챔피언을 향해, 진태경은 한 치의 망설임 없이 창날을 내리그었다.

아니, 그러려고 했다.

그 순간 양옆에서 들이닥친 파공성이 아니었다면.

쉬이이익!

진태경은 벼락처럼 허리를 뒤로 젖혔다. 머리카락이 땅에 닿았고, 두 줄기의 맹렬한 바람이 얼굴 위를 아슬아슬하게 스쳐 지나갔다.

피핏!

압력을 이기지 못하고 터져 나간 살갗에서 따끔한 통증이 전해졌지만, 이 정도쯤은 아무런 문제도 되지 않는다.

이것이 공격을 피하는 대가라고 생각한다면 터무니없는 헐값이니까.

‘받은 것 이상으로 되갚아 주면 그만이지.’

생각보다 앞서 몸이 움직인다. 신형을 바로 세운 진태경은 창대를 놓으며 쌍장(雙掌)을 뻗었다.

후웅, 콰앙!

지면을 뒤흔드는 충격과 굉음.

그러나 막대한 마력에 휩싸인 검과 발톱이 화염신장(火焰神掌)의 여파를 상쇄시켰다.

아니, 거기에서 그치지 않고 한발 더 나아갔다.

쏴악!

데스나이트 군단장이 빛살처럼 내리그은 일격이 공간을 가르고.

- 크허어어엉!

포효와 함께 쇄도하는 라이칸스로프의 옆으로, 만티코어 로드의 강철 같은 가시가 돋아난 꼬리가 채찍처럼 휘둘려졌다.

‘합공? 서로 종족도 다른 몬스터가?’

진태경은 세 갈래로 나뉘어 날아드는 공격을 보며 눈을 크게 떴다. 그리고 그 잠깐의 머뭇거림이, 아주 약간의 빈틈을 만들었다.

쐐애애액! 꽈앙!

자그마치 세 마리나 되는 S급 몬스터다.

하나로 합쳐진 파괴력은 폭발적으로 끌어올린 열양지기로도 감당할 수 없을 만큼 엄청났고, 그중에서도 만티코어 로드의 교활함과 힘은 생각했던 것 이상이었다.

쉭, 서걱!

뜨겁다. 불에 지지는 것처럼.

그러나 허벅지로부터 전해지는 고통을 온전히 느낄 새도 없이 잇따라 터져 나온 세 개의 섬광이 눈앞을 물들였다.

쾅!

하늘이 쪼개지는 듯한 굉음과 함께 뒤로 쏘아지는 신형.

허공에서 몸을 틀어 중심을 되찾은 진태경은 착지하는 동시에 일권(一拳)을 내질렀다.

퍼엉!

주먹을 타고 터져 나온 멸염신권(滅炎神拳)의 열기가 전방을 휩쓸었다.

불길 속에서 괴성을 내지르며 타들어 가는 몬스터들의 사이로 검붉은 마력이 뿜어져 나왔다.

화아악.

사방을 짓누르는 압력과 함께 삽시간에 잦아드는 불길.

몸부림치는 부하들마저 망설임 없이 베어 낸 세 마리의 S급 몬스터가 진태경을 향해 재차 쏘아지려던 그때, 불현듯 누군가의 목소리가 울려 퍼졌다.

- 좋아. 거기까지.

의심의 여지가 없는 마계어(魔界語)에 발걸음이 우뚝 멈췄다.

그런 S급 몬스터들을 바라보며 씩 웃은 스켈레톤 킹이 진태경을 향해 한 마디를 툭 내뱉었다.

“미친놈.”

곱지 않은 눈초리에 진태경이 담담하게 되물었다.

“왜.”

“그렇게 혼자서 튀어 나가면 뭐 어쩌란 말이냐? 조금 전에는 한 마리씩 맡자며?”

“이것저것 간 좀 봤다. 어느 놈이 제일 강하고, 어떤 놈이 제일 약한지.”

스켈레톤 킹의 시선이 문득 아래를 향했다. 무언가에 의해 뜯겨 나간 듯한 진태경의 허벅지는 이미 피범벅이 되어 있었다.

상반신을 감싼 화룡갑(火龍鉀)을 염두에 둔 듯한 일격. 만티코어 로드는 강한 것만큼이나 영리했다.

“간을 본 게 아니라 피를 본 것 같은데.”

“생각 이상으로 강해. 그중에서도 특히 한 놈은 S급 중에서도 네임드 수준이고.”

“저놈들 중에? 누구?”

“가운데에 있는 저놈.”

“만티코어? 확실히 척 보기에도 특출난 놈이군.”

굳은 얼굴로 만티코어 로드를 노려보던 스켈레톤 킹이 스산하게 뇌까렸다.

“그래, 네놈에게 부상을 입힌 게 저놈이란 말이지.”

“어차피 그렇게 심한 부상도 아냐. 내가 만티코어를 상대하는 편이 훨씬…….”

“좋아. 이 몸이 데스 나이트를 상대하겠다.”

“……?”

“뭐지. 그 기분 나쁜 눈빛은?”

“아니 그, 보통 이럴 때는 친구의 복수라고 해야 하나. 뭐 그런 맥락으로 흘러가지 않냐?”

진태경의 말을 들은 스켈레톤 킹이 눈을 동그랗게 떴다.

“그게 무슨 개소리냐. 제일 센 놈끼리 붙어야 훨씬 승산이 있지.”

“…….”

“어쨌든 그렇게 결정한 거다. 네놈이 만티코어. 이 몸이 데스 나이트. 그리고 마지막으로 저기 저 라이칸스로프는…….”

문득 말꼬리를 흐린 스켈레톤 킹이 주위를 둘러보았다. 그리고 눈을 깜빡였다.

“왜 우리 둘뿐이지?”

허벅지를 지혈한 진태경이 친절하게 대답했다.

“한 새끼는 이미 도망쳤으니까.”

“어?”

“그나마 양심은 있었는지, 아예 도망치진 않고 저기 뒤로 빠져 있네. 선두 대열.”

저 멀리, 은근슬쩍 최민우의 옆으로 다가가 결의에 찬 표정을 짓고 있는 야마모토 겐지의 모습을 발견한 스켈레톤 킹이 중얼거렸다.

“저놈. 반드시 죽여 버릴 거다.”

“그래, 그전에 이 지긋지긋한 싸움부터 빠르게 끝내자고.”

진태경이 피가래를 탁 뱉으며 창을 늘어트렸다.

이미 등 뒤에서는 비행 몬스터들이 내지르는 괴성과 폭발음이 터져 나오는 중이었다.

‘매직 존슨이라면 충분히 막을 수 있다.’

그저 믿을 뿐이다. 그가, 저들이 자신을 믿어 주었듯이.

저벅. 쿵.

세 마리의 S급 몬스터가 걸음을 내딛자 군단 전체가 움직인다.

아무리 죽이고 또 죽여도, 도무지 줄어들 것 같지 않은 몬스터의 파도.

반면 사방이 탁 트인 사막은 인간들에게 있어 최악의 전장이었다.

“빌어먹을. 이 몸이 몬스터가 된 이후로 가장 후회하는 일이 뭔 줄 아느냐?”

진태경이 망설임 없이 대답했다.

“알지. 클럽 못 간 거.”

“틀렸어. 바로 네놈과 얽혔다는 거다.”

“그래? 나랑 정반대네.”

“뭐?”

“내가 살면서 가장 잘한 것 중 하나가, 널 그 게이트에서 꺼내 온 거거든.”

“……제기랄. 나만 쓰레기냐?”

“알면서 뭘 물어.”

피식 웃은 스켈레톤 킹이 깊게 심호흡했다. 숨 대신 흘러나온 죽음의 기운이 주위에 널브러진 몬스터들을 일으켜 세웠다.

그 숫자가 도합 일천.

전투과 통솔을 동시에 치른다는 가정하에 유지할 수 있는 최대치였지만, 서서히 속력을 높여 다가오는 저 대군세를 막아 내기에는 초라한 병력이다.

“저것들을…… 전부 막을 수 있을까?”

아니.

진태경은 혀끝에서 맴도는 그 대답을 삼키며 생각했다.

‘누군가는 죽게 되어 있다. 반드시.’

그것이 전투고, 그렇기에 전쟁이다.

모두를 살릴 방법 따위는 어디에도 없다.

다만 그가 한 가지 약속할 수 있는 것은, 모두 살아 나갈 수 있다는 공허한 약속이 아닌 복수다.

“오늘 이 자리에서 우리 중 몇 명이 죽건…….”

스릉.

길게 늘어지는 말꼬리와 함께, 번뜩이는 창날이 몬스터들을 겨누었다.

“저놈들은 전부 내 손에 뒈진다.”

스켈레톤 킹의 눈이 크게 뜨인 그 순간.

콰드드드득!

헤아릴 수 없을 만큼 무수한 몬스터의 파도가, 그들을 덮쳤다.



* * *



……!

……!!

귓가가 먹먹하다. 일만이 넘는 몬스터 대군이 움직이는 것만으로도 지축이 뒤흔들리고, 놈들이 내지르는 괴성은 땅끝과 하늘 위까지 닿을 듯했다.

그리고 그 선두이자 중심에, 바로 놈들이 있었다.

화륵, 서걱!

화룡일미(火龍一尾).

창날을 따라 그려 낸 화염의 선이 허공을 가른다. 피할 수도, 막을 수도 없는 그 궤적에 걸려든 수십여 개의 목이 지면으로 굴러떨어진다.

푸화아악!

뒤늦게 터진 핏물이 사방을 적신다. 그러나 흉포한 괴성과 함께 달려들어야 했을 몬스터들은 나와 스켈레톤 킹을 피해 뿔뿔이 흩어졌다.

내가 보인 무위와 [위압] 때문에?

아니다. 나를 피해 헌터들에게 돌격하는 놈들에게서 보이는 건 두려움이 아닌, 다른 누군가에 대한 복종이었다.

마치 훈련받은 정예군만이 보일 수 있는 복종.

“이런 개 같은……!”

퍼걱!

오우거의 머리통을 터트린 스켈레톤 킹이 분노 어린 외침을 토해 냈다.

그와 나, 그리고 언데드 군단이 있었지만 적들 모두의 앞길을 막아서는 것은 무리였다.

열을 죽이면 백이. 백을 죽이면 천 마리의 몬스터가 빠져나간다.

우리가 펼친 그물은 촘촘했지만 너무나도 작았고, 그것이 바로 놈들이 의도했던 바였다.

- 그래, 너로구나. 그분께서 말씀하셨던 인간이.

머릿속으로부터 들려오는 듯한 목소리.

마치 귀족이 말하는 것처럼 매끄럽고 침착한 어조는 높은 지능을 증명하고, 그 말에 담긴 의미는 내 짐작과 일치한다.

“선지자. 지금 어디 있어?”

호랑이의 얼굴과 몸뚱어리. 맷돼지의 송곳니와 황소의 뿔을 지닌 신화 속 괴물.

만티코어 로드가 빙긋 웃으며 대답했다.

- 어디에나 있고, 어디에도 없으시지.

“저게 무슨 개소리냐?”

스켈레톤 킹의 물음에, 나는 대답했다.

“존나게 처맞으면 말해 주겠다는 뜻이지.”

그리고 놈을. 아니, ‘놈들’을 향해 창날을 내리그었다.

슈확!

바람이 갈라졌다.
```

## Final English reading copy

```markdown
# Chapter 805

A beast.

At this very moment, Jin Taekyung looked like a beast to everyone watching. Fierce as a hungry tiger, majestic as a lion, and swift as a leopard.

*Rumble!*

Sand and earth surged up, swirling in every direction. Jin Taekyung’s figure vanished from where he stood, as if rippling out of sight, then shot forward at terrifying speed.

Flamefire Path.

A single streak of flame cut across the space between them. It was incomparably faster than his earlier, reckless charge—and, at the same time, controlled.

Jin Taekyung felt he could now understand, if only a little, the enlightenment the two giants known as the Fire King and the Slaughter Saint had achieved over the course of their lives.

He even felt he knew how to bring down the enemies drawing closer by the second.

> **System**
> Lv. 130 Lycanthrope Champion
> Lv. 140 Death Knight Legion Commander
> Lv. 148 Manticore Lord

S-rank monsters whose levels had risen along with the increased concentration of magical power.

But Level wasn’t an absolute measure of an opponent’s strength.

A lower-Level enemy might possess far greater energy, while a higher-Level one could be physically weaker.

Once your opponent reached the highest tier, it ultimately came down to timing and matchup.

Just as Jin Taekyung had turned the Level 140 Scorpion King into a roast with his surprise attack a moment ago.

And there was only one way to figure out an opponent’s strength and matchup as quickly as possible.

Go head-to-head and find out.

*Whoosh.*

In the instant the distance of several dozen meters vanished—

Three streaks of light fell toward Jin Taekyung as he charged straight at them, keeping his center of gravity low.

*Shraaah!*

The Death Knight’s sword. The Lycanthrope’s axe. And, last of all, the Manticore’s claws.

Dark crimson magical power, so thick it seemed to warp space, pierced Jin Taekyung’s body.

Or at least, the three S-rank monsters had no doubt that it had.

*Boom!*

The earth flipped over with a deafening crash. Then a dark shadow fell overhead—

—and their instincts awakened alongside the warning lights flashing in their minds.

The S-rank monsters were intelligent enough that they couldn’t be dismissed as simple beasts. They immediately realized what had happened, and at the same time, were forced to accept the incomprehensible reality before their eyes.

That inside the small, frail body of that human, a force and energy greater than their own were boiling.

And in that moment—

*Heavenly Strike.*

As Jin Taekyung plunged toward the ground, blue-white hellfire poured down along White Flame’s spearhead and swept in every direction.

*Fwoosh—KRAAAAAASH!*

The ultra-hot flames, spreading as wide as a Grand Mage’s Fire Wall spell and burning even hotter, swallowed the front ranks of the monster army.

They were horribly ravenous to behold, more ferocious than any beast.

—Aaaaaaagh!

—Kieeet!

*Ding. Ding. Ding.*

System alerts mingled with the dying screams of monsters.

But the screams and System alerts weren’t all that awaited Jin Taekyung as he rose from the center of the blackened ash.

—How. Dare. You!

The Lycanthrope Champion.

The strongest half-man, half-beast, trapped beneath the curse of the eternal moon, roared and swung its enormous axe.

*Whoooom!*

Dark crimson magical power stormed through the air, cleaving space and erasing the wind.

Just as it was about to split the human in front of it clean in two, White Flame’s fire-wreathed spearhead shot up in a flash.

*Clang!*

A sharp ring. At the same time, the impossibly sturdy axe blade burst apart.

*Crack—BOOM!*

The shattered axe flew in every direction.

Hundreds of fragments rained down on the monsters rushing to save their commander.

*Thud, thud, thud!*

Screams and blood burst into the air. Corpses piled atop corpses.

Jin Taekyung stared at the Lycanthrope Champion, frozen with its bright yellow eyes wide, and slashed down with his spearhead without a moment’s hesitation.

Or he would have, if not for the whistling sounds rushing in from both sides.

*Whoooosh!*

Jin Taekyung bent backward like a lightning bolt had struck him. His hair touched the ground, and two fierce gusts passed just inches from his face.

*Pip!*

The skin split under the pressure, and a sharp sting ran through him—but that was nothing.

If this was the price of dodging an attack, it was an absurdly cheap one.

*I’ll just pay them back more than they gave me.*

His body moved before the thought was even complete. Straightening up, Jin Taekyung let go of the spear shaft and thrust out both palms.

*Whoom—BOOM!*

A shockwave and crash shook the ground.

But the sword and claws, shrouded in immense magical power, canceled out the aftershock of the Flame Divine Palm.

No—they didn’t stop there. They pressed the attack.

*Shraaah!*

The Death Knight Legion Commander’s strike cut down like a streak of light.

—Grrraaaah!

As the Lycanthrope charged with a roar, the Manticore Lord swung its iron-hard, spike-covered tail like a whip.

*Are they working together? Monsters of different species?*

Jin Taekyung’s eyes widened as he saw the attacks converging from three directions. That brief hesitation left him with the slightest opening.

*Fwoooosh! BOOM!*

There were no less than three S-rank monsters.

Together, their destructive power was too much to withstand even with his Scorching Yang Qi pushed to its limit. The Manticore Lord’s cunning and strength, in particular, exceeded his expectations.

*Whoosh. Slice!*

It was hot. Like being seared by fire.

But before he could fully register the pain in his thigh, three more flashes erupted one after another, filling his vision.

*BOOM!*

A deafening crash, as if the sky had split, sent him flying backward.

Jin Taekyung twisted in midair to regain his balance, and the moment he landed, he threw a punch.

*Poom!*

The heat of the Flame-Extinguishing Divine Fist erupted from his knuckles and swept forward.

Dark crimson magical power burst from between the monsters shrieking as they burned in the flames.

*Whoooosh.*

The flames died down in an instant beneath a pressure crushing in from every direction.

The three S-rank monsters, who had cut down even their struggling subordinates without hesitation, were about to charge at Jin Taekyung again when someone’s voice suddenly rang out.

—Good. That’s far enough.

The unmistakable sound of the Demon Realm language made them stop in their tracks.

Looking at the S-rank monsters, the Skeleton King grinned and tossed a remark at Jin Taekyung.

“You lunatic.”

Jin Taekyung met his hostile glare with a calm question.

“What?”

“What the hell are you doing charging off alone like that? Weren’t we just saying we’d each take one?”

“I was testing them out. Seeing which one was strongest and which was weakest.”

The Skeleton King’s gaze suddenly dropped. Jin Taekyung’s thigh looked as if something had torn a chunk out of it, and it was already covered in blood.

The Manticore Lord had aimed its attack with the Fire Dragon Armor around his upper body in mind. It was as clever as it was strong.

“Looks more like it tested your blood.”

“They’re stronger than I expected. One of them, especially, is practically a named monster even among the S-ranks.”

“Which one?”

“The one in the middle.”

“The Manticore? It does look exceptional, even at a glance.”

The Skeleton King glared at the Manticore Lord, his face hardening. His voice turned cold.

“So that’s the one who wounded you.”

“It’s not that bad. I’d be much better off taking the Manticore…”

“Fine. I’ll take the Death Knight.”

“…?”

“What’s with that unpleasant look?”

“No, I just thought this was where you’d say you were avenging your friend or something.”

The Skeleton King’s eyes widened at Jin Taekyung’s words.

“What the hell are you talking about? We’ve got a much better chance if the strongest fight the strongest.”

“…”

“Anyway, that’s the plan. You take the Manticore. I’ll take the Death Knight. And that Lycanthrope over there…”

The Skeleton King trailed off and looked around. Then he blinked.

“Why is it just the two of us?”

Jin Taekyung, who had staunched the bleeding in his thigh, kindly explained.

“One of them already ran off.”

“Huh?”

“Maybe he had a shred of conscience left, because he didn’t run off entirely. He’s back there in the front ranks.”

Far off, Yamamoto Genji had sidled up beside Choi Minwoo and was putting on a determined expression. The Skeleton King spotted him and muttered,

“I’ll kill that bastard someday.”

“Sure. But first, let’s finish this damn fight as quickly as we can.”

Jin Taekyung spat a mouthful of bloody phlegm and lowered his spear.

Behind him, the flying monsters were already screaming, and explosions were going off.

*Magic Johnson can hold them off.*

All he could do was trust him. Just as he, and the others, had trusted Jin Taekyung.

*Clop. Thud.*

The three S-rank monsters took a step forward, and the entire army moved with them.

No matter how many monsters they killed, the wave seemed like it would never get any smaller.

Meanwhile, the open desert all around them was the worst possible battlefield for humans.

“You know what I regret most since I became a monster?”

Jin Taekyung answered without hesitation.

“I know. Not getting to go clubbing.”

“Wrong. It’s getting mixed up with you.”

“Really? I’m the exact opposite.”

“What?”

“One of the best things I ever did was get you out of that Gate.”

“…Damn it. Am I the only piece of trash here?”

“You knew that already. Why ask?”

The Skeleton King let out a quiet laugh and took a deep breath. The aura of death that flowed out in place of breath raised the monsters scattered around them.

A total of one thousand.

That was the maximum he could maintain while fighting and directing them at the same time. But it was a meager force against the vast army drawing nearer, gradually picking up speed.

“Can we… hold them all back?”

No.

Jin Taekyung swallowed the answer that hovered on the tip of his tongue.

*Someone is going to die. No matter what.*

That was battle. That was why it was war.

There was no way to save everyone.

But there was one thing he could promise: not the hollow promise that everyone would make it out alive, but revenge.

“No matter how many of us die here today…”

*Shing.*

His words trailed off as his gleaming spearhead leveled at the monsters.

“They’re all going to die by my hand.”

The Skeleton King’s eyes widened.

*KRUNCH!*

A wave of monsters beyond counting swept over them.

* * *

…!

…!!

His ears were ringing. The ground shook beneath the movement of a monster army more than ten thousand strong, and their cries seemed to reach the ends of the earth and the heavens above.

And right at the head of that army, at its center, were those monsters.

*Fwoosh. Slice!*

Fire Dragon’s Single Tail.

A line of flame traced along the spearhead and cut through the air. Dozens of heads caught in its path—unable to dodge or block—rolled across the ground.

*Splatter!*

Blood burst belatedly, soaking the ground in every direction. But the monsters that should have charged with savage cries scattered in every direction, avoiding me and the Skeleton King.

Was it because of the martial prowess I’d shown, or my Intimidation?

No. The monsters avoiding me to charge the Hunters weren’t afraid. They were obeying someone else.

The kind of obedience you only saw in a trained elite army.

“You’ve got to be fucking kidding me…”

*Crunch!*

The Skeleton King blew apart an ogre’s head and let out an angry shout.

He and I had the undead army with us, but it was impossible to block every enemy’s path.

For every ten we killed, a hundred got through. For every hundred, a thousand monsters broke past.

The net we’d spread was tight, but far too small—and that was exactly what the enemy had intended.

—So it’s you. The human that person spoke of.

The voice seemed to come from inside my head.

Its smooth, composed tone, like a nobleman’s, showed a high level of intelligence. And the meaning behind its words matched my guess.

“The Prophet. Where is he now?”

A mythical monster with the face and body of a tiger, the tusks of a boar, and the horns of a bull.

The Manticore Lord smiled and answered.

—He is everywhere, and nowhere.

“What the hell does that mean?”

I answered the Skeleton King’s question.

“It means he’ll tell us if we beat the shit out of him.”

Then I brought my spearhead down toward the monster. No—toward *them*.

*Shwoosh!*

The wind split apart.
```
