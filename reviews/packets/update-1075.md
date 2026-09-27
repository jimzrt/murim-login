<!-- packet-manifest
{
  "included": [
    {
      "path": "source/1075.txt",
      "sha256": "34a7a3467ab2fee22deba68098b5707fdfb33e4597b5f5b59429c43081065ea3",
      "bytes": 12283
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "c55e5a998ba0a39a9273349a68c70ea3e633bf4e421de75f0a86cf494a9f9f12",
      "bytes": 922
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "ddb28ab57c0989c9486f4f046aff6af84289786a1af72e74325cceb626661668",
      "bytes": 242537
    },
    {
      "path": "characters/Cheongpung.md",
      "sha256": "0ffb11c5e6ce67359d7e9f7f5d6668614d9f3dafe880a195b68bb85303d30b41",
      "bytes": 1326
    },
    {
      "path": "characters/Gung Gibang.md",
      "sha256": "62758da0e734535aa37a9a0540b8798bb3a04c2ac88bf8a0fe8adbb00a0e50f6",
      "bytes": 687
    },
    {
      "path": "characters/Jeok Cheongang.md",
      "sha256": "d509fce7803898694d462290ff58176281a46b5b851c0f1da178606ac103e52a",
      "bytes": 1502
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "897c7dfae3a0af03cf68fcef5df32450a4a34b4e593833d2bec4e0841a29ec2a",
      "bytes": 1828
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "5203b6930e8cb66b2e51a1b94b6afaec0f72a34618c6304b0d205c9165a3ea4b",
      "bytes": 623
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "fc0e22f2ecc1764fc5c1138b0a3b209e3433397150cd10ac32975d9ae735310a",
      "bytes": 284483
    }
  ],
  "estimated_tokens": 10203
}
-->

# Durable State Update — Chapter 1075

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
1 and safe_through 1075. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 1075. Profile updates may replace only one
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
  "chapter": 1075,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 1075,
    "continuity_sources": [1075],
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
    "Taekyung’s group reunited with Cheongpung and the Slaughter Saint after several months.",
    "Bow Saint recognizes the Slaughter Saint, who acts to set the changed world right.",
    "The Slaughter Saint and Cheongpung defeated the ten thousand monsters; the Slaughter Saint stopped Dark Heaven’s pursuit over nearly two days.",
    "The group reached a large lake with Gung Gibang’s group and brought a bound black-robed captive."
  ],
  "continuity_sources": [
    1074
  ],
  "open_questions": [
    "Who is the black-robed captive, and what does he know?",
    "What is the connection between Soonja and the Slaughter Saint?",
    "What does Bow Saint mean by setting everything right?",
    "What happened to the Great Sir’s boy companion?",
    "What awaits Taekyung’s group at the lakeside camp?"
  ],
  "safe_through": 1074,
  "temporary_decisions": [],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 진태경    | **Jin Taekyung**   |
| 적천강    | **Jeok Cheongang** |
| 청풍     | **Cheongpung**     |
| 살성     | **Slaughter Saint**           | —              |
| 곤륜파    | **Kunlun Sect**                  |
| 암천     | **Dark Heaven**                  |
| 남만야수궁  | **Nanman Beast Palace**          |
| 전음     | **Sound Transmission**                           | Fixed skill terminology; preserve the internal-energy mechanism when the source explains it, but do not add an explanation where it does not |
| 강호     | **martial world**                                | Prefer “Murim” where the setting itself is meant      |
| 제자     | **Disciple**                                 |
| 선배     | **Senior**                                   |
| 은인     | **Benefactor**                               |
| 시스템              | **System**                     |
| 감숙     | **Gansu**              |
| 청해     | **Qinghai**            |
| 곤륜     | **Kunlun**             |
| 대협      | **Great Hero** or **Sir** depending tone                        |
| 소협      | **Young Hero**                                                  |
| 궁기방 | **Gung Gibang** | Beggars' Sect Successor Beggar and finalist. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 갑자 | **jiazi** | Traditional sixty-year cycle. |
| 주신 | **God of Drinking** | Wipeng's drinking epithet. |
| 개방 | **Beggars' Sect** | Murim organization counted among the Nine Sects and One Gang. |
| 전하 | **His Highness** | Formal royal address for the resident prince; the official insists on this form instead of king. |
| 피어 | **Fear** | Monster effect that overwhelms a target’s mental fortitude. |
| 남만 | **Nanman** | Historical regional term used for the source of the imported ebony. |
| 후개 | **Successor Beggar** | Title of the Beggars' Sect successor competing in the preliminaries. |
| 준이 | **Jun** | Family nickname used in the form Jun's dad. |
| 살인멸구 | **Silencing the Witnesses** | Killing witnesses to prevent a secret from being exposed. |
| 살수 | **assassin** | Professional killer considered as a possible suspect. |
| 기련산 | **Qilian Mountains** | Mountain range in Qinghai from which the Qilian Three Fiends emerged. |
| 청해성 | **Qinghai** | Source form specifying Qinghai as a province. |
| 이룡 | **Two Dragons** | Collective ranking beneath the Ten Kings in Murim gossip. |
| 은잠술 | **concealment technique** | Technique used by Hidden Shadow Pavilion agents to hide their presence. |
| 이룡각 | **Two Dragons Pavilion** | Named pavilion whose masters are identified as Taekyung and Cheongpung at the chapter's close. |
| 건량 | **dry rations** | Compact travel food discussed for the Nanman journey. |
| 서리 | **seori** | Colloquial term for stealing crops or produce from a field. |
| 전서 | **missive** | A written message exchanged or delivered in secret. |
| 마력 | **magical power** | Distinct from mana; the Skeleton King's area of expertise. |
| 태청전 | **Taiqing Hall** | Hall in Kunlun where the Blood Lord and Grand Mage meet. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 청풍 | 진태경 | newly met beneficiary to benefactor | Benefactor | deferential | Cheongpung repeatedly addresses Taekyung as 은인 after receiving food. |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 진태경 | 청풍 | companion_to_young_martial_artist | Young Master Cheongpung | formal-polite | Taekyung uses 청 공자 while correcting Cheongpung's royal-etiquette mistake. |
| 적천강 | 진태경 | overwhelming stranger to interrogated young martial artist | you; you bastard | blunt, threatening, and taunting | Uses 너, 네놈, and 이놈 while demanding Taekyung explain Qi Sense and the System. |
| 진태경 | 적천강 | frightened young martial artist to overwhelming elder | elder | polite and fearful | Uses the honorific 어르신 while explaining that the System may have felt like a cheat. |
| 적천강 | 청풍 | overwhelming_elder_to_young_martial_artist | you / little punk | blunt, amused, and threatening | Jeok Cheongang uses 네, 이놈, and related blunt forms while testing Cheongpung. |
| 청풍 | 적천강 | young_martial_artist_to_overwhelming_elder | Grandpa Jeok | casual-familiar despite deference | Cheongpung uses 적 할아버지 while asking Jeok Cheongang to confirm Taekyung's condition; this is a familial form of address, not literal kinship. |
| 궁기방 | 진태경 | rival_finalists | you bastard | insulting-casual | Gung Gibang answers Taekyung's collective insult with a profane threat. |
| 진태경 | 궁기방 | rival_finalists | you three idiots | insulting-casual | Taekyung addresses Gung Gibang as part of the trio and threatens them before a duel. |
| 진태경 | 선배님들 | junior_to_senior_team_members | Seniors | polite-but-threatening | Taekyung addresses the Myeongdong Guild Team 1 Hunters while ordering them to clear a path. |
| 궁기방 | 청풍 | martial_companions | Young Hero Cheongpung | formal-polite | Gung Gibang uses 청 소협 while asking why Cheongpung is at the temporary clinic. |
| 적천강 | 궁기방 | overwhelming_elder_to_younger_martial_artist | you | blunt and threatening | Jeok Cheongang rebukes Gung Gibang for speaking informally and orders him to lie down. |
| 살성 | 청풍 | senior martial figure to younger companion | you | blunt and familiar | The Slaughter Saint scolds Cheongpung for disappearing without a word. |
| 청풍 | 살성 | younger companion to senior martial figure | old man | polite and familiar | Cheongpung apologizes and explains why he wandered off. |

## Listed compact profiles

### Cheongpung.md

# Cheongpung (청풍)

- **Safe through:** Chapter 1074
- **Aliases:** Huashan Divine Dragon
- **Role:** Cheongpung is a twenty-three-year-old Huashan outsider, the grandson and Disciple of Sword Saint Mae Jonghak, a Supreme Peak martial master known as the Huashan Divine Dragon, the creator of the snake-inspired Mimi Step footwork technique, and the master of the Azure Dragon Pavilion within the Alliance Leader's Two Dragons Pavilion.
- **Personality:** Affable, dreamy, hazy, and childlike in manner, with innocent curiosity, delight in novel public attention, a deep love of martial arts, competitive pride, unusual resistance to monster-induced Fear, and discomfort when someone copies his martial arts.
- **Voice:** Dreamy and hazy, with innocent, polite phrasing; he has begun imitating Taekyung's profanity.
- **Relationships:** Mae Jonghak is his grandfather and martial instructor, Baek Museong is his Martial Nephew, and Jin Taekyung and Hyuk Mujin are his Benefactors and companions while Taekyung is his only true martial rival; Tang Sadok has temporarily entrusted Mimi, now a large horned snake, to him, and Cheongpung is accompanying Mungyeong while learning his martial arts through observation to become stronger and adapt to this world.

### Gung Gibang.md

# Gung Gibang (궁기방)

- **Safe through:** Chapter 1074
- **Aliases:** Successor Beggar, Beggar Prince, pure-blooded beggar, ultimate beggar
- **Role:** Gung Gibang is the Beggars' Sect Successor Beggar and a unique eight-knot disciple.
- **Personality:** Vulgar, aggressive, and quick-tempered.
- **Voice:** Blunt, profane, and vividly threatening.
- **Relationships:** Gung Gibang is a rival finalist alongside Baek Woo and Zhuge Gyun who trades insults with Taekyung, uses Beggars’ Sect intelligence to investigate Tang Taesang’s murder and Dark Heaven’s Hubei forces, and has now found a trace of Honglan.

### Jeok Cheongang.md

# Jeok Cheongang (적천강)

- **Safe through:** Chapter 1074
- **Aliases:** Fire King; eighteenth Sect Leader of the Fire Gate Clan
- **Role:** Jeok Cheongang is the Fire Gate Clan’s current Sect Leader, a legendary martial master who has surpassed the Three Saints, Jin Taekyung’s Master and intended heir’s mentor, and a trusted confidant who occupies the chief seat of the Murim Alliance’s Five Kings Hall.
- **Personality:** Secretive, sharp-eyed, gruff, dryly teasing, and pathologically afraid of water; he distrusts process-first excuses when outcomes fail and hopes to make good choices while protecting those he still has.
- **Voice:** Sharp and ringing when calling out; otherwise gruff, dryly teasing, blunt, and threatening during interrogation or confrontation.
- **Relationships:** He considers Jin Taekyung his one and only Disciple and trusted confidant, and insists on protecting Taekyung while urging him not to risk his life; he warmly regards Ju Hwaran, sees Mae Jonghak as a kindred spirit, recognizes Cheongpung as Mae's grandson and successor, was close to Hong Dao, accepted Jangcheon as a Disciple before he became Jopil, and was Peng Cheolhu’s longtime rival and friend until Peng’s death, when they parted reconciled as brothers in all but blood; he once fought alongside Murong Baek, now his enemy, and personally killed his former ally the Junzi Saber after that man joined the Demonic Cult.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 1071
- **Aliases:** Blazing Flame Divine Dragon; Apostle of the Earth Mother Goddess; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan and the original owner of his current body, Jeok Cheongang’s Disciple, the Fire Gate Clan’s nineteenth successor, Pavilion Master of the Fire Dragon Pavilion, a Supreme Peak master who has reached the realm of the Ten Kings as its eleventh member and can detect and eavesdrop on nearby Sound Transmissions subject to the participants’ relative levels, and a publicly recognized S-rank-level Hunter with an A-rank license, a traveler between Murim and another world, and the World Hunter Federation’s Alliance Leader; the Emperor appointed him Marquis of Shangshan and Thousand Captain of the Embroidered Uniform Guard.
- **Personality:** Hungry, self-aware, and dryly observant; pragmatic under pressure, willing to risk himself for others, and fiercely defiant when others try to dictate his choices or survival.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, and Jeok Cheongang is his Master and trusted confidant; Hyuk Mujin trusts Taekyung to fight beside him; Taekyung trusts Sama Pyo as a friend despite suspecting his betrayal, and values him beyond his unorthodox affiliation; Peng Cheolhu regarded Taekyung as a worthy successor, and the Bow Saint relayed the Martial God’s message to him.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 1071
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

## Korean source

```text
1075화




간혹 잠시 미뤄 두었던 인연들이 한 번에 밀려올 때가 있다.

바로 지금처럼.

“무림 말학 궁기방, 여러 대선배님들을 뵙습니다!”

발바닥에 불이 나도록 달려온 궁기방의 씩씩한 인사에, 내가 모두를 대표하여 준엄한 어조로 입을 열었다.

“개방의 후개(後丐)인가. 그래, 반갑다.”

“…….”

“나는 진태경이라고 한다. 나이도 비슷하니 앞으로는 편하게 어르신이라고 칭하도록.”

“……여전하군. 여전해.”

가뜩이나 못생긴 얼굴에 더해 똥 씹은 표정까지 짓는 녀석을 향해, 나는 어깨를 으쓱해 보였다.

“당연히 여전해야지. 멀쩡했던 사람이 갑자기 변하면 죽을 때가 됐다는 뜻이니까.”

“그, 원래도 멀쩡하지는 않았던 것 같은데.”

“누구보단 훨씬 나았어.”

“도대체 어느 부분이?”

“워낙 많지만, 우선 생겨 먹은 것부터가 수준이 다르잖아.”

“빌어먹을, 그것만큼은 부정할 수가 없군.”

한숨을 푹 내쉰 궁기방이 이내 실소를 흘렸다.

“그래도 다행이다. 여전해서.”

나도 녀석을 따라 웃었다.

여전하다는 그 한 마디가, 퍽 듣기 좋아서.

그리고 나 또한 같은 생각을 하고 있어서.



* * *



궁기방과 개방의 제자들은 우리를 모닥불 근처로 이끌었다.

비록 사방에는 한겨울처럼 싸늘한 눈보라가 휘몰아치고 있었지만, 곧 곳곳에서 피어오르기 시작한 모닥불의 열기는 추위를 잊을 수 있을 만큼 따뜻했고 지칠 대로 지친 아군들의 허기와 기력을 채울 건량들이 마련되어 있었다.

그것도 부족하지 않을 만큼.

“기다리고 있었던 건가?”

“물론. 감숙성에서 지원군이 오리라는 것 정도는 충분히 예상했던 바였으니까.”

궁기방이 육포를 건네며 덧붙였다.

“그 지원군이 기련산맥을 가로질러 오는 미친 선택을 할지도 모른다는 것도.”

“너무 섣부른 판단이었나? 곤륜파에서 보낸 전서(傳書)의 내용만 보면 한시가 급해 보였는데.”

“아니, 매우 옳은 판단이었다. 실은 우리도 고작 며칠 전에야 한숨 돌릴 수 있게 됐거든.”

그 말이 거짓이 아님을 증명하듯, 궁기방의 이마에는 아직 아물지 않은 피딱지가 굳어 있었다.

명백한 전투의 흔적.

밝은 표정과 목소리를 하고 있지만, 녀석 역시 최근 생사를 오가는 격전을 치렀음이 확실했다.

“아, 이거? 별거 아니니까 신경 쓸 필요 없다. 살아남았으니 된 거지.”

씁쓸한 미소와 함께 분위기를 잡는 궁기방의 전신을 위아래로 훑은 내가 대답했다.

“응. 확실히 별거 아니긴 하네.”

“…….”

“왜?”

“딱 한 번만 맞아 줄 수 있나?”

“음. 정중하게 부탁한다면 가능할지도.”

“그렇다면 맞은 이후의 보복은?”

“아, 사람을 뭐로 보고. 당연히 있지. 죽기 직전까지 팰 거야.”

“……내가 사람을 아주 정확히 봤군.”

고개를 절레절레 흔든 궁기방이 말을 이었다.

“여하튼 끝까지 최후방에 남아 있던 것치고는 아주 싸게 먹힌 거다. 물론 그것도 때마침 시의적절한 도움이 있어서 가능했던 일이었지만.”

슬쩍 고개를 돌려 쳐다보는 궁기방의 모습에, 말없이 육포를 씹고 있던 살성이 입을 열었다.

“전부 네 녀석의 운이다. 때마침 우리가 주위에 있었으니.”

“처음에는 정말이지 깜짝 놀랐습니다. 대협께서 청풍 소협과 함께 청해에 머무르고 계실 줄은…….”

“아는 사람이 많아질수록 목적을 이루기 어려워지는 법이지. 그리고 나는 대협이 아니다.”

그 말은 즉 아군에게도 존재를 숨기고 있었다는 뜻.

담담하게 대답한 살성을 향해, 내가 불쑥 질문을 던졌다.

“그럼 저희가 남만야수궁으로 떠날 때부터 줄곧 이곳에 머무르고 계셨던 겁니까?”

“글쎄, 줄곧이라고 표현하기에는 어폐가 있군. 우리는 불과 한 달 전쯤에야 청해성에 도착했으니까.”

나는 지나간 시간과 기억을 더듬었다.

살성과 마지막으로 만난 것은 나와 청풍을 중심으로 한 이룡각(二龍閣)이 창설된 직후, 남만으로 떠날 무렵.

그렇다면 청해성에서의 한 달을 제외하더라도 지난 몇 달간 그 또한 청풍과 함께 모종의 임무를 수행했다는 뜻인데…….

‘왜 그에 대해서는 전혀 들어본 적이 없지?’

희한한 일이었다.

나는 그들과 헤어진 이후에도 남만야수궁을 시작으로 여러 굵직한 사건들에 개입해 왔고, 그럴 때마다 매번 천하의 이목이 집중되었으니까.

발이 없어도 수만 리 너머까지 뻗어 나가는 것이 바로 소문이다.

그런데 지난 몇 달의 시간 동안, 나는 살성과 청풍의 행보에 대해 별다른 이야기를 들은 적이 없었다.

그리고 눈앞의 살성 역시, 그에 대해 말하고 싶지 않아 하는 기색이 역력했다.

바로 다음 순간, 내가 뭐라 말을 꺼내기도 전에 씹고 있던 육포를 뱉었으니까.

“질기군. 근처에서 잠시 쉬고 있을 테니 찾지 마라.”

비록 어떤 직접적인 언급도 없었지만, 이러한 일련의 행동은 한마디 말보다 더 확실한 의미를 담고 있었다.

“언제나 비밀이 많은 놈이군. 저러니까 사람들한테 성질 더럽다는 소리를 듣지.”

멀어지는 살성의 뒷모습을 향해 작게 혀를 차던 적천강이 내 표정을 보고 눈살을 찌푸렸다.

“뭐냐, 그 썩은 눈빛은?”

“……제가 뭘요.”

“해명해라.”

“그, 아닙니다. 스스로가 더 잘 아시겠죠.”

“무슨 의미지?”

곤궁에 처한 나를 대신해, 모닥불 근처에 앉아 노곤한 표정을 짓고 있던 청풍이 입을 열었다.

“그야 당연히 적 할아버지께서도 만만치 않게 성질이 더럽다는 뜻 아닐까요? 그렇죠, 은인?”

“…….”

“어, 아니에요?”

당연히 맞다.

하지만 세상에는 대놓고 드러낼 수 없는 불편한 진실도 있는 법이다. 누군가에게 맞아 죽을 수도 있는 상황에서라면 더더욱.

‘청풍, 이 새끼…….’

못 본 사이에 살성에게서 신종 암살법을 배워 온 청풍을 짜게 식은 눈빛으로 쳐다보던 나는, 옆에서 느껴지는 적천강의 강렬한 시선을 애써 외면하며 화제를 돌렸다.

“그래서, 청 소협은 지난 몇 달간 어디서 뭘 하고 돌아다녔던 거야?”

“음. 작은 할아버지가 말하지 말랬어요.”

“나한텐 말해도 돼.”

“그렇게 말씀하실 줄 아시고, 상대가 설령 은인이라 할지라도 함구하랬어요.”

“진짜 괜찮다니까. 정 그러면 전음으로 살짝…….”

“우와, 신기하다. 혹시 은인께서 전음으로 말하면 괜찮다고 꼬드겨도 함구하랬어요.”

“…….”

“뭐든 말하면 죽여 버린대요. 지금까지 살인멸구(殺人滅口)만 오천 번쯤 들은 것 같아요.”

“……그냥 안 들을게.”

물론 청풍이 지금까지의 일을 전부 털어놓는다고 해서 살성이 살인멸구를 시도하지는 않겠지만, 이 정도면 더 묻지 않는 게 예의다.

음.

조금 솔직해지자면, 진짜 살인멸구를 시도할 것 같아서 쫄리는 것도 있다.

“청해성의 일은? 그것도 비밀인가?”

“아뇨. 거기에 대해서는 별말 없으셨으니까 괜찮을 것 같아요.”

천진난만하게 대답한 청풍은 지난 한 달간의 일들을 대략적으로 알려 주었다.

첫 번째로, 그 누구에게도 알리지 않고 청해성에 잠입한 이유와 목적을.

“우선적으로 내부에 있을지도 모르는 세작을 색출하기 위해서였다고?”

“네. 원래 눈앞의 적보다 등 뒤의 배신자가 더 무서운 거라고 하셨어요.”

맞는 말이다.

이미 몇 번에 걸쳐 뼈저리게 겪기도 했으니, 그 말에 담긴 의미는 결코 가볍게 다가오지 않았다.

“그래서, 세작을 찾았느냐?”

적천강의 물음에 청풍이 대답했다.

“없었어요. 적어도 우리가 파악한 바로는요.”

청풍 혼자만의 일이었다면 백 번쯤 검수해도 못 미더웠겠지만, ‘우리’라는 두 글자 안에 살성이 포함되어 있다면 충분히 믿을 만하다.

그 정도의 철두철미함도 없다면 고금제일의 살수라 불리지도 못했을 테니까.

하지만…….

“그것으로 안심하기에는 이르다. 무슨 일이 벌어질지 모르는 것이 무림이니까.”

노강호다운 연륜이 느껴지는 적천강의 한 마디에 청풍이 고개를 끄덕였다.

“맞아요. 작은 할아버지께서도 같은 생각이셨어요. 그래서 더욱 자세히 파고들기 위해 곤륜파 내부로 잠입하려고 하셨죠.”

했다, 와 하려 했다. 는 많은 차이가 있다.

그리고 그럴 수밖에 없던 이유를, 나는 이미 알고 있었다.

“때마침 암천이 쳐들어왔군. 맞지?”

“네. 순식간이었어요.”

실로 압도적인 머릿수와 전력.

곤륜파를 포함한 일부 청해 무림인들은 그 즉시 본산에서 물러나 동쪽으로 퇴각했지만, 살성과 청풍은 달랐다.

“우리는 남았어요. 그들 사이에 숨어 때를 기다렸죠.”

만약 다른 누군가가 같은 방법을 시도했다면 진작 발각되어 죽었을 것이다.

그러나 적어도 살성만큼은 예외였다.

아니, 지난 몇 달간 그의 곁에서 가르침을 이어받은 또 다른 한 사람 역시 그랬다.

“작은 할아버지께서 가르쳐 주신대로 숨을 참고, 인기척을 죽였더니 아무도 알아차리지 못하더라고요. 이렇게.”

말이 끝나기가 무섭게 흡, 하고 호흡을 멈춘 청풍의 모습에 나는 대답 대신 헛웃음을 흘렸다.

정확히는, 그 우스꽝스러운 모습과는 달리 바로 코앞에 있음에도 흡사 귀신처럼 흐릿해진 녀석의 기척 때문이었다.

‘이게 된다고? 고작 그 몇 달 만에?’

나도 모르게 그런 생각이 들었지만, 그에 대한 답은 이미 오래전부터 알고 있었다.

가능하다.

그 대상이 청풍이라면.

시스템 따위는 없어도 된다고 주장하는 듯한, 저 미친 재능의 소유자라면 그토록 까다로운 은잠술(隱潛術)을 단숨에 익힐 수도 있다.

‘저런 재능에 대해 살성의 가르침까지 이어받았으니, 놈들의 이목을 피하는 것도 가능했겠지.’

일타강사와 하늘이 내린 천재의 만남.

그리고 그 결과는 두 사람의 성공적인 잠입으로 이어졌다.

물론, 그런 그들에게도 한계는 있었지만.

“최선을 다했는데, 아쉽게도 태청전(太淸殿)까지는 갈 수 없었어요.”

“태청전이라면…….”

“곤륜산의 가장 높은 봉우리에 위치한 곳이에요. 곤륜파의 대소사가 모두 결정되는. 그런데 이상한 기운이 그 일대를 둘러싸고 있더라고요.”

마치 그때의 감각을 떠올린 듯, 청풍이 부르르 몸을 떨었다.

“뭔가가, 보이지 않는 끈적한 뭔가가 느껴졌어요. 저도 모르게 오싹해지는 기분이었죠.”

“끈적했고, 오싹해졌다고?”

“네. 몸서리가 쳐질 정도로요. 작은 할아버지께서도 그걸 느끼셨는지, 때마침 하산하는 괴물들의 틈에 섞여 되돌아오기로 하셨어요. 그렇게 며칠 뒤에 은인을 만났고요.”

말을 끝마치고도 표정이 나아지지 않는 청풍을, 나는 깊게 가라앉은 눈빛으로 응시했다.

이야기를 들은 순간 무의식적으로 머릿속에 떠오른, 두 글자를 조용히 곱씹으며.

‘마력(魔力).’

그리고 바로 그 순간.

촤아악.

짙은 안개에 휩싸인 넓고 푸른 강물 너머로, 잔잔한 파동이 일었다.
```

## Final English reading copy

```markdown
# Chapter 1075

Sometimes the people you’d put off seeing for a while all come flooding back at once.

Like right now.

“I’m Gung Gibang, a junior of Murim. It’s an honor to meet you, Seniors!”

At Gung Gibang’s hearty greeting—he’d run here so fast his feet must’ve been on fire—I spoke on everyone’s behalf in a stern voice.

“The Beggars’ Sect’s Successor Beggar, is it? Good. Pleased to meet you.”

“……”

“I’m Jin Taekyung. We’re about the same age, so from now on, feel free to call me Elder.”

“……You haven’t changed. Not one bit.”

I shrugged at the guy, whose already ugly face had twisted into an expression like he’d just swallowed shit.

“Of course I haven’t. If a perfectly normal person suddenly changes, it means he’s about to die.”

“I don’t think you were ever perfectly normal.”

“I was a lot better than you.”

“In what way, exactly?”

“There are plenty, but let’s start with our looks. We’re on completely different levels.”

“Damn it. I can’t deny that one.”

Gung Gibang let out a deep sigh, then chuckled.

“Still, I’m glad. You haven’t changed.”

I laughed along with him.

Those words—I haven’t changed—felt good to hear.

And I felt the same way.



* * *



Gung Gibang and the Beggars’ Sect disciples led us over to the campfires.

A winter-cold blizzard was howling all around us, but the warmth of the fires springing up here and there was enough to make us forget the cold. They’d also laid out dry rations to replenish our exhausted allies’ hunger and strength.

And plenty of them.

“Were you waiting for us?”

“Of course. We expected reinforcements to come from Gansu.”

Gung Gibang handed me some jerky and added:

“We even figured those reinforcements might make the insane choice of crossing the Qilian Mountains.”

“Was that too hasty a judgment? The missive from the Kunlun Sect made it sound like every second counted.”

“No. It was exactly the right call. We only got a chance to catch our breath a few days ago ourselves.”

As if to prove he wasn’t lying, a scab of dried blood still clung to Gung Gibang’s forehead.

A clear mark of battle.

His expression and voice were bright, but there was no doubt he’d recently fought a desperate battle for his life, too.

“Oh, this? It’s nothing. Don’t worry about it. I survived, and that’s what matters.”

Gung Gibang put on a somber look with a bitter smile. I looked him up and down and replied:

“Yeah. It really is nothing.”

“……”

“What?”

“Could you let me hit you just once?”

“Hmm. If you ask nicely, maybe.”

“And what about revenge afterward?”

“Oh, come on. What do you take me for? Of course there’ll be revenge. I’ll beat you within an inch of your life.”

“……I had you pegged perfectly.”

Gung Gibang shook his head and went on.

“Anyway, considering we stayed at the very rear until the end, we got off cheap. Though that was only possible thanks to some timely help.”

At Gung Gibang’s subtle glance, the Slaughter Saint—who’d been chewing on jerky without a word—spoke up.

“You were just lucky. We happened to be nearby.”

“I was truly shocked at first. I never imagined you’d be in Qinghai with Young Hero Cheongpung…”

“The more people who know about you, the harder it is to accomplish your goal. And I’m no Great Hero.”

In other words, he’d kept his existence hidden even from his own allies.

The Slaughter Saint answered calmly. I suddenly asked him:

“Then had you been here the whole time since we left for the Nanman Beast Palace?”

“I wouldn’t say the whole time. We only arrived in Qinghai about a month ago.”

I sifted through the time and memories that had passed.

The last time I’d seen the Slaughter Saint was just after the Two Dragons Pavilion was founded, with Cheongpung and me at its center, around the time we left for Nanman.

So even setting aside that month in Qinghai, he’d spent the past several months carrying out some kind of mission with Cheongpung…

*Why hadn’t I heard a single thing about it?*

It was strange.

Even after we parted, I’d been involved in one major incident after another, starting with the Nanman Beast Palace. Every time, the whole world’s attention had turned our way.

Rumors traveled tens of thousands of miles, even without legs.

And yet over the past several months, I hadn’t heard anything about the Slaughter Saint and Cheongpung’s movements.

The Slaughter Saint in front of me clearly didn’t want to talk about it, either.

Because the next moment, before I could say anything, he spat out the jerky he’d been chewing.

“Tough. I’ll be resting nearby for a bit. Don’t look for me.”

He hadn’t said anything directly, but his actions made his meaning clearer than words.

“Always keeping secrets. No wonder people say he’s got a foul temper.”

Jeok Cheongang clicked his tongue softly as he watched the Slaughter Saint walk away, then frowned at my expression.

“What’s with that rotten look?”

“……What did I do?”

“Explain yourself.”

“W-well, nothing. You probably know better than I do.”

“What’s that supposed to mean?”

Cheongpung, sitting near the campfire with a drowsy expression, spoke up on my behalf.

“Obviously, it means Grandpa Jeok’s temper is just as foul, doesn’t it, Benefactor?”

“……”

“Huh? Am I wrong?”

Of course he was right.

But some truths were better left unspoken. Especially when saying them out loud could get you beaten to death.

*Cheongpung, you little shit…*

I stared at him with a dead-eyed look. He’d been gone a while, but apparently he’d learned a new assassination technique from the Slaughter Saint. I did my best to ignore Jeok Cheongang’s scorching gaze beside me and changed the subject.

“So, Young Master Cheongpung, where have you been and what have you been doing for the past few months?”

“Hmm. Little Grandpa told me not to say.”

“You can tell me.”

“He knew you’d say that, so he told me not to say anything, even to you, Benefactor.”

“I’m telling you, it’s fine. If you’re worried, just whisper it to me with Sound Transmission…”

“Wow, that’s amazing. He even told me to keep quiet if you tried to convince me it would be fine to tell you by Sound Transmission.”

“……”

“He said he’d kill me if I said anything. I think I’ve heard ‘Silencing the Witnesses’ about five thousand times by now.”

“……Then I just won’t ask.”

Of course, the Slaughter Saint wouldn’t try to silence the witnesses just because Cheongpung told me everything that had happened so far.

But at this point, it was polite not to ask any further.

Well.

To be honest, I was also a little scared he really might try to silence the witnesses.

“What about what happened in Qinghai? Is that a secret, too?”

“No. He didn’t say anything about that, so I think it’s fine.”

Cheongpung answered innocently and gave us a rough account of what had happened over the past month.

First, why they’d infiltrated Qinghai without telling anyone, and what they’d hoped to accomplish.

“To start with, it was to find any spies who might be inside?”

“Yes. He said a traitor at your back is scarier than an enemy right in front of you.”

He was right.

I’d learned that the hard way more than once, so the meaning behind those words hit hard.

“So, did you find any spies?”

Jeok Cheongang asked. Cheongpung answered:

“No. At least, not as far as we could tell.”

If Cheongpung had been on his own, I might’ve checked a hundred times and still had my doubts. But if the Slaughter Saint was included in that *we*, then I could trust it.

He wouldn’t have been called the greatest assassin of all time if he weren’t that thorough.

Still…

“It’s too soon to relax. You never know what might happen in Murim.”

At Jeok Cheongang’s words, seasoned with the wisdom of an old martial artist, Cheongpung nodded.

“That’s right. Little Grandpa thought so, too. So he was going to infiltrate the Kunlun Sect to investigate further.”

There was a big difference between *wanted to* and *did*.

And I already knew why he hadn’t been able to.

“Dark Heaven attacked just then. Right?”

“Yes. It happened in an instant.”

They had an overwhelming advantage in numbers and strength.

Some of the Qinghai martial artists, including the Kunlun Sect, immediately withdrew from their main compound and retreated east. But the Slaughter Saint and Cheongpung did something different.

“We stayed behind. We hid among them and waited for the right moment.”

Anyone else who’d tried the same thing would’ve been discovered and killed long ago.

But the Slaughter Saint was an exception.

And so was the one other person who’d spent the past several months learning at his side.

“I held my breath and hid my presence, just like Little Grandpa taught me. No one noticed. Like this.”

As soon as he finished speaking, Cheongpung stopped breathing with a sharp *hup*. Instead of answering, I let out a hollow laugh.

Not because of how ridiculous he looked, but because his presence had faded to a ghostly blur, even though he was right in front of me.

*Can he really do that? After only a few months?*

The answer had been clear to me for a long time.

He could.

If the person in question was Cheongpung.

The owner of that insane talent, who seemed to be making a case that you didn’t need a System at all, could master such a difficult concealment technique in no time.

*With talent like that, and the Slaughter Saint teaching him, it makes sense they could slip past the enemy’s eyes.*

A star instructor and a heaven-sent genius.

And the result was a successful infiltration by the two of them.

Of course, even they had their limits.

“I did my best, but unfortunately, I couldn’t get as far as Taiqing Hall.”

“Taiqing Hall…?”

“It’s on the highest peak of Kunlun Mountain. It’s where the Kunlun Sect makes all its major decisions. But there was a strange energy surrounding the area.”

As if remembering the sensation, Cheongpung shuddered.

“I felt something… something sticky that I couldn’t see. It gave me chills before I knew it.”

“Sticky, and it gave you chills?”

“Yes. It made me shudder. Little Grandpa must have felt it too, because he decided we should slip in among the monsters that happened to be coming down the mountain and head back. A few days later, we met you, Benefactor.”

Even after he finished, Cheongpung’s expression didn’t improve. I watched him with a deep, steady gaze and quietly turned over the two words that had come to mind the moment I heard his story.

*Magical power.*

And at that very moment—

*Splash!*

A gentle ripple stirred in the wide, blue river beyond the thick veil of fog.
```
