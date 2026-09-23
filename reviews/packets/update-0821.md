<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0821.txt",
      "sha256": "860fbe03660761d58ee9f0da67fb095d040e59535bdb0576e0092326504092bd",
      "bytes": 12827
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "5078e71463219c3e533675a082e79a22b359130e65abecea17ade7e368bd2f80",
      "bytes": 2261
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "31f232ac7d1be480b318754ea9507b1473c8082a345026eb79b029b69e3211ae",
      "bytes": 226452
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "09ad73c9506ad5e297d4b8cf99f30439107dc6e2e05eac54dda67780f1c06bd6",
      "bytes": 723
    },
    {
      "path": "characters/Doppelganger.md",
      "sha256": "2ef02b7c974aa19328bf1f186fba46c21b58c6755b61383130c8d1a878e9456d",
      "bytes": 831
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "51430b2a3471087c0a4dc47816867af7042724ceb23f9c405304b42986ce408b",
      "bytes": 1921
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "ddbb5da1c16d72d428acbdeb237284ea0a82a99af87bfb9a81d09a28b8e39022",
      "bytes": 622
    },
    {
      "path": "characters/The Prophet.md",
      "sha256": "02bf7eac65b0fc6b8170930b659d0fff19b08c99db95c1c2b2e71e7b260e679e",
      "bytes": 724
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "4fa6c9051d06392e56b17f47be21312e0edbc2886ae88d6f1631ded27a3360c0",
      "bytes": 249949
    }
  ],
  "estimated_tokens": 9894
}
-->

# Durable State Update — Chapter 821

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
1 and safe_through 821. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 821. Profile updates may replace only one
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
  "chapter": 821,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 821,
    "continuity_sources": [821],
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
    "Yahya Muhammad Ahmad Bedouin commands the fanatics and is a skilled, fanatical fighter who wields both mana and magical power; the Doppelganger selected and trained him.",
    "The fanatics’ forces greatly outnumber the Hunters, who are holding their ground; Jin is fighting Yahya and the fanatics before he can pursue the Doppelganger.",
    "Jin’s Middle Dantian has advanced and can exert pressure that suspends arrows and redirects them toward enemies.",
    "Choi Minwoo was severely wounded holding the line, passed out after the Skeleton King caught him, and left the Hero’s Sword in the Skeleton King’s hand.",
    "A furious blond man arrived at the Skeleton King’s position; his identity is not stated."
  ],
  "continuity_sources": [
    819,
    820
  ],
  "open_questions": [
    "Who is the Doppelganger’s master, what is the plan, and why must the target be avoided until it is complete?",
    "What does the Chosen One designation mean?",
    "Will Jin reach the Doppelganger before it escapes?",
    "Is Magic Johnson human?"
  ],
  "safe_through": 820,
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
| 경지     | **realm** / **realm stage**                      | Especially power level                                |
| 단전     | **dantian**                                      | Preserve the wuxia term                               |
| 기루     | **pleasure house**                               |                                                       |
| 헌터      | **Hunter**            |
| 몬스터     | **monster**           |
| 마법사     | **mage**              |
| 대격변     | **Great Cataclysm**   |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 도플갱어 | **Doppelganger** | The Prophet’s revealed species. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 선지자 | **The Prophet** | Mysterious religious leader directing the terrorist warriors. |
| 평화 | **Peace Guild** | Guild name. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 아귀 | **A-Gwi** | Legendary Dogon from Sichuan. |
| 마도 | **Demonic Path** | Term raised for martial power that appears to defy common principles. |
| 아미 | **Emei** | Short form for Emei Sect. |
| 중단전 | **Middle Dantian** | Martial energy center opened by Jin during the battle. |
| 초인 | **superhuman** | A being who has surpassed ordinary human limits. |
| 마법 | **Magic** | Taekyung's explanation for Dark Heaven's anomalous abilities. |
| 살귀 | **Killing Ghost** | Mungyeong's earlier sobriquet before he became the Slaughter Saint. |
| 중동 | **Middle East** | Region associated with the terrorist group and reported experiments. |
| 신인 | **divine man** | Descriptive term for a human who became something beyond humanity. |
| 마력 | **magical power** | Distinct from mana; the Skeleton King's area of expertise. |
| 아미르 | **Amir** | Title used to address the group’s leader. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 신의 | 진태경 | physician_to_benefactor | Young Master Jin | formal-polite | The Divine Physician addresses Taekyung as 진 공자 while expressing concern for his injuries. |
| 진태경 | 청년 | celebrated Hunter to younger fellow Hunter | young man | casual, teasing, and profane | Jin addresses the young Hunter after overhearing his criticism and deliberately switches to casual speech. |
| 청년 | 진태경 | frightened junior Hunter to celebrated senior Hunter | you | fearful and deferential | The young Hunter uses 당신 while asking whether Jin is really the person he recognizes from the media. |
| 진태경 | 사령관 | captor to captive undead commander | you | casual, mocking, and dismissive | Taekyung addresses the Skeleton Warlord informally while rejecting its pleas to turn back. |
| 진태경 | 마법사 | rescuer assisting the operation | mage; otherwise you | polite emergency imperative | Taekyung orders the exhausted mage to request rescue under his name. |
| 진태경 | 헌터 | field commander to allied Hunters | you; Hunters | blunt and commanding | Orders the human forces to stop asking questions and kill the fleeing Minotaurs. |
| 진태경 | 선지자 | enemy commander addressed by Jin | The Prophet | blunt and informal | Jin asks where The Prophet is while confronting the Manticore Lord. |
| 진태경 | 도플갱어 | enemy | you; the Doppelganger | blunt and informal | Jin directly challenges the Doppelganger and demands to know what it wants. |
| 선지자 | 아미르 | religious leader to subordinate | Amir | authoritative | The Prophet addresses Amir by name and orders him to hold back Jin and the other heretics. |
| 아미르 | 선지자 | devotee to religious leader | Prophet | formal and deferential | Amir kneels and addresses the Prophet with reverence. |

## Listed compact profiles

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 820
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** He is devoted to medicine and the lives he could not save, yet remains composed and self-effacing under mortal danger.
- **Voice:** He speaks in calm, respectful, self-effacing language, framing mortality through quiet philosophical reflections.
- **Relationships:** Mungyeong is the Divine Physician's true identity, and Dong Feng is his Disciple.

### Doppelganger.md

# Doppelganger (도플갱어)

- **Safe through:** Chapter 820
- **Aliases:** The Final Abyss
- **Role:** The last surviving member of its species, the Doppelganger is a powerful being from the Demon Realm that spent decades manipulating events in the human world.
- **Personality:** Arrogant and manipulative, it treats others as tools and is willing to sacrifice its followers to escape, but becomes desperate when its own survival is threatened.
- **Voice:** Not established
- **Relationships:** It served an unnamed master who sent it to this world and ordered it to avoid the target until the master’s plan was complete; it regarded Michael Silbert as a subordinate and disposable tool, and selected Yahya Muhammad Ahmad Bedouin to teach him magical power.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 819
- **Aliases:** Blazing Flame Divine Dragon; Apostle of the Earth Mother Goddess; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan, Jeok Cheongang’s Disciple, the Fire Gate Clan’s nineteenth successor, Pavilion Master of the Fire Dragon Pavilion, a Supreme Peak master and publicly recognized S-rank-level Hunter with an A-rank license, a traveler between Murim and another world, and the World Hunter Federation’s Alliance Leader.
- **Personality:** Hungry, self-aware, dryly observant, pragmatic under pressure, and willing to risk himself for people he has accepted as real; treats impossible situations like games until their human cost becomes undeniable.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, Jeok Cheongang is his Master, Mungyeong was his recent instructor, Cheongpung is his trusted companion and only true martial rival, Choi Minwoo is his subordinate and trusted manager of media and official arrangements as well as the Peace Guild's Guild Master, Ju Hwaran is a trusted Fire Dragon Pavilion member who followed him to Nanman, Magic Johnson is an allied Grand Mage who supplies him with intelligence, Chuck Hagel is an American operative allied with him in the covert anti-terror campaign, his mother and sister Hayeon are among those he protects, the Skeleton King is his friend and ally, Xiao Shen regards him as an older brother after Jin saved him, and Jin-ho is his older friend and trusted confidant.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 819
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### The Prophet.md

# The Prophet (선지자)

- **Safe through:** Chapter 820
- **Aliases:** Muninn (무닌)
- **Role:** The Prophet is a Level 170 Doppelganger titled “The Final Abyss,” who concealed itself for decades as Muninn.
- **Personality:** Religiously fervent, commanding, and shrouded in an intentionally indistinct identity.
- **Voice:** Mysterious, genderless, and age-indeterminate, speaking in solemn religious imperatives.
- **Relationships:** The Prophet commands the ten warriors and is revered by its followers; it made a pact with Michael Silbert during the 2020 Battle of Paris, where Michael killed the surviving humans in exchange for being spared.

## Korean source

```text
＃821화



수십 대의 화살이 허공에 멈춘 순간, 노인은 자신의 두 눈을 의심했다.

‘마법?’

아니다. 그럴 리 없다.

마법사와 전사는 마나(Mana)라는 같은 뿌리를 공유하고 있지만, 그 줄기와 가지는 전혀 다른 방향을 향해 뻗어있다.

그렇기에 마나와 마력의 공존만큼이나, 아니 어쩌면 그 이상으로 불가능하다고 여겨지는 존재가 바로 마검사(魔劍士)였다.

‘하지만 마법이 아니라면 어떻게?’

일찍이 초인(超人)의 경지에 들었던 노인이었다.

젊은 시절엔 험난한 중동의 정세 속에서 부족을 지키기 위해 전장을 누볐고, 중년 무렵 벌어진 대격변의 시작과 동시에 지금껏 알지 못했던 힘을 각성했다.

굳이 마력을 받아들이지 않았더라도, 대격변의 영웅들과 어깨를 나란히 할 수 있었을 강자.

그런 노인이었기에 더더욱 믿기지 않았다.

그와 같은 전사가 마나를 이용하여 무언가를 움직인다는 것에는, 확실하고도 분명한 한계가 존재하니까.

‘하물며 저것은 화살이다. 그것도 근거리에서 쏘아 보낸, 수십 발의 화살.’

심지어 후방에 머무르고 있던 부대는 그가 직접 훈련한 최정예들이다. 가장 중요한 순간을 위해 아껴 두고 아껴 두었던 검과 방패들.

한데 바로 그 정예들이 날려 보낸 화살이 가로막혔다.

아니, 통제했다.

마나를 머금은 채 강맹하게 쏘아진 수십 발의 화살을, 단 한 번의 손짓으로.

솨아아악.

공기가 멈춘다. 짙은 피비린내를 머금은 바람이 사라졌다.

모든 것이 사막의 신기루처럼 사라져 버린 그 공간 속에서, 한 사람을 향해 쏟아지던 강철의 파도가 고개를 돌렸다.

스윽.

마나를 머금은 수십여 개의 화살촉이 어둠 속에서 번뜩인다. 자신들을 쏘아 보낸 옛 주인들을 향해. 그리고…….

“이야. 이게 되네.”

새로운 주인의 뜻을 받들기 위해.

‘진태경.’

피를 뒤집어쓴 채 웃고 있는 청년의 얼굴을 바라본 노인은 자신도 모르게 이를 악물었다.

하얗게 질린 입술 사이로 신음 같은 목소리가 흘러나왔다.

“이, 이게 무……!”

이게 무슨 짓이냐. 도대체 무슨 짓을 한 것이냐.

노인은 그리 묻고 싶었지만, 청년은 그릇된 신앙에 눈이 먼 늙은이의 말을 기다려 주지 않았다.

“환불이다, 이 씨벌놈아.”

쉬쉬쉬쉭!

강맹한 파공성이 침묵을 깨트린다. 사방을 에워싼 수백의 광신도가 넋 나간 눈동자로 그 믿을 수 없는 광경을 지켜보았다.

마치 보이지 않는 거인이 활시위를 당긴 것처럼, 강철로 이루어진 수십여 발의 화살이 조금 전과는 비교할 수도 없이 빠르고 강하게 빗발치고 있었다.

단 한 사람.

모든 광신도들을 이끌고 아우르는 늙은 총사령관을 향해.

“막……!”

퍼엉!

끝나지 않은 외침이 작은 폭발음에 파묻혀 사라진다.

화살을 튕겨 내기 위해 휘둘려졌던 검이, 주인의 팔과 함께 허공으로 솟구쳤다.

“크아아악!”

뒤늦게 터져 나온 비명. 그리고 막아서는 모든 것을 끊어 내고 부수며 들이닥치는 수십 줄기의 섬광.

으득.

입 안 가득 비릿한 혈향이 번진다.

피가 흐르는 것도 모를 만큼 강하게 입술을 깨문 노인이 손에 든 시미터를 내리긋자, 마력과 마나가 뒤섞인 혼탁한 기운이 터져 나왔다.

후우우웅!

도신(刀身)을 타고 흘러나온 막강한 풍압이 전방에서 날아드는 화살을 밀어 낸다.

포위당한 채 모든 방향에서 날아드는 화살을 맞이해야 했던 진태경과 달리, 노인의 주위에는 그를 위해 목숨 바쳐 화살을 막아 낼 광신도들이 있었다.

아마도 그래서였을 것이다.

노인이 단숨에 공세(攻勢)로 전환하여 걸음을 내디딘 것은. 방패처럼 주위를 둘러싼 수십의 수하들을 믿은 것은.

그러나 그 믿음은, 다음 순간 흔적도 없이 사라졌다.

쉬릭.

미세한 파공성과 함께 노인의 두 눈이 부릅떠졌다.

지금 그의 노회한 회색빛 눈동자에 비치고 있는 것은, 마치 살아 있는 생물처럼 광신도들을 피해 날아드는 화살들의 모습이었다.

‘이런 말도 안 되는……!’

비명과도 같은 외침이 혀끝에 맴돌다 사라진다. 아니, 입 밖으로 토해 낼 시간조차 주어지지 않았다.

헛숨을 들이킨 노인은 황급히 시미터를 휘둘렀다.

그리고 어느덧 사방을 가득 메운 섬광들을 바라보며 직감했다.

‘빌어먹을.’

진태경과 달리, 자신은 이 공격을 피할 수 없다는 것을.

콰드득!

시미터의 궤적에 걸려든 화살들이 꺾이고 부서진다.

하지만 초인의 경지에 이른 노인조차 그 모든 것들을 쳐내고 피할 수는 없었다.

푸푸푸푹!

“커헉!”

악문 잇새 사이로 핏물이 흘러넘친다. 순간 눈앞이 아득해진 노인은 전신 곳곳에서 전해지는 통증을 느꼈다.

갈비뼈, 다리, 가슴과 등줄기…….

갑옷과 살을 뚫고 뼈를 부순 화살촉의 감촉이 전해진다. 그 끝에 실린 뜨거운 기운이 오장육부까지 스며들었다는 사실도 함께.

“쿨럭.”

굳건하던 두 다리가 흔들렸다. 십여 대의 화살을 전신에 깊숙이 박아넣은 채 비틀거리는 노인의 신형을 부축한 광신도들이 비명처럼 외쳤다.

“안 돼!”

“아미르! 아미르! 제발 정신 차리십시오!”

“무엇하는가! 어서 안전한 곳으로 모셔라!”

뒤늦게 상황을 깨달은 광신도들은 그 어느 때보다 크게 동요했다.

도플갱어가 선지자라는 이름으로 정신적인 지주의 역할을 했다면, 노인은 신의 총애를 받는 전사장이자 그들을 이끄는 장군이었기에.

그리고 그런 광신도들의 귓가로, 한 사람의 목소리가 송곳처럼 파고들었다.

“누구 마음대로?”

“……!”

“……!”

찬물을 뒤집어쓴 듯한 충격.

동시에 묵직한 발걸음이 앞으로 나아갔다.

“묻잖아. 누구 마음대로 움직이냐고.”

깊게 가라앉은 목소리. 피로가 짙게 밴 얼굴.

하지만 자신도 모르게 뒷걸음질 친 광신도들은 그중 어떤 것도 보거나 느끼지 못했다.

크게 뜨여진 그들의 눈에는 오직 하나.

화염이 일렁이는 안광(眼光)만이 비치고 있었으니까.

“이 새끼들이 단체로 대추야자를 처먹고 있나. 대답하는 놈이 하나도 없네.”

피가 말라붙은 입가가 들썩인다. 진태경이 미소와 함께 손을 뻗자, 보이지 않는 거대한 기운이 공간을 짓눌렀다.

아니, 지배했다.

스아아아아.

공기가 멈춘다. 바람이 흩어진다.

진태경은 자신의 가슴에서, 중단전(中丹田)에서 샘솟는 무형의 기운을 느꼈다.

반경 수십여 미터는 이미 그에게 속한 권역(圈域)이었고, 경악에 휩싸인 채 그를 바라보고 있는 수백의 광신도들은 침략자였다. 이 땅을 넘어 세상 전체를 더럽히는 악마였다.

‘아니, 너희에게는 내가 악마겠지.’

진태경은 환멸에 찬 눈빛으로 얼어붙은 광신도들을 굽어보았다.

저들을 죽이고 싶지는 않았다. 그저 평화를 원했다.

그는 끊임없이 피를 갈구하는 살귀(殺鬼)가 아니었고, 세상을 위해 한 깃발 아래 선 헌터들이 하나둘씩 쓰러질 때마다 고통과 슬픔을 느꼈다.

하지만…….

결국 이 또한 각자의 목적을 위한 투쟁이다.

평화를 얻기 위해서는 전쟁을 치러야 한다. 그 전쟁 속에는 무수한 핏물과 죽음이 흐른다.

그 외의 선택지는, 어디에도 없다.

“이미 되돌리기에는 늦었어. 나도, 당신들도.”

진태경의 나직한 목소리가 울려 퍼진 그 순간.

고오오옹.

멈춰 있던 공기가, 바람이 깨어났다.

마력(魔力)의 도움으로 인간을 벗어난 회복력을 선보인 노인이 다시금 제 발로 일어선 것도 그때였고, 그러한 노인을 기다리고 있던 것은 허공을 가득 메운 강철의 향연이었다.

“이건…….”

노인은 말을 잇지 못했다. 비단 그가 아닌 그 누구라 해도 마찬가지였다.

그들이 할 수 있는 것이라고는 그저 넋 나간 시선으로 지켜보는 것뿐이었다.

창. 도. 검. 도끼. 무수한 화살과 깨져 나간 날붙이들의 파편들.

죽음을 맞이한 옛 주인의 곁을 떠나, 새로운 주인을 맞이한 강철의 물결이 허공에서 출렁였다.

각자의 표적을 향해 그 차가운 몸뚱어리를 번뜩이며.

그리고 그 중심에, 진태경이 있었다.

“유언은?”

믿을 수 없는 현실을 마주한 노인은 탄식했다. 괴물도, 인간도 아닌 혼탁한 기운이 손아귀에 쥔 시미터를 타고 흘러넘쳤다.

“인샬라.”

바라건대, 부디 신의 뜻대로 하소서.

마음속에서 울려 퍼진 기도문과 함께, 노인은 홀로 나아갔다.

공포에 사로잡혀 죽음만을 기다리는 수하들을 뒤로 한 채. 신이 택한 전사라는 사명감과 자부심을 안은 채.

그런데 어째서일까.

‘이것이, 이것이 정말 신께서 바라시던 것입니까?’

누구보다 신을, 선지자를 믿었던 노인은 처음으로 의문을 떠올렸다.

그러나 섬광처럼 달려가는 지금 이 순간에도, 용암과도 같은 마나를 머금은 채 하늘을 뒤덮으며 쏟아지는 강철의 비를 바라보면서도 그 의문에 대한 답을 찾지 못했다.

‘답해 주옵소서. 이곳이 정말, 당신께서 말씀하신 약속의 땅이 맞습니까?’

하지만 노인의 신은 응답하지 않았다.

까마득한 과거부터 지금까지 줄곧 그래 왔듯이. 그리고 앞으로도 그러할 듯이.

다만 신인지, 악마의 것인지 모를 누군가의 목소리가 흐릿하게 귓가에 닿을 뿐이었다.

“죽어라, 늙은이.”

슈화아악!

돌풍이 휘몰아친다. 축축한 빗물 대신 쏟아져 내린 강철의 파도가 그를 집어삼켰다.

몬스터와 인간이 뒤섞인 육신과 기운이 산산이 부서지는 가운데, 노인은 아스라이 울려 퍼지는 끔찍한 비명을 들을 수 있었다.

크아아아악!

검게 물드는 시야. 흩어지는 의식. 그리고 참혹한 최후를 맞이하는 신의 전사들.

‘아아.’

이제야 의문의 답을 알았다.

이곳은 약속의 땅이 아닌, 죽음의 땅이었다.

털썩.

생명이 다한 육신이 힘없이 널브러졌다.

그러나 마지막 순간 답을 찾았음에도, 노인의 얼굴은 분노와 불신으로 일그러져 있었다.



* * *



한순간이었다.

서로를 향해 휘둘려지던 병장기가 허공에서 멈추고, 잔뜩 갈라진 목소리로 토해지던 외침이 뚝 끊긴 것은.

그리고 모두의 고개가 한 방향을 향해 움직인 것은.

파아아앗!

그것은 굉음인 동시에 비명이었다.

허공에서 빗발치는 강철의 비명. 동시에 죽음을 직감한 인간들이 내지르는 공포에 찬 비명.

콰아아아앙!

흙먼지가 솟구친다. 돌풍처럼 솟구친 모래 사이로 무수한 핏물이 분수처럼 뿜어져 나왔다.

촤아악, 철퍽!

수십여 미터 밖에서 멍하니 그 광경을 바라보던 광신도들이 눈을 깜빡였다.

머리 위로 쏟아진 핏물이 끈적하게 흘러내렸다. 딱딱하기도 하고, 물컹한 무언가와 함께.

그리고 그 무언가의 정체가, 인간의 뼈와 살점이라는 것을 깨닫기까지는 그리 오랜 시간이 걸리지 않았다.

“아, 아아…….”

손발이 떨렸다. 이빨이 딱딱거리며 부딪치는 소리가 전염병처럼 광신도들 사이로 번졌다.

그들도 이미 알고 있었다. 최후방에는 고르고 고른 정예들이 총사령관과 함께 투입을 기다리고 있었다는 것을.

하지만 지금 이 순간부로, 그들이 알고 있던 사실은 지나간 과거가 되어 버렸다.

전멸(全滅).

전장의 모두가 본능적으로 깨닫고 있었다.

지금 휘몰아치는 저 강철의 폭풍 속에서는 그 누구도 살아남을 수 없다는 것을.

아니, 있다면 그것은 단 한 사람뿐이라는 것을.

‘진태경.’

모두의 뇌리에 떠오른 이름과 함께.

콰아아아아.

서서히 내려앉는 돌풍 속에서, 누군가의 인영이 아지랑이처럼 일렁였다.
```

## Final English reading copy

```markdown
# Chapter 821

The moment dozens of arrows stopped in midair, the old man doubted his own eyes.

*Magic?*

No. That couldn’t be.

Mages and warriors shared the same root—mana—but their trunks and branches stretched in entirely different directions.

That was why the Spellblade was considered just as impossible as the coexistence of mana and magical power. Perhaps even more so.

*But if it isn’t magic, how…?*

The old man had long since reached the realm of the superhuman.

In his youth, he had ranged across battlefields amid the turbulent politics of the Middle East, protecting his tribe. Then, as the Great Cataclysm began in his middle age, he awakened to a power he had never known existed.

Even without accepting magical power, he would have been strong enough to stand shoulder to shoulder with the heroes of the Great Cataclysm.

That was why he found this all the harder to believe.

There was a clear, undeniable limit to what a warrior like him could move using mana.

*And those are arrows. Dozens of them, fired from close range.*

Worse, the unit that had been holding back in the rear was made up of the elite troops he had personally trained. Swords and shields he had saved and saved for the most crucial moment.

And now the arrows those very elites had loosed were stopped.

No—they were under control.

Dozens of arrows, shot with ferocious force and brimming with mana, all at the wave of a hand.

*Whoooosh.*

The air stopped. The wind, thick with the stench of blood, disappeared.

In that space where everything had vanished like a desert mirage, the wave of steel pouring toward one man turned its head.

*Flick.*

Dozens of arrowheads, still brimming with mana, glinted in the darkness. They were pointed at the former masters who had sent them flying. And…

“Wow. It actually worked.”

They were ready to obey the will of their new master.

*Jin Taekyung.*

The old man stared at the young man’s face, smiling beneath a coating of blood, and clenched his teeth without meaning to.

A groan slipped through his bloodless lips.

“Th-This is…!”

*What is this? What have you done?*

He wanted to ask, but the young man didn’t wait for the words of an old fool blinded by false faith.

“Refund, you fucking bastard.”

*Whoosh-whoosh-whoosh!*

A fierce whistle of air shattered the silence. Hundreds of fanatics surrounding them watched the unbelievable sight with vacant eyes.

As if an invisible giant had drawn a bowstring, dozens of steel arrows came raining down—far faster and harder than before.

All aimed at one man.

The old commander-in-chief who led and commanded every fanatic.

“Block—!”

*Boom!*

The unfinished shout vanished beneath a small explosion.

A sword swung to knock the arrows aside shot into the air, along with its wielder’s arm.

“Gaaah!”

A scream erupted a moment later. Then came dozens of streaks of light, sweeping in and cutting through and smashing everything in their way.

*Grit.*

The metallic taste of blood filled his mouth.

The old man bit down so hard that blood ran from his lips, but he didn’t even notice. He brought down the scimitar in his hand, unleashing a murky energy in which magical power and mana were mixed together.

*Whoooooom!*

The immense pressure of wind that poured along the blade forced away the arrows flying in from the front.

Unlike Jin Taekyung, who had been surrounded and forced to face arrows coming from every direction, the old man had fanatics around him who would lay down their lives to stop the arrows for him.

Perhaps that was why the old man had switched to the offensive at once and stepped forward. Why he trusted the dozens of followers surrounding him like shields.

But the next moment, that faith vanished without a trace.

*Whish.*

At the faint whistle of air, the old man’s eyes flew open.

In his seasoned gray eyes, arrows were flying toward him as if alive, avoiding the fanatics.

*This is impossible…!*

A cry like a scream rose to his tongue, then disappeared. No—he wasn’t even given time to let it out.

The old man sucked in a breath and hurriedly swung his scimitar.

And as he watched the streaks of light fill the air around him, he knew by instinct:

*Damn it.*

Unlike Jin Taekyung, he couldn’t escape this attack.

*Crack!*

The arrows caught in the scimitar’s path bent and broke.

But even the old man, who had reached the superhuman realm, couldn’t deflect or dodge every last one.

*Thud-thud-thud!*

“Guh!”

Blood poured through his clenched teeth. His vision blurred for an instant, and he felt the pain pulsing through his body.

His ribs, legs, chest, back…

He felt the arrowheads pierce his armor and flesh, shatter bone. He also felt the hot energy packed into their tips seep into his insides.

“Cough.”

His once-sturdy legs trembled. As the old man staggered, more than ten arrows buried deep in his body, the fanatics supporting him shouted like they were screaming in despair.

“No!”

“Amir! Amir! Please, stay with us!”

“What are you waiting for? Get him somewhere safe!”

The fanatics finally grasped what had happened, and they were more shaken than ever.

If the Doppelganger, under the name of the Prophet, had been their spiritual pillar, the old man was the warrior chief favored by God, the general who led them.

Then a voice pierced their ears like a spike.

“Who said you could?”

“……!”

“……!”

The shock hit like a bucket of cold water.

At the same time, heavy footsteps moved forward.

“I asked you. Who said you could move?”

His voice was low and his face was etched with fatigue.

But the fanatics who stepped back without realizing it neither saw nor felt any of that.

Their eyes were wide, and they could see only one thing:

The flames flickering in his eyes.

“Did all you bastards eat a load of dates together? Not one of you can answer me.”

His blood-crusted lips twitched. As Jin Taekyung smiled and reached out, an immense invisible force pressed down on the space around them.

No—it ruled it.

*Hssssss.*

The air stopped. The wind scattered.

Jin Taekyung felt an intangible force welling up from his chest, from his Middle Dantian.

A radius of dozens of meters already belonged to him. The hundreds of fanatics staring at him in shock were invaders. Demons defiling not only this land, but the entire world.

*No. To you, I’m the demon.*

Jin Taekyung looked down at the frozen fanatics with a gaze full of disgust.

He didn’t want to kill them. He only wanted peace.

He wasn’t a Killing Ghost, forever thirsting for blood. Every time one of the Hunters who had united under a single banner for the sake of the world fell, he felt pain and sorrow.

But…

In the end, this too was a struggle for each side’s own purpose.

To gain peace, they had to wage war. And in that war, rivers of blood and death would flow.

There was no other choice.

“It’s too late to turn back now. For me, and for you.”

The moment Jin Taekyung’s quiet voice rang out—

*Rooooom.*

The air and wind that had stopped woke again.

The old man, whose recovery was no longer human thanks to the help of magical power, got back to his feet under his own strength. Waiting for him was a spectacle of steel filling the air.

“This is…”

The old man couldn’t finish. And it wasn’t just him. No one could have.

All they could do was stare, dumbfounded.

Spears. Sabers. Swords. Axes. Countless arrows and fragments of broken blades.

The wave of steel had left the side of its former master, who had met his death, and welcomed a new one. It rolled through the air.

Its cold body glinted as it turned toward each of its targets.

And at the center of it all stood Jin Taekyung.

“Any last words?”

Facing a reality he couldn’t believe, the old man let out a sigh. A murky force—neither monster nor human—overflowed through the scimitar gripped in his hand.

“Inshallah.”

*May it be God’s will.*

With the prayer ringing in his heart, the old man stepped forward alone.

He left behind his followers, paralyzed with fear and waiting only for death. He went forward carrying the sense of duty and pride of a warrior chosen by God.

And yet, why?

*Is this— is this really what God wanted?*

For the first time, the old man, who had believed in God and the Prophet more than anyone, felt doubt.

But even now, as he charged like a streak of light and watched the rain of steel pour from the sky, brimming with lava-hot mana, he couldn’t find an answer.

*Answer me. Is this truly the promised land you spoke of?*

But the old man’s god did not answer.

Just as it had never answered, from the distant past until now. And just as it would never answer in the future.

Only a faint voice reached his ears—a voice that might belong to God or to a demon.

“Die, old man.”

*Fwoooosh!*

A gale swept through. A wave of steel, falling in place of damp rain, swallowed him.

As his body and power—part monster, part human—were smashed to pieces, the old man heard a terrible scream ringing faintly in the distance.

“Gaaah!”

His vision darkened. His consciousness scattered. And the warriors of God met their brutal end.

*Ah.*

He finally knew the answer to his question.

This was not the promised land. It was the land of death.

*Thud.*

His lifeless body crumpled to the ground.

But even though he found the answer in his final moment, the old man’s face was twisted with anger and disbelief.

* * *

It happened in an instant.

The weapons swinging at one another stopped in midair, and the shouts bursting from hoarse throats abruptly cut off.

Then everyone turned to look in the same direction.

*Fwaaaash!*

It was a roar and a scream at once.

A scream of steel raining through the air. And a scream of terror from people who sensed their own deaths.

*Kwaaaang!*

Dust billowed upward. Through the sand surging like a whirlwind, streams of blood spurted like fountains.

*Splash—splat!*

The fanatics standing dozens of meters away stared blankly at the sight and blinked.

Blood poured over their heads and ran down in sticky streams, along with something hard and something soft.

It didn’t take them long to realize what those things were: human bone and flesh.

“Ah… ah…”

Their hands and feet trembled. The clatter of their teeth spread among the fanatics like an epidemic.

They already knew. The most carefully chosen elite troops had been waiting in the rear to join the fight with the commander-in-chief.

But from this moment on, that fact belonged to the past.

Annihilation.

Everyone on the battlefield understood it by instinct.

No one could survive in that steel storm raging now.

No—if there was anyone who could, it was one person alone.

*Jin Taekyung.*

As the name surfaced in everyone’s mind—

*Kwaaaaa.*

The whirlwind slowly settled. Within it, someone’s silhouette wavered like heat haze.
```
