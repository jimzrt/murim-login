<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0734.txt",
      "sha256": "131aa981ab748b6f793e51c84027f66261ae5744433e71e815a9659567b4247a",
      "bytes": 13333
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "ebed001ffa2124f189139c9ecfd2bf7ff7e9a501c6da4004c48758fb5c1e4701",
      "bytes": 1671
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "512c3eb86a30b2732283b9b079cbc5ece7e368eef1217282288ee834c71ac05c",
      "bytes": 211104
    },
    {
      "path": "characters/Cheon Taemin.md",
      "sha256": "6260b96775e46122f01ee65e12352be84bb77981b45435f34d1ec74b6ad84f35",
      "bytes": 752
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "8ecd425c88da3e4a31b3b6078d004868704f2d2875b347095402b87f2dc1306e",
      "bytes": 553
    },
    {
      "path": "characters/Felix.md",
      "sha256": "bcc1977fdf449dd7871b3182ff8f38dfc6f7f3be0a534dd67092c119c6dd8033",
      "bytes": 464
    },
    {
      "path": "characters/Go Jun.md",
      "sha256": "1910dae7ff668b91c0f4a5ddcb117934fd2cffda69e72e015873bcc8429f97d5",
      "bytes": 817
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "34a26c7df110fd8444b3038b1872b4af82acd47e8f38954756088db2b3a9adb6",
      "bytes": 2011
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "a066d006a3ea88ea061bc79e18888fe5c4ece3ecf9c0e7007fbf2b7d30d5a6d7",
      "bytes": 622
    },
    {
      "path": "characters/Lee Jungryong.md",
      "sha256": "14cbcce6f50a4363cbf7675454b04ed52e59017d10452bc7c39d185d4e06f40f",
      "bytes": 1384
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "751959807df812ba42382efc8b6b374fe7d66e42a50b5d4339721cc99c434517",
      "bytes": 223842
    }
  ],
  "estimated_tokens": 11179
}
-->

# Durable State Update — Chapter 734

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 734. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 734. Profile updates may replace only one
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
  "chapter": 734,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 734,
    "continuity_sources": [734],
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
    "Jin Taekyung, his family, Team Leader Choi, and the Skeleton King are staying at Cheon Taemin's heavily protected mansion.",
    "The public still knows the mansion as Cheon Taemin's residence, and its symbolic importance and security exceed that of the Blue House.",
    "Wu Shaiming was a former Chinese premier, a Politburo Standing Committee member, and leader of the Crown Prince Party before his imprisonment.",
    "Wu Shaiming and more than fifty Wu family members, including children, were killed simultaneously while in custody.",
    "Xiao Yang sought the Wu family's Mana Cultivation Method, which had made Wu Heixing an S-rank Hunter.",
    "Jin and Team Leader Choi believe Odin Guild most likely caused the Wu family's extermination to prevent the method's transfer or answer the previous night's events.",
    "Jin intends to go to Paris with Team Leader Choi to confront Odin Guild's master."
  ],
  "continuity_sources": [
    733
  ],
  "open_questions": [
    "Who is Odin Guild's master?",
    "Did Odin Guild destroy the Wu family to prevent the Mana Cultivation Method from being transferred, to retaliate for the previous night's events, or both?",
    "How did Odin Guild learn about the Wu family's Mana Cultivation Method and Xiao Yang's attempt to obtain it?",
    "What consequences will follow from the Wu family's extermination and Jin's planned visit to Odin Guild?"
  ],
  "safe_through": 733,
  "temporary_decisions": [
    "Render 우 쉐이밍 as Wu Shaiming.",
    "Render 우 헤이싱 as Wu Heixing.",
    "Render 멸문지화 as “the annihilation of an entire household.”"
  ],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 진태경    | **Jin Taekyung**   |
| 천태민    | **Cheon Taemin**  |
| 이정룡    | **Lee Jungryong** |
| 깨달음    | **enlightenment** / **insight**                  | Martial enlightenment                                 |
| 헌터      | **Hunter**            |
| 몬스터     | **monster**           |
| 길드      | **Guild**             |
| 길드장     | **Guild Master**      |
| 팀장      | **Team Leader**       |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 필릭스 | **Felix** | British prince and S-rank Hunter. |
| 고준 | **Go Jun** | Personal name of Team Leader Seok; Lee Jungryong's prized Disciple. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 아레스 | **Ares Guild** | The leading Guild in Korea; formerly employed Team Leader Choi and Song Song. |
| 환각 | **Hallucination** | System effect that the Matador’s Shield can activate against bovine-type monsters. |
| 성주 | **City Lord** | Official who sends the invitation for a gathering with young prodigies. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 마도 | **Demonic Path** | Term raised for martial power that appears to defy common principles. |
| 석고준 | **Go Jun** | Source full-name form for the established Go Jun, also known as Team Leader Seok. |
| 스켈레톤 | **Skeleton** | Undead monster species. |
| 존슨 | **Johnson** | Co-host of the American talk show that replays Taekyung's viral interview. |
| 영국 | **United Kingdom** | Country associated with BCC. |
| 중국 | **China** | Country from which Team Leader Choi’s video originates. |
| 리치 | **Lich** | Named Monster; fallen archmage and apex undead monster. |
| 쓰촨성 | **Sichuan Province** | Source spelling variant of the established Sichuan location. |
| 대통령 | **President** | Title for Korea's head of state. |
| 주석 | **Chairman** | Political title used for Xiao Yang. |
| 청두 | **Chengdu** | Administrative capital of Sichuan Province and destination airport city. |
| 종석 | **Jongseok** | The elder whom Jin jokingly calls Grandpa Jongseok. |
| 쓰촨 | **Sichuan** | Variant spelling used for the region associated with the pattern Jin recognizes. |
| 정룡 | **Jungryong** | Cheon Taemin's trusted associate who joined the Peace Guild. |
| 인터폴 | **Interpol** | International organization issuing wanted notices for the fleeing security-team members. |
| 오딘 | **Odin** | The name of the world's greatest Guild, invoking the Norse god. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 이정룡 | 진태경 | senior S-rank Hunter to younger Hunter and adversary | Young man | polished, teasing, and veiled-threatening | Uses a genial tone and indirect threats while trying to make Taekyung release the captives. |
| 진태경 | 이정룡 | younger Hunter to senior S-rank Hunter and adversary | you | polite but mocking and defiant | Taekyung answers Lee's soft threats with the wolf-and-tiger metaphor and refuses to yield. |
| 이정룡 | 고준 | Master to Disciple | Go Jun | familiar and testing | Lee switches from Seok's office title to his personal name while considering whether he can defeat Taekyung. |
| 고준 | 이정룡 | Disciple to Master | Master | deferential | Go Jun responds to Lee's personal-name address as 스승님. |
| 이정룡 | 천태민 | younger_to_older_brother_by_choice | older brother | reverent and familiar; internal | Lee Jungryong uses 형님 in unspoken thoughts and regards Cheon Taemin as an older brother despite having no blood relation. |
| 진태경 | 석고준 | returning Hunter to hostile Ares security leader | you fucking bastard | hostile and profane | Taekyung directs his final insults and challenge at Go Jun after returning alive. |
| 석고준 | 진태경 | hostile_opponents | brat | hostile and overconfident | Go Jun addresses Taekyung internally as 애송아 while launching his full-strength attack. |
| 신의 | 진태경 | physician_to_benefactor | Young Master Jin | formal-polite | The Divine Physician addresses Taekyung as 진 공자 while expressing concern for his injuries. |
| 필릭스 | 이정룡 | British prince to senior S-rank Hunter | Jungryong Lee | formal through a translation device | Felix permits Lee to omit His Highness and gives his own preferred form of address. |
| 진태경 | 필릭스 | Korean S-rank Hunter addressing a British prince | His Highness | mock-formal and sarcastic | Felix demands formal address, and Jin complies by calling him His Highness while continuing to mock him. |
| 필릭스 | 진태경 | British prince and S-rank Hunter to allied Korean S-rank Hunter | Jin | lofty and aristocratic | Felix addresses Jin while discussing royal duty and their teleport. |
| 진태경 | 존슨 | Allied Hunter to Grand Mage | Johnson | polite and familiar | Jin repeatedly addresses Magic Johnson directly while requesting explanations and permission to visit the site. |
| 고준 | 진태경 | Ares Guild combatant confronting the killer of his Master | you | hostile and informal | Go Jun uses 너 while demanding Jin confess to Lee Jungryong's death and threatening retaliation. |
| 진태경 | 고준 | dominant adversary confronting Lee Jungryong's Disciple | you | contemptuous and informal | Jin uses 너 and 놈 while overpowering Go Jun and ordering him to end the conflict with Lee Jungryong. |
| 진태경 | 대통령 | Hunter_to_President | Mr. President | formal-polite | Taekyung addresses the President respectfully during their airport greeting. |
| 대통령 | 진태경 | President_to_Hunter | Mr. Jin Taekyung | formal-polite | The President addresses Taekyung by name at the airport photo line. |

## Listed compact profiles

### Cheon Taemin.md

# Cheon Taemin (천태민)

- **Safe through:** Chapter 733
- **Aliases:** Slayer; Sky (the American epithet used for him)
- **Role:** Cheon Taemin is Ares Guild Master and the world's greatest Hunter, known as the Slayer for killing the Demon King and creating the first Mana Cultivation Method during the Great Cataclysm, and he remains unconscious after more than twenty years in a wired mechanical capsule at his former mansion.
- **Personality:** Not established.
- **Voice:** Not established.
- **Relationships:** Maternal grandfather of Team Leader Choi and Jin Taekyung and father of Soyeong; regarded by Lee Jungryong as an older brother despite their lack of blood relation.

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 733
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** Publicly reputed to be selfless and devoted to treating patients in the lowest places.
- **Voice:** Not established.
- **Relationships:** Mungyeong is the Divine Physician's true identity, and Dong Feng is his Disciple.

### Felix.md

# Felix (필릭스)

- **Safe through:** Chapter 733
- **Aliases:** Prince Felix
- **Role:** British prince and S-rank Hunter who joins the reinforcement force against the Arch Lich.
- **Personality:** Haughty, self-important, and conscious of royal duty.
- **Voice:** Formal, lofty, and aristocratic.
- **Relationships:** Travels with Faye Chen and Magic Johnson and is allied with Jin Taekyung.

### Go Jun.md

# Go Jun (고준)

- **Safe through:** Chapter 732
- **Aliases:** Team Leader Seok
- **Role:** Go Jun was Ares Guild's Vice Guild Master, Lee Jungryong's Disciple and former Head of Security, the de facto successor to Lee's Ares legacy, and a mutated monster who was killed by Jin Taekyung in Area A.
- **Personality:** Disciplined and controlled under ordinary pressure, fiercely loyal to Lee Jungryong, but consumed by humiliation and rage when Ares Guild's authority is challenged.
- **Voice:** Dry, controlled, and formal with subordinates; deferential when addressing his Master.
- **Relationships:** Go Jun inherited Lee Jungryong's Ares legacy after becoming his Disciple and regarded Jin Taekyung and Choi Minwoo as enemies before his death.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 733
- **Aliases:** Blazing Flame Divine Dragon; Apostle of the Earth Mother Goddess; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan, Jeok Cheongang's publicly acknowledged Disciple, the Fire Gate Clan's nineteenth successor, and the Pavilion Master of the Fire Dragon Pavilion within the Murim Alliance, a Supreme Peak master with the Heavenly Martial Physique and Force, a publicly recognized S-rank-level Hunter who formally retains an A-rank license, a traveler between Murim and another world resembling the realm of immortals, and the creator of the beginner-accessible Smiling Mana Cultivation Method.
- **Personality:** Hungry, self-aware, dryly observant, pragmatic under pressure, and willing to risk himself for people he has accepted as real. Treats impossible situations like games until their human cost becomes undeniable.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, Jeok Cheongang is his Master, Mungyeong was his recent instructor, Cheongpung is his trusted companion and only true martial rival, Choi Minwoo is his subordinate, trusted manager of media and official arrangements, and now the Peace Guild's Guild Master, Ju Hwaran is a trusted Fire Dragon Pavilion member who followed him to Nanman, Chuck Hagel is an American operative allied with him in the covert anti-terror campaign, his mother and sister Hayeon are among those he protects, the Skeleton King is his friend and ally, Xiao Shen regards him as an older brother after Jin saved him, and Jin-ho is his older friend and trusted confidant.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 733
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Lee Jungryong.md

# Lee Jungryong (이정룡)

- **Safe through:** Chapter 733
- **Aliases:** None
- **Role:** Former Vice Guild Master of Ares Guild, one of Korea's two S-rank Hunters, and a Supreme Peak-level martial artist who was killed by Jin Taekyung.
- **Personality:** Outwardly genial, calm, and humorous; calculating, opportunistic, manipulative, coercive, and ruthless when challenged
- **Voice:** Smooth, good-natured, and indirect, using teasing conversation and veiled threats before becoming openly furious
- **Relationships:** Master of Park Jihoon and Go Jun (Team Leader Seok), whom he personally selected and trained; longtime Great Cataclysm acquaintance of Park Tae Seop; adversary of Jin Taekyung; knew Team Leader Choi from childhood; has an antagonistic history with Kim Hwajong, who saved his life at the collapse of Mapo Bridge eighteen years earlier; was visibly shaken by learning that Choi is Cheon Taemin's maternal grandson; regarded Cheon Taemin as an older brother despite no blood relation and long held him in respect and fear; secretly supported the orphanage where Lee Dongseok grew up and was regarded by Dongseok as a father; operated as Ares Guild's senior authority beneath its Guild Master; concealed Taemin's condition with Song Cheonwoo and participated in purging aides who knew the truth.

## Korean source

```text
＃734화



평소의 최 팀장은 표정 변화가 거의 없다.

다른 사람에게 자신의 감정을 쉽게 내보이지 않고, 언론과의 인터뷰에서도 늘 핵심만 간단히 말하기 때문에 돌잡이 때 마이크를 잡았다는 베테랑 리포터도 쩔쩔 멜 정도다.

하지만 그런 최 팀장도 결국 피가 흐르는 사람. 그도 가끔은 제법 풍부한 감정을 보여 준다.

특히 나와 함께 대화를 나눌 때는 숨겨 두었던 감정을 아낌없이 쏟아 내고는 했다.

바로 지금처럼.

“오딘 길드요. 거기 주인장 면상이나 한번 보러 가고 싶네?”

“……!”

말이 끝나기가 무섭게 멍하니 벌어지는 입. 파르르 떨리는 눈꺼풀 아래에서는 이미 동공 지진이 일어나는 중이다.

이 새끼, 또 사고 치려고 작정했구나.

딱 그런 눈빛으로 나를 바라보던 최 팀장은, 한참의 침묵 후에 간신히 목소리를 끄집어냈다.

“지금 그거, 진심으로 하는 말입니까?”

“흠.”

잠시 생각하던 내가 말을 이었다.

“아마도 반반?”

“반쯤 미쳤다는 소리군요.”

“그게 그렇게 되나?”

“이건 정말 궁금해서 묻는 건데, 당장 오딘 길드장을 만나러 가겠다는 정신 나간 생각은 어디에서 나온 겁니까? 가슴? 머리?”

“가슴.”

내 짤막한 대답에 최 팀장이 한숨을 내쉬었다.

“그나마 다행입니다. 아직 완전히 미친 건 아니라서.”

“멀쩡한 사람 보고 미쳤다니. 그냥 얼굴 보고 커피나 한잔하려는 건데. 어차피 프랑스에도 아레스 길드 체인점 있으니까 구실 삼아서 겸사겸사…….”

“체인점이 아니라 길드 지부입니다. 그리고 지금 그 소리를 저더러 믿으라고요? 농담하시는 겁니까?”

정색하며 묻는 최 팀장의 모습에, 나는 입맛을 다셨다.

“뭐, 만약 그쪽이랑 대화가 잘 풀리지 않는다면 약간의 트러블이 생길 수도 있죠.”

“엄청난 트러블이 발생한다는 뜻으로 알아듣겠습니다.”

뭘 또 그렇게까지, 라고 반문하려다 참았다.

나로서도 양심상 최 팀장의 우려가 너무 과장되었다고 말할 수는 없으니까.

단신으로 아레스 길드에 쳐들어가 석고준 뚝배기를 깬 것이 현대의 시간으로 불과 몇 주 전의 일이다.

‘해 먹은 게 있어서 뭐라 말도 못 하겠네.’

더군다나 나는 바보가 아니다.

지금 당장 가슴이 시키는 대로 움직였다간, 썩 좋지 못한 결말을 맞이할 거라는 사실 역시 충분히 인지하고 있었다.

“알았어요.”

“에펠탑이 무너지고, 길드가 무너지고, 우리를 향한 여론이 황폐화…… 네?”

“알았다고요.”

이미 한발 앞서 환각에 시달리고 있던 최 팀장이 눈을 깜빡였다.

“정말입니까?”

나는 작게 고개를 끄덕이며 대답했다.

“애초에 명분이 없잖아요.”

하다못해 사람 목숨이 가축과 동급인 무림에서도 최소한의 명분이 필요한 법인데, 지금 당장 파리로 날아가서 오딘 길드를 들이받아 봤자 얻을 수 있는 건 인터폴 수배령이 전부다.

‘그나마 석고준을 처리할 때는 국민들의 지지라도 있었지.’

세계적으로 큰 반향을 불러일으켰다고는 해도 국내에서 벌어진 사건이었고, 이번과는 달리 증언과 증거도 확실했다.

거기에 온갖 반인륜적 범죄를 저지른 석고준에 대한 국민들의 분노까지.

내가 법의 테두리를 벗어난 행동을 했음에도 범죄자가 되지 않을 수 있었던 이유는 그런 여러 가지 요소들 때문이다.

‘하지만 파리는 다르겠지.’

가슴은 당장 파리로 쳐들어가 깽판을 치라고 외치고 있지만, 아직 살아 있는 이성은 현실을 직시하고 있다.

그리고 이런 내 선택에 최 팀장은 눈을 동그랗게 떴고, 열심히 스마트폰을 보며 육개장을 퍼먹던 스켈레톤 킹은 숟가락을 툭 떨어트렸다.

“이럴 수가. 지금 명분이라고 하신 겁니까?”

“말도 안 돼. 너 이 새끼 몬스터지! 도대체 간악한 인간을 어찌 한 것이냐!”

“…….”

“진태경 씨, 이건 간단한 확인 절차니까 너무 불쾌하게 받아들이지 마십시오. 우리가 처음 만났던 장소가 어딥니까?”

“야! 도플갱어! 간악한 인간의 몸속에서 나가!”

아주 염병들 하고 자빠졌네.

나는 대답 대신 식탁 위에 올려 둔 숟가락으로 스켈레톤 킹의 정수리를 후려갈겼다.

빡!

“두개골! 내 아름다운 두개골이!”

울부짖는 스켈레톤 킹의 모습을 바라본 최 팀장이 고개를 끄덕였다.

“다행입니다. 진태경 씨가 맞군요.”

“…….”

묘하게 기분 나쁜 확인 절차를 끝마친 최 팀장이 안도의 한숨을 내쉬었다.

“어쨌든 생각을 바꾸셔서 다행입니다.”

“이런 식으로 해결할 수 있는 문제였으면, 국제 범죄고 나발이고 지금이라도 당장 파리행 티켓 끊었겠죠.”

“맞습니다. 오딘 길드가 사라지면, 또 다른 오딘 길드가 나타날 테니까요.”

아레스 길드가 적이었을 때와 마찬가지다.

세상은 넓고, 쓰러트린 적의 빈자리는 또 다른 적으로 채워진다.

우리가 공성(攻城)으로 아레스 길드를 차지했듯이, 저들도 마찬가지다. 이제는 주위에 바글대는 경쟁자들로부터 성을 지켜 내고, 최대한 영토를 넓혀야 하는 것이 성주의 의무였다.

더군다나 오딘 길드는 어디서 굴러먹다 왔는지 모를 이리 따위가 아니다.

거대한 몸과 날카로운 발톱을 지닌 맹수.

심지어는 탐욕스럽기까지 하다. 지금 막 최 팀장이 내민 태블릿 PC에 적힌 내용처럼.

“이건…….”

“쓰촨성 몬스터 웨이브 당시, 중국 정부에서 오딘 길드 측에 전달한 참여 제안서입니다. 물론 법적 효력이 없는 비공식이고요.”

비공식 제안서라.

유출이 거의 불가능한 자료를 어떻게 최 팀장이 손에 넣었나 하는 의문이 들었지만, 답은 금방 나왔다.

“종석 아저씨가 줬어요?”

“종석 아저씨가 아니라, 샤오 양 주석입니다.”

“예. 그러니까 종석 아저씨.”

“…….”

“뭐 어때요. 친근하고 좋구만. 어차피 그 아저씨도 나 되게 좋아하는데.”

반쯤 포기한 듯한 눈빛으로 나를 바라본 최 팀장이 말을 이었다.

“진태경 씨도 아시다시피, 사태 초기 중국 국무원과 상무위원회에서는 국외에 도움을 요청하는 것을 탐탁지 않게 생각했습니다. 특히 서구권의 지원을 극렬히 반대했죠.”

두개골을 소중히 쓰다듬고 있던 스켈레톤 킹이 이해가 가지 않는다는 표정으로 불쑥 끼어들었다.

“반대했다고? 왜?”

글쎄, 왜일까.

이유를 말하자면 여러 가지가 있겠지만, 결국 답은 하나로 귀결된다. 나는 친절한 목소리로 의문에 대한 정답을 알려 주었다.

“중국이니까.”

“그게 무슨 소리냐. 같은 인간이 죽어 나가는데?”

“중국이라고.”

“아니, 간악한 인간이여. 지금 이 몸의 질문을 이해하지 못한 모양인데…….”

“응. 중국.”

“……?”

“그런 게 있어. 넌 아직 모를 수도 있겠지만.”

물음표로 가득한 스켈레톤 킹의 얼굴을 뒤로한 나는, 최 팀장을 향해 고개를 돌렸다.

“하지만 어쨌거나 서구권에도 지원 요청을 했잖아요? 영국의 필릭스 왕자나, 매직 존슨도 마찬가지고.”

“네. 아크 리치로 인한 피해가 천문학적으로 커지자, 중국 지도층도 어쩔 수 없이 샤오 양 주석의 주장을 받아들일 수밖에 없던 겁니다. 단, 사태가 마무리되면 외교적, 물질적으로 합당한 대가를 치러야 하니 이를 생각해서 전력을 구축해야 했죠.”

그렇게 모인 S급 헌터가 나를 제외하고서라도 무려 네 명.

물론 그 자체만으로도 엄청난 전력인 것은 맞지만, 지금 중요한 것은 이정룡이 이끄는 아레스 길드와 더불어 핵심이 되어야 했을 오딘 길드가 발을 뺐다는 사실이다.

“그런데 왜 제안을 거절했대요? 이 정도면 오딘 길드도 충분히, 아니, 무조건 받아들여야 할 정도의 금액 같은데.”

내가 이렇게 물어볼 만큼, 태블릿 PC 화면 속 비공식 제안서에 적힌 고용 수당은 실로 어마어마했다.

전에 언뜻 들었던 아레스 길드의 고용 수당과 비교해도 두 배에 가깝고, 그 외에도 여러 가지 옵션들까지 붙어 있었다.

그야말로 오딘이라는 이름값을 톡톡히 쳐준 최고의 대우.

하지만 이런 내 의문은, 다음 순간 들려온 최 팀장의 목소리에 깔끔히 해결되었다.

“최종적으로 거절한 쪽은 중국 정부입니다.”

“예?”

“협상이 거의 끝날 때쯤, 오딘 길드에서 추가 조건을 붙였거든요.”

“추가 조건이라면…….”

미지근한 커피를 한 모금 삼킨 최 팀장이 나직이 말을 이었다.

“쓰촨성의 대표 행적 구역인 청두, 메이산, 쯔양, 쑤이닝을 포함한 10개 시(市)를 향후 99년간 오딘 길드에 임대하고, 베이징에 정식 지부 설립을 허가해 줄 것.”

“……!”

“사실상 쓰촨성을 할양(割讓)하라는 제안이었습니다. 중국 정부에 의해 금지되어 있는 정식 지부 설립은 덤이고요.”

세상에, 지금 내가 뭘 들은 거야.

멍하니 최 팀장을 바라보던 나는 작게 중얼거렸다.

“와, 미친 새끼들. 이건 짱깨보다 더하네.”

“샤오 양 주석이 알려 준 정보에 따르면, 오딘 길드가 협상 직전 프랑스 정부와 접촉했다고 하더군요.”

“아무리 그래도 그렇지. 어떻게 저런 정신 나간 제안을 하지?”

“프랑스잖습니까.”

“아니, 아무리 그래도 상식이라는 게.”

“프랑스라고요.”

“……저기요. 최 팀장님?”

“프랑스.”

“…….”

왠지 모르게 묘한 기시감이 드는데. 단지 기분 탓인가.

그리고 떨떠름한 표정을 짓는 내게, 최 팀장이 부드러운 목소리로 말을 건넸다.

“진태경 씨, 혹시 우리나라 사람들이 프랑스를 다른 이름으로 부른다는 걸 알고 계십니까.”

“아.”

순간 뇌리를 스치는 깨달음과 함께, 나는 탄성을 토해 냈다.

“유럽 짱깨……!”

그런 나를 보며 최 팀장이 고개를 끄덕였다.

“피부색과 문화가 다를 뿐. 그들 역시 ‘그 부류’입니다. 대통령이 불륜을 저지르건, 무슨 짓을 하건 프랑스인들은 신경 안 써요. 괜히 오딘 길드가 파리에 본사를 둔 게 아닙니다. 구설수가 있어도 별다른 잡음이 일어나지 않거든요.”

“하지만 그건 그냥 인터넷 밈 아니었어요?”

“파리에서 보낸 학창 시절이 생각나는군요. 역사 교과서에 외조부님의 사진이 등장하자, 교실 안의 모두가 저를 바라보며 눈을 찢었습니다.”

“아.”

“선생님도 같이 찢고 있었습니다.”

“아앗. 아아…….”

“괜찮습니다. 다 지난 일이니까요.”

문득 떠오른 어린 시절의 아픈 기억을 접은 최 팀장이 말을 이었다.

“지금 무엇보다 중요한 사실은, 저런 프랑스 정부를 등에 업은 오딘 길드라 해도 쉽게 움직일 수 없다는 점입니다. 이번에 우 쉐이밍 일가를 암살한 것처럼, 물리적인 위협 대신 단지 경고로 그칠 수밖에 없죠.”

그건 그렇다.

현재 아레스 길드의 성벽에는 천태민의 깃발이 휘날리고 있고, 지금껏 내가 세상에 보여 준 모습 역시 무시하지 못한다.

설령 그것이 세계 최고로 꼽히는 오딘 길드나, 다른 어떤 거대 길드라 해도 마찬가지다.

그리고 무엇보다…….

“전 세계의 사람들이 우리를 향해 환호하고 있습니다. 비록 언론은 거대 길드를 노골적으로 비난하지는 못하지만, 그들을 질타하는 여론도 상당하고요.”

민심(民心).

마나 연공법 공개를 통해 얻은, 가장 강력한 무기인 동시에 방패.

우리는 손에 들어온 민심을 최대한 활용해야 한다. 오딘 길드조차 범접할 수 없도록 해야…….

“음, 분위기 깨서 미안한데.”

불쑥 입을 연 스켈레톤 킹이 스마트폰을 내밀었다.

“그 환호라는 게, 이런 거 말하는 거냐?”

녀석이 내민 스마트폰의 화면에는, 불과 수십여 초 전 게시된 뉴스 속보가 떠올라 있었다.



[오딘 길드, 아레스 지지 선언]

[오딘 길드, 새로운 마나 연공법 공개]

[고위 관계자, “이미 수년 전부터 준비해 온 프로젝트”]

[“비록 한 걸음 늦었지만, 그들과 함께 세상을 바꾸고 싶다.” 세계 최고의 품격]



시벌, 이건 또 뭐야.
```

## Final English reading copy

```markdown
# Chapter 734

Team Leader Choi usually shows almost no change in expression.

He never reveals his feelings easily to other people, and he always keeps his interviews with the press short and focused on the essential points. Even veteran reporters—the kind who supposedly picked up a microphone at their first-birthday celebration—were reduced to stammering in his presence.[^1]

But even Team Leader Choi was ultimately a man of flesh and blood. Sometimes, he showed a surprisingly wide range of emotions.

Especially when he was talking with me. That was when he tended to pour out all the feelings he kept hidden.

Just like now.

“Odin Guild. I feel like going to see the boss’s ugly mug.”

“……!”

The instant I finished speaking, his mouth fell open in a daze. Beneath his trembling eyelids, his pupils were already shaking like an earthquake.

*This bastard’s planning to cause trouble again.*

Team Leader Choi stared at me with exactly that look in his eyes. After a long silence, he finally managed to force out his voice.

“Are you being serious right now?”

“Hm.”

After thinking for a moment, I continued.

“Probably fifty-fifty?”

“So you’re saying you’re half-insane.”

“Does it work like that?”

“This is a genuine question: where did the insane idea of going to see the Odin Guild Master right now come from? Your heart? Your head?”

“My heart.”

At my brief answer, Team Leader Choi sighed.

“That is a relief, at least. You are not completely insane yet.”

“You’re calling a perfectly sane person crazy? I’m just planning to look the man in the face and have a cup of coffee with him. Ares Guild has branches in France anyway, so I can use that as an excuse and kill two birds with one stone……”

“They are not chain stores. They are Guild branches. And you expect me to believe that? Are you joking?”

At Team Leader Choi’s utterly serious question, I smacked my lips.

“Well, if the conversation doesn’t go smoothly, there might be a little trouble.”

“I will interpret that as meaning there will be an enormous amount of trouble.”

I almost asked him what he was making such a big deal about, but I held back.

Even I could not honestly claim that Team Leader Choi’s concern was exaggerated.

It had only been a few weeks by modern reckoning since I had stormed into Ares Guild alone and smashed Go Jun’s head in.

*I’ve caused enough trouble that I can’t exactly argue with him.*

Besides, I was not an idiot.

I was fully aware that if I acted on what my heart was telling me right now, the outcome would probably be less than pleasant.

“All right.”

“The Eiffel Tower collapses, the Guild collapses, public opinion against us turns into a wasteland…… What?”

“I said all right.”

Team Leader Choi, who had already been suffering from vivid hallucinations one step ahead of me, blinked.

“Really?”

I nodded slightly as I answered.

“We don’t have a pretext in the first place.”

Even in Murim, where human lives were treated as no more valuable than livestock, you needed at least some justification. If I flew to Paris right now and picked a fight with Odin Guild, the only thing I would gain was an Interpol wanted notice.

*At least I had public support when I dealt with Go Jun.*

Even though that incident had caused a major stir around the world, it had taken place in Korea. Unlike this situation, there had been clear testimony and evidence.

And on top of that, the public had been furious with Go Jun for committing all kinds of crimes against humanity.

Those were the reasons I had been able to act outside the boundaries of the law without becoming a criminal myself.

*But Paris would be different.*

My heart was screaming at me to storm into Paris and raise hell, but the part of my reason that was still alive was facing reality.

At my decision, Team Leader Choi’s eyes grew round. The Skeleton King, who had been enthusiastically shoveling yukgaejang into his mouth while staring at his smartphone, dropped his spoon.

“This cannot be! Did you just say ‘justification’?”

“No way. You bastard, you’re a monster! What have you done to the treacherous human?”

“……”

“Mr. Jin Taekyung, this is merely a simple verification procedure, so please do not take offense. Where was the first place we met?”

“Doppelganger! Leave the treacherous human’s body!”

*These two were acting like fucking idiots.*

Instead of answering, I grabbed the spoon sitting on the dining table and smacked the Skeleton King on the crown of his head.

Crack!

“My skull! My beautiful skull!”

Team Leader Choi watched the Skeleton King howl and nodded.

“Thank goodness. You really are Jin Taekyung.”

“……”

After completing that strangely unpleasant verification procedure, Team Leader Choi let out a sigh of relief.

“In any case, I am glad you changed your mind.”

“If this were a problem that could be solved that way, I would have bought a ticket to Paris and left already, to hell with international crime and everything else.”

“That is true. If Odin Guild disappeared, another Odin Guild would appear.”

It was the same as when Ares Guild had been our enemy.

The world was vast, and the empty space left by a defeated enemy would always be filled by another one.

Just as we had taken Ares Guild by siege, the same was true of them. Now it was a lord’s duty to defend his castle from the competitors swarming around it and expand his territory as much as possible.

Besides, Odin Guild was not some wolf that nobody knew where had rolled in from.

It was a predator with a massive body and sharp claws.

It was even greedy. Just like the information written on the tablet PC Team Leader Choi had placed in front of me.

“What is this……?”

“This is the participation proposal the Chinese government sent to Odin Guild during the monster wave in Sichuan Province. Of course, it was unofficial and had no legal force.”

An unofficial proposal.

I wondered how Team Leader Choi had obtained material that should have been almost impossible to leak, but the answer came quickly.

“Grandpa Jongseok gave it to you?”

“Not Grandpa Jongseok. Chairman Xiao Yang.”

“Yes. So, Grandpa Jongseok.”

“……”

“What? It’s friendly. Besides, that old man likes me a lot, too.”

Team Leader Choi looked at me with an expression that suggested he had half given up and continued.

“As you know, Mr. Jin Taekyung, during the early stages of the crisis, China’s State Council and Politburo Standing Committee were reluctant to request help from abroad. They were especially vehemently opposed to support from the West.”

The Skeleton King, who had been tenderly stroking his skull, suddenly interrupted with an expression of confusion.

“They opposed it? Why?”

*Well, why would that be?*

There could have been many reasons, but in the end, they all led to one answer. In a kind voice, I gave him the correct response.

“Because it’s China.”

“What does that mean? Humans are dying either way!”

“Because it’s China.”

“No, treacherous human. It appears you have failed to understand this body’s question……”

“Yeah. China.”

“……?”

“Some things are just like that. You might not understand yet.”

Leaving the Skeleton King’s face covered in question marks behind me, I turned back toward Team Leader Choi.

“But you did ask the West for help eventually, didn’t you? Prince Felix of the United Kingdom and Magic Johnson, too.”

“Yes. Once the damage caused by the Arch-Lich reached astronomical levels, China’s leadership had no choice but to accept Chairman Xiao Yang’s argument. However, they would have to pay an appropriate diplomatic and material price once the crisis ended, so they had to take that into account when assembling their forces.”

That was how four S-rank Hunters had gathered, even without counting me.

Of course, that alone constituted an incredible force. But what mattered now was that Odin Guild, which should have been one of the central pillars alongside Ares Guild under Lee Jungryong’s leadership, had withdrawn.

“But why did they reject the proposal? At this amount, it seems like enough money for Odin Guild to accept without hesitation. No, they absolutely should have accepted it.”

I had asked because the employment fee written in the unofficial proposal on the tablet screen was truly staggering.

It was nearly twice the fee I had once heard Ares Guild received, and there were several other options attached as well.

It was the best possible treatment, paying full value for the name Odin.

But Team Leader Choi’s next words neatly answered my question.

“The Chinese government was the one that ultimately rejected it.”

“What?”

“When the negotiations were nearly complete, Odin Guild added an additional condition.”

“What kind of additional condition……?”

Team Leader Choi took a sip of his lukewarm coffee before speaking in a low voice.

“They wanted China to lease ten cities—including Chengdu, Meishan, Ziyang, and Suining, the representative administrative districts of Sichuan Province—to Odin Guild for the next ninety-nine years, as well as authorize the establishment of an official branch in Beijing.”[^2]

“……!”

“In effect, they were asking China to cede Sichuan Province. The authorization to establish an official branch, which the Chinese government prohibited, was merely an added bonus.”

*Good God. What did I just hear?*

I stared blankly at Team Leader Choi and muttered:

“Wow, those bastards are insane. They’re worse than Chinks.”

“According to the information Chairman Xiao Yang provided, Odin Guild contacted the French government just before the negotiations.”

“Even so, how could they make such a completely insane proposal?”

“They’re French.”

“Even so, there’s such a thing as common sense.”

“They’re French.”

“……Excuse me, Team Leader Choi?”

“French.”

“……”

For some reason, I felt a strange sense of déjà vu. Was it just my imagination?

As I stared at him with a sour expression, Team Leader Choi spoke to me in a gentle voice.

“Mr. Jin Taekyung, did you know that Koreans call the French by another name?”

“Oh.”

With a sudden flash of insight, I let out an exclamation.

“European Chinks……!”

Team Leader Choi nodded as he looked at me.

“Their skin color and culture are different, but they are still ‘that sort.’ Whether the President commits adultery or does anything else, the French do not care. It is not a coincidence that Odin Guild has its headquarters in Paris. Even when scandals arise, they cause very little commotion.”

“But wasn’t that just an Internet meme?”

“I remember my school days in Paris. When a photograph of my maternal grandfather appeared in our history textbook, everyone in the classroom looked at me and pulled their eyes into slits.”

“Oh.”

“The teacher did it, too.”

“Oh, no. Oh……”

“It is all right. That happened long ago.”

Team Leader Choi put away the painful memory from his childhood that had suddenly resurfaced and continued.

“More important than anything else is the fact that even Odin Guild, with that kind of French government behind it, cannot move freely. Just as when they assassinated Wu Shaiming’s family this time, they have no choice but to stop at a warning rather than pose a direct physical threat to us.”

That was true.

The flag of Cheon Taemin was flying above the walls of Ares Guild, and the image I had shown the world until now could not be ignored, either.

Even if the opponent was Odin Guild, considered the greatest Guild in the world, or any other massive Guild, the same applied.

And more than anything else……

“People around the world are cheering for us. The media may not be able to openly criticize the major Guilds, but there is still a considerable amount of public sentiment condemning them.”

*Public sentiment.*

The strongest weapon—and shield—we had gained by releasing the Mana Cultivation Method.

We had to make the fullest possible use of the public sentiment in our hands. We had to make sure even Odin Guild could not approach us……

“Um, sorry to ruin the mood.”

The Skeleton King suddenly spoke and held out his smartphone.

“Is this the cheering you were referring to?”

On the screen of the smartphone he offered me was a breaking-news alert that had been posted only a few dozen seconds earlier.

> **Odin Guild Announces Its Support for Ares**

> **Odin Guild Reveals a New Mana Cultivation Method**

> **Senior Official: “This Project Has Been in Preparation for Several Years”**

> **“Though We’re a Step Late, We Want to Change the World with Them.” The World’s Greatest Guild Shows Its Class**

*Fuck. What the hell is this now?*

[^1]: A **doljanchi** is a Korean child’s first-birthday celebration, traditionally featuring a ceremony in which the child chooses an object symbolizing their future.

[^2]: Meishan, Ziyang, and Suining are cities in Sichuan Province.
```
