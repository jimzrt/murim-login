<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0946.txt",
      "sha256": "8a10e9264986e39cd90891d0435759ad9f4cb76224b003919234d8e2f4d0d767",
      "bytes": 12226
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "eeec347f3c82995e56d0ccaffb44f7eaf8289ca9ada7576e88a317d4b2558367",
      "bytes": 2465
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "9fe0f6f78a8493547692832f3f4778c9f0fdc21697955c77a22c8fa8cea623f3",
      "bytes": 233382
    },
    {
      "path": "characters/Cheongpung.md",
      "sha256": "8a28ba80540fe24472bf13de2ffd4113f0d57e31cbb32c2a21534870f040e6b9",
      "bytes": 1325
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "321408232312ae26ac8859ccc6a6c9a0ba54f051a51ee4cf0635fc98c3499af6",
      "bytes": 759
    },
    {
      "path": "characters/Human Butcher.md",
      "sha256": "46a5823ffb461de3c1c2ae9ec6f02fd9639f3194822f3783da8713bf51f47621",
      "bytes": 667
    },
    {
      "path": "characters/Jang Il.md",
      "sha256": "363be7726842a1828ceb6a428f6e6293e3dd034ffbb3b1bde46c837318ddcd49",
      "bytes": 477
    },
    {
      "path": "characters/Jeok Cheongang.md",
      "sha256": "f2236695a7449132922ae8afa646daf9cb7f5388ddf811c26e0ebe90ef30c775",
      "bytes": 1204
    },
    {
      "path": "characters/Pung Yang.md",
      "sha256": "53a9cd7923a6311b64664722c51f33d63afd55958dc0762c6a52583c7baea678",
      "bytes": 1446
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "f66daa4bae985fcbafa7ec30ad9fc462f9834c125f917088f6bc22c9afe669f8",
      "bytes": 267309
    }
  ],
  "estimated_tokens": 10266
}
-->

# Durable State Update — Chapter 946

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
1 and safe_through 946. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 946. Profile updates may replace only one
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
  "chapter": 946,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 946,
    "continuity_sources": [946],
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
    "The Emperor was poisoned with Blood Soul Gu, which reached his marrow; the Divine Physician said his vitality was at its limit and could not guarantee survival for another couple of months.",
    "The Divine Physician says the Emperor’s only path to survival requires him to die once; the method is not yet explained.",
    "Taekyung’s System Quest requires him to remove the Blood Soul Gu from the Emperor’s head and successfully treat him; its reward and failure consequence are unknown.",
    "War against Dark Heaven is imminent: its main force is targeting Shanxi as a foothold for invasion of the Central Plains, with the Double Ninth Festival as the expected date.",
    "Taekyung was appointed Marquis of Shangshan and Thousand Captain, with a thousand Embroidered Uniform Guards entrusted to him to fight the foreign enemy.",
    "Jang Sam abruptly rose from Level 40 to Level 60, attacked Taekyung while apparently irrational, and is now unconscious and being taken to the Nangong Family.",
    "Taekyung suspects Jang Sam’s sudden change may involve a Temporary Strength Pill, recalling that Pung Yang’s ambitions were enabled by one; the suspected connection is unconfirmed.",
    "Jang Il says Jang Sam moved his stronghold from near Hubei to Anhui about three months ago and took over two small strongholds there.",
    "The Eastern Heaven Demon Lord’s hidden iron chest contained old bamboo slips, recent papers, and a small silk pouch of unknown significance.",
    "The Bow Saint says the Martial God chose her; she tested Taekyung to confirm he was the chosen one and assess his power and character."
  ],
  "continuity_sources": [
    945,
    944
  ],
  "open_questions": [
    "What is the Martial God’s identity, and what is the full nature of his connection to the chosen one and the Bow Saint?",
    "How far has Dark Heaven infiltrated the Great Nation, and which officials or commanders are involved?",
    "Where is Ma Sanbao, and what is his current status?",
    "What do the Eastern Heaven Demon Lord’s papers and silk pouch contain, and what is their significance?",
    "What caused Jang Sam’s sudden Level increase and apparent loss of reason, and is it connected to a Temporary Strength Pill?"
  ],
  "safe_through": 945,
  "temporary_decisions": [
    "Taekyung intends to keep the pocket watch for half a month before deciding whether to give it to Mujin."
  ],
  "version": 1
}
```

## Exact glossary matches

| 적천강    | **Jeok Cheongang** |
| 청풍     | **Cheongpung**     |
| 궁성     | **Bow Saint**                 | —              |
| 항산검문   | **Mount Heng Sword Sect**        |
| 암천     | **Dark Heaven**                  |
| 일류     | **First Rate**    |
| 절정     | **Peak**          |
| 초절정    | **Supreme Peak**  |
| 무인     | **martial artist**                               | Default term                                          |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 경지     | **realm** / **realm stage**                      | Especially power level                                |
| 정파     | **orthodox faction**                             |                                                       |
| 마적     | **mounted bandits**                              |                                                       |
| 장로     | **Elder**                                    |
| 대장로    | **Head Elder**                               |
| 제자     | **Disciple**                                 |
| 상태               | **Status**                     |
| 산서     | **Shanxi**             |
| 항산     | **Mount Heng**         |
| 노부      | **this old man / I**                                            |
| 귀가      | **your family**                                                 |
| 대협      | **Great Hero** or **Sir** depending tone                        |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 인도 | **Human Butcher** | Epithet of a mysterious Han Chinese mounted-bandit power commanding fifty subordinates. |
| 장일 | **Jang Il** | Twenty-five-year-old two-knot Beggars' Sect Disciple killed near Emei. |
| 풍양 | **Pung Yang** | Personal name of the Red Wind Band Leader. |
| 적풍단 | **Red Wind Band** | Rising mounted-bandit power from the northern plateau. |
| 잠력단 | **Temporary Strength Pill** | Rare pill that temporarily enhances strength; Pung Yang has only three and uses one against Cheol Mubaek and another during the battle. |
| 산서성 | **Shanxi Province** | Province containing the Lower District Sect branches. |
| 선천지기 | **innate qi** | Vital energy said to be damaged by the pill's aftereffects. |
| 황상 | **Emperor** | Address or reference to the reigning Emperor. |
| 전하 | **His Highness** | Formal royal address for the resident prince; the official insists on this form instead of king. |
| 고자 | **eunuch** | Castrated man; Hong Jin openly identifies himself by this term. |
| 무재 | **martial talent** | Innate aptitude for learning martial arts. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 중독 | **Poisoned** | System status abnormality caused by the poisons. |
| 아귀 | **A-Gwi** | Legendary Dogon from Sichuan. |
| 마도 | **Demonic Path** | Term raised for martial power that appears to defy common principles. |
| 초절 | **supreme mastery** | Realm beyond Peak described as accessible only to the greatest martial artists. |
| 천주 | **Lord of Heaven** | Authority invoked by the masked attackers. |
| 꼬리 | **the “tail”** | Codename for the Black Hunter traced by Butler Kim. |
| 준이 | **Jun** | Family nickname used in the form Jun's dad. |
| 살인멸구 | **Silencing the Witnesses** | Killing witnesses to prevent a secret from being exposed. |
| 호북 | **Hubei** | Province on Ju Gongsan's route from Guangdong to Henan. |
| 강기 | **Force** | Generic manifestation of concentrated martial energy; distinct from Sword Force. |
| 단환 | **pill** | A martial elixir in pill form; Mungyeong gives Taekyung a custom-made one. |
| 황하 | **Yellow River** | River along which civilization began. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 마적 | 풍양 | mounted-bandit subordinate to bandit leader | Leader | deferential | Uses 단주 when reporting to Pung Yang. |
| 적천강 | 청풍 | overwhelming_elder_to_young_martial_artist | you / little punk | blunt, amused, and threatening | Jeok Cheongang uses 네, 이놈, and related blunt forms while testing Cheongpung. |
| 청풍 | 적천강 | young_martial_artist_to_overwhelming_elder | Grandpa Jeok | casual-familiar despite deference | Cheongpung uses 적 할아버지 while asking Jeok Cheongang to confirm Taekyung's condition; this is a familial form of address, not literal kinship. |
| 적천강 | 신의 | senior_martial_master_to_physician | Divine Physician | blunt and familiar | Uses 신의 while recognizing Dong Feng’s medical identity. |
| 신의 | 적천강 | physician_to_legendary_martial_master | Sir Jeok | formal-deferential | Uses 적 대협 while thanking and counseling Jeok. |
| 적천강 | 궁성 | old acquaintance and fellow martial master | you; nasty old hag | blunt and familiar | Uses a contemptuous insult while expressing concern for his Disciple. |
| 궁성 | 적천강 | old acquaintance and fellow martial master | you | familiar and lightly teasing | Speaks with dry familiarity about his unchanged, impulsive nature. |
| 황제 | 신의 | Emperor addressing a physician | Divine Physician | direct and familiar | The Emperor asks whether the Divine Physician left something behind. |
| 신의 | 황제 | physician addressing his patient and sovereign | Your Majesty | formal and deferential | The Divine Physician addresses the Emperor as 폐하 while explaining the treatment. |

## Listed compact profiles

### Cheongpung.md

# Cheongpung (청풍)

- **Safe through:** Chapter 927
- **Aliases:** Huashan Divine Dragon
- **Role:** Cheongpung is a twenty-three-year-old Huashan outsider, the grandson and Disciple of Sword Saint Mae Jonghak, a Supreme Peak martial master known as the Huashan Divine Dragon, the creator of the snake-inspired Mimi Step footwork technique, and the master of the Azure Dragon Pavilion within the Alliance Leader's Two Dragons Pavilion.
- **Personality:** Affable, dreamy, hazy, and childlike in manner, with innocent curiosity, delight in novel public attention, a deep love of martial arts, competitive pride, unusual resistance to monster-induced Fear, and discomfort when someone copies his martial arts.
- **Voice:** Dreamy and hazy, with innocent, polite phrasing; he has begun imitating Taekyung's profanity.
- **Relationships:** Mae Jonghak is his grandfather and martial instructor, Baek Museong is his Martial Nephew, and Jin Taekyung and Hyuk Mujin are his Benefactors and companions while Taekyung is his only true martial rival; Tang Sadok has temporarily entrusted Mimi, now a large horned snake, to him, and Cheongpung is accompanying Mungyeong while learning his martial arts through observation to become stronger and adapt to this world.

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 944
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** He is devoted to medicine and the lives he could not save, yet remains composed and self-effacing under mortal danger.
- **Voice:** He speaks in calm, respectful, self-effacing language, framing mortality through quiet philosophical reflections.
- **Relationships:** Mungyeong is the Divine Physician's true identity, the Slaughter Saint was his Master, and Dong Feng is his Disciple.

### Human Butcher.md

# Human Butcher (인도)

- **Safe through:** Chapter 945
- **Aliases:** None
- **Role:** Former mysterious Han Chinese mounted-bandit power in Northern Gaoyuan commanding fifty subordinates; a Peak master killed by an unnamed old man in a single move
- **Personality:** Cold, intimidating, and murderous; he kills people as though slaughtering livestock
- **Voice:** Cold, curt, and quietly threatening
- **Relationships:** He is one of four powerful participants at the Northern Gaoyuan gathering, intimidates Temur, and has claimed Ghost Sword Wipeng as his personal target in the proposed attack

### Jang Il.md

# Jang Il (장일)

- **Safe through:** Chapter 945
- **Aliases:** None
- **Role:** Jang Il is a junior military officer and one of the seven gate commanders at Yichang’s West Gate.
- **Personality:** He is complacent and greedy, yet regards his restrained corruption as respectable.
- **Voice:** Not established
- **Relationships:** He commands soldiers at Yichang’s West Gate and has an elderly servant.

### Jeok Cheongang.md

# Jeok Cheongang (적천강)

- **Safe through:** Chapter 945
- **Aliases:** Fire King; eighteenth Sect Leader of the Fire Gate Clan
- **Role:** Jeok Cheongang is the Fire Gate Clan’s current Sect Leader, a legendary martial master who has surpassed the Three Saints, Jin Taekyung’s Master and intended heir’s mentor, and a trusted confidant who occupies the chief seat of the Murim Alliance’s Five Kings Hall.
- **Personality:** Secretive, sharp-eyed, gruff, dryly teasing, and pathologically afraid of water; believes there is no absolute justice and hopes to make good choices while protecting those he still has.
- **Voice:** Sharp and ringing when calling out; otherwise gruff, dryly teasing, blunt, and threatening during interrogation or confrontation.
- **Relationships:** He considers Jin Taekyung his one and only Disciple and says they have shared everything since he accepted him; he warmly regards Ju Hwaran, sees Mae Jonghak as a kindred spirit, recognizes Cheongpung as Mae's grandson and successor, was close to Hong Dao, accepted Jangcheon as a Disciple before he became Jopil, and remains Peng Cheolhu's rival.

### Pung Yang.md

# Pung Yang (풍양)

- **Safe through:** Chapter 945
- **Aliases:** Red Wind Band Leader
- **Role:** Former leader of the Red Wind Band, commanding at least two hundred mounted bandits; became a mounted bandit at thirteen, reached First Rate by age thirty, and rose from squad leader to band leader three years ago; discovered the Crimson Blood martial arts and a case containing five Temporary Strength Pills in a hidden plateau tomb, reached the Peak realm in two years, and could temporarily manifest imperfect Sword Force and powerful Body-Protecting Qi by taking a pill; reached approximately seventy percent mastery of the Crimson Blood Twelve Sabers; after secretly incapacitating Jin Mukyung, resumed killing Mount Heng Sword Sect martial artists; was seriously injured by Taekyung's dagger, defeated One Annihilation, seized Taekyung, and was killed by Taekyung after the Unnamed Sword's Ten-Thousand-Year Cold Iron destroyed his Body-Protecting Qi and pierced his chest; had fled from the steppe and commanded nearly four hundred subordinates before his death
- **Personality:** Foxlike, ruthless, observant, controlled, and willing to kill subordinates who disobey his orders
- **Voice:** Calm, concise, and authoritative when issuing orders
- **Relationships:** Leads the Red Wind Band and controls former members of other mounted-bandit groups who joined his force

## Korean source

```text
＃946화



시간은 공평하다.

산 것에게도, 죽은 것에게도, 심지어는 형체조차 없는 무언가에도.

그리고 그런 의미에서, 지금 이 순간 불현듯 뇌리를 스친 누군가의 이름은 조금씩 색이 바래져 가고 있는 상태였다.

만약 그날에 있었던 치열한 혈투와, 승리 후 우연히 손에 넣은 한 가지 물건이 아니었다면 금세 잊어버렸어도 이상하지 않을 만큼.

‘잠력단(潛力團)……!’

벼락이 정수리를 관통한다면 이런 기분일까.

순간 뇌리를 뒤흔드는 충격과 함께, 나도 모르게 몸이 덜컥 굳는 것이 느껴졌다.

‘설마.’

가장 먼저 떠오른 감정은 부정(否定)이다.

그러나 누구보다 나 스스로가 더 잘 알고 있다.

지금 이 순간 머릿속을 스친 저 생각을 부정하는 이유는, 그만큼 믿고 싶지 않기 때문이라는 것을.

“그놈이, 네 두령이 도대체 뭘 갖고 있었지?”

“예?”

“석연치 않은 비밀. 전에는 볼 수 없었던 희한한 물건. 그게 뭐든 간에 기억해 내란 말이다.”

“대, 대협, 그게 대관절 무슨 말씀이신지…….”

찰거머리처럼 등에 착 달라붙어 있던 장일이 떨리는 목소리로 묻는다.

나는 대답 대신 말고삐를 쥔 손아귀에 힘이 들어가지 않도록 안간힘을 썼다.

이곳에서 멈춰선 안 된다.

한순간이라도 더 달려야 한다.

지금 당장 말을 멈춰 세운다고 한들 달라지는 것은 아무것도 없으니까.

“이상한 점이 있었을 거야. 분명히.”

“자, 잠시만. 잠시만 진정해 주십시오. 대협.”

당황한 기색이 역력한 장일의 모습에, 차라리 혼절해 있던 두령 놈을 데려왔어야 했나 하는 후회를 품은 그때였다.

“……어?”

불현듯 귓가를 파고드는 얼빠진 목소리.

황급히 고개를 돌린 내 시선에, 눈이 동그래진 장일의 모습이 닿았다.

“그러고 보니, 언제부턴가 웬 비단 주머니를 항상 갖고 다녔습니다.”

“비단 주머니?”

“예에. 똑똑히 기억 납니다요. 몇 달 전 호북에서 재수 없게 저희 산채를 지나가던 과객에게 통행료 대신 받은 물건인데, 그 후로 늘 신줏단지처럼 품고 다니길래 귀한 사향(麝香)이라도 되는 줄 알았지요.”

호북에서 만난 과객.

신줏단지처럼 품고 다니던 정체불명의 비단 주머니.

그리고 그 후에 두령이 보인 이해할 수 없는 행동들.

“저어, 혹시 그 비단 주머니에 무슨 문제라도 있습니까? 사향 특유의 향이 안 나서 소인도 조금 의심스럽긴 했는데.”

나는 장일의 물음에 대답하지 않았다.

아니, 대답하지 못했다.

불길했던 짐작이 확신으로 변하는 순간이었으니까.

더불어 장일에게서는 더 이상의 어떤 정보도 알아낼 수 없음을 알았다.

과연 그 비단 주머니 안에 무엇이 들어 있었는지, 그리고 그것의 원주인이었던 과객의 정체가 무엇인지.

그는 수십 년이 흐른 뒤에도 알 수 없을 것이다.

‘틀림없다. 잠력단이야.’

잠력단은 말 그대로 몸 안에 내재되어 있던 모든 힘을 끌어올리는 단환.

과거 풍양을 상대하며 그 위험성을 몸소 겪은 바가 있는 나로서는 이를 악물 수밖에 없었다.

으득.

“무슨 일이냐.”

이상함을 눈치챈 것은 가장 가까이에 있던 장일뿐만이 아니다.

어느새 딱딱하게 굳은 얼굴을 한 적천강을 바라보며, 나는 호흡을 가다듬었다.

“혹시 과거 산서성에서 있었던 일, 기억하십니까?”

“과거라면, 언제를 말하는 것이냐?”

“항산검문을 습격한 마적 집단에 관한 이야기입니다. 일전에 한 번 말씀드렸던.”

정확히 말하자면, 적천강이 산서성에 발을 디딘 것은 항산검문의 일이 마무리된 직후다.

그러나 그 역시 풍양과 잠력단에 관한 사실을 속속들이 알고 있는 소수의 인물 중 하나였다.

“……그렇다면 혹시.”

무언가를 짐작한 듯, 크게 뜨이는 두 눈동자.

“예.”

나는 나직한 목소리로 말을 이었다.

“그럴 가능성이 높습니다. 아니, 정황상 틀림없어요.”

“이런 염병할.”

적천강이 탄식하듯 욕설을 흘린 그때, 가라앉은 눈빛으로 오가는 대화를 듣고 있던 궁성이 불현듯 입을 열었다.

“그 해괴한 단환(團丸)에 관련된 이야기인가 보구나.”

“……!”

“그렇게 볼 것 없다. 과거라고 한들 이제 고작 일이 년 남짓. 항산검문과 적풍단의 일은 이미 알고 있었으니까.”

궁성은 놀란 내 모습에도 아랑곳하지 않고 말을 이었다.

“입단속을 제법 철저히 한 건 알고 있다만, 살인멸구(殺人滅口)가 아닌 이상 진실은 새어 나가는 법이지.”

잠력단에 관한 충격으로 잠시 잊고 있었다.

궁성이 왜 굳이 황제의 곁에 머무르고 있었는지.

그리고 이 광활한 천하에 흩뿌려진 황실의 눈과 귀가 얼마나 많은지도.

“이미 알고 계신다니, 굳이 장황하게 설명할 필요는 없겠군요.”

빠르게 침착함을 되찾은 내 모습에 궁성이 뜻 모를 미소를 입가에 띄웠다.

물론 그 흐릿한 미소는, 언제 그랬냐는 듯 금세 사라져 버렸지만.

“항산검문에서 있었던 일련의 상황들은 나로서도 의구심을 품을 수밖에 없었다. 적풍단을 이끌던 풍양이라는 자에 관한 추가 정보를 입수하고 난 후에는 특히나.”

모든 것을 떠나, 한 사람의 무인으로서 의구심이 드는 것은 당연한 일이었을 것이다.

그날, 적지 않은 이목이 지켜보는 앞에서 풍양은 초절정에 버금가는 힘을 드러냈으니까.

이미 완숙한 절정의 경지에 다다라 있었던 놈은 그 자체로도 상당한 강자였지만, 불완전하게나마 강기(罡氣)를 선보였다는 것부터가 상식을 벗어난 일이다.

‘절정의 끝자락에 도달해 있던 대장로가 선천지기(先天眞氣)까지 끌어올린 후에야 그런 힘을 보일 수 있었다는 것을 생각한다면 더더욱.’

무공을 익힌다는 것은 끝없는 계단을 오르는 것과 같다.

막 시작한 초심자는 한 번에 몇 계단을 뛰어넘을 수도 있지만, 절정의 경지에서는 혼신의 힘을 다해야만 다음 계단을 밟을 수 있다.

하늘이 내린 무재(武才)를 타고난 청풍조차 눈부신 속도로 강해졌을 뿐이지, 정해진 단계를 벗어나진 않았을 것이다.

‘하지만 잠력단은 그걸 가능하게 만들지.’

물론 엄청난 효력만큼이나 부작용이 끔찍한 데다 유지 시간도 길지 않지만, 그야말로 순리(順理)를 뒤트는 힘.

풍양에 대한 자세한 정보를 입수한 궁성이 그 사실을 눈치채지 못했을 리 없다.

“당시에는 잠시나마 그런 생각을 하기도 했었지.”

궁성이 작은 목소리로 흘리듯 중얼거렸다.

“풍양. 과욕 끝에 죽음을 맞이한 그자가, 혹시 내가 찾던 사람이었을지도 모른다는 생각을.”

문득 그녀에게 묻고 싶은 말이 생각났다.

만약 그날의 전투에서 살아남은 것이 내가 아니라 풍양이었다면, 그리고 정말 그가 선택받은 자였다면 당신은 어떤 선택을 했을지.

그러나 마음속에서 불쑥 고개를 쳐든 그 의문을, 나는 조용히 억눌러 삼킬 수밖에 없었다.

현재 직면한 상황은 그만큼 심각했으니까.

“아무래도…… 과거 풍양이 사용했던 그것이 누군가에 의해 은밀히 유통되고 있는 것 같습니다.”

당연하게도 내가 말하는 누군가가 무엇을 뜻하는지, 적천강과 궁성은 이미 알고 있었다.

암천.

잠력단을 만든 장본인들.

놈들이 정확히 언제부터 이 상황을 준비했던 것인지는 모르나, 이제는 일개 산적의 손에 들어갔다는 것은 결코 쉽게 볼 수 없는 일이었다.

“확실하느냐? 노부가 들은 것에 비하면 효력이 턱없이 부족한 것 같은데.”

깊게 가라앉은 적천강의 물음에, 궁성이 나를 대신해서 고개를 가로저었다.

“당신을 막아섰던 그 산적은 일류의 경지에도 접어들지 못한 자였어요. 이후 그에게서 드러난 변화를 생각해 봤을 때, 가능성은 두 가지로 좁혀지겠죠.”

“두 가지라면?”

“복용자의 수준에 따라 그 위력도 달라지거나. 혹은…….”

흐려지는 말꼬리와 함께 이쪽을 향한 궁성의 시선에, 내가 입을 열었다.

“효력을 줄인 만큼, 그에 뒤따르는 부작용도 감소시켰거나.”

“……!”

짧은 침묵이 흘렀다. 무거운 눈빛으로 나와 궁성을 번갈아 바라보던 적천강이 낮은 목소리로 뇌까렸다.

“후자가 틀림없겠군.”

“그것까지는 아직 확실치 않습니다.”

“아니, 무슨 말을 가져다 붙여도 현실을 회피하려는 말장난에 불과하다.”

대번에 고개를 가로저은 적천강이 단호한 어조로 말을 이었다.

“이 세상 모두가 힘을 원한다. 부, 명예. 무력. 그것이 무엇이든 간에 강자로 우뚝 서길 원하지. 하지만 모든 것에는 그만한 대가가 따르기 마련이다.”

큰 힘에는 큰 대가가 따른다.

그리고 대부분의 사람들은 무언가를 강렬히 소망하면서도 그만한 노력을 기울이지 못한다.

그 과정이 얼마나 힘든지 아니까.

미래에 자신이 원하는 것을 얻기 위해서는, 현재의 행복과 달콤함을 희생해야 하니까.

“그러나 찰나의 힘을 얻기 위해 마땅히 치러야 할 그 대가가 충분히 감당할 수 있는 수준이라면 어떻겠느냐?”

그 순간, 나는 적천강이 이토록 확신할 수밖에 없는 이유를 깨달았다.

그가 진정으로 말하고자 하는 것이 무엇인지도 함께.

“놈들이 그것을 만든 이유는, 단지 자신들의 전력을 높이기 위해서만이 아니다.”

“……!”

“한낱 마적 떼를 이끌던 풍양이, 그리고 산적 나부랭이 따위가 어찌 그것을 손에 넣었겠느냐? 아니, 놈들이 어찌하여 그런 놈들에게까지 마수를 뻗쳤겠느냐.”

폭탄에는 그 누구도 손을 대지 않는다.

자칫하면 작은 충격에도 터져 버릴 수도 있으니까. 가까이 다가간 것만으로도 그 폭발력에 의해 전신이 갈기갈기 찢겨져 버릴 테니까.

하지만 폭탄이 아닌 모닥불이라면 어떨까.

추운 겨울날, 원하는 것을 찾아 눈밭을 헤매던 이들은 그 모닥불의 온기를 느끼기 위해 손을 뻗을 것이다.

설령 너무 가까이 다가선다 해도 괜찮다.

약간의 화상만 입을 뿐이니까. 그 정도로는 죽지 않는다는 것을 이미 알고 있으니까.

모두가 손을 뻗을 수 있는 모닥불.

온기를 느끼기 위해 치러야 할 사소한 대가.

아마도 그것이야말로, 암천이 원하는 그림이었을 것이다.

이 광활한 천하에는, 그 사소한 대가를 치르면서까지 힘을 맛보고 싶은 미친 인간들이 사방에 깔려 있으니까.

그리고 정파(正波)라 불리는 이들 역시 예외는 아닐 테니까.

‘누구나 얻을 수 있는 힘……!’

그것이 바로 새로운 잠력단이 가진 진정한 위험성이었다.

그것에 담긴 매혹적인 힘은 십 년, 혹은 수십 년간 제자리걸음만 하던 이들을 유혹할 것이다.

눈 깜짝할 새에 그들을 중독시키고, 망가트릴 것이다.

그리고 동시에 천주(天主)는 자신을 따르는 수많은 추종자에게, 아니 일회용 고기 방패나 다름없는 그들에게 보다 더 강한 생명력을 부여할 수 있게 되었다.

지금 이 순간에도 산서성을 향해 파도처럼 나아가고 있을, 무수한 암천의 무리에게.
```

## Final English reading copy

```markdown
# Chapter 946

Time is fair.

To the living, the dead, and even things without form.

And in that sense, the name of someone that suddenly crossed my mind at this very moment was already starting to fade.

If not for the fierce battle that day and the item I’d happened to get my hands on after winning, it wouldn’t have been strange if I’d forgotten it in no time.

*The Temporary Strength Pill…!*

Was this what it felt like to be struck by lightning right on the crown of your head?

The shock shook my mind, and I felt my body stiffen before I knew it.

*No way.*

The first emotion that came to mind was denial.

But I knew better than anyone that the reason I wanted to deny the thought that had just crossed my mind was that I didn’t want to believe it.

“What did that bastard—your leader—have?”

“Pardon?”

“Some secret that didn’t sit right. A strange item he didn’t have before. Whatever it was, remember.”

“G-Great Hero, what on earth do you mean…?”

Jang Il, who’d been clinging to my back like a leech, asked in a trembling voice.

Instead of answering, I did everything I could to keep my grip from tightening around the reins.

We couldn’t stop here.

We had to ride even a moment longer.

Even if I reined in the horse right now, nothing would change.

“There must have been something strange. There has to be.”

“P-Please, wait. Please calm down, Great Hero.”

Jang Il looked completely flustered. I was just beginning to regret not bringing the leader, who was still unconscious, when—

“…Huh?”

A dazed voice suddenly reached my ears.

I whipped my head around. Jang Il was staring back at me, eyes wide.

“Come to think of it, at some point he started carrying a silk pouch everywhere.”

“A silk pouch?”

“Yes. I remember it clearly. A few months ago, he got it from a traveler passing our stronghold in Hubei—bad luck for the traveler, I suppose—instead of a toll. After that, he kept it close like it was some kind of sacred relic. I thought it might be precious musk or something.”

A traveler he’d met in Hubei.

A mysterious silk pouch the leader had kept close to his heart.

And the leader’s inexplicable behavior after that.

“Um, was there something wrong with the pouch? I did wonder about it a little, since it didn’t have the distinctive smell of musk.”

I didn’t answer Jang Il’s question.

No—I couldn’t answer.

The moment my ominous suspicion became certainty had arrived.

And I knew there was no more information I could get out of Jang Il.

What had been inside the silk pouch, and who the traveler who’d owned it was—

Even decades from now, he wouldn’t know.

*There’s no doubt. It was the Temporary Strength Pill.*

The Temporary Strength Pill was just what its name suggested: a pill that drew out all the strength latent within the body.

Having experienced its dangers firsthand when I fought Pung Yang, I could only grit my teeth.

Crunch.

“What is it?”

Jang Il wasn’t the only one who’d noticed something was wrong.

I looked at Jeok Cheongang, whose face had gone rigid, and steadied my breathing.

“Do you remember what happened in Shanxi Province?”

“What do you mean by ‘what happened’? When?”

“I mean the mounted bandits who attacked the Mount Heng Sword Sect. I told you about it once before.”

Strictly speaking, Jeok Cheongang had set foot in Shanxi Province just after the Mount Heng Sword Sect affair had ended.

But he was one of the few people who knew everything about Pung Yang and the Temporary Strength Pill.

“…Then could it be?”

His eyes widened as he realized what I was getting at.

“Yes.”

I continued in a low voice.

“It’s likely. No—in light of the circumstances, there’s no doubt.”

“Goddamn it.”

Just as Jeok Cheongang let out the curse like a sigh, the Bow Saint, who’d been listening to us with a grave expression, spoke up.

“This is about that bizarre pill, isn’t it?”

“……!”

“Don’t look so surprised. Even if it was in the past, it was barely a year or two ago. I already knew about the Mount Heng Sword Sect and the Red Wind Band.”

The Bow Saint continued, unfazed by my surprise.

“I know you were careful to keep it quiet, but the truth always leaks out unless you silence the witnesses.”

For a moment, I’d forgotten all about it in the shock of the Temporary Strength Pill.

Why the Bow Saint had chosen to stay by the Emperor’s side.

And just how many eyes and ears of the imperial court were scattered across this vast land.

“If you already know, then there’s no need for me to go into a long explanation.”

The Bow Saint’s lips curved into a faint, inscrutable smile as I quickly regained my composure.

Of course, that faint smile vanished as quickly as it had appeared.

“The events at the Mount Heng Sword Sect gave me reason to wonder, too. Especially after I learned more about a man named Pung Yang, who led the Red Wind Band.”

Setting everything else aside, any martial artist would have had questions.

That day, in front of a fair number of onlookers, Pung Yang had displayed power close to the Supreme Peak realm.

He’d already reached the fully developed Peak realm, making him a formidable fighter in his own right. But the fact that he’d manifested Force, even imperfectly, was beyond all reason.

*Especially when you consider that the Head Elder, who’d reached the very limits of the Peak realm, could only show power like that after drawing on his innate qi.*

Learning martial arts was like climbing an endless flight of stairs.

A beginner just starting out might skip several steps at once. But at the Peak realm, you had to give everything you had just to reach the next one.

Even Cheongpung, born with heaven-sent martial talent and strengthened at a dazzling pace, wouldn’t have skipped the steps laid out before him.

*But the Temporary Strength Pill could make that possible.*

Its effects were tremendous, but the side effects were terrible, and the power didn’t last long. It twisted the natural order itself.

There was no way the Bow Saint could have missed that after learning more about Pung Yang.

“At the time, I even wondered if the man I’d been searching for might have been Pung Yang—who died because of his greed.”

The Bow Saint murmured the words softly.

A question suddenly came to mind.

If Pung Yang, not I, had survived that battle—and if he really had been the chosen one—what choice would she have made?

But I could only quietly suppress that question as it rose within me and swallow it down.

The situation we were facing was far too serious for that.

“It seems… someone is secretly distributing the pill Pung Yang used.”

Naturally, Jeok Cheongang and the Bow Saint already knew who I meant by *someone*.

Dark Heaven.

The ones who had made the Temporary Strength Pill.

I didn’t know exactly how long they’d been setting all this up. But the fact that it had reached the hands of an ordinary bandit was no small matter.

“Are you sure? From what this old man heard, its effects seem far too weak.”

At Jeok Cheongang’s deeply grave question, the Bow Saint shook her head on my behalf.

“The bandit who stood in your way hadn’t even reached First Rate. Considering the changes he showed afterward, there are two possibilities.”

“What two?”

“Either its power varies according to the user’s level. Or…”

The Bow Saint’s voice trailed off as she looked toward me. I spoke up.

“Or they reduced its effects—and the side effects along with them.”

“……!”

A brief silence fell. Jeok Cheongang looked between the Bow Saint and me with a heavy gaze, then muttered in a low voice,

“It must be the latter.”

“We can’t be sure of that yet.”

“No matter what you call it, that’s just wordplay meant to avoid facing reality.”

Jeok Cheongang shook his head at once, then continued in a firm tone.

“Everyone in this world wants power. Wealth, fame, strength—whatever it is, they want to stand above others. But everything comes at a price.”

Great power came at a great price.

And most people, however fiercely they wished for something, couldn’t bring themselves to put in the effort it took to get it.

Because they knew how hard the process was.

Because to obtain what they wanted in the future, they had to sacrifice the happiness and sweetness of the present.

“But what if the price you had to pay for a moment of power was something you could easily bear?”

That was when I understood why Jeok Cheongang was so certain.

And what he was really trying to say.

“They didn’t make it just to bolster their own fighting strength.”

“……!”

“How could Pung Yang, who led a mere band of mounted bandits, and some lowly bandit have gotten his hands on it? No—why would they reach out to people like that in the first place?”

No one would touch a bomb.

It might go off at the slightest jolt. Just getting too close could tear your whole body to pieces with its blast.

But what if it wasn’t a bomb, but a campfire?

On a cold winter day, those wandering through the snow in search of something would reach out to feel its warmth.

Even if they got too close, it would be fine.

They’d get a small burn, that was all. They already knew it wouldn’t kill them.

A campfire anyone could reach toward.

A trivial price to pay for its warmth.

That was probably exactly the picture Dark Heaven wanted to create.

There were madmen scattered all across this vast land, eager to taste power even if they had to pay that small price.

And those called the orthodox faction would be no exception.

*Power anyone can obtain…!*

That was the true danger of the new Temporary Strength Pill.

Its alluring power would tempt people who’d spent ten years, or even decades, stuck in the same place.

It would addict and ruin them in the blink of an eye.

And at the same time, the Lord of Heaven would be able to give greater vitality to the countless followers who served him—or rather, to those who were little more than disposable meat shields.

To the innumerable hordes of Dark Heaven, even now surging like a wave toward Shanxi Province.
```
