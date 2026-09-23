<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0822.txt",
      "sha256": "c4327b5f298138eb00987c6d71973492f1438326fb39d42a8911d45da0b78fe4",
      "bytes": 14188
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "46e4aa856dc6f0b0b879cd9321e486db1d6e398d4a364d8e7c325fe2d2db3de1",
      "bytes": 1953
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "31f232ac7d1be480b318754ea9507b1473c8082a345026eb79b029b69e3211ae",
      "bytes": 226452
    },
    {
      "path": "characters/Amir.md",
      "sha256": "6ea182eca82077f4cf7ab8dad193c9d8c750a65fadab887af42f0c275aa36ebe",
      "bytes": 575
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "c34fa2b7f901a88b6a24b752b9b6ab018eed990de3a2c10fa52c0e3792297fa4",
      "bytes": 723
    },
    {
      "path": "characters/Human Butcher.md",
      "sha256": "b5f8c878dd8973b6c3801ff8e3e204260fcaa2232785f29dc8c926a4b5ddc479",
      "bytes": 667
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "2c5ea4c7139b31e2f197cf7d1146aec1cbd969809a072fe36e87596708f44fa0",
      "bytes": 1921
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "2a4637d376433f902f795c113e601bc5b95107850df59b1795c01f41ecca5e5d",
      "bytes": 622
    },
    {
      "path": "characters/The Prophet.md",
      "sha256": "51a0dbef43194eae3bf5e53f0e378b3d44998164b400fa252ce1f5164ea9c076",
      "bytes": 724
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "882dd1ff01e09ade4bbd6c22806383c99a4e6301378ef486d5e0234e052c54fb",
      "bytes": 250079
    }
  ],
  "estimated_tokens": 10774
}
-->

# Durable State Update — Chapter 822

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
1 and safe_through 822. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 822. Profile updates may replace only one
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
  "chapter": 822,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 822,
    "continuity_sources": [822],
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
    "The Doppelganger can resurrect by consuming absorbed lives and reproduce absorbed people’s appearances, abilities, and memories; it has taken Siegfried Bassman’s face and Grand Mage abilities.",
    "The Doppelganger’s absorbed lives are dwindling; its left arm was torn off, and its regeneration is slow after forcing Blink beyond its normal range.",
    "The Doppelganger is fleeing with a small escort; Jin intends to stop its plan, which it has spent more than thirty years building.",
    "The fanatics’ commander-in-chief, Amir, and the elite troops waiting with him were killed by Jin’s steel storm.",
    "Jin can control weapons within a radius of dozens of meters using force from his Middle Dantian, directing them around allies and toward selected targets.",
    "The fanatics greatly outnumber the Hunters, but Jin’s steel storm has devastated their forces and left the survivors terrified."
  ],
  "continuity_sources": [
    820,
    821
  ],
  "open_questions": [
    "Who is the Doppelganger’s master, what is the plan, and why must the target be avoided until it is complete?",
    "What does the Chosen One designation mean?",
    "Will Jin reach the Doppelganger before it escapes?",
    "Is Magic Johnson human?"
  ],
  "safe_through": 821,
  "temporary_decisions": [
    "Keep magical power distinct from mana.",
    "Keep Demon Realm language distinct from other languages.",
    "Keep Blink distinct from Teleport and Warp; extended-range Blink causes severe strain.",
    "Keep Fire Storm and Aqua Storm as distinct named spells."
  ],
  "version": 1
}
```

## Exact glossary matches

| 진태경    | **Jin Taekyung**   |
| 살기     | **killing intent**                               |                                                       |
| 기세     | **aura** / **momentum**                          | Depends on scene                                      |
| 헌터      | **Hunter**            |
| 게이트     | **Gate**              |
| 몬스터     | **monster**           |
| 대격변     | **Great Cataclysm**   |
| 귀가      | **your family**                                                 |
| 아미르 | **Amir** | Title used to address the group’s leader. |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 인도 | **Human Butcher** | Epithet of a mysterious Han Chinese mounted-bandit power commanding fifty subordinates. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 선지자 | **The Prophet** | Mysterious religious leader directing the terrorist warriors. |
| 화시 | **fire arrow** | Flaming arrow Lee Seowol fires to signal Cheol Mubaek. |
| 검신 | **Sword God** | Alternate title used for Mae Jonghak; kept distinct from 검성, rendered Sword Saint. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 아귀 | **A-Gwi** | Legendary Dogon from Sichuan. |
| 도도 | **Dodo** | Term for the Star-Array Grand Banquet's major gambling matches. |
| 꼬리 | **the “tail”** | Codename for the Black Hunter traced by Butler Kim. |
| 그분 | **that person** | Unidentified figure whom Jihoon reveres and credits with disabling cameras and microphones. |
| 스켈레톤 | **Skeleton** | Undead monster species. |
| 존슨 | **Johnson** | Co-host of the American talk show that replays Taekyung's viral interview. |
| 아미 | **Emei** | Short form for Emei Sect. |
| 마법 | **Magic** | Taekyung's explanation for Dark Heaven's anomalous abilities. |
| 마수드 | **Masoud** | Rebel named during the battlefield footage. |
| 고든 | **Gordon** | Pentagon employee tasked with repairing smashed warning lights. |
| 마력 | **magical power** | Distinct from mana; the Skeleton King's area of expertise. |
| 하미드 | **Hamid** | Amir’s subordinate, addressed by name. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 아이들 | 청년 | children_to_stranger | beggar bastard | childlike-insulting | The children repeat their mother's insulting description of Taekyung's beggar-like appearance. |
| 신의 | 진태경 | physician_to_benefactor | Young Master Jin | formal-polite | The Divine Physician addresses Taekyung as 진 공자 while expressing concern for his injuries. |
| 진태경 | 청년 | celebrated Hunter to younger fellow Hunter | young man | casual, teasing, and profane | Jin addresses the young Hunter after overhearing his criticism and deliberately switches to casual speech. |
| 청년 | 진태경 | frightened junior Hunter to celebrated senior Hunter | you | fearful and deferential | The young Hunter uses 당신 while asking whether Jin is really the person he recognizes from the media. |
| 진태경 | 존슨 | Allied Hunter to Grand Mage | Johnson | polite and familiar | Jin repeatedly addresses Magic Johnson directly while requesting explanations and permission to visit the site. |
| 진태경 | 헌터 | field commander to allied Hunters | you; Hunters | blunt and commanding | Orders the human forces to stop asking questions and kill the fleeing Minotaurs. |
| 하미드 | 아미르 | subordinate to leader | Amir | formal and deferential | Apologizes for speaking out of turn and addresses the leader as Amir. |
| 아미르 | 하미드 | leader to subordinate | Hamid | formal, authoritative | Addresses him as Hassan’s son Hamid. |
| 진태경 | 선지자 | enemy commander addressed by Jin | The Prophet | blunt and informal | Jin asks where The Prophet is while confronting the Manticore Lord. |
| 존슨 | 진태경 | allied friend and comrade-in-arms | Jin | familiar and conversational | Johnson calls Jin 진 while asking what he was thinking. |
| 선지자 | 아미르 | religious leader to subordinate | Amir | authoritative | The Prophet addresses Amir by name and orders him to hold back Jin and the other heretics. |
| 아미르 | 선지자 | devotee to religious leader | Prophet | formal and deferential | Amir kneels and addresses the Prophet with reverence. |
| 진태경 | 아미르 | enemy commander | old man | blunt and insulting | Jin tells Amir to die, addressing him as 늙은이. |

## Listed compact profiles

### Amir.md

# Amir (아미르)

- **Safe through:** Chapter 821
- **Aliases:** None
- **Role:** Amir was the fanatics’ warrior chief and commander-in-chief, regarded by them as a warrior favored by God.
- **Personality:** Faithful and duty-bound, he advances alone against Jin despite the danger and questions his faith only as he faces death.
- **Voice:** Not established
- **Relationships:** The fanatics looked to Amir as their military leader and warrior chief, while The Prophet served as their spiritual leader.

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 821
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** He is devoted to medicine and the lives he could not save, yet remains composed and self-effacing under mortal danger.
- **Voice:** He speaks in calm, respectful, self-effacing language, framing mortality through quiet philosophical reflections.
- **Relationships:** Mungyeong is the Divine Physician's true identity, and Dong Feng is his Disciple.

### Human Butcher.md

# Human Butcher (인도)

- **Safe through:** Chapter 817
- **Aliases:** None
- **Role:** Former mysterious Han Chinese mounted-bandit power in Northern Gaoyuan commanding fifty subordinates; a Peak master killed by an unnamed old man in a single move
- **Personality:** Cold, intimidating, and murderous; he kills people as though slaughtering livestock
- **Voice:** Cold, curt, and quietly threatening
- **Relationships:** He is one of four powerful participants at the Northern Gaoyuan gathering, intimidates Temur, and has claimed Ghost Sword Wipeng as his personal target in the proposed attack

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 821
- **Aliases:** Blazing Flame Divine Dragon; Apostle of the Earth Mother Goddess; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan, Jeok Cheongang’s Disciple, the Fire Gate Clan’s nineteenth successor, Pavilion Master of the Fire Dragon Pavilion, a Supreme Peak master and publicly recognized S-rank-level Hunter with an A-rank license, a traveler between Murim and another world, and the World Hunter Federation’s Alliance Leader.
- **Personality:** Hungry, self-aware, dryly observant, pragmatic under pressure, and willing to risk himself for people he has accepted as real; treats impossible situations like games until their human cost becomes undeniable.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, Jeok Cheongang is his Master, Mungyeong was his recent instructor, Cheongpung is his trusted companion and only true martial rival, Choi Minwoo is his subordinate and trusted manager of media and official arrangements as well as the Peace Guild's Guild Master, Ju Hwaran is a trusted Fire Dragon Pavilion member who followed him to Nanman, Magic Johnson is an allied Grand Mage who supplies him with intelligence, Chuck Hagel is an American operative allied with him in the covert anti-terror campaign, his mother and sister Hayeon are among those he protects, the Skeleton King is his friend and ally, Xiao Shen regards him as an older brother after Jin saved him, and Jin-ho is his older friend and trusted confidant.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 821
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### The Prophet.md

# The Prophet (선지자)

- **Safe through:** Chapter 821
- **Aliases:** Muninn (무닌)
- **Role:** The Prophet is a Level 170 Doppelganger titled “The Final Abyss,” who concealed itself for decades as Muninn.
- **Personality:** Religiously fervent, commanding, and shrouded in an intentionally indistinct identity.
- **Voice:** Mysterious, genderless, and age-indeterminate, speaking in solemn religious imperatives.
- **Relationships:** The Prophet commands the ten warriors and is revered by its followers; it made a pact with Michael Silbert during the 2020 Battle of Paris, where Michael killed the surviving humans in exchange for being spared.

## Korean source

```text
＃822화



대격변 직후, 인류가 지니고 있던 상식과 비상식의 경계는 모래성처럼 허물어졌다.

각성자, 몬스터, 마법, 게이트.

소설과 영화 속에서나 등장하던 것들이 현실이 됐다.

재앙은 이웃이었고, 죽음이라는 단어는 헐값이 되었다.

그러나 인간은 적응의 동물이다.

그들은 자신들에게 닥친 그 믿기지 않는 현실을 빠르게 받아들였고, 비상식을 새로운 상식으로 인정했다.

인류 역사상 두 번 다시 이런 일은 벌어지지 않을 것이라 생각하며.

아니, 제발 그러기를 희망하며.

하지만 지금 이 순간, 룹 알 할리 사막의 이름 모를 협곡에서 끊임없이 피와 시체를 쌓아 올리던 이들은 인정할 수밖에 없었다.

그들이 받아들였던 상식이, 또다시 무너졌음을.

콰아아아.

어둠 속에서 빗발치던 강철의 비가 멎는다. 사막 전체를 집어삼킬 것 같던 돌풍이 서서히 가라앉았다.

그리고 모두를 집어삼킨 침묵과 경악 속에서, 마침내 모습을 드러낸 한 사람을 바라보는 수천 쌍의 눈동자가 있었다.

“맙소사.”

“내가 지금 도대체 뭘 본 거지?”

헌터들은 경외와 환희로.

“악마다. 놈은 악마가 틀림없어.”

“인샬라. 신이시여…….”

광신도들은 두려움과 증오로 몸을 떨었다.

그리고 이 자리의 수많은 이들 중, 유일하게 인간이 아닌 어느 존재는 모두가 하고 싶었던 한 단어를 토해 냈다.

“괴물.”

입꼬리를 말아 올린 스켈레톤 킹이 눈앞의 상대를 바라보며 말을 이었다.

“말했잖나. 이 몸보다 더 무서운 놈이 오기 전에 빨리 끝내자고.”

“……!”

사내가 눈을 부릅떴다. 산발이 된 머리카락과 전신에 가득한 크고 작은 상처.

이미 스켈레톤 킹을 상대로 어려운 싸움을 이어 가고 있던 그였지만, 이제 부상 따위는 아무래도 좋았다.

“어떻게……. 어떻게 저럴 수 있지?”

사내는 넋 나간 목소리로 중얼거렸다.

툭 튀어나온 그의 눈은 피와 시체만이 가득한 돌풍 너머를 응시하고 있었다.

일천.

후방에 대기하고 있던 전사의 머릿수만 무려 일천이다.

마지막 종지부를 위해 아껴 두었던 최정예. 거기에 더해 최고의 전사이자 지휘관인 아미르(ãmir)도 있다.

아니, 있었다.

거대한 강철의 돌풍이 그들을 휩쓸기 전까지는.

‘모두 죽었다고? 그것도 단 한 사람에게?’

믿을 수도, 이해할 수도 없는 현실.

검 자루를 움켜쥔 사내의 손아귀가 파르르 떨렸다. 어느새 악문 잇새로 신음과도 같은 목소리가 흘러나왔다.

“이, 이건 말도 안…….”

“돼.”

위태롭게 이어지던 음성이 뚝 끊긴다.

마치 단두대의 칼날처럼 사내의 말을 끊어 낸 스켈레톤 킹이 담담하게 말을 이었다.

“진태경. 저 인간이라면 가능하지.”

“입 닥치지 못할까!”

창노(滄怒)한 음성이 사막을 갈랐다. 사내는 타오르는 눈빛으로 스켈레톤 킹을 노려보았다.

스아아아.

사내를 중심으로 일어난 막대한 살기와 기파가 공간을 잠식한다.

여느 평범한 헌터라면 숨도 쉬지 못할 정도의 기세. 하지만 스켈레톤 킹은 눈 하나 깜짝하지 않았다.

언데드에게 있어 살기(殺氣)란 무엇보다 친숙한 기운이었다.

그는 존재하는 것만으로 죽음과 맞닿아 있었기에.

사내가 피워 올리는 기세 역시 마찬가지였다.

‘잘 쳐줘야 그놈의 절반 정도는 되려나.’

저 멀리 아지랑이처럼 일렁이는 ‘그놈’을 생각하며, 스켈레톤 킹은 피식 실소를 흘렸다.

세상은 자신과 같은 몬스터를 괴물이라 부르지만, 진정한 괴물은 따로 있었다.

“그러게 왜 이런 짓을 벌였느냐. 조용히 사막 한구석에 처박혀 있었다면, 저놈을 화나게 할 일도 없었을 텐데.”

“……신께서, 신께서 우리를 선택하셨다. 위대하신 그분께서 친히 선지자를 보내어 당신의 전사들을 약속의 땅으로 인도하셨단 말이다!”

“약속의 땅?”

스켈레톤 킹은 반문과 함께 주위를 둘러보았다.

사방에 시체가 널려 있었다.

강처럼 흐르는 핏물은 발목까지 차올랐고, 누구의 것인지 모를 팔다리와 살점이 사막의 꽃처럼 흐드러지게 피었다.

“네놈들이 그토록 지긋지긋하게 지껄이던 약속의 땅이, 설마 이런 광경을 말하는 건 아니겠지?”

“……!”

“여기서 다 같이 뒈지기로 신과 약속을 해서 약속의 땅이라고 하는 거라면, 뭐 어느 정도는 인정해 주지.”

사내의 눈동자가 흔들렸다. 아니, 주위의 광신도 모두가 마찬가지였다.

마력이 실린 스켈레톤 킹의 음성은 멀리 퍼져 나갔다.

헌터와 광신도, 그들 모두의 귓가에 닿을 만큼.

그리고 그 한 마디, 한 마디는 영원히 꺼지지 않을 것처럼 활활 타오르던 광신(狂信)의 불길에 찬물을 끼얹고, 헌터들로 하여금 다시 병장기를 쥐게 만들었다.

“어느 인간이 있었다. 아니, 인간들이 있었다. 이 몸과는 비교도 할 수 없을 만큼 허약한, 필멸(必滅)의 운명을 타고난 자들이었지.”

스켈레톤 킹은 떠올렸다.

지금껏 세상에 나와 마주친, 수도 없이 많은 얼굴들이 눈앞을 스쳐 지나갔다.

“그 인간들은 수없이 싸웠고, 끊임없이 죽어 갔다. 하지만 그건 단지 그들이 믿었던 신을 위해서가 아니었어.”

가족이 있고, 친구가 있다. 사랑하는 연인이, 지켜야 할 가치가 있었다.

“나는 그 멍청한 인간들을 이해할 수 없었다. 죽음이라는 것에 종류가 존재한다는 것조차 받아들이지 못했다.”

하지만 이제는 아니다.

스켈레톤 킹은 어떤 몬스터보다 가까운 곳에서 인간들을 지켜보았다.

그들과 함께했다.

하여 마침내 깨달았다.

자신이 지켜본 무수한 죽음은, 단지 죽음이라 부를 수 없는 종류의 것이라는 사실을.

“그건 희생이었다.”

누군가는 돈과 권력을 위해 살인을 저지른다. 부모와 자식을 버리고, 연인과 친구를 배신한다.

그러나 횃불처럼 타올라 들불처럼 스러져 가던 이들 역시 있었다.

죽기를 각오하고 나아가는 이들.

죽음 앞에서도 타인을 위해, 더 좋은 세상을 위해 물러섬 없이 맞서 싸우는 이들.

세상은 그들을 영웅이라 칭한다.

그 죽음을 희생이라 부른다.

“한데 너희를, 너희의 죽음은 무엇이라 불러야 하느냐.”

“……!”

“입이 있다면 대답해 보아라. 허상에 속아 재앙을 일으킨 어리석은 자들아.”

키이이잉.

스켈레톤 킹의 이마 위, 흐릿해져 가던 금빛 왕관이 빛을 토해 내는 광경에 사내가 숨을 삼켰다.

방향을 잃고 흔들리는 동공이 주위를 둘러싼 수많은 얼굴들을 스쳤다.

증오와 경멸.

원망과 혼란.

헌터들만이 아니다.

휘하의 광신도들마저 동요하고 있었다.

어느덧 원망과 혼란이 뒤섞인 눈빛으로 자신을 바라보다 고개를 돌려 시선을 피하는 그들의 모습에, 사내는 단단하던 무언가가 와르르 무너지는 듯한 충격을 느꼈다.

“나, 난. 나는…….”

말하고 싶었다.

흔들리는 저들을 향해 호통치고 싶었다.

악마의 혓바닥에 놀아나지 말라고.

감히 위대한 신과 그분의 선지자께 삿된 의문을 품지 말라고.

그러나 혀가 움직이지 않았다. 칼자루를 쥔 손에 자꾸만 힘이 풀리는 듯했다.

새하얗게 물든 머릿속에서, 조금 전 들었던 악마의 속삭임만이 끊임없이 반복되고 있었다.



‘한데 너희를, 너희의 죽음은 무엇이라 불러야 하느냐.’



사내는 자신도 모르게 이를 악물었다. 이미 부서진 어금니에서 강렬한 통증이 올라왔지만, 그에게는 꿈처럼 멀게만 느껴졌다.

사방을 가득 메운 신도들의 시체도.

발아래에 고여 있는 끈적한 피 웅덩이도.

‘이곳이 정말…….’

푸르고 아름다워야 할 약속의 땅이란 말인가.

전지전능하신 신께서, 선지자께서 당신의 백성들을 위해 준비한 천국이란 말인가?

가까스로 삼켜 낸 목소리가 의문이 되어 뇌리에 울려 퍼진다.

그리고 꿈처럼 몽롱한 시야 속에서, 휘황한 빛줄기가 어둠을 밝혔다.

후우우웅.

오색창연한 검신을 타고 솟아오르는 금빛 섬광.

그 빛이 얼마나 따스하게 느껴지던지. 또 성스럽게 느껴지던지.

사내는 검을 쥔 것이 스켈레톤 킹이라는 사실조차 깜빡 잊었다.

선택받은 자에게만 허락된 휘황한 빛을 뿜어 내는 [영웅의 검]을 든 채, 자신을 응시하는 악마를 향해 이렇게 묻고야 말았다.

“네놈은…… 정말 악마가 맞느냐?”

바로 그 순간이었다.

저벅.

모든 것이 멈춘 세상 속에서, 한 사람의 발걸음 소리가 울려 퍼진 것은.

그와 동시에 담담한 목소리가 사내의 귓가를 파고든 것은.

“믿고 싶은 대로 보는 법이지. 너희가 어느 괴물을 선지자라 부르며 떠받들었던 것처럼.”

바람이 숨을 죽였다.

모두의 고개가 한 방향을 향해 움직였다.

그리고 그 수많은 시선의 끝에, 진태경이 있었다.

“하미드 샤 마수드.”

사내가 멍하니 진태경을 바라보았다.

그건 아미르를 제외하면 누구도 모르는 이름이었다. 눈앞의 상대가 알 수 없는 이름이기도 했다.

“도대체 어떻게?”

“신께서 알려 주셨다고 하면, 내 말을 믿을까?”

“……!”

“너희는 참 알기 쉬운 족속이야. 그저 믿고 싶은 대로 보고, 보고 싶은 대로 믿었겠지. 이 모든 것이 신의 뜻이라고 생각하면서.”

철벅.

거친 발걸음이 나아간다.

살점이 둥둥 떠올라 있던 피 웅덩이가 사방으로 튀었다. 그러나 이미 혈인(血人)이나 다름없는 몰골이 되어 버린 청년은 아랑곳하지 않았다.

“너희 같은 병신들 덕분에 이미 수만 명. 아니, 수십만 명이 죽었다.”

도시가 불타고, 거대한 해일이 항구를 휩쓸었다.

갑작스러운 재앙 속에서 셀 수 없이 많은 사람들이 죽어 나갔다. 단란하던 가정이 사라지고 부모를 잃은 아이들은 고아원으로 옮겨졌다.

그리고 그 모든 것이 천재(天災)가 아닌, 인재(人災)였다.

“신은 없다. 설령 있다 해도 너희 같은 쓰레기들을 굽어살피는 등신은 아니겠지.”

한 음절, 한 음절을 씹어 뱉듯이 토해 낸 진태경이 수많은 광신도들을 눈에 담았다.

누군가는 충격에 신형을 비틀거리고, 누군가는 뒤늦게 자신이 해 온 일을 깨닫고 흐느꼈다.

하지만 짧은 말 몇 마디로 그들을 감화시킬 수 있었다면, 지난 재앙들 역시 벌어지지 않았을 것이다.

“감히, 감히 사특한 이교도 따위가!”

“신은 위대하시다!”

파파팟!

날 선 외침과 함께 곳곳에서 빛살처럼 들이닥치는 신형들.

증오가 들끓는 눈빛들을 마주한 진태경의 입가에 서늘한 냉소가 맺혔다.

“그래, 이렇게 나와야지.”

그 순간.

슈확!

사방에서 솟구친 은빛 섬광이 바람을 갈랐다.

공간을 찢고, 세차게 날아들던 날붙이와 몸뚱어리를 꿰뚫고 베었다.

쉬이이익! 서걱!

푸푸푸푸푹!

그제야 살아남은 모두는 알게 되었다.

앞서 일어난 돌풍이 무엇이었는지.

그리고 그 범위 안에 있던 이들이 어떤 식으로 죽음을 맞이했는지.

콰드드득!

섬뜩한 소음이 반경 십여 미터를 뒤덮었다.

핏물이 소나기처럼 쏟아져 내리고, 공간을 가르며 쏘아지던 화살과 단검이 왔던 곳으로 되돌아가 주인의 목숨을 앗았다.

“커……헉!”

단말마라도 남길 수 있다면 다행이었다.

일시에 달려들었던 백여 명의 광신도 중 절반은 형체조차 제대로 남기지 못하고 갈기갈기 찢겨져 버렸으니.

투두두둑.

살점이, 피가, 뼛조각이 비명의 빈 자리를 채웠다.

그리고 부릅뜬 눈으로 이 모든 광경을 그저 지켜볼 수밖에 없었던 사내, 하미드 샤 마수드의 손아귀에서 칼자루가 미끄러졌다.

철컹.

누구도 입을 열지 않았다.

헌터도, 광신도도.

영웅의 검을 늘어트린 스켈레톤 킹과 허공에 우뚝 선 매직 존슨도.

지금 이 순간 입을 열 수 있는 것은, 한 사람만이 유일했다.

오직 그만이 심판자였고 용서자였다.

그렇기에 하미드 샤 마수드는 덜덜 떨리는 목소리로 마지막 용서를 구할 수밖에 없었다. 살아남기 위해서는, 하나뿐인 목숨을 구걸할 수밖에 없었다.

검을 놓고, 무릎을 꿇은 채.

이미 형체도 알아볼 수 없을 만큼 산산조각 난 마음속 신앙심을 쓰레기통에 처박은 채.

“사, 살려 주십시오.”

간절한 애원.

흔들림 없는 눈동자로 그를 내려다보던 진태경이 문득 손을 뻗었다.

피에 젖은 손가락 끝에 뜨거운 열기가 감돌았다.

푹. 털썩.

한 줄기 열풍(熱風).

그것이 전부였고, 온순하게 쓰러진 사내는 두 번 다시 일어나지 않았다.

‘마침내.’

진태경은 참았던 숨을 토해 내며 고개를 들었다.

철컹. 투두둑!

아직 날 서 있던 수많은 병장기가 무릎이 피에 젖은 모래알 위를 덮었다.

어스름한 새벽녘에 찾아온 승리. 전투의 종지부.

그러나 진태경의 시선은, 아직 어둠에 잠겨 있는 서쪽을 향하고 있었다.
```

## Final English reading copy

```markdown
# Chapter 822

In the wake of the Great Cataclysm, the boundary between what humanity considered common sense and nonsense crumbled like a sandcastle.

Awakened people, monsters, magic, Gates.

Things that had existed only in novels and movies became reality.

Calamity became a neighbor, and the word *death* lost its value.

But humans are adaptable creatures.

They quickly accepted the unbelievable reality that had come upon them and recognized the absurd as the new normal.

They thought nothing like this would ever happen again in human history.

No—they hoped, please, that it wouldn’t.

But at this very moment, in an unnamed canyon in the Rub’ al Khali Desert, those who had been piling up blood and bodies without end had no choice but to admit it.

The common sense they had accepted had crumbled once more.

*Rooooar.*

The rain of steel that had lashed down through the darkness stopped. The whirlwind that had seemed ready to swallow the entire desert slowly died away.

And amid the silence and shock that swallowed everyone, thousands of eyes finally settled on the figure who had appeared.

“Oh my God.”

“What the hell did I just see?”

The Hunters stared in awe and elation.

“He’s a demon. That thing has to be a demon.”

“Inshallah. God…”

The fanatics trembled with fear and hatred.

And among all the people gathered there, the one being who wasn’t human spat out the one word they had all wanted to say.

“Monster.”

The Skeleton King curled up the corners of his mouth and looked at the man before him.

“I told you, didn’t I? Let’s finish this before someone scarier than me shows up.”

“……!”

The man’s eyes flew wide open. His hair was disheveled, and large and small wounds covered his body.

He had already been fighting a difficult battle against the Skeleton King, but now he couldn’t care less about his injuries.

“How… How can someone do that?”

The man muttered in a dazed voice.

His bulging eyes stared beyond the whirlwind, where nothing remained but blood and corpses.

A thousand.

There had been a thousand warriors waiting in the rear.

An elite force he had saved for the final blow. And on top of that, Amir—the finest warrior and commander.

No. He *had* been there.

Until that enormous whirlwind of steel swept them away.

*They’re all dead? By the hand of one man?*

A reality he couldn’t believe or understand.

The man’s hand trembled around the hilt of his sword. A groan slipped through his clenched teeth.

“Th-That’s impossible—”

“—It’s possible.”

The man’s wavering voice cut off abruptly.

The Skeleton King, cutting off his words like a guillotine’s blade, continued in an even tone.

“Jin Taekyung could do it.”

“Shut your mouth!”

The man’s furious roar split the desert. He glared at the Skeleton King with blazing eyes.

*Shhhhh.*

The immense killing intent and aura he unleashed swallowed up the space around him.

It was a presence strong enough to leave an ordinary Hunter unable even to breathe. But the Skeleton King didn’t so much as blink.

Killing intent was the most familiar energy in the world to the undead.

Simply by existing, he was already in contact with death.

The aura the man brought forth was no different.

*At most, half as strong as that guy.*

Thinking of *that guy*, shimmering in the distance like a mirage, the Skeleton King let out a quiet snort.

The world called monsters like him monsters, but the real monster was someone else.

“Why did you have to do something like this? If you’d stayed quietly tucked away in some corner of the desert, you wouldn’t have made that guy angry.”

“……God, God chose us. The great God Himself sent the Prophet to lead His warriors to the promised land!”

“The promised land?”

The Skeleton King glanced around as he echoed the words.

Corpses littered the ground in every direction.

Blood flowed like a river, rising to their ankles. Limbs and chunks of flesh—no one knew whose—bloomed across the desert like flowers.

“Is this the promised land you’ve been blathering on about all this time?”

“……!”

“If you mean you promised God that you’d all die here together, then sure, I’ll give you that one.”

The man’s eyes wavered. So did those of every fanatic around him.

The Skeleton King’s voice, infused with magical power, carried far.

Far enough to reach the ears of every Hunter and fanatic.

Each word doused the flames of their fanaticism, which had blazed as though they would never go out. And his words made the Hunters take up their weapons once more.

“There were humans. No—there were many humans. Frail beyond comparison to me, born with death as their fate.”

The Skeleton King remembered.

Countless faces he had encountered since coming out into the world flashed before his eyes.

“They fought countless battles and died again and again. But they didn’t do it just for the gods they believed in.”

They had families and friends. People they loved. Values worth protecting.

“I couldn’t understand those stupid humans. I couldn’t even accept that there were different kinds of death.”

But not anymore.

The Skeleton King had watched humans from closer than any monster.

He had been with them.

And finally, he understood.

The countless deaths he had witnessed weren’t all the same kind of thing. Some of them couldn’t simply be called death.

“They were sacrifices.”

Some people killed for money and power. They abandoned their parents and children, betrayed their partners and friends.

But there were others, too, who burned like torches and then vanished like wildfires.

People who marched forward prepared to die.

People who stood their ground and fought for others, for a better world, even in the face of death.

The world called them heroes.

It called their deaths sacrifices.

“But what should I call you? What should I call your deaths?”

“……!”

“If you have a mouth, then answer me. You foolish people who brought calamity upon the world after being deceived by an illusion.”

*Kiiiiing.*

The man swallowed a breath as the fading golden crown above the Skeleton King’s brow began to shine.

His bewildered gaze passed over the countless faces surrounding him.

Hatred and contempt.

Resentment and confusion.

And it wasn’t just the Hunters.

Even the fanatics under his command were wavering.

Some of them looked at him with eyes clouded by resentment and confusion, then turned away. The sight struck the man as though something solid inside him had suddenly collapsed.

“I, I… I…”

He wanted to speak.

He wanted to shout at the people wavering before him.

Tell them not to be taken in by a demon’s silver tongue.

Tell them not to dare question the great God and His Prophet.

But his tongue wouldn’t move. The hand gripping his sword seemed to be losing its strength.

In his whitened mind, all that repeated was the demon’s whisper from a moment ago.

> *But what should I call you? What should I call your deaths?*

Without realizing it, the man clenched his teeth. A sharp pain flared from a broken molar, but it felt impossibly distant, like a dream.

The corpses of his followers filling every direction.

The sticky pools of blood gathered at his feet.

*Is this really…*

Was this the promised land that was supposed to be beautiful and green?

Was it heaven, prepared by an omnipotent God and His Prophet for His people?

The voice he had just managed to swallow echoed in his mind as a question.

And through his dreamlike, hazy vision, a dazzling shaft of light illuminated the darkness.

*Whoooooom.*

Golden radiance rose along the many-colored blade.

The light felt so warm. So sacred.

The man even forgot that the Skeleton King was the one holding the sword.

The Skeleton King held the [Hero’s Sword], shining with a brilliant light reserved for the chosen, and stared at him. The man found himself asking the demon:

“Are you… really a demon?”

It was at that very moment.

*Step.*

In a world where everything had stopped, a single person’s footfall rang out.

At the same time, a calm voice reached the man’s ears.

“You see what you want to believe. Just like you called a monster the Prophet and worshiped it.”

The wind held its breath.

Everyone turned their heads in the same direction.

And at the end of all those gazes stood Jin Taekyung.

“Hamid Shah Masoud.”

The man stared blankly at Jin Taekyung.

It was a name no one knew except Amir. It was also a name his opponent couldn’t possibly know.

“How could you know?”

“If I said God told me, would you believe me?”

“……!”

“You’re an easy bunch to read. You saw what you wanted to believe, and believed what you wanted to see. You thought all of this was God’s will.”

*Splash.*

His rough footsteps carried him forward.

The pool of blood, with pieces of flesh floating in it, splashed in every direction. But the young man, who looked no different from a man drenched in blood, didn’t care.

“Tens of thousands are dead because of idiots like you. No—hundreds of thousands.”

Cities burned. A massive tidal wave swept through a harbor.

Countless people died in sudden disasters. Happy families were torn apart, and children who lost their parents were sent to orphanages.

And none of it had been a natural disaster.

It had been man-made.

“There is no God. And even if there is, He’d have to be an idiot to watch over trash like you.”

Jin Taekyung spat out each word as he looked across the countless fanatics.

Some swayed on their feet, stunned. Others wept as they belatedly realized what they had done.

But if a few short words could change their hearts, then the disasters of the past would never have happened.

“How dare you, you wicked heretic!”

“God is great!”

*Papapat!*

At the sharp shouts, figures rushed in from all sides like streaks of light.

A cold smile touched Jin Taekyung’s lips as he met their hate-filled gazes.

“Good. That’s more like it.”

At that moment—

*Shwoosh!*

Silver flashes shot up from every direction, splitting the wind.

They tore through space, piercing and slicing the bodies and blades hurtling toward him.

*Whoooosh! Slice!*

*Thud-thud-thud-thud!*

Then the survivors finally understood.

What the whirlwind that had come before had been.

And how the people caught within its range had died.

*Krrrunch!*

An eerie sound swallowed up everything within a radius of more than ten meters.

Blood poured like a rain shower. Arrows and daggers that had shot through the air turned around and flew back to where they had come from, taking their owners’ lives.

“Guh…!”

They were lucky if they managed to get out a dying gasp.

Of the hundred or so fanatics who had charged all at once, half were torn to pieces, hardly a recognizable shape left behind.

*Thud, thud, thud.*

Flesh, blood, and bone fragments filled the empty spaces where screams had been.

And from the hand of Hamid Shah Masoud, the man who could only stare wide-eyed at it all, the sword hilt slipped free.

*Clang.*

No one spoke.

Not the Hunters. Not the fanatics.

Not the Skeleton King, holding the Hero’s Sword lowered at his side, nor Magic Johnson, standing upright in midair.

At this moment, only one person could speak.

Only he was the judge and the one who could grant forgiveness.

So Hamid Shah Masoud had no choice but to plead for mercy in a trembling voice. If he wanted to survive, he had to beg for his one and only life.

He dropped his sword and fell to his knees.

He threw away the faith in his heart, shattered beyond recognition, as if tossing it into a trash can.

“P-Please spare me.”

A desperate plea.

Jin Taekyung looked down at him with an unwavering gaze, then suddenly reached out his hand.

A searing heat gathered at the tips of his bloodstained fingers.

*Thwip. Thud.*

A single blast of hot wind.

That was all. The man fell quietly and never got up again.

*At last.*

Jin Taekyung let out the breath he had been holding and lifted his head.

*Clang. Thud-thud.*

Countless still-sharp weapons and knees covered the blood-soaked sand.

Victory had come at the break of dawn. The battle was over.

But Jin Taekyung’s gaze was fixed on the west, still shrouded in darkness.
```
