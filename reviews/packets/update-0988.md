<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0988.txt",
      "sha256": "4572484fc1aa2c1051ea48f78c8d577b99c13cf19544be855588a955649a7e7d",
      "bytes": 12890
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "345563b648b6c611c6974a412a6ae0a87ae340690392a56bd28905115fe6654b",
      "bytes": 1469
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "d13308fe31a2c64daebd8b79b1737ef2a4f6a2f6e86338670363f6d7acf5174f",
      "bytes": 236719
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "47ee4acca927887bf1353bcee6ff2043957c98e162ad791efe3bc6a16e7c7e1e",
      "bytes": 759
    },
    {
      "path": "characters/Jeok Cheongang.md",
      "sha256": "d31bf3c2a425088e6166a018a6adeff00fa35eba7eb9bcd60f7f4b8593c5c758",
      "bytes": 1291
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "70d8e48ae072e86bc8deea5a7b543536a0070480783b3ab10495f1658b3f696a",
      "bytes": 1479
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "08f2a8fa2bdbcdd5853c0e5e26255b8f3ff6abf1cd53e8ebab5653ca12171514",
      "bytes": 622
    },
    {
      "path": "characters/Peng Cheolhu.md",
      "sha256": "dae82d11e04deeb82947e75cb33e4de74f0abc8e060d635d2832cfabdf6209bd",
      "bytes": 803
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "01a31c8e350480d5fc6f56874db538d312ebb17cba112c5bed6f9815f652a372",
      "bytes": 272857
    }
  ],
  "estimated_tokens": 10315
}
-->

# Durable State Update — Chapter 988

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
1 and safe_through 988. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 988. Profile updates may replace only one
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
  "chapter": 988,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 988,
    "continuity_sources": [988],
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
    "The Jin Family of Taiyuan is recognized as one of the Five Great Families; the fallen Murong Family is no longer among them.",
    "The System granted Jin Taekyung a level-up, 10 bonus stat points, increased Fame, and feudal-lord status; Jin Wikyung and Jin Mukyung received undisplayed healing effects and bonus buffs.",
    "The Murong survivors’ innocence and whether they can rebuild as a household remain unresolved.",
    "A Murim Alliance envoy arrived to deliver the Alliance Leader’s message to Jin Wikyung.",
    "Jin Taekyung successfully absorbed the Heavenly Power Demon’s energy and the dying giant’s lightning; the three currents are now unified, and the Middle Dantian’s summit is illuminated.",
    "Jin Taekyung lost consciousness after entering a state of no-self; the Upper Dantian remains unreached."
  ],
  "continuity_sources": [
    986,
    987
  ],
  "open_questions": [
    "What is the Alliance Leader’s message to Jin Wikyung?",
    "Are the Murong survivors innocent, and can they rebuild as a household?",
    "Why did Murong Baek suggest the Heaven Demon Lords’ plans failed and that he may have been used?",
    "Why has Dark Heaven continued costly schemes without revealing its full strength?",
    "Who was the unfamiliar, strangely familiar voice that called Taekyung’s choice wise “just like back then”?"
  ],
  "safe_through": 987,
  "temporary_decisions": [],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 진태경    | **Jin Taekyung**   |
| 적천강    | **Jeok Cheongang** |
| 팽철후    | **Peng Cheolhu**   |
| 화왕     | **Fire King**                 | Jeok Cheongang |
| 벽력도왕   | **Thunderbolt Saber King**    | Peng Cheolhu   |
| 열화문    | **Fire Gate Clan**               |
| 하북팽가   | **Hebei Peng Family**            |
| 경지     | **realm** / **realm stage**                      | Especially power level                                |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 제자     | **Disciple**                                 |
| 전각     | **pavilion**                                 | Use “hall” only when established for a specific named building |
| 극양                        | **Extreme Yang**      |
| 정마대전   | **Great Faction War**         |
| 노부      | **this old man / I**                                            |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 만년한철 | **Ten-Thousand-Year Cold Iron** | Material that destroys Pung Yang's Body-Protecting Qi when the Unnamed Sword satisfies a specific condition. |
| 갑자 | **jiazi** | Traditional sixty-year cycle. |
| 구주 | **Nine Provinces** | Traditional geographic expression used in a threat. |
| 하북 | **Hebei** | Province where Hyuk Family Textile Shop has a branch. |
| 환골탈태 | **Bone Transformation** | Advanced transformation described as optional in martial-arts novels. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 피어 | **Fear** | Monster effect that overwhelms a target’s mental fortitude. |
| 오기조원 | **Five Qi Returning to Origin** | High martial realm displayed by Jeok Cheongang. |
| 마도 | **Demonic Path** | Term raised for martial power that appears to defy common principles. |
| 삼화취정 | **Three Flowers Gather at the Crown** | Near-completed phenomenon associated with entering the Supreme Peak realm. |
| 열화 | **Blazing Flame** | Lineage term in Taekyung's declaration as the Fire King's successor. |
| 겁화 | **hellfire** | Destructive fire energy used by Taekyung. |
| 악귀 | **Fiend** | Descriptive epithet applied to the First Fiend. |
| 열화신룡 | **Blazing Flame Divine Dragon** | New sobriquet bestowed on Jin Taekyung. |
| 의지 | **Will** | System attribute that replaces Endurance after its dramatic increase. |
| 소하 | **Xiao He** | Historical civil official invoked in the same exchange. |
| 신룡 | **Divine Dragon** | Title used when discussing the Water God Dragon's intentions. |
| 만족 | **Man people** | An ethnic group mentioned by the Poison Flower Pavilion owner. |
| 화신 | **Fire God** | A local deity worshiped by one Nanman believer. |
| 육부 | **Six Ministries** | The central government ministries. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 적천강 | 진태경 | overwhelming stranger to interrogated young martial artist | you; you bastard | blunt, threatening, and taunting | Uses 너, 네놈, and 이놈 while demanding Taekyung explain Qi Sense and the System. |
| 진태경 | 적천강 | frightened young martial artist to overwhelming elder | elder | polite and fearful | Uses the honorific 어르신 while explaining that the System may have felt like a cheat. |
| 적천강 | 벽력도왕 | rival_martial_master_to_rival_martial_master | Virility Saber King | insulting and taunting | Jeok coins 정력도왕 as a taunting replacement for the established title. |
| 벽력도왕 | 적천강 | rival_martial_master_to_rival_martial_master | Jeok Cheongang | boisterous and hostile-teasing | The Thunderbolt Saber King calls Jeok by name before their argument escalates. |
| 신의 | 진태경 | physician_to_benefactor | Young Master Jin | formal-polite | The Divine Physician addresses Taekyung as 진 공자 while expressing concern for his injuries. |
| 적천강 | 신의 | senior_martial_master_to_physician | Divine Physician | blunt and familiar | Uses 신의 while recognizing Dong Feng’s medical identity. |
| 신의 | 적천강 | physician_to_legendary_martial_master | Sir Jeok | formal-deferential | Uses 적 대협 while thanking and counseling Jeok. |
| 진태경 | 청년 | celebrated Hunter to younger fellow Hunter | young man | casual, teasing, and profane | Jin addresses the young Hunter after overhearing his criticism and deliberately switches to casual speech. |
| 청년 | 진태경 | frightened junior Hunter to celebrated senior Hunter | you | fearful and deferential | The young Hunter uses 당신 while asking whether Jin is really the person he recognizes from the media. |
| 벽력도왕 | 진태경 | elder martial master to younger rival | you | boisterous and confrontational | Peng addresses Taekyung as 네놈 while discussing Peng Dojin. |
| 진태경 | 벽력도왕 | younger martial artist to senior martial master | Great Hero Peng | formal and deferential | Taekyung offers a respectful salute and addresses Peng as 팽 대협. |

## Listed compact profiles

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 987
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** He is devoted to medicine and the lives he could not save, yet remains composed and self-effacing under mortal danger.
- **Voice:** He speaks in calm, respectful, self-effacing language, framing mortality through quiet philosophical reflections.
- **Relationships:** Mungyeong is the Divine Physician's true identity, the Slaughter Saint was his Master, and Dong Feng is his Disciple.

### Jeok Cheongang.md

# Jeok Cheongang (적천강)

- **Safe through:** Chapter 987
- **Aliases:** Fire King; eighteenth Sect Leader of the Fire Gate Clan
- **Role:** Jeok Cheongang is the Fire Gate Clan’s current Sect Leader, a legendary martial master who has surpassed the Three Saints, Jin Taekyung’s Master and intended heir’s mentor, and a trusted confidant who occupies the chief seat of the Murim Alliance’s Five Kings Hall.
- **Personality:** Secretive, sharp-eyed, gruff, dryly teasing, and pathologically afraid of water; believes there is no absolute justice and hopes to make good choices while protecting those he still has.
- **Voice:** Sharp and ringing when calling out; otherwise gruff, dryly teasing, blunt, and threatening during interrogation or confrontation.
- **Relationships:** He considers Jin Taekyung his one and only Disciple and trusted confidant, and insists on protecting Taekyung while urging him not to risk his life; he warmly regards Ju Hwaran, sees Mae Jonghak as a kindred spirit, recognizes Cheongpung as Mae's grandson and successor, was close to Hong Dao, accepted Jangcheon as a Disciple before he became Jopil, remains Peng Cheolhu's rival, and once fought alongside Murong Baek, now his enemy.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 986
- **Aliases:** Blazing Flame Divine Dragon; Apostle of the Earth Mother Goddess; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan, Jeok Cheongang’s Disciple, the Fire Gate Clan’s nineteenth successor, Pavilion Master of the Fire Dragon Pavilion, a Supreme Peak master and publicly recognized S-rank-level Hunter with an A-rank license, a traveler between Murim and another world, and the World Hunter Federation’s Alliance Leader; the Emperor has appointed him Marquis of Shangshan and Thousand Captain of the Embroidered Uniform Guard.
- **Personality:** Hungry, self-aware, and dryly observant; pragmatic under pressure, willing to risk himself for others, and unwilling to excuse cruelty as the inevitable price of survival.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, and Jeok Cheongang is his Master and trusted confidant; So Gyo says he is the chosen one spoken of by the Martial God, while the Bow Saint sought him for decades and relayed the Martial God’s message to him.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 986
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Peng Cheolhu.md

# Peng Cheolhu (벽력도왕)

- **Safe through:** Chapter 986
- **Aliases:** Thunderbolt Saber King
- **Role:** Peng Cheolhu is the Thunderbolt Saber King, a Ten Kings master and Great Hero of the Hebei Peng Family.
- **Personality:** Boisterous and teasing with old friends, yet calm and accepting in the face of death; willing to give everything he has left to protect the world.
- **Voice:** Loud, blunt, confrontational, and prone to disguising embarrassment or retreat as serious martial instruction.
- **Relationships:** Long-standing rival and friend of Jeok Cheongang; close friend of Hong Dao; protective toward Hong Dao's Disciple Unnamed; father of Peng Cheolyeong; longtime friend and former youthful rival of Murong Baek.

## Korean source

```text
＃988화



어느 순간부터인가, 벽력도왕 팽철후는 소리 없이 웃고 있었다.

오랜 세월 동안 쌓아 올린 수 갑자의 공력이, 전신에 깃든 모든 힘이 녹아내리듯 사라졌음에도 주름진 입가에 맺힌 선명한 미소는 지워지지 않았다.

마치, 지금 이 순간에도 그의 시야를 밝게 물들이고 있는 휘황한 빛무리가 그러하듯이.

스아아아.

휘몰아치는 바람.

그 안에 스며든 미증유의 기운이 부풀어 오르고, 저마다의 색을 지닌 세 가지의 빛은 쉼 없이 서로를 끌어당기고 뒤섞였다.

그리고 마침내, 변화했다.

화악!

삽시간에 끓어오르는 그 뜨거운 공기 속에서, 벽력도왕은 똑똑히 보았다.

찬란하게 피어오른 세 개의 꽃봉오리를.

아니, 정확히는 가부좌를 튼 채 서서히 허공으로 떠오르고 있는 한 청년을.

‘그래, 그렇겠지.’

무림에 속한 모든 이가 꿈꿔 마지않는 삼화취정(三花聚頂)의 경지를 지켜보고 있음에도, 벽력도왕은 조금도 놀라지 않았다.

이는 과거 그가 지나왔던 길이자, 누군가의 현재였으니까.

열화신룡(烈火神龍) 진태경.

열화문의 계승자이자, 화왕 적천강의 후인.

벽력도왕은 알고 있었다. 동시에 믿고 있었다.

고작 이 년 전에야 약관을 넘긴 저 핏덩이에게 있어, 삼화취정의 경지는 더 높은 곳으로 향하기 위해 머무른 하나의 계단에 불과하다는 것을.

지금 이 순간에도, 진태경은 다음 계단을 향해 나아가고 있다는 것을.

그리고 그런 벽력도왕의 믿음은 이내 현실이 되어 나타났다.

화륵.

불현듯 타들어 가는 세 개의 꽃봉오리.

치열한 힘겨루기 끝에 칠흑처럼 어두운 기운을 집어삼킨 극양(極陽)의 화염이 다섯 개의 고리를 완성한 순간, 벽력도왕은 실소를 터트렸다.

‘삼화취정을 넘어, 오기조원(五氣朝元)이라.’

아마 진태경은 모를 것이다.

저 다섯 개의 고리에 담긴 정확한 의미를.

그러나 벽력도왕은 안다.

아니, 천하 무림인 모두가 알고 있었다.

오기조원의 경지에 발을 디뎠다는 것은, 이 광활한 구주 천하에서 왕이라 불릴 최소한의 자격을 갖추었다는 뜻이었으므로.

하지만 변화는 그것으로 끝이 아니었다.

치지직!

화염과 뇌전이 뒤얽혔다.

앞서 어둠을 집어삼킨 겁화(劫火)와 벽력(霹靂)의 싸움은 치열했고, 또한 처절했다.

허공에 떠오른 진태경의 신형이 고통으로 떨려올 만큼.

그의 전신을 중심으로 터져 나온 거대한 울림이, 전각 너머 온 사방으로 뻗어 나갈 만큼.

“갈(喝)-!”

찰나의 순간.

불현듯 터져 나온 적천강의 일갈에 사시나무처럼 떨던 몸뚱어리의 경련이 천천히 잦아들기 시작했다.

지금 느끼고 있을 끔찍한 격통을 증명하듯, 악귀처럼 일그러져 있던 얼굴에도 새로운 감정이 깃들었다.

의지.

그것은 의지였다.

부러질지언정 꺾이지 않겠다는, 이 벽을 넘어 더 높은 곳에 닿겠다는 강렬한 의지.

그리고 그러한 진태경의 의지를 느꼈을 때, 벽력도왕은 비로소 확신할 수 있었다.

‘내 선택이, 옳았다.’

어느 때보다 환한 미소가 그의 만면에 피어올랐다.

곧이어 일평생에 걸쳐 축적한 공력이, 그 길었던 세월이, 한 줌밖에 남지 않았던 생기(生氣)가 화염에 녹아드는 광경을 바라보며 벽력도왕 팽철후는 입을 열었다.

마음과는 전혀 다른, 애써 퉁명스러운 어조로.

“염병할. 열화문에 좋은 일만 해 주고 가는군.”

아득한 빛무리 속, 마침내 하나로 합쳐진 기운에 휘감긴 제자를 바라보던 늙은 스승이 대꾸했다.

“억울하면 자식이라도 더 낳지 그랬느냐. 좀 더 노력했다면 저런 녀석 하나쯤은 팽가에 나왔을지도 모를 텐데.”

“이런 정신 나간 늙은이를 봤나. 운 좋게 괴물 같은 놈을 제자로 들였다고 못 하는 소리가 없군.”

“그래. 맞다. 노부는 운이 좋았지.”

“빌어먹을. 인정하지 마.”

“어째서?”

“그렇게 쉽게 인정해 버리면 할 말이 없어지니까.”

화왕 적천강과 벽력도왕 팽철후.

두 거인은 서로를 바라보며 피식 웃었다.

“혹시 그거 기억나나?”

“기억? 뭘?”

“아마 정마대전이 끝난 직후였던가, 다 같이 모여서 기념 삼아 한잔했을 때.”

“아, 네놈이 노부에게 깝죽대다가 코피 터진 그 날?”

벽력도왕이 눈살을 찌푸렸다.

“말은 똑바로 하지. 그전까지는 막상막하였어.”

“그랬지. 한 삼십여 초까지는. 그런데 결국 처맞았잖나. 명백히 노부가 한 수 위였어.”

“……끝까지 유치하게 구는군. 사람 안 변한다는 옛말이 괜히 나온 게 아니야.”

“사람이 변하면 죽을 때가 됐다는 소리지. 여하간 노부의 완승이었다.”

“지긋지긋한 늙은이 같으니라고. 그 많은 나이는 전부 똥구멍으로 처먹었나?”

아마도 오십여 년 전이었다면, 지금쯤 분명 서로를 향해 주먹을 날리고 있었을 것이다.

하지만 두 노인은 여전히 웃는 얼굴로 서로를 바라보고 있었다.

한 사람은 마음속 깊은 곳에서 치밀어오르는 씁쓸함을 애써 감추며.

또 다른 한 사람은 오래전에 지나가 버린 세월과 다가오는 죽음을 받아들이며.

그리고 적천강은, 어느덧 새하얀 백발이 되어 버린 그를 바라보며 짐짓 얼굴을 굳혔다.

“이런 버르장머리 없는 놈을 봤나. 늙은이 취급할 거면 나이 제대로 따져서 공대(恭待)하라 그리 일렀거늘.”

“제기랄. 또 그놈의 나이 얘기로군.”

“지금까지 한 수백 번은 말했는데, 대가리가 만년한철이라 기억을 못 하는 게냐?”

“듣기 싫은 소리는 그쯤에서 집어치우게. 알겠어, 알았다고. 그깟 공대 해 주면 될 거 아니오?”

“하여간 팽가 놈들은…… 지금 뭐라고?”

문득 놀라서 말까지 멈춘 적천강의 반응에, 벽력도왕이 너털웃음을 흘렸다.

“왜, 이제는 하도 늙는 바람에 귀까지 먹으셨소? 적 형(兄).”

“……!”

“쯧쯧. 겉모습만 회춘하면 뭐 하나. 나이만 많았지 실속이 없어, 실속이.”

들으라는 듯 혀를 차는 그의 모습을, 아무런 말 없이 그저 물끄러미 응시하던 적천강이 불현듯 소리 내어 웃었다.

“어라, 왜 웃소?”

“그냥, 오래 살다 보니 이런 날도 오는구나 싶어서 그랬다. 불만 있느냐?”

“불만이야 항상 있기는 한데, 그렇다고 아우가 형에게 대들 수 있나.”

아우.

그 별것 아닌 두 글자에 가슴 한구석이 울렁이는 것은 어째서일까. 적천강은 흐릿해져 가는 입가의 미소를 애써 되살리며 입을 열었다.

“드디어 네놈이 정신을 차렸구나. 언제까지 그렇게 뻗대나 늘 궁금했었는데.”

“어허, 아우에게 네놈이라니. 적 형은 아직도 정신을 못 차린 모양이오.”

“그럼, 지금부터 팽 아우라고 부르면 되나?”

이번에는 벽력도왕이 소리 내어 웃었다.

자신이 가진 모든 것을 남김없이 비워 낸 뒤, 잔주름과 검버섯으로 가득해진 그의 얼굴 곳곳에 깊은 골이 팼다.

“아니, 그 호칭은 안 쓰는 것이 좋겠소. 적 형이 그런 말을 하니 오장육부까지 간지러워지는 기분이라.”

“이런 염병할 놈 같으니. 도대체 어느 장단에 발을 맞춰야 직성이 풀리겠느냐?”

“그래, 차라리 훨씬 낫소. 드디어 내가 아는 화왕 적천강으로 돌아오셨군.”

그제야 만족스럽게 웃어 보인 벽력도왕이, 부드러워진 어조로 입을 열었다.

“적 형.”

적천강은 대답하지 않았다.

아니, 대답할 수 없었다.

갑작스럽게 변한 벽력도왕의 어조와 표정이.

이제는 완연한 노인의 그것이 된 늙수그레한 목소리가 보이지 않는 무언가가 되어 적천강의 목을 막았기 때문이었다.

그리고 그런 적천강의 모습을, 벽력도왕은 모두 안다는 듯한 눈빛으로 바라보며 말을 이었다.

“적 형만큼은…… 변치 마시오.”

“……!”

“앞으로도, 지금까지 그러했듯이 그 모습 그대로 이 무림에 남아 주시오.”

아득한 세월이 흘렀다.

해와 달이 쉼 없이 자리를 바꾸고, 그에 맞춰 강산은 옷을 바꿔입었으며, 힘찬 울음소리로 이 세상에 태어난 이들은 흙으로 돌아갔다.

그러나 변치 않은 이들 또한 있었다.

비록 세월의 흐름에 따라 육신은 노쇠해졌을지언정, 흔들리지 않는 굳건한 마음을 지닌 그들이 있었다.

“돌이켜보면, 나는 참 운이 좋았소.”

흐릿해져 가는 벽력도왕의 눈동자에, 지난 세월이 유성처럼 스쳐 지나갔다.

일대를 호령하는 하북팽가의 핏줄로 태어나, 남부러울 것 없이 흘러간 유년 시절.

북방을 넘어 천하에까지 이름을 떨친 소싯적의 나날들.

그리고.

“그 끔찍한 전란(戰亂) 속에서도, 등을 맞대고 싸울 수 있는 벗들이 있었지.”

“……그래, 그랬지. 지금 또한 마찬가지다.”

적천강이 메마른 목소리로 대답했다. 조용히 입술을 깨문 그는 더는 웃고 있지 않았다.

“적 형.”

“말하거라. 듣고 있다.”

“혹시 기억하고 있소? 내가 버릇처럼 했던 말.”

망설임 없이 고개를 끄덕인 적천강이 입을 열었다.

“무릇 사내라면, 전장에서 당당히 죽음을 맞이해야 한다고 했지.”

“기억하고 있었구려.”

“그럴 수밖에. 하루에도 몇 번씩 말했으니까.”

“맞소. 그럴 때마다 적 형이 내 주둥이를 찢어 놓겠다며 으름장을 놓았지.”

옛 기억을 떠올린 벽력도왕은 즐겁게 웃었지만, 천둥처럼 우렁차던 웃음소리 대신 흘러나온 것은 희미한 숨결이었다.

“그 말, 취소하겠소. 막상 여기까지 와 보니…… 이런 죽음도 제법 나쁘지는 않구려.”

벽력도왕은 자꾸만 기울어지려는 고개를 힘주어 들어 올렸다.

그리고 굽어진 허리를 곧게 펴고, 똑바로 응시했다.

적천강의 어깨너머, 짙은 빛무리에 휩싸인 채 허공에 떠올라 있는 누군가를.

뿌득. 으드득.

파육음과 함께 전신 곳곳으로 번져가는 잔 떨림.

자신도 겪지 못한 환골탈태(換骨奪胎)의 과정에 들어선 진태경의 모습이, 기쁨에 물든 벽력도왕의 눈동자에 비치고 있었다.

‘등봉조극(登峰造極).’

마침내 봉우리에 올라 극을 이루었으니, 이는 지상에서 가장 드높음과 동시에 하늘과 가장 가까운 길이라.

“적 형. 보이시오?”

감격으로 떨려오는 벽력도왕의 음성에, 적천강은 고개를 돌려 자신의 제자를 바라보았다.

“그래, 보고 있다. 노부의 하나뿐인 제자이자, 네 모든 것을 물려받은 후인(後人)을.”

“그래, 그렇구려.”

죽음에 젖어든 눈동자는 이미 초점을 잃었다.

이제 벽력도왕의 눈에는 더 이상 적천강의 얼굴도, 진태경의 모습도 보이지 않았다.

하지만 그럼에도, 그는 서서히 찾아오는 어둠 속에서 꺼지지 않는 환한 빛무리를 볼 수 있었다.

“저, 저 아이는…….”

벽력도왕은 숨을 헐떡였다.

흐려지는 정신을 부여잡으며, 어둠 너머에서 또렷하게 빛나는 그것을 향해 손을 뻗었다.

자신이 남긴 미래이자, 희망을 향해.

그리고 이내, 전신을 짓누르던 모든 것을 벗어 던지고 빛을 향해 달려들었다.

이승에는 존재하지 않는, 그를 기다리고 있는 새로운 산봉우리를 향해.

죽음이라는 또 다른 등봉조극을 향해.

툭.

그 무엇에도 닿지 못한 채 힘없이 떨어지는 손끝.

조용히 눈을 감은 적천강의 입술 사이로, 나직한 음성이 흘러나왔다.

“잘 가거라. 팽가 놈아.”

아우라는 두 글자는, 언젠가 다시 만날 그 날을 위해 아껴두기로 했다.

그것이 벽력도왕, 아니 팽철후와의 마지막 약속이었으니.

적 형이 아닌, 화왕 적천강에게는 앞으로 해야 할 일들이 너무나도 많이 남아 있었으니.

화아악.

마침내 서서히 줄어들기 시작하는 빛무리를 느끼며, 적천강은 눈을 떴다.
```

## Final English reading copy

```markdown
# Chapter 988

At some point, the Thunderbolt Saber King, Peng Cheolhu, began to laugh without a sound.

Even as the several sixty-year cycles’ worth of internal energy he’d accumulated, along with every ounce of strength in his body, melted away and vanished, the clear smile at the corners of his wrinkled mouth remained.

Just like the brilliant halo of light still brightening his view in this very moment.

*Whoooosh.*

The wind howled.

The unprecedented energy seeping into it swelled. Three lights, each with its own color, endlessly drew together and mingled.

And at last, they changed.

*Whoosh!*

In the air that rapidly grew hot enough to boil, the Thunderbolt Saber King saw it clearly.

Three flower buds blossoming in radiant splendor.

No—more precisely, a young man seated cross-legged, slowly rising into the air.

*Yes. I suppose so.*

Though he was watching the realm of the Three Flowers Gather at the Crown, the dream of everyone in Murim, the Thunderbolt Saber King wasn’t surprised in the least.

He’d walked this path himself once. And it was someone else’s present.

The Blazing Flame Divine Dragon, Jin Taekyung.

The heir to the Fire Gate Clan, and the successor to the Fire King, Jeok Cheongang.

The Thunderbolt Saber King knew. And he believed it, too.

For that callow brat, who’d only passed twenty two years ago, the realm of the Three Flowers Gather at the Crown was nothing more than a step on the way to a greater height.

Even now, Jin Taekyung was moving toward the next step.

And the Thunderbolt Saber King’s belief soon became reality.

*Fwoosh.*

The three flower buds suddenly began to burn.

After an intense struggle, the Extreme Yang flames swallowed the pitch-black energy. The moment they completed five rings, the Thunderbolt Saber King let out a quiet laugh.

*Beyond the Three Flowers Gather at the Crown, he’s reached Five Qi Returning to Origin.*

Jin Taekyung probably didn’t know the exact meaning of those five rings.

But the Thunderbolt Saber King did.

No—all the martial artists beneath Heaven knew.

To set foot in the realm of Five Qi Returning to Origin meant one had attained the bare minimum qualifications to be called a king in the vast world of the Nine Provinces.

But the transformation didn’t end there.

*Crackle!*

Flame and lightning intertwined.

The fight between the hellfire that had swallowed the darkness and the lightning was fierce—and desperate.

The force of their struggle made Jin Taekyung’s body, floating in the air, tremble with pain.

A massive shockwave burst from his body and spread in every direction beyond the pavilion.

“*Hah!*”

In that instant, Jeok Cheongang’s sudden shout rang out. The body trembling like a quaking aspen slowly began to settle.

As if to prove the terrible pain he must be feeling, a new emotion appeared on his face, still twisted like a fiend’s.

Will.

It was Will.

A fierce determination to reach beyond this wall, even if it broke him—never to be bent.

When the Thunderbolt Saber King felt Jin Taekyung’s Will, he was finally certain.

*My choice was right.*

A brighter smile than ever bloomed across his face.

Watching the internal energy he’d built up over his whole life, those long years, and the last spark of life he had left melt into the flames, the Thunderbolt Saber King opened his mouth.

His tone was deliberately gruff, completely at odds with how he felt.

“Damn it. I’ve done nothing but good things for the Fire Gate Clan before I go.”

The old master, gazing at his Disciple wrapped in the energy that had finally united within the distant halo of light, answered.

“If you’re so sore about it, you should’ve had more kids. If you’d tried a little harder, maybe the Peng Family would’ve had a brat like him.”

“Would you listen to this senile old man? You took a monster for a Disciple by pure luck, and now you’re saying whatever you please.”

“That’s right. I was lucky.”

“Damn it. Don’t admit it!”

“Why not?”

“If you admit it that easily, I’ve got nothing to say.”

The Fire King, Jeok Cheongang, and the Thunderbolt Saber King, Peng Cheolhu, looked at each other and chuckled.

“Do you remember that?”

“Remember what?”

“Wasn’t it right after the Great Faction War ended? We all got together for a drink to celebrate.”

“Oh, the day you mouthed off to this old man and got a bloody nose?”

The Thunderbolt Saber King frowned.

“Get it straight. We were evenly matched until then.”

“We were. For about thirty exchanges. But you got beaten in the end, didn’t you? This old man was clearly a cut above.”

“...You’re childish to the very end. There’s a reason they say people never change.”

“If a person changes, it means they’re about to die. Anyway, it was my complete victory.”

“You insufferable old bastard. Did you eat all those years through your asshole?”

If this had happened fifty years ago, they’d surely be throwing punches at each other by now.

But the two old men continued to look at each other with smiles on their faces.

One was desperately hiding the bitterness welling up from deep inside.

The other had accepted the years that had long since passed and the death drawing near.

Then Jeok Cheongang gazed at Peng Cheolhu, whose hair had turned completely white, and deliberately scowled.

“You ill-mannered brat. I’ve told you: if you’re going to treat me like an old man, you’d better mind your manners and give me the respect my age deserves.”

“Damn it. There you go talking about age again.”

“I’ve told you hundreds of times by now. Is your skull made of Ten-Thousand-Year Cold Iron? Is that why you can’t remember?”

“Cut the talk I don’t want to hear. Fine, fine, I get it. I’ll show you some respect, all right?”

“Peng Family bastards, honestly… What did you just say?”

Jeok Cheongang stopped mid-sentence, suddenly startled. The Thunderbolt Saber King let out a hearty laugh at his reaction.

“What’s the matter? Have you gotten so old you’ve gone deaf, Jeok hyung?”

“...!”

“Tsk, tsk. What good is it to look young again? You’ve got plenty of years, but nothing to show for them.”

Jeok Cheongang stared silently at him as he clicked his tongue for all to hear. Then he suddenly laughed out loud.

“What are you laughing at?”

“Nothing. I was just thinking that after living so long, a day like this would come. Got a problem with that?”

“I always have a problem with something, but can a younger brother talk back to his hyung?”

Younger brother.

Why did those simple words make something stir in Jeok Cheongang’s chest? He forced the fading smile back onto his lips and spoke.

“You’ve finally come to your senses. I was always wondering how long you’d keep digging in your heels.”

“Now, now. Calling your younger brother ‘you’ and ‘brat’? It seems Jeok hyung still hasn’t come to his senses.”

“Then should I start calling you little brother Peng?”

This time, the Thunderbolt Saber King laughed out loud.

After emptying himself of everything he had, deep creases appeared all over his face, now covered in fine wrinkles and age spots.

“No, it’d be best if you didn’t use that title. Hearing those words from Jeok hyung makes me feel itchy down to my guts.”

“You damnable bastard. What do I have to do to satisfy you?”

“That’s much better. You’ve finally turned back into the Fire King Jeok Cheongang I know.”

Only then did the Thunderbolt Saber King smile with satisfaction. In a gentler tone, he spoke.

“Jeok hyung.”

Jeok Cheongang didn’t answer.

No—he couldn’t.

The sudden change in the Thunderbolt Saber King’s tone and expression, that aged voice now unmistakably an old man’s, became something unseen that lodged in Jeok Cheongang’s throat.

The Thunderbolt Saber King looked at him as if he understood everything and continued.

“You, at least… don’t change, Jeok hyung.”

“...!”

“From now on, just as you have until now, stay in Murim as you are.”

Long years had passed.

The sun and moon kept changing places. The mountains and rivers changed their clothes in turn, and those born into this world with vigorous cries returned to the soil.

But there were also those who didn’t change.

Though their bodies grew old with the passage of time, their hearts remained unshaken and firm.

“Looking back, I’ve been very lucky.”

In the Thunderbolt Saber King’s fading eyes, the years gone by flashed past like meteors.

Born into the Hebei Peng Family, which commanded the region, he’d spent a childhood wanting for nothing.

In his youth, his name had spread beyond the northern lands and across the world.

And then—

“Even in that terrible war, I had friends I could fight back to back with.”

“...Yes. We did. And we still do.”

Jeok Cheongang answered in a dry voice. He quietly bit his lip and was no longer smiling.

“Jeok hyung.”

“Go on. I’m listening.”

“Do you remember what I used to say out of habit?”

Jeok Cheongang nodded without hesitation and answered.

“You used to say that a man should meet death with his head held high on the battlefield.”

“You remembered.”

“How could I forget? You said it several times a day.”

“True. Every time, Jeok hyung threatened to rip my mouth open.”

The Thunderbolt Saber King laughed happily at the old memory. But instead of the thunderous laughter that had once boomed from him, only a faint breath came out.

“I take it back. Now that I’ve come this far… this kind of death isn’t so bad after all.”

The Thunderbolt Saber King forced his head upright when it kept drooping to one side.

He straightened his bent back and fixed his gaze ahead.

Over Jeok Cheongang’s shoulder, at someone floating in the air, engulfed in a deep halo of light.

*Crack. Creak.*

With the sound of flesh tearing, fine tremors spread throughout Jin Taekyung’s body.

In the Thunderbolt Saber King’s eyes, alight with joy, was Jin Taekyung, entering the process of Bone Transformation—a process even he had never experienced.

*Supreme Peak.*

At last, he’d climbed the summit and attained the ultimate. The highest place on earth, and the path closest to Heaven.

“Jeok hyung. Do you see him?”

At the Thunderbolt Saber King’s voice, trembling with emotion, Jeok Cheongang turned to look at his Disciple.

“Yes. I see him. My one and only Disciple—and the successor who has inherited everything you had.”

“Is that so?”

The Thunderbolt Saber King’s eyes, steeped in death, had already lost focus.

Now, he could no longer see Jeok Cheongang’s face or Jin Taekyung’s form.

And yet, in the darkness slowly approaching, he saw a radiant halo of light that would not go out.

“Th-that child…”

The Thunderbolt Saber King gasped for breath.

Clinging to his fading consciousness, he reached toward the thing shining clearly beyond the darkness.

Toward the future he’d left behind, toward hope.

Then he cast off everything pressing down on his body and lunged toward the light.

Toward a new mountain peak that didn’t exist in this world, waiting for him.

Toward another Supreme Peak: death.

*Thud.*

His fingertips fell limply, touching nothing.

Jeok Cheongang quietly closed his eyes. A low voice slipped between his lips.

“Farewell, you Peng bastard.”

He decided to save the words “younger brother” for the day they met again.

That had been his last promise to the Thunderbolt Saber King—or rather, to Peng Cheolhu.

And as the Fire King Jeok Cheongang, rather than Jeok hyung, he still had far too much left to do.

*Whoosh.*

Feeling the halo of light finally begin to fade, Jeok Cheongang opened his eyes.
```
