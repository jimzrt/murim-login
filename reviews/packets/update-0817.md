<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0817.txt",
      "sha256": "9822a9acb0477c14b5f6608b183874ca9c22cd4dc892934abeea3eef52c1ace0",
      "bytes": 13477
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "b97e7cbe9695e9c578dc9374508465dd8cd74e605e2de633d7d8600df1f519e2",
      "bytes": 1608
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "3058a17075f2e26242c2c44256fa9a4f5d86c0de54766ae8d188b23c0ef18a27",
      "bytes": 226002
    },
    {
      "path": "characters/Cheon Taemin.md",
      "sha256": "bf6d58fff75e02c057c52bc06227b4e72ac760d37f803650c5dc44291d79216c",
      "bytes": 776
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "ec5946c37cab55855eb91c088d39ca9a3d92ac473c299c91e70d4c0ecc38ebe4",
      "bytes": 723
    },
    {
      "path": "characters/Doppelganger.md",
      "sha256": "56d3fe0467207209059c8c3e485f91e4186393be968a9f24d4443b59e641040d",
      "bytes": 708
    },
    {
      "path": "characters/Human Butcher.md",
      "sha256": "615e31ef3e8785817cc89fb45b48bed2d185c72e4ff755fb47d50dcf92bbbbb7",
      "bytes": 667
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "6ccf2b7204a8146fd4f06a7aafde5ee2f8bd8bbb76252bb92638e536002a0f46",
      "bytes": 1921
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "08f9f8645d06925e90c083d4812b58b1bfd1bb7b32ec070a96089f54e0d8110f",
      "bytes": 622
    },
    {
      "path": "characters/Michael.md",
      "sha256": "9a2387ff6d034b63dc76a57d093a02d66dcd786fc28b36dcbadaf3b36eca22f5",
      "bytes": 820
    },
    {
      "path": "characters/The Prophet.md",
      "sha256": "58b74eb7026506f0793365aaad8f03b1ef75f3af3b1afc5d9bef8dcfb8ab033d",
      "bytes": 724
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "129974e6f11f14cc393ae3bd0f5641ba588160bd005872ba6c36f3b8580fa33e",
      "bytes": 249016
    }
  ],
  "estimated_tokens": 10506
}
-->

# Durable State Update — Chapter 817

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
1 and safe_through 817. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 817. Profile updates may replace only one
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
  "chapter": 817,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 817,
    "continuity_sources": [817],
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
    "The Prophet is a Level 170 Doppelganger titled “The Final Abyss”; it concealed itself for decades, including under the name Muninn.",
    "The Doppelganger can resurrect by consuming absorbed lives and can reproduce absorbed people’s appearances, abilities, and memories.",
    "The Doppelganger has died more than two hundred times in under ten minutes; fewer than half of its absorbed lives remain.",
    "The Doppelganger says it is the last survivor of its species after a purge in the Demon Realm.",
    "The Doppelganger’s master ordered it to avoid the target until its plan was complete and called Jin Taekyung the Chosen One.",
    "The Doppelganger regarded Michael Silbert as a subordinate and disposable tool.",
    "The Doppelganger has taken on Siegfried Bassman’s face and gathered vast mana; Jin recognizes the face."
  ],
  "continuity_sources": [
    815,
    816
  ],
  "open_questions": [
    "Who is the Doppelganger’s master, what is the plan, and why must the target be avoided until it is complete?",
    "What does the Chosen One designation mean?",
    "What will the Doppelganger do with Siegfried Bassman’s face and gathered mana?",
    "Is Magic Johnson human?"
  ],
  "safe_through": 816,
  "temporary_decisions": [
    "Keep magical power distinct from mana.",
    "Keep Demon Realm language distinct from other languages."
  ],
  "version": 1
}
```

## Exact glossary matches

| 진태경    | **Jin Taekyung**   |
| 천태민    | **Cheon Taemin**  |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 살기     | **killing intent**                               |                                                       |
| 상태               | **Status**                     |
| 레벨               | **Level**                      |
| 헌터      | **Hunter**            |
| 도사      | **Daoist**                                                      |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 도플갱어 | **Doppelganger** | The Prophet’s revealed species. |
| 인도 | **Human Butcher** | Epithet of a mysterious Han Chinese mounted-bandit power commanding fifty subordinates. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 미카엘 | **Michael** | Guild Master of Odin Guild. |
| 선지자 | **The Prophet** | Mysterious religious leader directing the terrorist warriors. |
| 아스모데우스 | **Asmodeus** | Demon King referenced in Taekyung's sarcastic comparison; does not appear directly. |
| 화염신장 | **Flame Divine Palm** | Jopil's deadly palm technique, noted when Taekyung compares Jopil with Mukyung. |
| 링크 | **Link** | Mental connection between a mage and Familiar |
| 마도 | **Demonic Path** | Term raised for martial power that appears to defy common principles. |
| 마왕 | **Demon King** | The being Cheon Taemin killed. |
| 아미 | **Emei** | Short form for Emei Sect. |
| 대적자 | **the Adversary** | Ancient human enemy remembered by the Arch Lich. |
| 블링크 | **Blink** | Arch Lich movement spell |
| 소멸 | **Erasure** | Jin's term for the Skeleton Warlord's destruction by the Arch Lich's mana. |
| 텔레포트 | **Teleport** | Taekyung's label for the Blood Lord's unexplained disappearance. |
| 마법 | **Magic** | Taekyung's explanation for Dark Heaven's anomalous abilities. |
| 대마도사 | **Grand Mage** | Title used for Magic Johnson. |
| 신인 | **divine man** | Descriptive term for a human who became something beyond humanity. |
| 마력 | **magical power** | Distinct from mana; the Skeleton King's area of expertise. |
| 심해 | **deep sea** | Unexplored ocean depths where the ancient monster awakens. |
| 실베르트 | **Silbert** | Family name in Michael Silbert. |
| 아미르 | **Amir** | Title used to address the group’s leader. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 신의 | 진태경 | physician_to_benefactor | Young Master Jin | formal-polite | The Divine Physician addresses Taekyung as 진 공자 while expressing concern for his injuries. |
| 진태경 | 헌터 | field commander to allied Hunters | you; Hunters | blunt and commanding | Orders the human forces to stop asking questions and kill the fleeing Minotaurs. |
| 미카엘 | 진태경 | rival_to_target | you | quietly polite but threatening | Michael warns Jin to reconsider for the sake of Jin's monster friend. |
| 진태경 | 미카엘 | target_to_rival | Go fuck yourself | blunt and profane | Jin rejects Michael's proposal to resurrect the World Hunter Federation. |
| 진태경 | 선지자 | enemy commander addressed by Jin | The Prophet | blunt and informal | Jin asks where The Prophet is while confronting the Manticore Lord. |
| 진태경 | 도플갱어 | enemy | you; the Doppelganger | blunt and informal | Jin directly challenges the Doppelganger and demands to know what it wants. |

## Listed compact profiles

### Cheon Taemin.md

# Cheon Taemin (천태민)

- **Safe through:** Chapter 816
- **Aliases:** Slayer; Sky (the American epithet used for him)
- **Role:** Ares Guild Master and humanity's greatest Hunter, the Slayer who defeated the Demon King and created the first Mana Cultivation Method during the Great Cataclysm; after more than twenty years in seclusion, he remains unconscious in a secret area within Area A.
- **Personality:** Not established.
- **Voice:** Not established.
- **Relationships:** Maternal grandfather of Team Leader Choi and Jin Taekyung and father of Soyeong; regarded by Lee Jungryong as an older brother despite their lack of blood relation.

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 816
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** He is devoted to medicine and the lives he could not save, yet remains composed and self-effacing under mortal danger.
- **Voice:** He speaks in calm, respectful, self-effacing language, framing mortality through quiet philosophical reflections.
- **Relationships:** Mungyeong is the Divine Physician's true identity, and Dong Feng is his Disciple.

### Doppelganger.md

# Doppelganger (도플갱어)

- **Safe through:** Chapter 816
- **Aliases:** The Final Abyss
- **Role:** The last surviving member of its species, the Doppelganger is a powerful being from the Demon Realm that spent decades manipulating events in the human world.
- **Personality:** Arrogant and manipulative, it treats others as tools but becomes desperate when its own survival is threatened.
- **Voice:** Not established
- **Relationships:** It served an unnamed master who sent it to this world and ordered it to avoid the target until the master’s plan was complete; it regarded Michael Silbert as a subordinate and disposable tool.

### Human Butcher.md

# Human Butcher (인도)

- **Safe through:** Chapter 803
- **Aliases:** None
- **Role:** Former mysterious Han Chinese mounted-bandit power in Northern Gaoyuan commanding fifty subordinates; a Peak master killed by an unnamed old man in a single move
- **Personality:** Cold, intimidating, and murderous; he kills people as though slaughtering livestock
- **Voice:** Cold, curt, and quietly threatening
- **Relationships:** He is one of four powerful participants at the Northern Gaoyuan gathering, intimidates Temur, and has claimed Ghost Sword Wipeng as his personal target in the proposed attack

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 816
- **Aliases:** Blazing Flame Divine Dragon; Apostle of the Earth Mother Goddess; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan, Jeok Cheongang’s Disciple, the Fire Gate Clan’s nineteenth successor, Pavilion Master of the Fire Dragon Pavilion, a Supreme Peak master and publicly recognized S-rank-level Hunter with an A-rank license, a traveler between Murim and another world, and the World Hunter Federation’s Alliance Leader.
- **Personality:** Hungry, self-aware, dryly observant, pragmatic under pressure, and willing to risk himself for people he has accepted as real; treats impossible situations like games until their human cost becomes undeniable.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, Jeok Cheongang is his Master, Mungyeong was his recent instructor, Cheongpung is his trusted companion and only true martial rival, Choi Minwoo is his subordinate and trusted manager of media and official arrangements as well as the Peace Guild's Guild Master, Ju Hwaran is a trusted Fire Dragon Pavilion member who followed him to Nanman, Magic Johnson is an allied Grand Mage who supplies him with intelligence, Chuck Hagel is an American operative allied with him in the covert anti-terror campaign, his mother and sister Hayeon are among those he protects, the Skeleton King is his friend and ally, Xiao Shen regards him as an older brother after Jin saved him, and Jin-ho is his older friend and trusted confidant.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 816
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Michael.md

# Michael (미카엘)

- **Safe through:** Chapter 816
- **Aliases:** None
- **Role:** Michael Silbert was the former Odin Guild Master, executed by Jin Taekyung after the World Hunter Federation’s first resolution.
- **Personality:** Controlled, calculating, condescending, and confident in his intelligence and ability to manipulate events, but increasingly impatient and anxious since learning of Jin Taekyung.
- **Voice:** Polite and conversational when relaxed, but quietly authoritative and coercive when asserting control.
- **Relationships:** Michael personally selected and trained Huginn, commands Odin Guild's hidden alliance, secretly confers with The Prophet, and regards Jin Taekyung's friendship with the monster as his fatal weakness.

### The Prophet.md

# The Prophet (선지자)

- **Safe through:** Chapter 815
- **Aliases:** Muninn (무닌)
- **Role:** The Prophet is a Level 170 Doppelganger titled “The Final Abyss,” who concealed itself for decades as Muninn.
- **Personality:** Religiously fervent, commanding, and shrouded in an intentionally indistinct identity.
- **Voice:** Mysterious, genderless, and age-indeterminate, speaking in solemn religious imperatives.
- **Relationships:** The Prophet commands the ten warriors and is revered by its followers; it made a pact with Michael Silbert during the 2020 Battle of Paris, where Michael killed the surviving humans in exchange for being spared.

## Korean source

```text
＃817화



도플갱어의 새로운 얼굴은 진태경에게 있어 더없이 익숙했다.

직접 마주한 것은 미라처럼 말라붙은 모습이 처음이자 마지막이었지만, 미카엘 실베르트를 조사하는 도중 사진을 통해서 지긋지긋하게 봐 왔던 바로 그 얼굴이었으니까.

게다가…….

스아아아.

손을 뻗으면 만져질 것 같은 저 거대한 마력까지.

굳이 레벨 창을 확인해 보지 않더라도, 정답은 이미 나와 있었다.

“지크프리트 바스만?”

혼잣말처럼 흘러나온 진태경의 목소리에, 도플갱어는 대답 대신 손가락을 튕겼다.

파직.

새하얀 섬광이 번뜩인다.

손가락을 타고 흘러나온 미세한 전류가 수십 줄기의 벼락으로 화하여 쏟아지기까지 걸린 시간은, 그야말로 찰나에 불과했다.

츠팟!

눈부신 섬광으로 가득 찬 시야.

그러나 자신도 모르게 눈을 감은 진태경은 분명하게 느낄 수 있었다.

사방을 둘러싼 암반, 공기, 땅. 그 모든 것을 통해 전해지는 엄청난 전류를.

쾅!

단단한 바위와 흙으로 이루어진 지면이 거미줄처럼 갈라진다.

땅을 박차고 솟구친 진태경이 일장(一掌)을 뻗었다. 화염신장의 열기가 벼락을 불사르며 쏘아졌다.

꽈아아앙!

거대한 굉음과 함께 협곡이 뒤흔들린다.

하지만 진태경은 안력(眼力)을 끌어 올려 아주 짧은 순간 벌어진 모든 상황을 시야에 담았다.

솟구치는 불길과 매캐한 연기.

그리고 그 모든 것이 터져 나오기 직전, 유령처럼 사라져 버린 도플갱어의 모습까지도.

‘블링크(Blink).’

텔레포트와 워프가 장거리 공간 이동 마법이라면, 블링크는 뜻 그대로 찰나의 깜빡임처럼 사라지는 단거리 순간 이동.

그만큼 이동 범위도 짧았고, 진태경의 감각과 시야는 협곡 전체를 뒤덮을 만큼 넓었다.

‘저곳이다.’

보이지 않는다. 그러나 느껴진다.

진태경은 호흡을 삼켰다. 그는 자신의 오감과 능력을 믿었다.

공력을 실은 발끝으로 텅 빈 허공을 밟으며, 흩날리는 불씨와 매캐한 연기 너머에 있을 도플갱어를 향해 쏘아져 갔다.

후욱, 펑!

신형에 실린 속도를 이기지 못한 공기가 터져 나간다. 연기와 불씨가 폭발하듯 흩어지고 시야가 선명해졌다.

그렇게 한 줄기 불꽃이 되어 도달한 그 끝에, 자신을 도와줄 추종자들을 향해 도망치고 있는 도플갱어가 있었다.

“……!”

등 뒤에서 느껴지는 오싹한 감각에 본능적으로 뒤를 돌아본 도플갱어는 눈을 부릅떴다.

느려진 세상 속, 어느새 코앞까지 들이닥친 진태경의 모습이 그의 눈동자에 가득 찼다.

‘도대체 어떻게?’

분명 1초도 되지 않았던 짧은 시간.

그러나 진태경은 그 찰나의 순간 블링크 마법의 이동 위치를 파악한 것으로도 모자라, 십여 미터의 거리마저 뛰어넘어 자신을 따라잡았다.

‘이런 미친……!’

도플갱어는 입 밖으로 튀어나오려는 욕을 삼켰다.

아니, 정확히 말하자면 욕을 내뱉을 시간조차 없었다.

그랬다가는 지금껏 수없이 버려 온 다른 생명과는 비교도 할 수 없을 만큼 귀중한 대마도사의 힘을 영영 잃어버리게 될 테니까.

슈확!

불그스름하게 달아오른 창날이 바람을 찢었다. 그와는 상반되는 서늘한 살기(殺氣)에 몸이 얼어붙는다.

하지만 적어도 지금 이 순간, 도플갱어의 몸에 깃든 마나와 능력은 전 세계에서 단 셋뿐인 대마도사의 것이었다.

‘블링……크!’

화륵, 퍼엉!

창날을 타고 폭발한 화염이 허공을 살라 먹었다.

동시에 십여 미터 밖에서 나타난 도플갱어는 모골이 송연해지는 것을 느꼈다.

아슬아슬하게 위기를 넘겨서?

아니다.

정확히 자신을 응시하고 있는 한 쌍의 눈동자 때문이었다.

‘진태경.’

단지 시선이 마주쳤을 뿐인데, 심장이 덜컥 내려앉는다. 수백 년이 넘는 투쟁의 세월 동안 가다듬어진 본능이 속삭였다.

도망치라고.

저 맹수에게 목덜미를 물어뜯기기 싫다면, 조금도 방심해서는 안 된다고.

그리고 다음 순간, 쉴 틈도 없이 재차 블링크 마법을 발동시킨 도플갱어는 똑똑히 알 수 있었다.

자신의 본능이 정확했다는 것을.

쏴악! 서걱!

새로운 공간에서 눈을 뜬 도플갱어는 참았던 숨을 토해 냈다.

이미 본래의 형태와 용도를 일찌감치 잃어버린 갑옷의 뒷면은, 찰나에 스쳐 지나간 열기에 의해 뜨겁게 달아올라 있었다.

‘베였다. 놈의 속도가 블링크 마법을 따라잡고 있어.’

그야말로 간발의 차.

소름이 끼쳤다. 지금까지 흡수했던, 혹은 스치듯 마주했던 모든 인간들을 떠올려 봐도 저런 괴물은 없었다.

그가 유일하게 두려워했고, 그랬기에 일부러 피해 왔던 한 사람을 제외한다면.

‘천태민.’

인류의 구세주.

나약한 인간의 몸과 정신으로, 마왕 아스모데우스와 맞선 유일한 대적자이자 신인(神人).

도플갱어는 천태민을 향한 자신의 두려움을 부정하지도, 부끄러워하지도 않았다.

상대는 ‘한낱 인간’이라 칭할 수 있는 존재가 아니었으니까.

수년 전, 지크프리트 바스만을 흡수하여 천태민의 상태를 알게 된 후에도 감히 그를 넘보지 못했던 이유도 그 때문이다.

하지만 그런 도플갱어조차 도저히 상상할 수 없었다.

천태민이 아닌 다른 인간에게, 자신이 이 정도의 두려움을 품게 되리라고는.

‘블링크, 블링크, 블링크!’

조금이라도 머뭇거렸다간 영원한 소멸을 맞이할 수도 있다.

다급해진 도플갱어는 연달아 공간을 뛰어넘었다.

그의 신형이 지우개로 지워 낸 것처럼 사라질 때마다, 치열한 전투가 이어지는 협곡의 출구가 가까워졌다.

숨 가쁘게 도망치는 사냥감의 뒤를 쫓는 사냥꾼과의 거리도.

쐐액!

날카로운 파공성이 공간을 가른다.

섬광처럼 들이닥친 십여 개의 비수가 도플갱어의 전신을 노렸다. 블링크 마법을 발현시킬 틈조차 없는, 철저히 예측된 공격.

선택지가 없음을 깨달은 도플갱어가 이를 악물며 두 손을 펼쳤다.

우우웅, 콰직!

마나로 이루어진 보호막이 완성되기도 전에 박살 났다. 반발력에 의해 튕겨 나간 비수들이 양옆의 절벽과 지면에 틀어박혔다.

하지만 비수를 막아 내느라 소모한 그 짧은 시간 동안, 진태경의 신형은 어느덧 도플갱어의 코앞까지 다가와 있었다.

“잡았다.”

“……!”

콰득!

반응할 새도 없었다.

도플갱어는 손목을 통해 전해지는 엄청난 고통에 입을 딱 벌렸다.

생전의 지크프리트 바스만은 위대한 대마도사였지만, 진태경의 무시무시한 힘은 그의 기억 속에 존재하는 어떤 마법으로도 막을 수 없었다.

뿌드드득!

“크아아악!”

끔찍한 통증을 참지 못하고 입 밖으로 터져 나온 비명.

단지 강하게 손을 쥔 것만으로도 살과 근육이 짓이겨지고 뼈가 바스라진다.

순간 새하얗게 물든 도플갱어의 시야에, 하늘과 땅이 기울어지는 것이 보였다.

‘뒤집힌다. 아니, 죽는다.’

도플갱어는 본능적으로 깨달았다.

이 공포스러운 부유감(浮游感) 뒤에, 지면과 부딪쳐 전신이 으스러지는 죽음이 자신을 기다리고 있으리라는 사실을.

‘안 돼!’

지크프리트 바스만은 그가 흡수한 생명 중에서도 가장 귀중한 것이었다.

세상에 알려진 S급 헌터를 사냥하는 것 자체도 매우 까다롭지만, 활용성이 좋은 마법이라는 능력을 부여해 주는 대마도사는 특히나 귀중한 자원이었으니까.

‘마법을 잃어버리면 정말 끝장이다. 그렇다면 차라리……!’

공포가 불러온 의식의 흐름은 빛살처럼 빨랐고, 결심은 단호했다.

후우웅!

거센 파공음과 함께 지면으로 처박히던 그 순간. 도플갱어는 혼신의 힘을 다해 마나를 끌어 올렸다.

‘블링크!’

파앗.

세상이 느려졌다.

마나에 의해 일그러진 공간이 도플갱어의 전신을 빨아들이듯 집어삼켰다. 그러나 조금 전과는 달리 마나의 양도, 안정감도 달랐다.

도플갱어의 시선은 블링크 마법의 이동 한계를 아득히 벗어난, 수백 미터 밖의 전장에 향해 있었다.

‘해내야 한다.’

공간 마법의 한계를 벗어난 금기(禁忌).

그러나 이대로 죽는 것보다는 나았다. 저곳에는 그를 신처럼 받들어 모시는 광신도들이, 지난 수십여 년간 공들여 양성해 낸 추종자들이 있었으니까.

우드드득!

공간과 함께 뼈와 살이 뒤틀렸다.

보이지 않는 손이 심장을 쥐어 터트리려 하는 듯한 고통이 느껴졌지만, 아무래도 상관없었다.

진태경.

당장 이 괴물 같은 인간의 손에서 벗어날 수 있다면.

이대로 추종자들의 보호를 받으며 도망쳐, 오랫동안 준비해 온 계획을 이룰 수 있다면.

‘잘 있어라. 다음에 보자.’

도플갱어가 속으로 그렇게 중얼거리며, 피에 젖은 이빨을 드러내고 웃은 그 순간.

드득, 화아아악!

폭풍우처럼 거칠게 휘몰아친 마나와 일그러진 공간이 그를 집어삼켰다.

동시에 암전(暗轉)된 시야 속에서 새로운 빛과 소음. 그리고 얼굴들이 파도처럼 그를 감쌌다.

쾅! 콰아아아앙!

쉬쉭! 카가가각!

“커헉!”

“신의 전사들이여, 죽음을 두려워하지 말라!”

“좆 까, 이 미친 광신도 새끼들아!”

굉음과 비명이 사방에서 터져 나온다. 양측에서 울려 퍼진 고함이 찢어진 고막을 후려친다.

하지만 도플갱어에게 중요한 것은 흐릿한 시야 속에서 보이는 얼굴들이, 바로 자신의 추종자들이라는 사실이었다.

“자, 잠깐!”

“선지자시여!”

터번을 눌러쓴 광신도들이 그를 발견하고 에워쌌다. 내장 조각이 뒤섞인 핏물을 토해 낸 도플갱어가 소리 내어 웃었다.

“쿨럭. 푸흐흐…….”

고통?

괜찮다. 금방 회복할 수 있을 테니.

뼈마디 곳곳이 으스러졌고, 진태경에게 붙잡혔던 왼손은 어깨부터 뜯겨 나가 있었지만, 한계를 벗어난 블링크 마법이 성공했다는 사실이 중요했다.

‘평범한 인간이었다면 틀림없이 죽었겠지.’

운이 좋았다.

지크프리트 바스만이 대마도사였기에 성공했고, 도플갱어였기에 이런 부상을 입고도 살아남을 수 있었다.

스륵. 뿌드득.

뜯겨 나간 팔의 단면에서 어린아이처럼 뽀얀 살이 조금씩 차오른다. 끊어졌던 근육이 이어지고 새하얀 뼈가 자라났다.

처음과는 비교도 할 수 없이 느려진 회복 속도에, 도플갱어는 쓰게 입맛을 다셨다.

‘빌어먹을.’

지금껏 그가 흡수해 왔던 무수한 생명도 어느새 바닥을 드러내고 있었다.

아마도 이 자리를 완전히 벗어날 때쯤이면, 정말 손으로 헤아릴 수 있을 만큼의 생명만 남아 있을지도 몰랐다.

‘하지만 상관없다. 날 위해 목숨 바쳐 싸워 줄 것들이 있으니.’

사방을 가득 메운 광신도의 물결.

내심 미소를 흘린 도플갱어는 비틀거리며 일어났다.

협곡의 출구를 둘러싸고 치열한 전투가 벌어지는 와중에도, 그가 블링크로 도망쳐 온 후방은 평온했고 수많은 병력들이 남아 있었다.

도플갱어가 제법 공들여 키워 낸 핵심 전력도 함께.

“아미르.”

낮게 깔린 도플갱어의 목소리에 주위를 에워싸고 있던 광신도들이 길을 비켜 주었다.

아미르라 불린 지팡이를 쥔 노인이 다가와 그의 앞에 무릎을 꿇었다.

“기다리고 있었습니다, 위대한 선지자시여.”

경이(驚異)로 가득한 표정과 목소리.

도플갱어는 선지자라는 이름에 걸맞은 위엄 어린 태도로 그를 내려다보았다.

“신께서 나를 다른 곳으로 인도하사, 먼저 이곳을 떠나야겠다. 그대들은 혼신의 힘을 다해 진태경을 비롯한 이교도들을 막아라.”

신. 그리고 선지자라는 이름은 절대적이다.

그러나 아미르는 당혹스러운 표정으로 되물었다.

“진태경을, 말입니까?”

“왜, 그가 두려운가?”

“아닙니다. 하지만…… 이미 선지자께서 놈을 제압하신 게 아닌지요?”

도플갱어가 눈살을 찌푸렸다.

“그게 무슨 말이지? 그대는 보지도 못했을 터인데.”

“예. 그러나 선지자께오서 친히 놈을 제압하여 데려오시지 않았습니까.”

“뭐?”

그 말을 이해하지 못한 도플갱어가 눈을 깜빡인 그 순간.

그의 등 뒤에서 죽은 듯이 엎드려 있던 진태경이 부스스 눈을 떴다.

“어, 시벌. 여긴 또 어디야.”

“……!”
```

## Final English reading copy

```markdown
# Chapter 817

The Doppelganger’s new face was all too familiar to Jin Taekyung.

The only time he’d seen it in person had been when it was shriveled like a mummy, but while investigating Michael Silbert, he’d seen that very face in photographs so many times he was sick of it.

And on top of that…

*Whoooosh.*

That immense magical power, so close he could almost reach out and touch it.

He didn’t need to check the Level window to know the answer.

“Siegfried Bassman?”

At Jin Taekyung’s voice, which came out almost like a mutter to himself, the Doppelganger snapped its fingers instead of answering.

*Crackle.*

A white flash flared.

The faint current flowing along its finger transformed into dozens of bolts of lightning and came crashing down in no more than an instant.

*Zzap!*

Jin Taekyung’s vision filled with blinding light.

His eyes closed before he knew it, but he could still feel it clearly.

The immense electricity transmitted through the rock surrounding him, the air, and the ground. Through everything.

*Boom!*

The ground, made of solid rock and earth, split like a spiderweb.

Jin Taekyung kicked off the ground and shot upward, thrusting out one palm. The heat of Flame Divine Palm blazed toward the lightning, burning it away.

*KABOOOOOM!*

A tremendous boom shook the canyon.

But Jin Taekyung pushed his eyesight to its limits and took in everything that had happened in that brief moment.

The rising flames and acrid smoke.

And even the Doppelganger, which had vanished like a ghost just before it all exploded.

*Blink.*

If Teleport and Warp were long-distance spatial movement magic, Blink was a short-range instant movement spell that made the user disappear in the blink of an eye, just as its name suggested.

That also meant its range was short, while Jin Taekyung’s senses and field of vision covered the entire canyon.

*There.*

He couldn’t see it. But he could feel it.

Jin Taekyung drew in a breath. He trusted his five senses and his abilities.

He stepped on empty air with the tips of his feet, powered by internal energy, and shot toward the Doppelganger beyond the drifting embers and acrid smoke.

*Whoosh! Boom!*

The air burst under the force of his speed. Smoke and embers scattered like an explosion, and his vision cleared.

At the end of the path he’d blazed through like a streak of fire was the Doppelganger, fleeing toward the followers who could help it.

“……!”

A chill prickling its back, the Doppelganger instinctively turned around and widened its eyes.

In a slowed world, Jin Taekyung was already right in front of it, filling its vision.

*How the hell?*

The brief moment had lasted less than a second.

Yet Jin Taekyung had not only figured out where the Blink spell would take it in that instant, he’d also crossed more than ten meters and caught up.

*You’ve got to be fucking kidding me…!*

The Doppelganger swallowed the curse that almost escaped its lips.

No—to be precise, it hadn’t even had time to curse.

If it did, it would lose forever the power of the Grand Mage, an asset far more precious than any of the other lives it had discarded countless times before.

*Shwaa!*

A reddish-hot spearhead tore through the wind. The killing intent, cold in contrast, froze its body in place.

But at least in that moment, the mana and abilities inhabiting the Doppelganger’s body belonged to one of only three Grand Mages in the entire world.

*Blin—k!*

*Fwoosh, boom!*

Flames exploded along the spearhead and devoured the air.

At the same time, the Doppelganger appeared more than ten meters away, a chill running down its spine.

Was it because it had narrowly escaped danger?

No.

It was because of the pair of eyes staring right at it.

*Jin Taekyung.*

Their gazes had only met, but its heart sank. An instinct honed over centuries of struggle whispered to it.

Run.

If it didn’t want that beast to tear out the back of its neck, it couldn’t let its guard down for even a moment.

And the next instant, as the Doppelganger cast Blink again without a moment’s rest, it knew for certain.

Its instincts had been right.

*Whoosh! Slice!*

The Doppelganger opened its eyes in a new space and let out the breath it had been holding.

The back of its armor, which had long since lost its original shape and purpose, had been seared hot by the heat that had grazed past it in an instant.

*He cut me. His speed is catching up to Blink.*

It had been a hair’s breadth.

A shiver ran through it. Of all the humans it had absorbed or encountered in passing, it had never met a monster like that.

Except for the one person it had feared—and deliberately avoided because of that fear.

*Cheon Taemin.*

The savior of humanity.

The only Adversary to face the Demon King Asmodeus with the body and mind of a frail human, a divine man.

The Doppelganger neither denied nor felt ashamed of its fear of Cheon Taemin.

He wasn’t someone it could call “nothing more than human.”

That was why, even after absorbing Siegfried Bassman years ago and learning about Cheon Taemin’s condition, it still hadn’t dared to challenge him.

But even the Doppelganger could never have imagined this.

That it would feel this much fear toward a human other than Cheon Taemin.

*Blink, Blink, Blink!*

If it hesitated even a little, it might face permanent Erasure.

The desperate Doppelganger leaped through space again and again.

Each time its form disappeared as if erased by an eraser, it drew closer to the exit of the canyon, where a fierce battle was underway.

And closer to the hunter pursuing his breathless, fleeing prey.

*Whsssh!*

A sharp whistle split the air.

A dozen or so daggers flashed toward the Doppelganger from every direction. The attack had been predicted so perfectly that it left no room to cast Blink.

Realizing it had no choice, the Doppelganger gritted its teeth and spread both hands.

*Vrrrrm, crack!*

The mana shield shattered before it could even finish forming. The daggers ricocheted off and embedded themselves in the cliffs and ground on either side.

But in the brief moment it had spent blocking them, Jin Taekyung was already right in front of the Doppelganger.

“Got you.”

“……!”

*Crack!*

There was no time to react.

The Doppelganger’s mouth fell open at the tremendous pain shooting through its wrist.

Siegfried Bassman had been a great Grand Mage in life, but Jin Taekyung’s terrifying strength couldn’t be stopped by any magic in his memories.

*Crreeeak!*

“Gyaaaah!”

The scream burst from its lips, unable to bear the awful pain.

Just from Jin Taekyung gripping its hand hard, its flesh and muscles were crushed and its bones shattered.

The Doppelganger’s vision went white for an instant. It saw the sky and the ground tilt.

*I’m turning over. No—I’m going to die.*

The Doppelganger realized it instinctively.

After this terrifying feeling of weightlessness, death awaited: its body crushed as it hit the ground.

*No!*

Siegfried Bassman was the most precious of all the lives it had absorbed.

Hunting an S-rank Hunter known to the world was difficult enough, but a Grand Mage was especially valuable—their ability to use magic was so useful.

*If I lose magic, I’m finished. In that case, I’d rather…!*

The stream of thought brought on by fear was as fast as a flash of light, and its resolve was firm.

*Whoooom!*

The instant it was about to slam into the ground with a fierce rush of air, the Doppelganger summoned every last bit of its strength and drew up its mana.

*Blink!*

*Flash.*

The world slowed.

Space, warped by mana, swallowed the Doppelganger whole. But unlike before, the amount of mana was different, and so was its stability.

The Doppelganger’s gaze was fixed on the battlefield hundreds of meters away, far beyond the limit of the Blink spell.

*I have to do it.*

A taboo that went beyond the limits of spatial magic.

But it was better than dying here. His fanatics, who worshiped him like a god, were there—followers he’d spent decades carefully cultivating.

*Crreeeak!*

Its bones and flesh twisted along with space.

It felt as if an invisible hand were squeezing its heart until it burst, but it didn’t matter.

Jin Taekyung.

If it could escape the hands of this monstrous human right now…

If it could flee under its followers’ protection and carry out the plan it had been preparing for so long…

*Farewell. See you next time.*

The Doppelganger thought this to itself and bared its blood-soaked teeth in a grin.

*Grrk, whoooosh!*

Mana surged like a storm, and warped space swallowed it whole.

At the same time, darkness fell over its vision. New light, noise, and faces swept over it like waves.

*Boom! KABOOOOOM!*

*Shing! Krrrrk!*

“Gah!”

“Warriors of God, do not fear death!”

“Go fuck yourselves, you insane fanatics!”

Booms and screams erupted all around it. Shouts from both sides pounded against its ruptured eardrums.

But what mattered to the Doppelganger was that the faces in its blurry vision belonged to its followers.

“W-wait!”

“Prophet!”

Fanatics in turbans spotted it and surrounded it. The Doppelganger spat out bloody fluid mixed with bits of its entrails, then laughed aloud.

“Cough. Heh-heh…”

Pain?

It was fine. It would recover soon enough.

Bones throughout its body were shattered, and the left arm Jin Taekyung had grabbed had been torn off from the shoulder. But what mattered was that the Blink spell, pushed beyond its limits, had succeeded.

*If I’d been an ordinary human, I’d definitely have died.*

It had been lucky.

It succeeded because Siegfried Bassman was a Grand Mage, and the Doppelganger survived these injuries because it was a Doppelganger.

*Slide. Crack.*

Pale, childlike flesh slowly grew from the stump of its severed arm. The torn muscles reconnected, and pure white bone grew back.

The recovery was incomparably slower than before. The Doppelganger clicked its tongue bitterly.

*Damn it.*

The countless lives it had absorbed were already running low.

By the time it got completely away from here, it might have only enough lives left to count on its fingers.

*But it doesn’t matter. I have things willing to lay down their lives for me.*

A sea of fanatics filled the area around it.

Smiling to itself, the Doppelganger staggered to its feet.

Even as fierce fighting raged around the canyon exit, the rear where it had fled by Blink was peaceful, with a large number of troops still there.

Including the elite forces the Doppelganger had taken considerable care to raise.

“Amir.”

At the Doppelganger’s low voice, the fanatics surrounding it stepped aside.

An old man holding a staff approached and fell to his knees before it.

“I have been waiting for you, great Prophet.”

His face and voice were full of wonder.

The Doppelganger looked down at him with an air of authority worthy of the name Prophet.

“God has led me elsewhere, so I must leave this place first. You will fight with all your might to hold back Jin Taekyung and the other heretics.”

The names God and Prophet were absolute.

But Amir asked again, looking bewildered.

“Jin Taekyung, you say?”

“What, are you afraid of him?”

“No. But… hadn’t you already subdued him, Prophet?”

The Doppelganger frowned.

“What do you mean? You weren’t there to see it.”

“Yes. But you personally subdued him and brought him here.”

“What?”

As the Doppelganger blinked, unable to understand what he meant, Jin Taekyung, who had been lying motionless behind it as if dead, blearily opened his eyes.

“Uh, shit. Where the hell am I now?”

“……!”
```
