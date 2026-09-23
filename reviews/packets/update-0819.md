<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0819.txt",
      "sha256": "1f6275aa02deb2b8b9cd6bc9f041ecb46e77dec474ee3c4b7f6cb5c77b6eab81",
      "bytes": 13181
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "5e1d0fde303bbf03ed3c835af33f48a3e3d0b6ebdd6527367cb2d88115b7e19d",
      "bytes": 2047
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "b2ccfdb1449513d384a11ad0a70520df0527566268eb092ade57d44fd49a47d3",
      "bytes": 226214
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "05eb9daaf36848086b32ce0faf32f16f2293a6179bd9f7e3f0cc008c9c95f8c9",
      "bytes": 723
    },
    {
      "path": "characters/Doppelganger.md",
      "sha256": "dab76b22bc893efab569ef7f0799fa9abaea20fcfafb1fdd60ac243745657879",
      "bytes": 761
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "0c18d956d4771c2cec71433a692d55c12a568b018c1c600a49243c7b35fc0666",
      "bytes": 1921
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "b0728b5c81da24b459998c02897b7f1a28eb5e2d2811dd7c0d38eb73499354f7",
      "bytes": 622
    },
    {
      "path": "characters/Team Leader Choi.md",
      "sha256": "772f51b74d57966938e3b37c8835883c532f5b313ea8e25bde9512f053a9bf4b",
      "bytes": 635
    },
    {
      "path": "characters/The Prophet.md",
      "sha256": "96176f87797ab650f541e47a5e692981cd49d857c72e1ef28749d2d2971ef449",
      "bytes": 724
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "e84340e9c6d5a09f1b44a7b271ec7d6cd2892c35502a1166e641fe2fc639c93b",
      "bytes": 249740
    }
  ],
  "estimated_tokens": 10354
}
-->

# Durable State Update — Chapter 819

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
1 and safe_through 819. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 819. Profile updates may replace only one
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
  "chapter": 819,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 819,
    "continuity_sources": [819],
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
    "The Prophet is a Level 170 Doppelganger titled “The Final Abyss,” who concealed itself for decades, including under the name Muninn.",
    "The Doppelganger can resurrect by consuming absorbed lives and reproduce absorbed people’s appearances, abilities, and memories.",
    "The Doppelganger has taken on Siegfried Bassman’s face and wields his Grand Mage abilities.",
    "The Doppelganger’s absorbed lives are dwindling; its left arm was torn off, and its regeneration is slow after forcing Blink beyond its normal range.",
    "Jin interfered with the Doppelganger’s Blink spell and arrived with it; the attempt nearly tore the Doppelganger apart and cost it dozens of lives to heal, while Jin survived with severe nausea and is currently weaker than usual.",
    "The Doppelganger fled the battlefield, leaving its hundreds of followers to delay Jin; Jin intends to stop the plan it has spent over thirty years building.",
    "Yahya Muhammad Ahmad Bedouin is the fanatics’ real commander and a formidable martial artist; more than thirty skilled black-robed assassins serve among the fanatics.",
    "Jin has summoned White Flame and charged into the encircling fanatics and assassins."
  ],
  "continuity_sources": [
    818
  ],
  "open_questions": [
    "Who is the Doppelganger’s master, what is the plan, and why must the target be avoided until it is complete?",
    "What does the Chosen One designation mean?",
    "What will happen in Jin’s confrontation with Yahya and the assassins?",
    "Is Magic Johnson human?"
  ],
  "safe_through": 818,
  "temporary_decisions": [
    "Keep magical power distinct from mana.",
    "Keep Demon Realm language distinct from other languages.",
    "Keep Blink distinct from Teleport and Warp; extended-range Blink causes severe strain."
  ],
  "version": 1
}
```

## Exact glossary matches

| 진태경    | **Jin Taekyung**   |
| 최민우    | **Choi Minwoo**   |
| 체력               | **Stamina**                    |
| 헌터      | **Hunter**            |
| 몬스터     | **monster**           |
| 탱커      | **tank**              |
| 마법사     | **mage**              |
| 대격변     | **Great Cataclysm**   |
| 도사      | **Daoist**                                                      |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 도플갱어 | **Doppelganger** | The Prophet’s revealed species. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 선지자 | **The Prophet** | Mysterious religious leader directing the terrorist warriors. |
| 중상 | **Severe Injury** | System condition label causing a major drop in all stats. |
| 검신 | **Sword God** | Alternate title used for Mae Jonghak; kept distinct from 검성, rendered Sword Saint. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 신성 | **Morning Star** | Term in the summons referring to the Master of Morning Star. |
| 마도 | **Demonic Path** | Term raised for martial power that appears to defy common principles. |
| 스켈레톤 | **Skeleton** | Undead monster species. |
| 메이지 | **Mage** | Skeleton subtype mentioned alongside Soldiers and Warriors. |
| 골검 | **Bone Sword** | Sword wielded by the Skeleton Knights. |
| 존슨 | **Johnson** | Co-host of the American talk show that replays Taekyung's viral interview. |
| 미미 | **Mimi** | Worker at Honghwaru referenced in Taekyung's joke. |
| 소멸 | **Erasure** | Jin's term for the Skeleton Warlord's destruction by the Arch Lich's mana. |
| 마법 | **Magic** | Taekyung's explanation for Dark Heaven's anomalous abilities. |
| 대마도사 | **Grand Mage** | Title used for Magic Johnson. |
| 고든 | **Gordon** | Pentagon employee tasked with repairing smashed warning lights. |
| 가기 | **singing courtesan** | The favored entertainer identity Honglan used in Hubei. |
| 성우 | **Sacred Rain** | Name later given to the rain released as the Earth Mother Goddess's blessing. |
| 마력 | **magical power** | Distinct from mana; the Skeleton King's area of expertise. |
| 심해 | **deep sea** | Unexplored ocean depths where the ancient monster awakens. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 신의 | 진태경 | physician_to_benefactor | Young Master Jin | formal-polite | The Divine Physician addresses Taekyung as 진 공자 while expressing concern for his injuries. |
| 최민우 | 진태경 | trusted allied team leader to younger allied Hunter | Mr. Jin | formal-polite and concerned | Choi warns Jin about the danger of the operation and affirms his deep trust. |
| 진태경 | 최민우 | younger allied Hunter to allied team leader | Team Leader Choi | polite, familiar, and teasing | Jin jokes with Choi while acknowledging and dismissing his concern. |
| 진태경 | 존슨 | Allied Hunter to Grand Mage | Johnson | polite and familiar | Jin repeatedly addresses Magic Johnson directly while requesting explanations and permission to visit the site. |
| 진태경 | 미미 | rescuer to companion snake | Mimi or Mimi-chan | informal, pleading | Taekyung calls to Mimi while asking the snake to carry him and the survivors. |
| 진태경 | 마법사 | rescuer assisting the operation | mage; otherwise you | polite emergency imperative | Taekyung orders the exhausted mage to request rescue under his name. |
| 진태경 | 헌터 | field commander to allied Hunters | you; Hunters | blunt and commanding | Orders the human forces to stop asking questions and kill the fleeing Minotaurs. |
| 최민우 | 존슨 | allied Hunter to allied Grand Mage | Mr. Johnson | formal-polite | Minwoo calls out to Johnson during the battle. |
| 진태경 | 선지자 | enemy commander addressed by Jin | The Prophet | blunt and informal | Jin asks where The Prophet is while confronting the Manticore Lord. |
| 존슨 | 진태경 | allied friend and comrade-in-arms | Jin | familiar and conversational | Johnson calls Jin 진 while asking what he was thinking. |
| 진태경 | 도플갱어 | enemy | you; the Doppelganger | blunt and informal | Jin directly challenges the Doppelganger and demands to know what it wants. |

## Listed compact profiles

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 818
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** He is devoted to medicine and the lives he could not save, yet remains composed and self-effacing under mortal danger.
- **Voice:** He speaks in calm, respectful, self-effacing language, framing mortality through quiet philosophical reflections.
- **Relationships:** Mungyeong is the Divine Physician's true identity, and Dong Feng is his Disciple.

### Doppelganger.md

# Doppelganger (도플갱어)

- **Safe through:** Chapter 818
- **Aliases:** The Final Abyss
- **Role:** The last surviving member of its species, the Doppelganger is a powerful being from the Demon Realm that spent decades manipulating events in the human world.
- **Personality:** Arrogant and manipulative, it treats others as tools and is willing to sacrifice its followers to escape, but becomes desperate when its own survival is threatened.
- **Voice:** Not established
- **Relationships:** It served an unnamed master who sent it to this world and ordered it to avoid the target until the master’s plan was complete; it regarded Michael Silbert as a subordinate and disposable tool.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 818
- **Aliases:** Blazing Flame Divine Dragon; Apostle of the Earth Mother Goddess; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan, Jeok Cheongang’s Disciple, the Fire Gate Clan’s nineteenth successor, Pavilion Master of the Fire Dragon Pavilion, a Supreme Peak master and publicly recognized S-rank-level Hunter with an A-rank license, a traveler between Murim and another world, and the World Hunter Federation’s Alliance Leader.
- **Personality:** Hungry, self-aware, dryly observant, pragmatic under pressure, and willing to risk himself for people he has accepted as real; treats impossible situations like games until their human cost becomes undeniable.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, Jeok Cheongang is his Master, Mungyeong was his recent instructor, Cheongpung is his trusted companion and only true martial rival, Choi Minwoo is his subordinate and trusted manager of media and official arrangements as well as the Peace Guild's Guild Master, Ju Hwaran is a trusted Fire Dragon Pavilion member who followed him to Nanman, Magic Johnson is an allied Grand Mage who supplies him with intelligence, Chuck Hagel is an American operative allied with him in the covert anti-terror campaign, his mother and sister Hayeon are among those he protects, the Skeleton King is his friend and ally, Xiao Shen regards him as an older brother after Jin saved him, and Jin-ho is his older friend and trusted confidant.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 818
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Team Leader Choi.md

# Team Leader Choi

- **Safe through:** Chapter 815
- **Aliases:** Choi Minwoo (최민우)
- **Role:** Team Leader Choi is Jin Taekyung's meticulous intelligence and operations lead, a trusted ally and natural leader capable of guiding the reestablished World Hunter Federation.
- **Personality:** Calm, pragmatic, meticulous, and resolute under pressure.
- **Voice:** Measured, professional, and reassuring without minimizing responsibility.
- **Relationships:** A trusted ally and operational adviser to Jin Taekyung, and the maternal grandson of Cheon Taemin.

### The Prophet.md

# The Prophet (선지자)

- **Safe through:** Chapter 818
- **Aliases:** Muninn (무닌)
- **Role:** The Prophet is a Level 170 Doppelganger titled “The Final Abyss,” who concealed itself for decades as Muninn.
- **Personality:** Religiously fervent, commanding, and shrouded in an intentionally indistinct identity.
- **Voice:** Mysterious, genderless, and age-indeterminate, speaking in solemn religious imperatives.
- **Relationships:** The Prophet commands the ten warriors and is revered by its followers; it made a pact with Michael Silbert during the 2020 Battle of Paris, where Michael killed the surviving humans in exchange for being spared.

## Korean source

```text
＃819화



광신도와 헌터.

협곡을 중심으로 벌어지는 두 세력 간의 전투는 단 네 글자로 설명할 수 있었다.

일진일퇴(一進一退).

전장의 흐름은 그만큼 치열했고, 양측 진영에 속한 모두가 목숨을 걸고 전투에 임했다.

누군가는 일평생 믿어 온, 그렇기에 거짓이라고는 생각할 수조차 없는 신앙을 위해.

또 다른 누군가는 굳건한 신념을 위하여.

그렇게 그들은 싸웠다.

그것은 신앙과 신념의 충돌인 동시에 성전(聖戰)이었다.

하지만 무수한 피와 죽음이 오가는 그곳에서 더 이상 종교의 유무는 중요하지 않았다.

악마.

같은 모습을 한 인간이었으나, 각자가 품은 선악(善惡)의 기준은 다르다. 서로를 향해 짓쳐 드는 칼날 사이로 마주친 시선이 살의로 끓어오르고 있었다.

“죽어어엇!”

카가가각!

검과 도가 부딪힌다. 날카로운 마찰음과 함께 시퍼런 번갯불이 튀었다. 누가 토해 냈는지 모를 갈라진 고함 사이로 핏물이 솟구쳤다.

서걱, 촤아아악!

비명은 들려오지 않았다. 목이 베인 광신도는 독기 가득한 눈동자로 눈앞의 헌터를 노려보다 쓰러졌다.

허물어지는 시신의 머리 위로 푸른 빛이 번쩍였다.

“조심!”

쐐애액! 콰앙!

다급한 외침과 굉음이 뒤섞인다. 거대한 타워 실드를 반쯤 관통한 화살촉을 코앞에서 마주한 탱커가 숨을 삼켰다.

조금. 아주 조금만 방패를 드는 것이 늦었더라면 죽을 뻔했다.

하지만 헌터는 그 누구보다 죽음과 가까운 존재. 더군다나 이 자리의 모두는 지금과 같은 생사의 위기를 수도 없이 넘었다.

화살을 잡아 부러트린 탱커가 갈라진 목소리로 고함을 내질렀다.

“온다! 대형 유지!”

콰과과광!

무수한 섬광이 빗발쳤다. 예리한 날붙이가, 단단한 둔기가, 심지어는 죽음을 코앞에 둔 광신도들조차 억지로 몸을 일으켜 달려들었다.

방패 위를 두드리는 엄청난 충격에 숱한 전투 경험을 쌓은 베테랑 탱커들마저 죽음을 떠올렸다.

“으아아아!”

까드득.

고함으로 남은 힘을 쥐어 짜내고, 부서질 듯이 이를 악문다. 힘을 이기지 못해 밀려 나가는 발끝을 따라 깊은 고랑이 패였다.

“버텨! 무너지면 끝장이다!”

지휘관들의 외침도 멀게만 느껴졌다.

압도적인 병력 차이.

몬스터 군단과의 전투를 끝마친 지 불과 세 시간도 지나지 않았다.

격전의 피로는 몸과 정신을 동시에 좀먹었고, 이러한 상황에서 맞닥트린 광신도들은 최악의 상대였다.

무려 일만에 달하는 머릿수.

가슴을 베이고, 팔다리가 잘려 나가도 달려드는 독기.

바야흐로 수십여 년 전, 도플갱어가 선지자라는 이름으로 이 황량한 사막 어딘가에서 세상의 눈을 피해 키워 낸 광신도들은 또 다른 형태의 괴물이었다.

푹!

희미한 오러를 머금은 검신이 가슴을 관통하고 등 뒤로 솟구친다.

당장 포션을 사용해도 생사를 장담할 수 없는 중상. 그러나 가슴이 관통당한 광신도는 되려 피에 젖은 이빨을 드러내며 웃어 보였다.

“이, 인샬라…….”

“……!”

꺼질 듯한 목소리에 서린 광기(狂氣)를 느낀 헌터의 움직임이 덜컥 굳었다.

전신을 엄습하는 오싹한 기운.

하지만 뒤늦게 정신을 차렸을 때는, 모든 것이 늦어 있었다.

슈확!

순간 귓가를 파고드는 한 줄기의 파공성. 그리고 동시에 암전(暗轉)되는 시야.

스륵. 툭.

“한스. 한스!”

쓰러지는 몸뚱어리를 받아든 동료 헌터가 입술을 깨물었다.

그러나 지금껏 몇 번이나 서로의 목숨을 구해 준 전우는 대답하지 않았다.

정확히 미간을 파고든 비수는 그의 목소리와 생명을 동시에 앗아 가기에 충분했다.

‘빌어먹을.’

시신을 내려놓은 헌터의 눈동자가 암담하게 물들었다.

협곡은 다수의 적을 상대하기에 걸맞은 전장이었지만, 아무리 효율적으로 싸우더라도 희생은 피할 수 없었다.

더군다나 상대는 죽음을 순교(殉敎)라고 생각하는 미치광이들.

그렇게 생명을 도외시한 채 달려드는 광신도들의 물결 앞에서, 전열이 서서히 무너지려던 바로 그 순간이었다.

화아아악.

모두의 머리 위로 느껴지는 뜨거운 열기.

사람들이 고개를 들어 허공을 바라보기도 전에, 강렬한 파공성과 함께 불의 비가 유성우처럼 쏟아져 내렸다.

후우우웅!

헌터들의 머리 위에서 나타난 수십여 개의 불덩어리가 전장을 향해, 끊임없이 달려드는 광신도들을 향해 떨어져 내린다.

멍하니 입을 벌린 채 그 광경을 바라보던 모두의 머릿속에 한 사람의 이름이 스쳐 지나갔다.

‘매직 존슨.’

마나의 축복을 받았다고 알려진 대마도사. 그중에서도 대격변을 통해 입증된 세계 최고의 워 메이지(War Mage)가 드디어 진면목을 드러낸 것이다.

전장의 흐름을 뒤바꿀 강력한 범위 마법과 함께.

‘그래, 저것이라면.’

헌터들 모두가 그렇게 생각했다. 아니, 확신했다.

진태경이 보이지 않는 지금은 매직 존슨이야말로 자신들을 승리로 이끌 수 있는 가장 확실한 패라고.

적어도 사방에 존재하는 것이라고는 모래와 돌뿐인, 이 메마른 땅에서 푸른 물결이 솟구치기 전까지는 그랬다.

“아쿠아 스톰(Aqua Storm)!”

“아쿠아 스톰(Aqua Storm)!”

“아쿠아 스톰(Aqua Storm)!”

솨아아아아!

수십여 명의 목소리가 하나로 겹쳐진다. 중첩되고 또 중첩된 물의 구(球)가 거대한 해일이 되어 솟아올랐다.

그리고…….

꽈아아아앙!

하늘이 쪼개지는 듯한 굉음이 울려 퍼졌다.

물과 불. 불과 물.

서로의 대척점에 선 두 개의 기운이 서로를 향해 뒤섞였다. 충돌했다.

반경 수백 미터의 공간을 뒤흔드는 충격과 함께, 헌터와 광신도들의 머리 위에서 폭발했다.

화아아악. 퍼버벙!

“끄아아악!”

“시, 신이시여!”

바람과 함께 사방을 휩쓴 수증기 너머로 누군가의 비명이 울려 퍼진다.

짙은 수증기로 인해 시야가 가로막힌 이들은 상황을 좀처럼 파악할 수 없었지만, 마법을 시전한 장본인인 매직 존슨은 누구보다 잘 알고 있었다.

자신의 마법이 상쇄되었다는 것을.

‘가로막혔다. 그것도 거의 완벽하게.’

거의라고 표현한 이유는 그가 시전한 파이어 스톰(Fire Storm)의 일부가 광신도들을 집어삼켰기 때문이었지만, 그 피해가 예상했던 것보다 훨씬 미미하다는 것쯤은 짐작하고도 남았다.

‘미리 대비하고 있었어.’

매직 존슨은 똑똑히 보았다. 철통같은 호위 아래에 모습을 드러낸 서른 명의 마법사들을.

터번을 깊게 눌러쓴 그들은 하나 같이 A급. 그것도 자신처럼 전투에 특화된 워 메이지들이었다.

‘도플갱어…….’

매직 존슨은 신음을 삼켰다.

눈 앞에 펼쳐진 저 엄청난 전력이 모두 누구의 작품인지는 생각해볼 필요도 없다.

대격변은 극심한 혼란의 시기였고, 삼십여 년은 자연이 뒤바뀔 만큼 긴 세월이었으며, 사막은 무언가를 숨기기에 더없이 적합한 곳이었을 테니까.

그러니 매직 존슨이 알고 싶은 것은 도플갱어가 저들을 어떻게 규합했고 훈련시켰는지가 아니다.

그의 의문은 이 모든 것의 시작이자 끝에 맞닿아 있었다.

‘도대체 네가 원하는 것이 무엇이길래, 이토록 철저히 준비했던 거냐.’

하지만 매직 존슨의 물음은 어디에도 닿지 않았다. 설령 도플갱어가 그의 의문을 알았더라도, 답해 주지 않았을 것이다.

아니, 답할 시간조차 없었을 것이다.

지금 이 순간, 도플갱어는 소수의 호위 병력을 이끌고 전장을 이탈하고 있었으니까.

‘쫓아야 한다. 놈을 놓쳐서는 안 돼.’

그러나 마음과는 달리 매직 존슨은 쉽사리 움직일 수 없었다.

몬스터와 달리 철저하게 훈련받은 광신도들은 이 전투에서 가장 중요한 핵심을 알고 있었다.

열 배가 넘는 머릿수를 바탕으로 펼치는 차륜전.

그리고…….

“막아라! 저 두 놈만은 반드시 막아내야 한다!”

“일제 사격, 개시!”

매직 존슨과 스켈레톤 킹.

가장 강력한 전력이자, 지휘관이라 할 수 있는 두 존재를 향한 집중적인 견제.

쉬쉬쉬쉬쉭!

퍼버벙!

화살과 마법이 빗발친다. 제아무리 대마도사인 매직 존슨이라 하더라도 경시할 수 없는 공격들이 사방에서 쉴 새 없이 날아들었다.

이미 상당한 체력과 마나를 소진한 그와 달리 광신도들은 성전을 부르짖으며 끊임없이 힘을 끌어올렸다.

스켈레톤 킹 역시 상황은 마찬가지였다.

서걱, 서걱, 서걱!

뼈로 이루어진 골검(骨劍)이 매끄러운 궤적을 그린다.

하지만 피를 흩뿌리며 허물어지는 몸뚱어리들이 땅에 닿기도 전에, 눈부신 섬광이 시신을 가르며 스켈레톤 킹을 향해 날아들었다.

“이런 미친……!”

스켈레톤 킹은 기함했다. 이 세상에 나온 이래 이 정도의 미친놈들을 마주하는 것은 그로서도 낯선 경험이었다.

그 미친놈들이 무려 일만에 달한다면 더더욱.

‘미쳤군. 정말 제대로 미쳤어.’

죽음을 다루는 권능을 지닌 스켈레톤 킹이었지만, 끊임없이 몰려드는 광신도의 물결에 기가 질릴 지경이었다.

인간이라면 누구나 죽음을 두려워한다. 아니, 언데드 몬스터인 자신조차 소멸이 두렵다. 이는 탄생과 동시에 주어진 숙명 같은 문제였다.

그런데 어째서 눈앞의 인간들은 죽음을 두려워 하지 않는가.

아니, 무엇이 그들을 이렇게 만들었는가.

‘이놈들이야말로…… 진짜 괴물이다.’

푸푸푸푹!

침음성을 삼키며 휘두른 골검이 인간의 육신을 갈라 낸다.

그러나 스켈레톤 킹이 하나를 쓰러트리면 셋이, 셋을 쓰러트리면 열 명이. 그마저도 쓰러트리면 온 사방에서 몰려든 광신도들이 손에 쥔 무기를 휘둘렀다.

“죽어라! 이 악마야!”

퍼걱!

서늘한 절삭음이 울려 퍼졌지만, 당연하게도 고통은 없다.

스켈레톤 킹은 가슴어림을 관통한 한 자루의 검을 보며 한숨을 내쉬었다.

“누가 악마라는 거냐.”

쉭, 푸푹!

뒤집은 손목에서 튀어나간 뼛조각이 적의 목을 관통한다.

크르륵, 피 끓는 소리와 함께 쓰러지는 광신도를 힘차게 걷어차며 공간을 만들어 낸 그 순간.

후웅.

묵직한 파공성과 함께 날아든 검은 형체를, 스켈레톤 킹은 황급히 받아 들었다.

핏물이 섞인 기침을 토해 내는 그것은 아직 살아 있는 인간이었다.

더군다나 익숙하기까지 한.

‘빌어먹을. 이 녀석은…….’

틀림없다. 전신이 피에 뒤덮여 있었지만 똑똑히 알아볼 수 있었다.

서서히 바닥을 드러내고 있는 마력으로 언데드 몬스터를 일으킨 스켈레톤 킹이 뺨을 툭툭 건드렸다.

“이봐. 허우대만 멀쩡한 인간. 이 몸의 목소리가 들리나?”

쿨럭. 다시 한번 피를 토해 낸 최민우가 꺼질 것 같은 음성으로 대답했다.

“예, 아주 잘.”

“좋아. 시간이 없으니까 잘 들어. 우선 죽지는 않을 테니까 안심해. 만약 죽더라도 내가 언데드로 부활시켜 줄 테니까 걱정하지…… 제기랄. 기절했군.”

혀를 차며 일어난 스켈레톤 킹이 문득 덧붙였다.

“뭐, 그래도 이만하면 훌륭하게 잘 버텼지. 그렇게 생각하지 않나?”

쉬이이잉! 서걱!

대답 대신 날아든 오러가 스켈레톤 킹의 머리 위를 스쳤다.

흩날리는 금발을 보며 쌍욕을 중얼거린 그가 정면을 응시했다. 짙은 수증기 사이로 한 사람의 모습이 보였다.

“전혀. 그놈은 쓰레기야.”

산발이 된 머리카락과 뺨을 가로지른 상처.

분노로 타오르는 사내의 눈빛에 스켈레톤 킹이 피식 웃었다.

“아무리 생각해도 잘 싸운 게 맞군. 깨어나면 이 몸이 친히 칭찬해 줘야겠어.”

“그 더러운 아가리 닥쳐라, 저주받은 악마야.”

“어차피 죽으면 알게 될 거다. 우리 둘 중 누가 악마였는지.”

스켈레톤 킹은 기절한 최민우가 움켜쥐고 있던 검자루를 빼냈다. [영웅의 검]의 검신을 타고 신성한 빛이 퍼져나갔다.

“빨리 들어와라. 나보다 더 무서운 놈이 오기 전에.”
```

## Final English reading copy

```markdown
# Chapter 819

Fanatics and Hunters.

The battle between two forces, waged around the canyon, could be summed up in four characters:

Advance and retreat.

The fighting was that fierce, and everyone on both sides had put their lives on the line.

Some fought for a faith they had believed in all their lives—a faith they couldn’t even imagine might be false.

Others fought for their unshakable convictions.

And so they fought.

It was a clash of faith and conviction, and at the same time, a holy war.

But in a place awash with blood and death, religion no longer mattered.

Demons.

They were human beings with the same appearance, but each held a different standard for good and evil. Their eyes met between the blades lunging toward one another, burning with murderous intent.

“Die!”

*Clang!*

Swords and sabers clashed. A sharp screech rang out, and vivid blue sparks flew. Blood spurted amid broken shouts, impossible to tell who had cried out.

*Slice—shaaak!*

No scream followed. The fanatic, his throat cut, glared at the Hunter before him with venom in his eyes, then collapsed.

Blue light flashed above the fallen body.

“Watch out!”

*Whoosh! Boom!*

A panicked shout and a roar of impact collided. A tank stared at an arrowhead that had pierced halfway through his enormous tower shield, right in front of his face, and sucked in a breath.

If he’d raised his shield just a little—just a fraction—later, he would have died.

But Hunters were closer to death than anyone. And everyone here had survived countless brushes with death just like this one.

The tank grabbed the arrow and snapped it in two, then shouted in a hoarse voice.

“They’re coming! Hold formation!”

*Rumble!*

Countless flashes rained down. Blades flashed, heavy clubs swung, and even fanatics on the verge of death forced themselves upright and charged.

The impacts pounding their shields were so immense that even the veteran tanks, hardened by years of combat, thought of death.

“Arrrgh!”

*Grit.*

They squeezed out the strength they had left in their shouts and clenched their teeth until they felt ready to break. Their feet slid backward under the pressure, carving deep furrows into the ground.

“Hold the line! If we break, it’s over!”

Even the commanders’ shouts seemed distant.

The enemy had an overwhelming numerical advantage.

It had been less than three hours since the battle against the monster army ended.

The strain of that fierce fight was eating away at their bodies and minds alike, and the fanatics they now faced were the worst possible opponents.

Ten thousand of them.

They kept charging even after their chests were cut open or their limbs were severed, their eyes alight with venom.

More than thirty years ago, the Doppelganger had raised these fanatics somewhere in this barren desert, out of the world’s sight, under the name of the Prophet. Now they were monsters of another kind.

*Thrust!*

A sword blade bearing a faint aura pierced a chest and burst out the other side.

It was a grievous wound. Even if he used a potion right away, there was no telling whether he’d live or die. Yet the fanatic whose chest had been pierced bared his blood-soaked teeth and smiled.

“I-Inshallah…”

“……!”

The madness in that fading voice made the Hunter’s body seize up.

A chill swept over him from head to toe.

But by the time he came to his senses, it was too late.

*Whoosh!*

A single whistle of air pierced his ear. At the same instant, his vision went dark.

*Slump. Thud.*

“Hans! Hans!”

The Hunter who caught his falling comrade clenched his lips.

But the comrade with whom he had saved each other’s life time and again never answered.

The dagger had pierced him exactly between the eyes, taking his voice and his life at once.

*Goddammit.*

The Hunter’s eyes darkened as he laid down the body.

The canyon was an ideal battlefield for facing a larger force, but no matter how efficiently they fought, casualties were unavoidable.

Especially against madmen who thought of death as martyrdom.

It was just as their ranks were about to crumble before the wave of fanatics charging without regard for their lives—

*Fwoosh.*

A fierce heat washed over everyone’s heads.

Before anyone could look up, a rain of fire came pouring down like a meteor shower, accompanied by a sharp whistle.

*Whoooooosh!*

Dozens of balls of fire appeared above the Hunters and fell toward the battlefield, toward the fanatics who charged without end.

As everyone stared up at the sight, mouths hanging open, one name flashed through their minds.

*Magic Johnson.*

The Grand Mage said to have received the blessing of mana. Among Grand Mages, he was the world’s greatest War Mage, proven so during the Great Cataclysm. At last, he was showing his true strength.

With a powerful area spell that could turn the tide of battle.

*That’s it. If he can do that…*

Every Hunter thought the same thing. No—they were certain of it.

With Jin Taekyung nowhere to be seen, Magic Johnson was their surest bet to lead them to victory.

At least, that was what they thought—until blue waves surged up from this parched land, where all there was in every direction was sand and stone.

“Aqua Storm!”

“Aqua Storm!”

“Aqua Storm!”

*Fwoooooosh!*

Dozens of voices rang as one. Spheres of water stacked upon spheres of water, rising into an enormous tidal wave.

And then…

*BOOM!*

A roar like the sky splitting apart shook the air.

Water and fire. Fire and water.

Two forces, opposites of one another, twisted together. They collided.

With a shockwave that shook everything within hundreds of meters, they exploded above the heads of the Hunters and fanatics.

*Fwoosh! Boom-boom!*

“Gyaaaah!”

“M-My God!”

Someone screamed from beyond the steam that swept through the area on the wind.

The thick steam blocked the view, leaving everyone unable to make out what had happened. But Magic Johnson, the one who had cast the spell, knew better than anyone.

His magic had been canceled out.

*It was blocked. Almost completely.*

He said almost because part of his Fire Storm had swallowed some of the fanatics. But he could tell the damage was far less than he had expected.

*They were ready for it.*

Magic Johnson had seen them clearly: thirty mages under an ironclad escort.

Their turbans were pulled low over their brows. Every last one of them was A-rank, and, like him, a War Mage specialized in combat.

*The Doppelganger…*

Magic Johnson swallowed a groan.

There was no need to wonder who had created all that overwhelming power in front of him.

The Great Cataclysm had been a time of immense chaos. Thirty years was long enough for nature itself to change, and the desert must have been the perfect place to hide something.

So what Magic Johnson wanted to know wasn’t how the Doppelganger had gathered and trained them.

His question reached back to the beginning and end of all this.

*What on earth did you want that you prepared so thoroughly?*

But Magic Johnson’s question reached no one. Even if the Doppelganger had known what he was wondering, it wouldn’t have answered.

No—it wouldn’t even have had time.

At that very moment, the Doppelganger was leaving the battlefield with a small escort.

*I have to chase it. I can’t let it get away.*

But despite his determination, Magic Johnson couldn’t move easily.

Unlike monsters, the fanatics had been trained rigorously, and they knew what mattered most in this battle.

They used their more-than-tenfold numbers to attack in rotating waves.

And…

“Stop them! Those two must not get through!”

“Open fire!”

Magic Johnson and the Skeleton King.

The two strongest members of their force—and its commanders—were under concentrated attack.

*Whoosh-whoosh-whoosh!*

*Boom-boom!*

Arrows and magic rained down. No matter that Magic Johnson was a Grand Mage; attacks he couldn’t afford to take lightly kept flying in from every direction.

He had already spent a great deal of his stamina and mana. The fanatics, by contrast, kept drawing on their strength as they cried out for a holy war.

The Skeleton King was in the same situation.

*Slice. Slice. Slice!*

The Bone Sword, made of bone, swept in smooth arcs.

But before the bodies crumpling in sprays of blood could hit the ground, dazzling flashes cut through the falling bodies and shot toward the Skeleton King.

“This is insane…!”

The Skeleton King was aghast. Since coming into this world, he’d never faced anyone this crazy. The fact that there were ten thousand of them made it all the more unbelievable.

*They’re insane. Completely insane.*

The Skeleton King wielded the power of death, but even he was nearly overwhelmed by the endless wave of fanatics.

Everyone feared death. No—he himself, an undead monster, feared Erasure. It was a problem like a fate bestowed the moment one was born.

So why weren’t the humans before him afraid to die?

No—what had made them this way?

*These people are the real monsters…*

*Thrust-thrust-thrust!*

Swallowing a groan, he swung his Bone Sword and cut through a human body.

But each time the Skeleton King took one down, three more came. When he took down three, ten showed up. And when he felled those, fanatics poured in from every direction, swinging the weapons in their hands.

“Die, demon!”

*Crunch!*

A chilling sound of a blade slicing through flesh rang out, but naturally, there was no pain.

The Skeleton King sighed as he looked at the sword that had pierced his chest.

“Who are you calling a demon?”

*Whoosh—thrust!*

A bone shard shot from his turned wrist and pierced an enemy’s throat.

With a gurgling sound, the fanatic fell. The Skeleton King kicked him hard, clearing some space. At that moment—

*Whoom.*

A dark shape flew toward him with a heavy whistle. The Skeleton King hurriedly caught it.

It coughed up blood. It was a human, and still alive.

More than that, it was familiar.

*Goddammit. This guy…*

There was no doubt. Though blood covered his entire body, the Skeleton King recognized him at once.

The Skeleton King had raised the undead monster with his magical power slowly running dry. He tapped the man’s cheek.

“Hey. Human with a fine-looking build. Can you hear me?”

*Cough.* Choi Minwoo spat up blood again, then answered in a voice on the verge of fading.

“Yes. Very clearly.”

“Good. We’re short on time, so listen carefully. You’re not going to die, so don’t worry. And even if you do, I’ll bring you back as an undead, so don’t—dammit. He passed out.”

The Skeleton King clicked his tongue and stood up, then added, almost as an afterthought:

“Well, he held out damn well, all things considered. Don’t you think?”

*Whoooosh! Slice!*

An aura slashed past the Skeleton King’s head instead of an answer.

He watched blond hair flutter through the air, muttered a string of curses, then faced forward. Through the thick steam, he saw a man.

“Not at all. He’s trash.”

His hair was a mess, and a wound ran across his cheek.

The Skeleton King gave a short laugh at the man’s eyes, burning with rage.

“No matter how I look at it, he fought well. When he wakes up, I’ll have to praise him myself.”

“Shut your filthy mouth, cursed demon.”

“You’ll find out when you die. Which of us was the demon.”

The Skeleton King pulled the hilt of the sword from Choi Minwoo’s hand. Sacred light spread along the blade of the [Hero’s Sword].

“Get in here, quick. Before someone scarier than me shows up.”
```
