<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0685.txt",
      "sha256": "82fcab51963bcae0886f1353a58508f287188755356e54c409200e23a1dc40fb",
      "bytes": 15630
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "79ebfddbaef9e250357239783edfaa0b1fa4e437f7a98e3af2e94d0a0e210e9e",
      "bytes": 1205
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "22764fb38b28621564d76844c10cea4c71334f08d99cf84fb313c93d516bd87d",
      "bytes": 203778
    },
    {
      "path": "characters/Black Hand.md",
      "sha256": "45d0127feb3f6d19d2e09440dc64a9a0326ccc0be1e0b3cdee1bb51579ccb404",
      "bytes": 788
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "fc6fc52d28d396496506ef4220cfd6c8eecfacbfef3723be129fd20417c18806",
      "bytes": 553
    },
    {
      "path": "characters/Great Snow Fiend.md",
      "sha256": "f4757bfd200c57586f8776c58c1781cd878f8a92b8f5bd686a5de84499f89a28",
      "bytes": 919
    },
    {
      "path": "characters/Heugung.md",
      "sha256": "fcd6bb605d14649d7c59f388ac5f0a3179f24e10bdc5e2b848b9d9dfc91ea6fc",
      "bytes": 695
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "4ca6b96e77a79e4c668aa89078ae6f3ee20f6c732bb2e14e10c01fc6df7d03ed",
      "bytes": 1858
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "c6e340254e0ba24a9a9cf814e9512fe91f73a0b36a818ceafcd792bbfd3b3618",
      "bytes": 622
    },
    {
      "path": "characters/Muyaho.md",
      "sha256": "481d733460c60b97e248602e8bcc5c677a9d3706e9ec1dcab436efa788bf20c6",
      "bytes": 580
    },
    {
      "path": "characters/Yohi.md",
      "sha256": "48df94a9fd77adc969e88b5ab056f6eeff67af5058f0d87ddf77436fad4da0b2",
      "bytes": 671
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "bdb519c7bf57005ad6ed9051602dc3e0ada911bab0f037f1093f98e73fa29bb7",
      "bytes": 211187
    }
  ],
  "estimated_tokens": 12718
}
-->

# Durable State Update — Chapter 685

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 685. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 685. Profile updates may replace only one
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
  "chapter": 685,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 685,
    "continuity_sources": [685],
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
    "Black Hand Fist Demon is dead.",
    "Muyaho unexpectedly ambushed the Great Snow Fiend and then disappeared into the distance.",
    "The Great Snow Fiend lost his right arm but remained capable of fighting.",
    "White Flame pierced Jin's Fire Dragon Armor and lodged in his chest.",
    "The Fire Dragon Armor is partially destroyed and will take three days to repair.",
    "Jin is bleeding and suffering massive internal and external injuries with a risk of qi deviation.",
    "Jin drove White Flame deeper into his own chest to force himself forward.",
    "Jin's final blue-white light-flame attack struck the Great Snow Fiend."
  ],
  "continuity_sources": [
    684
  ],
  "open_questions": [
    "Will Jin survive the White Flame wound, massive internal injury, and risk of qi deviation?",
    "Will the Great Snow Fiend survive Jin's final blue-white light-flame attack?",
    "What will happen to the Fire Dragon Armor while its automatic repair is unavailable for three days?"
  ],
  "safe_through": 684,
  "temporary_decisions": [
    "Render 막대한 내상 as \"Massive Internal Injury.\"",
    "Render 광염 as \"light-flames.\""
  ],
  "version": 1
}
```

## Exact glossary matches

| 진태경    | **Jin Taekyung**   |
| 암천     | **Dark Heaven**                  |
| 절정     | **Peak**          |
| 초절정    | **Supreme Peak**  |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 내공     | **internal energy**                              |                                                       |
| 열양지기   | **Scorching Yang Qi**                            | Fire-aligned qi                                       |
| 심법     | **cultivation technique**                        | Especially internal cultivation                       |
| 영약     | **elixir**                                       |                                                       |
| 제자     | **Disciple**                                 |
| 시스템              | **System**                     |
| 상태               | **Status**                     |
| 레벨               | **Level**                      |
| 경험치              | **EXP**                        |
| 명성               | **Fame**                       |
| 퀘스트              | **Quest**                      |
| 몬스터     | **monster**           |
| 노부      | **this old man / I**                                            |
| 본가      | **our family / this family**                                    |
| 귀가      | **your family**                                                 |
| 흑수 | **Black Hand** | Sadistic Dark Heaven agent and Supreme Peak master. |
| 흑수권마 | **Black Hand Fist Demon** | Sobriquet revealed by Black Hand. |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 대설귀 | **Great Snow Fiend** | Fiend who ruled Great Snow Mountain and killed Baekhwi and Venerable Wusang. |
| 흑웅 | **Heugung** | Great chieftain of the Yi people; his name literally means Black Bear. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 무야호 | **Muyaho** | Yayul Mok's White Tiger's name; it means tiger of the mighty wilds. |
| 요희 | **Yohi** | Female great chieftain of the Yao people. |
| 추종향 | **tracking scent** | Scent used to guide the messenger hawk. |
| 화시 | **fire arrow** | Flaming arrow Lee Seowol fires to signal Cheol Mubaek. |
| 회광반조 | **final rally** | Terminal burst of apparent vitality before death. |
| 갑자 | **jiazi** | Traditional sixty-year cycle. |
| 광염 | **light-flames** | Violet manifestation surrounding Cheongpung when he uses the Zaha Divine Technique. |
| 천마 | **Heavenly Demon** | Demonic title used in Jeok Cheongang's impossible comparison. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 일각 | **fifteen minutes** | Quarter of a shichen; used for the remaining completion time. |
| 아귀 | **A-Gwi** | Legendary Dogon from Sichuan. |
| 초절 | **supreme mastery** | Realm beyond Peak described as accessible only to the greatest martial artists. |
| 천주 | **Lord of Heaven** | Authority invoked by the masked attackers. |
| 꼬리 | **the “tail”** | Codename for the Black Hunter traced by Butler Kim. |
| 리치 | **Lich** | Named Monster; fallen archmage and apex undead monster. |
| 오행 | **Five Elements** | Five elemental energies whose balance governs the body. |
| 음양 | **Yin and Yang** | Paired energies whose harmony has been disrupted in Jeok Cheongang. |
| 음한지기 | **Yin-Cold Qi** | Cold-aligned energy required in the treatment elixir. |
| 마두 | **fiend** | Demonic martial masters from the Great Faction War era. |
| 수신룡 | **Water God Dragon** | Legendary name for the true master of Dongting Lake; distinct from the modern Sea Serpent. |
| 원정 | **Origin Essence** | The Water God Dragon's purified energy core, which humans call an inner core. |
| 남천마후 | **Southern Heaven Demon Empress** | Title Honglan uses when revealing her identity. |
| 신룡 | **Divine Dragon** | Title used when discussing the Water God Dragon's intentions. |
| 칠공 | **seven apertures** | The seven bodily openings through which Taekyung's overflowing heat escapes. |
| 남천 | **South Heaven** | Dark Heaven power that the Lord of Heaven orders the servants to contact. |
| 백호 | **White Tiger** | Yayul Mok's tiger companion. |
| 독혈지 | **Poisonblood Grounds** | Hidden poisonous region created by the Five Poisons Sect inside Ailao Mountain. |
| 인벤토리 | **Inventory** | System storage summoned by Jin. |
| 마후 | **Demon Empress** | Title used for the Southern Heaven Demon Empress. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 신의 | 진태경 | physician_to_benefactor | Young Master Jin | formal-polite | The Divine Physician addresses Taekyung as 진 공자 while expressing concern for his injuries. |
| 진태경 | 수신룡 | hostile martial artist to monster | you, sibu-leol eel bastard | blunt, insulting, and fearless | Taekyung directly insults the emerged Water God Dragon before attacking it. |
| 남천마후 | 진태경 | hostile_supernatural_opponent_to_young_martial_artist | Young Great Hero / Child | lighthearted and taunting | Addresses Taekyung while refusing to explain the Gate. |
| 진태경 | 남천마후 | young_martial_artist_to_hostile_demon_empress | you | hostile and determined | Promises that the Southern Heaven Demon Empress will die when they meet again. |
| 요희 | 흑웅 | Yao great chieftain to Yi great chieftain | big brother | seductive and falsely affectionate | Uses 오라버니 to flatter and manipulate Heugung. |
| 흑웅 | 요희 | Yi great chieftain to Yao great chieftain | my dear | adoring and deferential | Responds to Yohi's manipulation with open infatuation. |
| 요희 | 진태경 | Yao great chieftain to Murim Alliance pavilion master | Jin Taekyung | casual and probing | Identifies him by his full name while allowing him to keep the mask on. |
| 진태경 | 요희 | Fire Dragon Pavilion pavilion master to Yao great chieftain | you | guarded and blunt | Answers Yohi's probing questions directly while warning her about Ju Hwaran. |
| 진태경 | 백호 | human ally to intelligent spiritual beast | you | casual and familiar | Converses with White Tiger after interpreting its warning. |
| 흑웅 | 진태경 | Nanman great chieftain to Central Plains ally and covert contact | you | cautious and informal | Heugung uses 자네 in private Sound Transmission while explaining the missive and Baeksang's alleged collusion. |
| 진태경 | 흑웅 | Central Plains investigator to covert informant and prospective witness | Heugung | blunt and confrontational | Jin questions Heugung's reliability, challenges his claims, and demands proof. |
| 흑수 | 요희 | hostile captor to captive | little bitch / little girl | cruel, mocking, and predatory | Black Hand taunts Yohi, threatens her life, and says the Demon Empress covets her. |
| 요희 | 흑수 | captured tribal chieftain to torturer | you | terrified and pleading | Yohi recognizes Black Hand as the Fiend who attacked her warriors and maimed Heugung. |
| 진태경 | 흑수 | hostile_martial_opponent | Black Hand | mocking and profane | Jin sarcastically addresses Black Hand after hearing his sobriquet. |
| 흑수 | 진태경 | hostile_Dark_Heaven_agent_to_enemy_martial_artist | Blazing Flame Divine Dragon Jin Taekyung | taunting and murderous | Black Hand identifies Jin while claiming that killing him will make the sobriquet famous. |
| 흑수권마 | 대설귀 | junior hostile subordinate to senior ally | Senior | deferential but urgent and protesting | Black Hand protests the Great Snow Fiend's order to capture Jin. |
| 대설귀 | 흑수권마 | senior hostile commander to junior subordinate | you | blunt, commanding, and threatening | The Great Snow Fiend orders Black Hand to stop questioning him. |
| 진태경 | 대설귀 | hostile_martial_opponents | old man | mocking, casual, and profane | Jin taunts the Great Snow Fiend while preparing to continue the fight. |
| 대설귀 | 진태경 | hostile_martial_opponent | Jin Taekyung | cold, incredulous, and confrontational | The Great Snow Fiend addresses Jin while demanding an explanation for his survival. |

## Listed compact profiles

### Black Hand.md

# Black Hand (흑수)

- **Safe through:** Chapter 684
- **Aliases:** Black Hand Fist Demon (흑수권마)
- **Role:** Black Hand was a sadistic Dark Heaven agent and Supreme Peak master who acted under orders associated with the Southern Heaven Demon Empress before his death.
- **Personality:** Black Hand is cruel, gleeful, predatory, and fascinated by the despair of his victims.
- **Voice:** Black Hand speaks in archaic first person with drunken mockery, humiliating insults, and casual threats.
- **Relationships:** Black Hand was the captor and torturer of Yohi and Heugung and an enemy of Jin Taekyung; the Great Snow Fiend was his senior and could overrule him under the Southern Heaven Demon Empress's orders.

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 684
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** Publicly reputed to be selfless and devoted to treating patients in the lowest places.
- **Voice:** Not established.
- **Relationships:** Mungyeong is the Divine Physician's true identity, and Dong Feng is his Disciple.

### Great Snow Fiend.md

# Great Snow Fiend (대설귀)

- **Safe through:** Chapter 684
- **Aliases:** None
- **Role:** The Great Snow Fiend is the former ruler of Great Snow Mountain and a fiend who killed Baekhwi and Venerable Wusang during the Great Faction War; the Southern Heaven Demon Empress has personally ordered him to capture Jin Taekyung alive if possible.
- **Personality:** The Great Snow Fiend is cold, pragmatic, controlled, proud, and unwilling to risk his life foolishly when outnumbered.
- **Voice:** The Great Snow Fiend speaks in measured, archaic, calm, and authoritative language that becomes frost-cold when challenged.
- **Relationships:** The Great Snow Fiend is an enemy of Baeksang, Baekhwi, Venerable Wusang, the Beast Miao King, and the allied Southern Army; he is senior to Black Hand and acts under the Southern Heaven Demon Empress's orders.

### Heugung.md

# Heugung (흑웅)

- **Safe through:** Chapter 678
- **Aliases:** None
- **Role:** Heugung is the middle-aged great chieftain of the Yi people, one of Nanman's four great tribes.
- **Personality:** Heugung presents as foolish and easily flattered in public but is capable of concealed planning, disguise, and covert contact.
- **Voice:** Heugung speaks with warm enthusiasm and genuine, openly devoted affection toward Yohi.
- **Relationships:** Heugung genuinely loves Yohi and had promised to cooperate with Jin Taekyung; Black Hand captured him and Yohi, and he is now bound and unconscious with his internal energy sealed.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 684
- **Aliases:** Blazing Flame Divine Dragon; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan, Jeok Cheongang's publicly acknowledged Disciple, the Fire Gate Clan's nineteenth successor, and the Pavilion Master of the Fire Dragon Pavilion within the Murim Alliance, a Supreme Peak master with the Heavenly Martial Physique and Force, a publicly recognized S-rank-level Hunter who formally retains an A-rank license, and an escaped prisoner still facing public execution at noon in two days.
- **Personality:** Hungry, self-aware, dryly observant, pragmatic under pressure, and willing to risk himself for people he has accepted as real. Treats impossible situations like games until their human cost becomes undeniable.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, Jeok Cheongang is his Master, Mungyeong was his recent instructor, Cheongpung is his trusted companion and only true martial rival, Choi Minwoo is his subordinate and trusted manager of media and official arrangements, Ju Hwaran is a trusted Fire Dragon Pavilion member who followed him to Nanman, Chuck Hagel is an American operative allied with him in the covert anti-terror campaign, his mother and sister Hayeon are among those he protects, the Skeleton King is his friend and ally, Xiao Shen regards him as an older brother after Jin saved him, and Jin-ho is his older friend and trusted confidant.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 684
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Muyaho.md

# Muyaho (무야호)

- **Safe through:** Chapter 684
- **Aliases:** White Tiger
- **Role:** Muyaho is Yayul Mok's enormous white tiger companion and a renowned Nanman spiritual creature.
- **Personality:** Muyaho is intelligent enough to understand speech, wary of threats, and strongly food-motivated.
- **Voice:** Muyaho communicates through growls, roars, and gestures rather than human speech.
- **Relationships:** Muyaho is Yayul Mok's cherished companion and currently carries Jin while aiding his escape.

### Yohi.md

# Yohi (요희)

- **Safe through:** Chapter 684
- **Aliases:** None
- **Role:** Yohi is the female great chieftain of the Yao people, one of Nanman's four great tribes.
- **Personality:** Yohi's public presence is charismatic and captivating, drawing widespread admiration and affection.
- **Voice:** Not established.
- **Relationships:** Yohi leads the Yao people and seeks to unite Nanman's four great tribes under Yao leadership; she manipulated Heugung while following Baeksang, deliberately suppressed suspicions about his Dark Heaven ties, and is now held captive with her internal energy sealed.

## Korean source

```text
＃685화



화륵. 콰아앙!

눈앞을 가득 채운 청백색의 광염(光焰).

그리고 모든 것의 끝을 알리는 폭발음과 함께, 포물선을 그리며 날아간 노구(老軀)가 거대한 바위를 부수며 처박혔다.

콰드득.

붉게 물든 시야는 아득하고, 귓가로 전해지는 소리는 수백 리 밖에서 들려오는 것처럼 멀게 느껴진다.

하지만 어째서일까. 이런 상황에서도 의식만은 또렷하게 살아 있었다.

마치 마지막 순간 더욱 화려하게 타오르는 촛불처럼.

‘회광반조(回光返照).’

순간 대설귀의 뇌리를 스친 네 글자. 그와 동시에 뜨거운 무언가가 목구멍을 타고 흘러넘쳤다.

쿨럭.

검붉은 핏물이 하반신을 적신다. 내장 조각이 섞인 그것을 멍하니 바라보던 대설귀는 문득 생각했다. 아니, 그것은 확신이었다.

이번에는 결코 변하지 않을 확신.

‘끝났다. 전부.’

실로 역설적이게도, 인간이 스스로가 살아 있음을 확인하는 순간은 고통을 느꼈을 때다.

그러나 열양지기에 의해 전신의 혈맥이 찢겨나가고 살과 뼈가 바스라진 지금 이 순간조차, 대설귀는 고통을 느끼지 못했다.

다만 한 가지 감정을 느낄 뿐이었다.

두려움.

마침내 눈앞에 드리워진 죽음에 대한, 그리고 온통 붉게 물든 시야 속에서 가까워지는 한 사람에 대한 두려움.

“진……태경.”

파르르 떨리는 입술 사이로 신음과도 같은 목소리가 흘러나온다.

하지만 죽음을 앞둔 늙은이의 부름에도 돌아오는 대답은 없었다.

아니, 대답할 수 없었다는 것이 옳았다.

투둑. 툭.

앞으로 내딛는 한 걸음, 한 걸음마다 점점이 떨어지는 핏물. 쓰러질 듯 비틀거리는 신형과 흐릿한 눈동자.

그러나 그는, 진태경은 분명 살아 있었다.

자신의 애병(愛兵)을 늑골 어림에 박아넣은 채. 엄습하는 죽음마저 물리치며 대설귀를 향해 다가오고 있었다.

‘이게 무슨…….’

대설귀의 전신이 잘게 떨리는 이유는 죽음과 추위 때문만이 아니었다.

그는 진정 두려웠고, 한편으로는 궁금했다.

분명 같은 피륙으로 이루어진 인간일진대, 저 젊은 괴물은 어찌 아직까지도 두 발로 서있을 수 있는지. 무엇이 진태경과 자신을 지금과 같은 상황으로 만들었는지.

‘어디서부터. 무엇이 잘못되었단 말이냐.’

혈육과 수하, 벗들을 뒤로한 채 혈혈단신으로 고향을 떠난 지 어언 반백 년.

자신에게 주어진 한계를 극복하기 위하여 새로운 무공을 창안했고, 수많은 사선을 넘나들며 무공의 완성을 위해 일평생을 바쳤다.

정도(正道)? 위선자들이 지껄이는 그런 얄팍한 단어 따위는 신경 쓰지 않았다.

어떻게든 살아남아야 했고, 다시 고향으로 돌아가기 위해서는 그 누구도 무시하지 못할 만큼 강해져야 했다.

그러한 일념이 아니었다면 수십여 년 전, 암천(暗天)이 내민 손을 잡지도 않았을 것이다.



‘천주께서 이 땅에 임하시는 날. 그대가 원하는 모든 것이 이루어질 것이다.’

‘모든 것이…… 말이오?’

‘그래, 원한다면.’



대설귀는 그 말을 믿었다. 암천에 충성을 바쳤고 남천마후의 명령에 따라 팔자에도 없는 후인(後人)을 들여 자신이 직접 창안한 독문 무공을 가르쳤다.

언젠가 도래할 ‘그날’을 기다리며.

한데 어찌하여.

“그런 노부가, 내가 왜. 네놈에게 죽어야 한단 말이냐. 왜!”

쥐어짜 낸 외침과 함께 고개를 든 대설귀는 볼 수 있었다. 아직 꺼지지 않은 불꽃이 담겨 있는 한 쌍의 눈동자를.

곧이어 희미한 목소리가 그의 귓가를 파고들었다.

“나한테는 이유가 있으니까.”

“뭐?”

“어떻게든 살아남아야 하는 이유, 때로는 죽음마저 무릅써야 하는 이유.”

“……!”

“그게 가장 큰 차이야.”

나직하게 대답한 진태경은 파르르 떨리는 손을 뻗었다. 피에 젖은 손아귀가 가슴에 박힌 창을 움켜잡았다.

푸확. 투두둑.

서서히 빠져나오는 창날과 함께 흘러나온 핏물이 대설귀의 얼굴 위에 흩뿌려진다.

끔찍한 고통으로 경련하는 진태경의 모습에, 대설귀는 실성한 듯 소리 내어 웃었다.

“늦지 않게 따라오너라. 저승에서 기다리고 있을 테니.”

스윽.

대답 대신 흔들리는 창끝이 목젖에 닿는다. 진태경이 지친 목소리로 중얼거렸다.

“병신. 가서 부모님이나 찾아.”

그리고 그것이 마지막이었다.

푸욱.

목젖을 파고드는 차가운 날붙이의 감촉.

모든 것이 정지한 느려진 시간 속에서, 대설귀는 서서히 어두워지는 세상을 바라보았다.

지난 일백여 년의 세월을 모두 돌아보기에는 너무나도 짧은 시간.

빌어먹을.

끝끝내 토해 내지 못한 욕설과 함께, 한 시대를 풍미한 노괴(老怪)는 짙은 어둠 속으로 굴러떨어졌다.



* * *



창날에 목이 관통당하고도 살아남을 수 있는 사람은 없다.

설령 그자가 수 갑자에 달하는 음한지기를 지닌 초절정 고수라거나, 한 세기(世紀)에 가까운 오랜 세월을 살아온 마두라 해도 그 사실은 달라지지 않는다.

바로 지금처럼.

푸욱.

투명한 창날이 목젖을 파고들었고, 그것이 마지막이었다.

한때 대설귀라 불렸던 초절정 고수는 이제 존재하지 않는다.

눈을 부릅뜬 채 굳어 버린 시신을 멍하니 내려다보던 나는 외마디 신음을 내뱉었다.

“……아.”

끝났구나. 드디어.

뇌리를 가득 채운 생각과 함께 현실을 인지한 그 순간. 세상이 기울었다.

스륵.

아니, 기울고 있는 것은 내 몸뚱어리였다.

어떻게든 버텨 보려 했지만 불가항력(不可抗力)이다. 그나마 남아 있던 한 줌의 힘이 빠져나간 손아귀에서 창대가 미끄러졌다.

쿵.

눈앞이 아득하다. 잠시나마 잊고 있던 고통과 피로. 그리고 안도감이 파도처럼 밀려와 전신을 짓누른다.

허물어지듯 제자리에 쓰러진 나는 숨을 헐떡이며 허공을 바라보았다.



- [Lv.155 한백]을 처치하셨습니다!

- 막대한 경험치를 획득했습니다!

- 막대한 명성치를 획득했습니다!



그것이 전부였다.

흐릿한 시야 너머로 보이는 홀로그램 창의 숫자는 세 개. 그중 어디에도 레벨 업을 알리는 내용은 없었고, 시스템은 침묵했다.

그리고 나는…….

‘몰래카메라면 재미없는데.’

실없는 생각과 함께 그냥 웃고 말았다. 어떤 별다른 이유 없이, 피로 말라붙은 입꼬리가 올라가고 실소가 흘러나왔다.

시발. 몰래카메라는 무슨.

‘그래. 그렇단 말이지.’

이 몸 상태로 얼마나 버틸 수 있을까.

일각? 혹은 반 각?

‘무야호. 그 녀석이라도 살아서 도망쳤으니 다행이라고 생각해야 하나.’

희한한 일이다.

마지막까지 부여잡고 있던 희망이 무너져 내렸음에도, 지금의 마음은 나 자신조차 놀랄 만큼 담담했다.

어쩌면 나는…… 이미 어렴풋이 짐작하고 있었을지도 모르겠다.

‘행운은 연달아 찾아오지 않으니까.’

흑수권마를 처치하며 부여받은 레벨 업도 사실상 도박에 가까운 한 수였다.

경험치의 정확한 수치를 볼 수 없는 이상, 나로서는 그저 짐작할 수밖에 없다.

아, 이 정도면 레벨 업 하겠구나.

혹은 이 정도로는 부족하겠구나. 하고.

불행하게도 이번에는 후자다.

대설귀는 시스템이 알려 준 것처럼 막대한 경험치를 남기며 뒈졌지만, 독혈지까지 오는 길에 얻은 경험치와 흑수권마의 것을 합친 것보다는 모자랐다.

혹은 앞서 찾아온 행운으로 인해 레벨 업에 필요한 절대치가 늘어났든지.

그렇게 해서 나온 결론은 간단하다.

내 첫 번째 도박은 성공했고, 두 번째 도박은 실패했다. 마치 처음부터 하늘이 정해 준 운명이라도 되는 것처럼.

‘빌어먹을 운명.’

그래, 운명(運命).

나는 오래전부터 저 단어가 싫었다.

좋게 쓰일 때도 있지만, 이 세상에서 벌어지는 모든 좆 같은 일들을 뭉뚱그려 표현할 수 있는 두 글자라고 생각했기 때문이다.

간혹 인생에서 일어나는 어떤 일들은, 단순히 운명이라 치부하기에는 너무나도 가혹하고 막막하다.

마음 한구석에 간직한 어느 날의 기억처럼.



‘크흠. 저기, 김 선생?’

‘앗, 네. 교감 선생님. 그런데 갑자기 무슨 일로……?’

‘그. 수업 도중에 미안한데. 잠깐만 밖에서 이야기 좀 할까요?’



지금 생각해도 그건 마치 싸구려 흑백 영화의 한 장면 같았다.

첫 번째 씬. 헛기침과 함께 등장한 대머리 교감이 담임 선생님과 함께 나가고.

두 번째 씬. 교실 앞문에 난 유리창 사이로 어리둥절해하던 담임의 얼굴이 서서히 굳어 가는 것이 보인다.

그리고 세 번째 씬. 다시 교실로 돌아온 담임 선생님은 잠깐의 침묵 끝에, 어느 학생의 이름을 부른다.



‘태경아. 잠깐 나와 볼래?’



그렇게 나는 엑스트라 1에서 영화의 주인공이 되었다.

아니. 처음부터 주인공 따위는 바라지도 않았으니, 그 모든 것이 그저 영화의 한 장면이었다면 좋았을 것이다.

만약 그랬다면 이런 개 같은 스토리를 짜낸 각본가와 감독을 반쯤 죽여서라도 NG 사인을 내게 만들었을 테니까.

그러나 인생은 원 테이크(One Take)다.

매 순간, 매 선택에 따라 나를 중심으로 이야기가 흘러간다.

그때까지 인생에 대하여 단 한 번도 진지하게 생각해 본 적 없던 나는, 하얀 천에 뒤덮인 아버지를 보고 나서야 비로소 깨달았다.

원인은 몬스터 웨이브. 사인은 압사(壓死).

운명이라는 빌어먹을 두 글자로 인해 아버지의 이야기가 끝나고, 이제 내 이야기가 시작되었음을.

“……쿨럭.”

촤륵. 투두둑.

하지만 차가운 지면에 쓰러진 채, 칠공(七空)에서 핏물을 쏟아 내며 죽는 것을 내 이야기의 마지막 장면으로 쓰기는 싫다.

잔잔한 배경 음악과 함께 가족과 친구, 동료들의 이름이 적힌 엔딩 크레딧도 사양이다.

아직 내게는…… 이 빌어먹을 운명을 거스를 수 있는 기회가 남아 있다.

곧 잿가루가 되어 흩날릴 목숨을 다시 한번 판돈으로 올려놓을 수 있는 세 번째 기회가.

‘살고 싶다.’

머릿속의 가득 채운 단 하나의 생각.

말 그대로다. 나는 이대로 죽기 싫다. 아직 해야 할 일이, 두고 온 사람들이 너무나도 많았다.

으득.

남아 있는 힘을 쥐어짜 혀를 깨물었다. 아릿한 고통과 함께 서서히 어두워지던 시야와 정신이 조금이나마 또렷해진다.

바로 지금이다. 나는 파르르 경련하는 손을 펼치며 마음속으로 명령어를 뇌까렸다.

‘인벤토리 오픈. 소환.’

스윽.

손바닥을 통해 전해지는 서늘하면서도 부드러운 촉감. 동시에 귓가를 파고드는 상반된 시스템 알림.

띠링.



- [수신룡의 원정(元淨)]을 성공적으로 소환했습니다.



삐빅!



- [수신룡의 원정]은 일반적인 영약과는 궤를 달리하는 막대한 기운을 품고 있습니다. 복용에 극히 주의하십시오!

- 당신의 [열양지기]는 [수신룡의 원정]이 품은 물의 기운과 상극입니다! 매우 위험하니 주의를 요합니다!



나도 안다. 이게 미친 짓이라는 것 정도는.

지금 내가 하려는 시도는 대다수 내공심법의 근간이 되는 음양오행설(陰陽五行說)을 역행하는 정신 나간 짓이다.

불에 물을 붓다니. 이건 리자드를 거북왕으로 진화시키려고 하는 꼴이나 다름없다.

하지만.

‘시간이 없어.’

이제는 상극이고 나발이고 따질 때가 아니다. 일각 뒤에 피를 쏟아 내며 죽건, 원정에 담긴 힘을 감당하지 못해 터져 죽건 간에 결국 뒈지는 것은 똑같다.

차라리 실낱같을 가능성이 있는 후자에 목숨을 걸어야 한다.

울컥.

다시 한번 솟구치는 핏물을 토해 낸 나는 한 줌밖에 남지 않은 힘을 쥐어짜 상체를 일으켰다.

이어 몸이 바스러지는 듯한 통증을 참으며 가부좌를 틀고, 마지막으로 하늘을 바라봤다.

시벌, 먹구름 보게. 하필이면 하늘도 존나게 어둡다.

밤이라 그런 것도 있겠지만, 아무리 봐도 죽기 딱 싫은 날이다.

지켜보는 시선도 없고, 담배 한 대 물려줄 놈도 없다. 물론 줘 봤자 피우지도 않을 거지만.

후우.

담배 연기 대신 파르르 떨리는 숨결이 흩어진다.

잠시나마 또렷해졌던 시야가 어두워졌다고 느낀 것은, 비단 지금 시간이 깊은 밤이기 때문만은 아니다.

나는 죽어 가고 있다. 지금 이 순간에도 빠르게.

어느덧 마지막 도박을 시작할 시간이 코앞까지 들이닥쳐 있었다.

‘바로 지금.’

나는 경련이 일어나는 손을 입가에 가져갔다.

그리고 곧장 극히 정순하면서도, 위험하리만치 거대한 기운이 담긴 푸른 진주를 삼켰다.

아니, 삼키려고 했다.

어디선가 불현듯 다가온 서늘한 기운이 나를 덮치기 전까지는.

화아아악!

뭐지?

전신의 털이 솟구치는 듯한 감각과 함께, 나는 석상처럼 굳어 버렸다. 그와 동시에 한 글자가 뇌리를 스쳤다.

‘적!’

하지만 아니었다. 분명 무언가가 몸을 스쳤음에도 나는 아직 살아 있었고, 다음 순간 저 멀리서 들려온 우렁찬 포효는 내 의문을 송두리째 날려 버렸다.

- 크아아앙!

“……!”

분명 도망친 줄 알았는데. 그나마 저 녀석이라도 살아남아서 다행이라고 생각했는데.

‘돌아왔구나. 결국.’

비록 시야는 흐릿했지만, 어둠 속에서도 환히 빛나는 새하얀 동체를 알아보는 것은 그리 어렵지 않았다.

나를 향해 바람처럼 달려오는 백호의 등 위에 앉아 있는 두 사람의 모습도.

흑웅. 그리고 요희.

빠르게 가까워지는 일남일녀(一男一女)의 얼굴을 확인한 나는, 문득 잠시 잊고 있던 퀘스트를 떠올렸다.

그리고 멍하니 하늘을 바라보며 뇌까렸다.

“역시. 죽기 딱 싫은 날이라니까.”

띠링.



- 임무 : 요희 발견 (완료).

- 퀘스트, [너의 추종향이 보여]를 성공적으로 완수하셨습니다!

- 상당량의 경험치를 획득했습니다!

- 상당량의 명성치를 획득하셨습니다!

- 레벨 업!



느껴진다.

눈앞에서 흩어지는 죽음이. 상처 입고 지친 몸을 감싸 안는 따스한 온기가.

띠링. 띠링. 띠링.

먹구름 가득한 하늘 아래 울려 퍼지는 맑은 종소리를 들으며, 나는 천천히 눈을 감았다.

스륵.

보이지 않는 달빛 대신 쏟아져 내린 수마(睡魔)는, 지금껏 상대한 그 어떤 적보다 강했다.
```

## Final English reading copy

```markdown
# Chapter 685

FWOOSH. KWAANG!

Blue-white light-flames filled the Great Snow Fiend’s entire field of vision.

Then, accompanied by an explosion that announced the end of everything, an old body flew in a parabola and slammed into a massive boulder, shattering it.

KRRRUNCH.

His blood-red vision was hazy, and the sounds reaching his ears seemed to come from hundreds of *li* away.[^1]

[^1]: A *li* is a traditional unit of distance, roughly one-third of a mile.

But why?

Even in this situation, my consciousness remained startlingly clear.

Like a candle that burned brightest in its final moment.

*Final rally.*

The four characters flashed through the Great Snow Fiend’s mind.

At the same time, something hot overflowed from his throat.

COUGH.

Dark-red blood soaked his lower body. As he stared blankly at it—the blood mixed with pieces of internal organs—the Great Snow Fiend suddenly thought of something.

No. It was a certainty.

A certainty that would never change this time.

*It’s over. All of it.*

Paradoxically, the moment human beings confirm that they are alive is when they feel pain.

Yet even now, with the meridians throughout his body torn apart by Scorching Yang Qi and his flesh and bones crushed, the Great Snow Fiend felt no pain.

He felt only one emotion.

Fear.

Fear of the death finally looming before him—and fear of the one person approaching through his blood-red field of vision.

“Jin… Taekyung.”

A voice like a moan slipped between his trembling lips.

But no answer came to the old man standing before death.

No. More accurately, Jin Taekyung could not answer.

DRIP. DRIP.

With every step forward, drops of blood fell to the ground.

His body staggered as though it might collapse at any moment, and his eyes were clouded.

But he—Jin Taekyung—was unquestionably alive.

With his cherished weapon buried near his ribs, he was approaching the Great Snow Fiend while driving back even the death closing in around him.

*What is this…?*

The Great Snow Fiend’s entire body trembled faintly, and it was not solely because of death or the cold.

He was genuinely afraid.

And, at the same time, he was curious.

They were both human beings made of the same flesh and blood, so how could that young monster still be standing on two feet?

What had brought Jin Taekyung and himself to this situation?

*Where did it begin? What went wrong?*

Nearly half a century had passed since he left his homeland alone, abandoning his family, subordinates, and friends.

To overcome the limits placed upon him, he created new martial arts and devoted his entire life to perfecting them, crossing the threshold of death countless times along the way.

The righteous path?

He had never cared about such a shallow word, one that hypocrites loved to prattle about.

He had to survive by any means necessary, and to return to his homeland, he had to become strong enough that no one could ignore him.

Without that single-minded resolve, he would never have accepted the hand Dark Heaven extended to him all those decades ago.

*The day the Lord of Heaven descends upon this land, everything you desire will come true.*

*Everything…?*

*Yes. If that is what you want.*

The Great Snow Fiend had believed those words.

He had pledged his loyalty to Dark Heaven, and under the orders of the Southern Heaven Demon Empress, he had taken on a successor he had never expected to have and passed down the unique martial arts he had created himself.

All while waiting for *that day* to arrive someday.

And yet, why?

“Why should someone like this old man—why should I—die by your hand? Why!”

With that strangled cry, the Great Snow Fiend raised his head.

He saw a pair of eyes that still held an undying flame.

Then a faint voice pierced his ears.

“Because I have a reason.”

“What?”

“A reason I have to survive somehow. A reason I sometimes have to risk even death.”

“……!”

“That’s the biggest difference between us.”

Jin Taekyung answered quietly and reached out with a trembling hand.

His blood-soaked fingers closed around the spear buried in his chest.

FWOOSH. DRIP, DRIP.

As the spearhead slowly emerged, the blood flowing out with it sprayed across the Great Snow Fiend’s face.

Watching Jin Taekyung convulse from the horrible pain, the Great Snow Fiend laughed aloud as if he had lost his mind.

“Follow me soon. I’ll be waiting in the afterlife.”

SWISH.

Instead of an answer, the wavering spearhead touched his throat.

Jin Taekyung muttered in an exhausted voice.

“You idiot. Go find your parents.”

And that was the end.

THRUST.

He felt the cold blade pierce his throat.

Within the slowed passage of time, where everything had come to a stop, the Great Snow Fiend watched the world slowly darken.

It was far too short a moment to look back on the entirety of the century he had lived through.

*Damn it.*

Along with the curse he could never quite spit out, the old monster who had dominated an entire era tumbled into deep darkness.

* * *

No one could survive having their throat pierced by a spearhead.

That fact would not change even if the person were a Supreme Peak master possessing several jiazi of Yin-Cold Qi, or a fiend who had lived for nearly a century.

Just as it was now.

THRUST.

The transparent spearhead pierced his throat.

That was the end.

The Supreme Peak master once called the Great Snow Fiend no longer existed.

I stared blankly down at the corpse, its eyes wide open and its body frozen in place, then let out a short groan.

“……Ah.”

It was over.

Finally.

The moment I recognized reality along with the thought filling my mind, the world tilted.

SLIP.

No. It was my body that was tilting.

I tried to keep myself upright somehow, but there was nothing I could do. The last handful of strength remaining in my hand drained away, and the spear shaft slipped free.

THUD.

My vision grew distant.

The pain and exhaustion I had forgotten for even a moment, along with the relief, swept over me like a wave and crushed my entire body.

I collapsed where I stood and stared up into the air, gasping for breath.

> **System**
>
> - You have defeated **Level 155 Hanbaek**!
>
> - You have acquired a massive amount of **EXP**!
>
> - You have acquired a massive amount of **Fame**!

That was all.

There were three numbers in the holographic window visible through my blurred vision. None of them announced a level-up, and the System remained silent.

And I…

*This would be pretty lame if it were a hidden-camera prank.*

I laughed at the ridiculous thought.

For no particular reason, the corners of my mouth—dried stiff with blood—lifted, and a hollow chuckle escaped me.

*Fuck. Hidden-camera prank, my ass.*

*Right. So that’s how it is.*

How long could I last in this condition?

*Fifteen minutes? Or seven and a half?*

*Should I just be glad that at least Muyaho made it out alive?*

It was strange.

Even though the last hope I had clung to until the very end had collapsed, my heart remained so calm that even I was surprised.

Perhaps I had already sensed it vaguely.

*Luck doesn’t come twice in a row.*

The level-up I had received after defeating the Black Hand Fist Demon had practically been a gamble.

Since I could not see the exact amount of EXP I possessed, all I could do was make an educated guess.

*Ah. I must have enough to level up now.*

Or:

*No, this much won’t be enough.*

Unfortunately, this time it was the latter.

The Great Snow Fiend had died after leaving behind the massive amount of EXP the System had announced, but it was still less than the EXP I had acquired on the way to the Poisonblood Grounds combined with the EXP from the Black Hand Fist Demon.

Or perhaps the absolute amount required to level up had increased because of the luck that had come before.

Either way, the conclusion was simple.

My first gamble had succeeded, and my second gamble had failed.

As though Heaven had decided my fate from the beginning.

*Damn fate.*

Yes. Fate.

I had hated that word for a long time.

It could be used positively, but I had always thought it was a two-character word that could lump together every fucking thing that happened in this world.

Sometimes, the things that happened in life were too harsh and hopeless to dismiss as mere fate.

Like the memory of a certain day I kept hidden in one corner of my heart.

“Um. Mr. Kim?”

“Oh, yes. Vice Principal. But what brings you here all of a sudden…?”

“I’m sorry to interrupt your class, but could we talk outside for a moment?”

Even now, it felt like a scene from a cheap black-and-white movie.

Scene one: The bald vice principal appeared with a clearing of his throat, then left with my homeroom teacher.

Scene two: Through the glass window in the classroom’s front door, I watched my homeroom teacher’s bewildered face slowly harden.

And scene three: After returning to the classroom, my homeroom teacher called out a student’s name after a brief silence.

“Taekyung. Could you step outside for a moment?”

That was how I went from Extra Number One to the protagonist of the movie.

No.

I had never wanted to be the protagonist in the first place. If everything had only been a scene from a movie, I would have been happy.

If that had been the case, I would have half-killed the screenwriter and director who had come up with this shitty story just to force them to call for a retake.

But life is *One Take*.

With every moment and every choice, the story flows with me at its center.

Until then, I had never seriously thought about life even once.

It was only when I saw my father covered by a white sheet that I finally understood.

Cause: a monster wave.

Cause of death: crushing.

Because of the two damn characters called fate, my father’s story had ended, and mine had begun.

“……COUGH.”

SPLASH. DRIP, DRIP.

But I didn’t want the final scene of my story to be me dying on the cold ground while blood poured from my seven apertures.

I had no interest in an ending-credits sequence accompanied by soft background music and listing the names of my family, friends, and comrades.

I still had a chance to resist this damn fate.

A third chance to put my life on the table once more before it turned to ash and scattered in the wind.

*I want to live.*

That was the only thought filling my mind.

I meant it literally.

I didn’t want to die like this. There were still too many things I had to do, and too many people I had left behind.

CRUNCH.

I squeezed out what strength remained and bit down on my tongue.

The sharp pain made my fading vision and consciousness a little clearer.

This was the moment.

I spread open my trembling hand and muttered the command inside my mind.

*Inventory Open. Summon.*

SWISH.

A cool, smooth sensation traveled through my palm.

At the same time, contrasting System alerts pierced my ears.

DING.

> **System**
>
> - **Water God Dragon’s Origin Essence** has been summoned successfully!
>
> - **Water God Dragon’s Origin Essence** contains an immense reserve of qi unlike that of ordinary elixirs. Use it with extreme caution!
>
> - Your **Scorching Yang Qi** is mutually incompatible with the water qi contained in **Water God Dragon’s Origin Essence**! This is extremely dangerous. Proceed with caution!

I knew.

I knew this was crazy.

What I was about to attempt ran counter to the Yin-Yang and Five Elements theory that formed the foundation of most internal energy cultivation techniques.

Pouring water onto fire.

It was no different from trying to evolve Charmeleon into Blastoise.

But…

*I’m out of time.*

This was no time to worry about elemental incompatibility or any other bullshit.

Whether I died vomiting blood fifteen minutes from now or exploded because I couldn’t withstand the power contained within the Origin Essence, the result would be the same.

I would be dead either way.

I had to stake my life on the latter, which at least offered the sliver of a possibility.

GULP.

After vomiting another mouthful of blood, I squeezed out the tiny amount of strength left to me and raised my upper body.

Then, enduring the pain that made it feel as though my body were being crushed apart, I crossed my legs and finally looked up at the sky.

*Damn, look at those storm clouds. Of course the sky has to be fucking dark too.*

It was partly because it was nighttime, but no matter how I looked at it, this was a perfect day to hate dying.

There was no one watching over me, and no one around to put a cigarette between my lips.

Of course, even if someone had handed me one, I wouldn’t have smoked it.

WHOOSH.

Instead of cigarette smoke, my trembling breath scattered through the air.

The darkness that had begun to cloud the vision that had briefly become clear was not only because the night had grown deep.

I was dying.

And I was dying quickly, even now.

The time to begin my final gamble had already arrived at my doorstep.

*Right now.*

I brought my convulsing hand to my mouth.

Then I immediately swallowed the blue pearl filled with an extremely pure and dangerously massive energy.

Or rather, I tried to swallow it.

Until cool qi suddenly swept in from somewhere and engulfed me.

FWOOSH!

*What is this?*

With the sensation of every hair on my body standing on end, I froze like a statue.

At the same time, one word flashed through my mind.

*Enemy!*

But it wasn’t.

Something had clearly brushed against my body, yet I was still alive.

Then a thunderous roar from far away swept away all my questions.

“GRAAAAH!”

“……!”

I had thought he had escaped.

I had thought it was fortunate that at least he had survived.

*You came back. In the end.*

Although my vision was blurred, it was not difficult to recognize the snow-white body shining brightly in the darkness.

Nor was it difficult to make out the figures of two people sitting on the back of the White Tiger as it raced toward me like the wind.

Heugung.

And Yohi.

As I confirmed the faces of the approaching man and woman, I suddenly remembered the Quest I had briefly forgotten.

Then I stared blankly up at the sky and muttered:

“Just as I thought. This is a perfect day to hate dying.”

DING.

> **System**
>
> - **Mission:** Find Yohi (**Complete**).
>
> - Quest, **I Can See Your Tracking Scent**, has been completed successfully!
>
> - You have acquired a substantial amount of **EXP**!
>
> - You have acquired a substantial amount of **Fame**!
>
> - **Level Up!**

I could feel it.

The death scattering away before my eyes.

The warm presence wrapping around my wounded, exhausted body.

DING. DING. DING.

As clear bell chimes rang out beneath the storm-cloud-filled sky, I slowly closed my eyes.

SLIP.

Instead of the unseen moonlight, the demon of sleep poured down over me.

It was stronger than any opponent I had ever faced.
```
