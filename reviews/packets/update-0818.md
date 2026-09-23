<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0818.txt",
      "sha256": "438d6b651acd880755cc6e1d32bbfeee41d1cc0443957732f52f1fb4ece0071f",
      "bytes": 13212
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "68bda9ced2978719abe354108e711f6944c1eabf77b6566771900cd3c0038223",
      "bytes": 1573
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "3058a17075f2e26242c2c44256fa9a4f5d86c0de54766ae8d188b23c0ef18a27",
      "bytes": 226002
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "d0c28ccf50dff74806bd5a15b09b7c40b6d445894d24f2f1083ea129c100fecb",
      "bytes": 723
    },
    {
      "path": "characters/Doppelganger.md",
      "sha256": "953544639a944d58102f524fc6c73c4f29b55762fcc34f7b161a17892067f94c",
      "bytes": 761
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "45d642640008e33013b7c0b4b390318cf894ab21e1d394be3f80a75801cd65f5",
      "bytes": 1921
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "0cf6ba26c30f488a649070a118a09a223c747834fc8df0fd62d90d31e0e5f442",
      "bytes": 622
    },
    {
      "path": "characters/Martial God.md",
      "sha256": "fa7bc96ad36466a176832d4df14d179bd8cc0b0a83200a3e837b6d91f0037f46",
      "bytes": 752
    },
    {
      "path": "characters/The Prophet.md",
      "sha256": "cc31f867c267c15c2af1af50a555f0aa03a1c8bc35eeb7a5806148f1bcd69e0a",
      "bytes": 724
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "e1968e5afd1d4d8dd4d9824b7d42e89378711946a958686cc521b426703db0a9",
      "bytes": 249339
    }
  ],
  "estimated_tokens": 10316
}
-->

# Durable State Update — Chapter 818

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
1 and safe_through 818. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 818. Profile updates may replace only one
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
  "chapter": 818,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 818,
    "continuity_sources": [818],
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
    "The Doppelganger escaped to its followers and ordered Amir and the others to hold off Jin and the heretics, but Jin is lying motionless behind it and has just awakened."
  ],
  "continuity_sources": [
    817
  ],
  "open_questions": [
    "Who is the Doppelganger’s master, what is the plan, and why must the target be avoided until it is complete?",
    "What does the Chosen One designation mean?",
    "How did Jin Taekyung reach the Doppelganger’s rear battlefield, and what will happen next?",
    "Is Magic Johnson human?"
  ],
  "safe_through": 817,
  "temporary_decisions": [
    "Keep magical power distinct from mana.",
    "Keep Demon Realm language distinct from other languages.",
    "Keep Blink distinct from Teleport and Warp; extended-range Blink causes severe strain."
  ],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 진태경    | **Jin Taekyung**   |
| 무신     | **Martial God**               | —              |
| 암천     | **Dark Heaven**                  |
| 무인     | **martial artist**                               | Default term                                          |
| 살기     | **killing intent**                               |                                                       |
| 헌터      | **Hunter**            |
| 탱커      | **tank**              |
| 도사      | **Daoist**                                                      |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 도플갱어 | **Doppelganger** | The Prophet’s revealed species. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 선지자 | **The Prophet** | Mysterious religious leader directing the terrorist warriors. |
| 천무지체 | **Heavenly Martial Physique** | Named physique or constitution mentioned hypothetically by Jin Mukyung. |
| 링크 | **Link** | Mental connection between a mage and Familiar |
| 나려타곤 | **Narye tagon** | Humiliating idiom comparing a fighter's evasive roll to a lazy donkey rolling on the ground. |
| 전하 | **His Highness** | Formal royal address for the resident prince; the official insists on this form instead of king. |
| 오우거 | **ogre** | B-rank monster species emerging from the Gate. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 신성 | **Morning Star** | Term in the summons referring to the Master of Morning Star. |
| 근골 | **Muscles and Bones** | System attribute increased by 2 during the climb. |
| 백염 | **White Flame** | Name of Jin Taekyung's newly forged spear. |
| 도도 | **Dodo** | Term for the Star-Array Grand Banquet's major gambling matches. |
| 마도 | **Demonic Path** | Term raised for martial power that appears to defy common principles. |
| 그분 | **that person** | Unidentified figure whom Jihoon reveres and credits with disabling cameras and microphones. |
| 지풍 | **Finger Qi** | Invisible qi attack fired by the Western Heaven Demon Lord. |
| 블링크 | **Blink** | Arch Lich movement spell |
| 의지 | **Will** | System attribute that replaces Endurance after its dramatic increase. |
| 비처 | **secret refuge** | Hidden retreat of the Dongting Fisherman. |
| 마법 | **Magic** | Taekyung's explanation for Dark Heaven's anomalous abilities. |
| 인자 | **ninja** | Japanese assassin skilled in concealment and concealed weapons. |
| 성하 | **Seongha** | Hunter named during the cave battle. |
| 대마도사 | **Grand Mage** | Title used for Magic Johnson. |
| 핫산 | **Hassan** | Subordinate addressed by the unidentified intruder. |
| 무함마드 | **Muhammad** | Prophet whose death is referenced in the history of the Islamic world. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 신의 | 진태경 | physician_to_benefactor | Young Master Jin | formal-polite | The Divine Physician addresses Taekyung as 진 공자 while expressing concern for his injuries. |
| 진태경 | 청년 | celebrated Hunter to younger fellow Hunter | young man | casual, teasing, and profane | Jin addresses the young Hunter after overhearing his criticism and deliberately switches to casual speech. |
| 청년 | 진태경 | frightened junior Hunter to celebrated senior Hunter | you | fearful and deferential | The young Hunter uses 당신 while asking whether Jin is really the person he recognizes from the media. |
| 진태경 | 사령관 | captor to captive undead commander | you | casual, mocking, and dismissive | Taekyung addresses the Skeleton Warlord informally while rejecting its pleas to turn back. |
| 무함마드 | 진태경 | terrorist_leader_to_enemy_Hunter | Jin Taekyung | fearful and deferential | Muhammad names Jin after recognizing him and pleads with him during the confrontation. |
| 진태경 | 무함마드 | enemy_Hunter_to_terrorist_leader | you; apostate bastard | taunting, then cold and condemning | Jin interrogates and denounces Muhammad before forcing him to issue the order. |
| 진태경 | 헌터 | field commander to allied Hunters | you; Hunters | blunt and commanding | Orders the human forces to stop asking questions and kill the fleeing Minotaurs. |
| 진태경 | 선지자 | enemy commander addressed by Jin | The Prophet | blunt and informal | Jin asks where The Prophet is while confronting the Manticore Lord. |
| 진태경 | 도플갱어 | enemy | you; the Doppelganger | blunt and informal | Jin directly challenges the Doppelganger and demands to know what it wants. |

## Listed compact profiles

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 817
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** He is devoted to medicine and the lives he could not save, yet remains composed and self-effacing under mortal danger.
- **Voice:** He speaks in calm, respectful, self-effacing language, framing mortality through quiet philosophical reflections.
- **Relationships:** Mungyeong is the Divine Physician's true identity, and Dong Feng is his Disciple.

### Doppelganger.md

# Doppelganger (도플갱어)

- **Safe through:** Chapter 817
- **Aliases:** The Final Abyss
- **Role:** The last surviving member of its species, the Doppelganger is a powerful being from the Demon Realm that spent decades manipulating events in the human world.
- **Personality:** Arrogant and manipulative, it treats others as tools and is willing to sacrifice its followers to escape, but becomes desperate when its own survival is threatened.
- **Voice:** Not established
- **Relationships:** It served an unnamed master who sent it to this world and ordered it to avoid the target until the master’s plan was complete; it regarded Michael Silbert as a subordinate and disposable tool.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 817
- **Aliases:** Blazing Flame Divine Dragon; Apostle of the Earth Mother Goddess; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan, Jeok Cheongang’s Disciple, the Fire Gate Clan’s nineteenth successor, Pavilion Master of the Fire Dragon Pavilion, a Supreme Peak master and publicly recognized S-rank-level Hunter with an A-rank license, a traveler between Murim and another world, and the World Hunter Federation’s Alliance Leader.
- **Personality:** Hungry, self-aware, dryly observant, pragmatic under pressure, and willing to risk himself for people he has accepted as real; treats impossible situations like games until their human cost becomes undeniable.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, Jeok Cheongang is his Master, Mungyeong was his recent instructor, Cheongpung is his trusted companion and only true martial rival, Choi Minwoo is his subordinate and trusted manager of media and official arrangements as well as the Peace Guild's Guild Master, Ju Hwaran is a trusted Fire Dragon Pavilion member who followed him to Nanman, Magic Johnson is an allied Grand Mage who supplies him with intelligence, Chuck Hagel is an American operative allied with him in the covert anti-terror campaign, his mother and sister Hayeon are among those he protects, the Skeleton King is his friend and ally, Xiao Shen regards him as an older brother after Jin saved him, and Jin-ho is his older friend and trusted confidant.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 817
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Martial God.md

# Martial God (무신)

- **Safe through:** Chapter 730
- **Aliases:** None
- **Role:** An unidentified legendary martial artist regarded as a pinnacle above the Ten Kings; more than fifty years ago, he defeated five Supreme Peak fiends and five hundred Blood Ghost Squad members alone.
- **Personality:** Not established.
- **Voice:** Not established.
- **Relationships:** He met the Beast Miao King twice more than fifty years ago, appearing first as a white-bearded elder and later as a young boy; Mae Jonghak received several teachings from him, while his identity, whereabouts, and possible connection to Cheon Taemin remain unknown.

### The Prophet.md

# The Prophet (선지자)

- **Safe through:** Chapter 817
- **Aliases:** Muninn (무닌)
- **Role:** The Prophet is a Level 170 Doppelganger titled “The Final Abyss,” who concealed itself for decades as Muninn.
- **Personality:** Religiously fervent, commanding, and shrouded in an intentionally indistinct identity.
- **Voice:** Mysterious, genderless, and age-indeterminate, speaking in solemn religious imperatives.
- **Relationships:** The Prophet commands the ten warriors and is revered by its followers; it made a pact with Michael Silbert during the 2020 Battle of Paris, where Michael killed the surviving humans in exchange for being spared.

## Korean source

```text
＃818화



“어, 시벌. 여긴 또 어디야.”

“……!”

진태경의 목소리가 귓가에 닿은 그 순간. 석상처럼 굳어 버린 도플갱어의 뇌리에 두 가지 의문이 떠올랐다.

‘저놈이 왜 여기에 있지?’

마법은 오롯이 시전자의 의지에 따라 발현된다.

그리고 당연하게도, 도플갱어는 자신에 한하여 블링크 마법을 사용했다.

정신이 서른다섯 바퀴쯤 돌아 버린 중증 사이코패스라 하더라도, 눈 깜짝할 사이에 자신의 목뼈를 서른여섯 번쯤 부러뜨릴 수 있는 진태경과 함께 위험천만한 이동 마법을 시전하는 미친 짓은 하지 않을 테니까.

결국 답은 하나뿐이었다.

‘내 의지와는 상관없이…… 놈이 블링크 마법에 끼어들었다.’

마나 간섭.

지크프리트 바스만이라는 이름을 가진, 학구파 대마도사가 긴 연구 끝에 완성한 이론이 흡수한 기억들 사이로 떠오른다.

도플갱어는 전신에 엄습하는 한기를 느꼈다. 비틀비틀 몸을 일으키는 진태경을 바라보는 그의 눈동자에는 아직 해결되지 않은 두 번째 의문이 서려 있었다.

‘도대체 어떻게, 어떻게 살아남은 거지?’

워낙 괴물 같은 놈이니 마나 간섭이야 그렇다고 치자.

말도 안 되지만, 정말 말도 안 되는 일이지만 근접 헌터 주제에 대마도사마저 뛰어넘는 마나 통제력을 지녔을 수도 있으니까.

그러나 조금 전의 블링크 마법은 지극히 비상식적이며 위험한 시도였다.

금기(禁忌)를 범한 대가로 도플갱어마저 전신이 분해될 뻔했고, 신체 회복을 위해 수십의 생명을 제물로 바쳐야 했으니 더 말해 봐야 입만 아플 지경이다.

그런데…….

“어우, 몸 저려.”

진태경의 중얼거림을 들은 도플갱어는 순간 정신이 혼미해졌다.

‘저려? 저리다고?’

말도 안 되는 일이다.

설령 진태경이 오우거라도 해도 양심상 팔다리 한두 개 정도는 잃었어야 하는 거 아닌가 하는 배신감마저 들었다.

‘몸이 강철로 이루어진 것도 아닐 텐데. 어째서?’

도플갱어는 꿈에도 몰랐다. 이미 오래전 무림에서 천무지체(天武肢體)라고까지 불린 진태경의 근골이, 금기를 범한 블링크 마법에도 부서지지 않을 만큼 한계를 뛰어넘었다는 사실을.

다만 그런 사정을 모르는 도플갱어조차 한 가지 진실쯤은 어렵지 않게 깨달을 수 있었다.

‘지금의 진태경은, 그 어느 때보다 약해져 있다.’

거대한 충격이 불러온 생각은 길고도 복잡했으나, 그 충격이 휩쓸고 지나간 시간은 찰나에 불과했다.

고작 수 초 남짓.

그리고 주위를 짓누르고 있던 그 숨 막히는 정적 끝에, 비명처럼 울려 퍼진 도플갱어의 외침이 있었다.

“놈을 막아!”

“……!”

“……!”

산산이 부서지는 정적.

동시에 순간 멈춰 있던 세상이, 느리게 흐르던 시간 속에서 멍하니 진태경과 자신들의 위대한 선지자를 번갈아 바라보던 광신도들이 움직였다.

“인샬라!”

“신은 위대하시다!”

쉬쉭, 쐐애애액!

사방에서 울려 퍼지는 함성과 파공성.

그리고 자신을 향해 빗발치는 무수한 섬광을 바라보며, 진태경은 문득 입을 열었다.

아니, 쏟아냈다.

“우욱. 쿠웨에에엑!”

핏물보다 먼저 흩뿌려지는 토사물.

블링크 마법에 무임승차한 대가는 지독한 멀미였다.



* * *



참으려고 했다. 참을 수 있다고 생각했다.

하지만 삶이라는 게, 마음처럼 되지만은 않더라.

“우웨에에엑!”

아니, 시발. 멋있게 한마디 하려고 했는데.

목소리 대신 튀어나온 토사물이 촤르륵 쏟아진다. 굼벵이처럼 허리를 굽힌 나는 황급히 땅바닥을 굴렀다.

서걱! 피피핏!

서늘하다. 예리한 날붙이가 머리카락을 한 움큼이나 잘려 나가는 것이 느껴진다.

사방에서 날아든 오러가 전신 곳곳을 스치듯 지나가자 화끈한 통증이 일었다.

‘여기까지 와서 나려타곤(懶驢打滾)이라니.’

눈물이 앞을 가린다. 그나마 불행 중 다행인 건, 저 광신도들 역시 이런 상황을 예상치 못했다는 것이다.

‘……예상하는 게 더 이상하지.’

어느 미친놈이 적들 한가운데에 떨어져서 구토부터 하겠나. 울렁거리는 속을 애써 가라앉힌 나는 손에 든 것을 휘둘렀다.

뻑!

둔탁한 타격음과 함께 살점과 핏물이 튀었다.

블링크 마법의 여파로 뜯겨 나간 선지자의 팔은 훌륭한 둔기였다.

“오, 파워 어택.”

“놈! 감히 그분의 성스러운 육신을……!”

“그럼 정정. 홀리 어택.”

퍽, 퍽, 퍼억!

가장 가까이 있던 세 명의 광신도들이 도미노처럼 쓰러졌다.

망가진 팔을 도끼처럼 집어 던진 나는, 사방을 빽빽하게 메운 적들의 중심에서 진각(震脚)을 밟았다.

쿠웅!

거대한 울림을 담은 충격파와 함께 반경 수 미터의 지면이 움푹 꺼진다.

순간 중심을 잃은 광신도들이 신형이 휘청거리고, 그런 주인을 따라 방향을 잃은 무기들이 전신을 스쳐 지나갔다.

쉭! 피핏!

날붙이에 실린 오러와 풍압(風壓)이 미세하게 피부를 가르는 것이 느껴진다.

그것만으로도 놈들이 어느 정도의 수준에 도달한 실력자라는 사실을 알 수 있었다.

‘절반 이상이 B급. 혹은 그 이상.’

그렇게 파악된 머릿수만 무려 수백이다.

아무도 찾지 못하는 황량한 사막 어딘가에서 도플갱어가 육성해 낸 추종자들은, 불과 백여 미터 밖에서 치열한 전투를 치르고 있는 세계 헌터 연맹의 정예들과 비교해도 별다른 손색이 없을 정도였다.

‘미친 새끼. 아니, 미친 새끼들.’

도플갱어도, 놈을 따르는 이 역겨운 놈들도 전부 한 똥통 속의 똥이다.

나는 솟구치는 욕설을 삼키며 양손을 뻗었다.

탱커 포지션으로 짐작되는 광신도들이 마법이 부여된 둥그런 방패를 들어 전방을 가로막았지만, 그보다 한발 앞서 쏘아진 열 줄기의 지풍(指風)을 막기에는 역부족이었다.

슈확! 투두두둑!

바람이 불고, 열 명의 광신도가 갈댓잎처럼 스러진다.

그리고 순간 드러난 공백 사이로 잠시 시야에서 사라졌던 한 존재의 뒷모습이 언뜻 내비쳤다.

‘거기 있었나.’

아주 짧은 순간이었지만, 똑똑히 보았고 짐작했다.

놈은 지금 전장을 이탈하고 있었다.

자신이 육성해 낸 수많은 추종자를 미끼 삼아. 그들의 피를 융단처럼 밟으며 내 손이 닿지 않을 곳으로 도망치고 있었다.

지금껏 그래 왔듯이. 그리고…….

‘앞으로도 마찬가지겠지.’

이미 너무 많은 희생을 치렀다.

놈이 삼십 년이 넘는 세월 동안 쌓아 올린 계획이 무엇인지는 아직 모르지만, 오늘 이 자리에서 내가 직접 그 계획을 무너트려야 한다.

그러지 못한다면 내 세상이, 사람들이 무너지고 말 테니까.

“더 이상 갈 수 없……!”

콰득. 푸푸푹!

앞을 가로막았던 광신도의 목을 부러트림과 동시에 전방에서 날아든 화살을 막았다.

마나를 머금은 화살촉은 시신을 관통하고 내 뺨을 스쳐 지나간 뒤, 때마침 근처에 있던 광신도 하나의 눈에 틀어박혔다.

“끄아아아악!”

뿜어지는 핏물과 함께 고통에 찬 비명이 울려 퍼진다.

그러나 그 비명은 얼마 지나지 않아 씻은 듯이 사그라들었다.

서늘한 절삭음과 함께.

서걱.

광신도의 목을 가로지르는 붉은 선과 함께. 죽음을 알리는 무거운 목소리가 울려 퍼졌다.

“핫산. 용감한 신의 전사여. 먼 훗날, 하늘의 왕국에서 다시 만나자.”

툭.

비명이 멎었다. 목이 떨어졌다.

허수아비처럼 풀썩 쓰러지는 시신은 두 번 다시 움직이지 않았고, 잘려 나간 목의 단면에서는 그제야 희미한 핏물이 몽글몽글 맺히기 시작했다.

‘이건.’

지금껏 수많은 강자를 마주한 나조차도 놀라움을 느낄 수밖에 없는 솜씨.

문득 움직임을 멈춘 나는 크게 뜨인 눈으로 목소리의 주인을 바라봤다.

사방을 촘촘히 포위한 광신도들 사이로, 건장한 체격의 노인이 철탑처럼 우뚝 선 채 나를 바라보고 있었다.

“이렇게 마주하는 것은 처음이군, 진태경. 사악한 이교도들의 왕이여.”

머리카락 한 올도 흘러내리지 않게 꼼꼼히 싸맨 터번. 곧은 허리와 깊게 가라앉은 눈빛.

처음 이 장소에서 눈을 떴을 때부터 느꼈지만, 노인은 엄청난 강자였다.

현대에서 헌터라는 명칭으로 통용되는 일반적인 각성자가 아닌, 무인(武人) 그 자체로서도.

동시에 나는 본능적으로 알아차렸다.

도플갱어가 광신도들이 떠받드는 신성불가침의 상징이라면, 저 노인이야말로 실질적인 총사령관이자 전력의 핵심이라는 것을.

“야흐야 무함마드 아흐마드 베두인…… 이거 맞나? 이름 한번 존나게 기네.”

머리 위에 둥둥 떠 있는 홀로그램 창의 정보를 읽자, 노인의 눈이 놀라움으로 물들었다.

“내 이름을 어떻게 알았지?”

“신이 알려 줬다. 이 정신 나간 늙은이야.”

“헛소리. 신께서 사악한 이교도의 왕에게 그런 것을 알려 주실 리 없지.”

“헛소리는 지금 당신이 지껄이는 게 헛소리지. 나는 무신론자라 이교도도 아니고, 왕은 더더욱 아니거든.”

“삿된 혓바닥으로 위대한 신의 존재를 부정하지 마라. 악마야.”

“어르신, 약 드실 시간이에요.”

스륵. 툭.

어깨에서 흘러내린 로브가 지면을 덮었다.

한 손에는 구불구불한 지팡이를, 또 다른 한 손에는 무림에서 곡도(曲刀)라 불릴 법한 시미터를 든 노인이 걸음을 내딛자, 주위의 공기가 차갑게 가라앉으며 나를 둘러싸고 있던 포위망이 좁혀졌다.

저벅. 스아아아아.

사방에서 날아드는 살기(殺氣)에 전신이 따끔거린다.

눈앞의 노인뿐만 아니라 온통 검은색 로브와 터번으로 휘감은 삼십여 명의 흑의인이 광신도들 사이 곳곳에 자리 잡은 것이 보였다.

‘저놈들이 진짜다.’

한 놈, 한 놈이 전 세계 어디에 내놔도 손색이 없는 실력자들이다.

더불어 같은 인간을 죽인다는 것에 익숙치 않은 헌터들과는 달리, 지금 이 순간 놈들에게서 머뭇거림 따위는 찾아볼 수 없었다.

‘숙련된 살인자들.’

저들의 모습 위로 암천(暗天)에 속한 무림인들이 겹쳐 보이는 것은 단순한 착각이 아닐지도 모른다.

놈들은 지독하리만치 서로를 닮아 있었다.

한 존재에게 맹목적인 충성과 믿음을 바친다는 점에서 그랬고, 이를 위해서 어떤 끔찍한 일이라도 저지를 수 있다는 점에서 더더욱 그랬다.

그리고…….

‘나는 그런 놈들을 수없이 죽여 왔지.’

세상에는 죽여 없애야 할 놈들이 너무 많았다. 그뿐이다.

내심으로는 이 세상에 신이라 불리는 절대자가 있으리라는 사실을 막연히 짐작하고는 있지만, 그를 믿거나 충성하지는 않는다.

고난 속에서 무언가를 이루어 내는 것은 결국 인간이었으니까.

다른 수많은 이들이 그러했듯이, 나 역시 그렇게 살아남았으니까.

하지만 만약 일 년 전 갑작스럽게 직장에서 잘린 누군가에게, 당장 이번 달을 걱정하며 높은 골목길을 오르는 어느 청년에게 고물 캡슐을 슬쩍 던져 준 것이 신이라면…… 그래, 그렇다면 좀 믿어 볼 의향이 있다.

“그럼 너희가 내 손에 죽는 것도, 전부 신의 뜻이 되겠지.”

낮은 뇌까림과 함께 허공을 그러쥐었다. 공기와 먼지를 제외하고는 아무것도 없던 그곳에서, 잠시 내 곁을 떠나가 있던 한 자루의 창이 붙잡힌다.

마법으로도 설명되지 않는 광경을 목격한 노인의 미간에 완고한 주름살이 잡혔다.

“악마. 너는 실로 악마로구나.”

나는 눈앞의 노인에게, 그리고 사방을 둘러싼 다른 광신도들에게 말해 주고 싶었다.

진짜 악마는 너희를 두고 도망치고 있다고. 선지자라 부르는 그 괴물이 새로운 재앙을 향해 달려가고 있다고.

하지만 나는 대답 대신 발을 뻗었다. 바람을 터트리고, 공간을 지우며 쇄도했다.

후욱.

뜨거운 열풍(熱風)이 어둠을 지워 낸다. 백염의 창날이 누구도 막을 수 없는 궤적을 그려 냈다.

서걱, 콰드드드득!

짙은 피 안개가 자욱하게 내리깔렸다.
```

## Final English reading copy

```markdown
# Chapter 818

“Uh, shit. Where the hell am I now?”

“……!”

The moment Jin Taekyung’s voice reached the Doppelganger’s ears, two questions surfaced in its mind, frozen like a statue.

*Why is he here?*

Magic manifested solely according to the caster’s will.

And, naturally, the Doppelganger had used Blink only on itself.

Even a full-blown psychopath with a mind that had spun around thirty-five times wouldn’t do something insane like cast a dangerous movement spell alongside Jin Taekyung—a man who could break the Doppelganger’s neck thirty-six times in the blink of an eye.

In the end, there was only one answer.

*Regardless of my will… he interfered with the Blink spell.*

Mana interference.

A theory completed after years of research by the scholarly Grand Mage named Siegfried Bassman surfaced among the memories it had absorbed.

The Doppelganger felt a chill sweep through its entire body. As it watched Jin Taekyung stagger to his feet, a second unanswered question lingered in its eyes.

*How? How did he survive?*

It could accept the mana interference. The man was a monster, after all.

It was absurd—utterly absurd—but perhaps this close-combat Hunter really did have mana control that surpassed even a Grand Mage’s.

But the Blink spell just now had been an utterly irrational and dangerous attempt.

The Doppelganger had nearly been torn apart for breaking the taboo, and it had to sacrifice dozens of lives to heal its body. There was no point saying more.

And yet…

“Ugh, my body’s all numb.”

Hearing Jin Taekyung mumble, the Doppelganger’s mind went hazy for a moment.

*Numb? He’s numb?*

That made no sense.

It felt betrayed. Even if Jin Taekyung were an ogre, shouldn’t he at least have lost an arm or a leg or two, out of basic decency?

*His body isn’t made of steel. So how?*

The Doppelganger had no idea that Jin Taekyung’s physique—once called the Heavenly Martial Physique in Murim—had long since surpassed its limits, enough to withstand even a Blink spell that broke the taboo.

Still, even without knowing the circumstances, the Doppelganger could easily grasp one truth.

*Jin Taekyung is weaker now than he’s ever been.*

The thoughts brought on by that immense shock were long and complicated, but the time swept away by it lasted no more than an instant.

Just a few seconds.

And at the end of the suffocating silence pressing down on everything came the Doppelganger’s shout, ringing out like a scream.

“Stop him!”

“……!”

“……!”

The silence shattered.

At the same time, the world that had momentarily stopped began moving again. The fanatics, who had been staring blankly back and forth between Jin Taekyung and their great Prophet in that slowed-down moment, sprang into action.

“Inshallah!”

“God is great!”

*Whoosh! Fwoooooosh!*

Shouts and the sharp whistle of incoming attacks rang out from every direction.

Looking at the countless flashes hurtling toward him, Jin Taekyung suddenly opened his mouth.

No—he let it all out.

“Ugh. Bwaaaaaagh!”

His vomit scattered before a drop of blood could.

The price of hitching a ride on the Blink spell was a hellish bout of motion sickness.

* * *

I tried to hold it in. I thought I could.

But life doesn’t always go the way you want.

“Bwaaaagh!”

Goddammit. I’d been about to say something cool.

Instead, vomit came pouring out of my mouth, splattering in a rush. Bent over like a grub, I hurriedly rolled across the ground.

*Slice! Spurt!*

A chill. I felt a sharp blade cut off a whole handful of my hair.

As the auras flying in from all sides grazed my body, stinging pain flared across my skin.

*After coming all this way, I have to roll around like a lazy donkey?*

Tears blurred my vision. The one small mercy was that those fanatics hadn’t expected this either.

*…It’d be weirder if they had.*

What kind of lunatic lands in the middle of a crowd of enemies and starts vomiting? I forced my churning stomach to settle and swung the thing in my hand.

*Thwack!*

Flesh and blood flew with a dull impact.

The Prophet’s arm, torn off in the aftermath of the Blink spell, made an excellent club.

“Oh, power attack.”

“You bastard! How dare you profane His sacred flesh—”

“Then let me rephrase. Holy attack.”

*Wham! Wham! Wham!*

The three fanatics nearest me fell like dominoes.

I hurled the ruined arm like an axe, then stamped down with a stomp in the middle of the enemies packed tightly around me.

*Thud!*

A shock wave packed with a tremendous rumble plunged the ground several meters around me.

The fanatics lost their footing and staggered. Their weapons, thrown off course along with their owners, whistled past my body.

*Whoosh! Spurt!*

I felt the aura and wind pressure carried by the blades graze my skin, leaving tiny cuts.

That alone told me they were skilled fighters.

*More than half are B-rank or higher.*

I’d counted hundreds of them.

The followers the Doppelganger had raised somewhere in a desolate desert no one could find were every bit as capable as the elite forces of the World Hunter Federation, fighting a fierce battle just a hundred meters away.

*Crazy bastard. No—crazy bastards.*

The Doppelganger and these disgusting followers of its were all shit from the same cesspit.

I swallowed the curses rising in me and stretched out both hands.

The fanatics who looked like tanks raised round, enchanted shields to block the way. But they were too late to stop the ten Finger Qi attacks I fired.

*Fwoosh! Thud-thud-thud!*

A gust of wind swept through, and ten fanatics fell like reed leaves.

Through the opening that appeared for an instant, I caught a glimpse of the back of someone who had disappeared from view.

*There you are.*

It was only for the briefest moment, but I saw it clearly and put the pieces together.

The bastard was leaving the battlefield.

Using the countless followers it had raised as bait. Stepping across their blood like a carpet as it fled somewhere beyond my reach.

Just as it always had. And…

*It’ll keep doing the same thing from now on.*

Too many people had already died.

I still didn’t know what plan the bastard had spent more than thirty years building, but I had to bring it down with my own hands here today.

If I didn’t, my world—and the people in it—would fall apart.

“You won’t get past—!”

*Crack. Thud-thud!*

I broke the neck of the fanatic blocking my way and used his body to block an arrow flying in from ahead.

The mana-infused arrowhead pierced the corpse, grazed my cheek, then lodged in the eye of a fanatic who happened to be nearby.

“Gyaaaaaah!”

A cry of pain rang out amid the spray of blood.

But the scream faded away as if washed clean, before long.

With a cold slicing sound.

*Slice.*

A red line crossed the fanatic’s neck. A heavy voice, announcing his death, rang out.

“Hassan. Brave warrior of God. We shall meet again in the Kingdom of Heaven, far in the future.”

*Thud.*

The screaming stopped. His head fell.

The body crumpled like a scarecrow and never moved again. Only then did faint beads of blood begin to well along the cut surface of the severed neck.

*This is…*

Even I, who had faced countless powerful fighters, couldn’t help being astonished by the skill.

I came to a stop and looked at the speaker, eyes wide.

Among the fanatics surrounding us on every side, a sturdy old man stood tall as an iron tower, looking at me.

“This is the first time we’ve met face to face, Jin Taekyung, king of the wicked heretics.”

A turban was wrapped tightly around his head, not a single strand of hair showing. His back was straight, his gaze deep and still.

I’d felt it ever since I first opened my eyes in this place: the old man was immensely powerful.

Not just as an Awakened one of the kind known in the modern world as a Hunter, but as a martial artist in his own right.

At the same time, I realized instinctively:

If the Doppelganger was the inviolable symbol of divinity, revered by the fanatics, then this old man was the real commander-in-chief—and the core of their fighting force.

“Yahya Muhammad Ahmad Bedouin… Is that right? That’s one hell of a long name.”

As I read aloud the information in the holographic window floating above his head, the old man’s eyes widened in surprise.

“How do you know my name?”

“God told me, you crazy old bastard.”

“Lies. God would never tell something like that to the king of the wicked heretics.”

“You’re the one talking nonsense. I’m an atheist, so I’m not a heretic—and I’m definitely not a king.”

“Do not deny the existence of the great God with your vile tongue, demon.”

“Come on, sir. It’s time to take your pills.”

*Slide. Thump.*

His robe slipped from his shoulder and spread over the ground.

The old man held a crooked staff in one hand and a scimitar—in Murim, you might call it a curved saber—in the other. As he stepped forward, the air around us turned cold and the circle closing in around me tightened.

*Step. Sssssss.*

Killing intent from every direction made my whole body prickle.

It wasn’t just the old man in front of me. I could see more than thirty men in black, wrapped head to toe in black robes and turbans, scattered among the fanatics.

*Those are the real deal.*

Every last one of them was a skilled fighter who could hold their own anywhere in the world.

And unlike Hunters, who weren’t used to killing other people, they showed not a hint of hesitation.

*Seasoned killers.*

It might not have been a mere trick of the eye that made the black-clad men overlap with the martial artists of Dark Heaven in my mind.

They resembled each other to a disturbing degree.

They were alike in their blind loyalty and faith in one being, and even more so in their willingness to do any terrible thing for that being.

And…

*I’ve killed countless people like them.*

There were too many people in the world who deserved to be killed. That was all.

Deep down, I had a vague sense that an absolute being called God might exist in this world. But I didn’t believe in him or pledge my loyalty to him.

In the end, it was people who achieved things in the face of hardship.

I’d survived that way, just like countless others.

But if that god was the one who’d slipped a beat-up capsule to someone who’d suddenly lost his job a year ago—to a young man climbing a steep alley, worried about how he’d get through this month… Well, in that case, I might be willing to believe in him a little.

“Then your deaths at my hands will be God’s will, too.”

With a low mutter, I grabbed at the empty air. In that place where there had been nothing but air and dust, I caught a spear that had been away from my side for a while.

A stubborn crease formed between the old man’s brows as he witnessed something magic couldn’t explain.

“Demon. You truly are a demon.”

I wanted to tell the old man in front of me, and the fanatics all around us, that the real demon was running away and leaving them behind. That the monster they called a prophet was racing toward a new catastrophe.

But instead of answering, I stepped forward. The wind burst and space vanished as I charged.

*Whoosh.*

A wave of scorching heat swept away the darkness. The White Flame spearhead traced a path no one could block.

*Slice—KRRRUNCH!*

A thick mist of blood settled over everything.
```
