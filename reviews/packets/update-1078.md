<!-- packet-manifest
{
  "included": [
    {
      "path": "source/1078.txt",
      "sha256": "e63feba7ff459c22b5a707afcc752aa6524ea58973581b27d0d890723e8d6c5c",
      "bytes": 12957
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "c1851c4e364189e0e80bba853f3b3c5563846d8887fb38be6feac7d9da361b96",
      "bytes": 1366
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "216361ec2af0a487c1fafa03364fc57b01a7ff585b2d9e383074e84057128d5d",
      "bytes": 242679
    },
    {
      "path": "characters/Cheongheoja.md",
      "sha256": "9db2b97584c8972c050dcc512bd445de690dfb948937ef4580e8de009236febf",
      "bytes": 544
    },
    {
      "path": "characters/Hak Woo.md",
      "sha256": "cb7dfbcf0e5ee9a1991788c08fee6c8564e4e4f186ff7da25148b14fdffe45ad",
      "bytes": 613
    },
    {
      "path": "characters/Hyuk Mujin.md",
      "sha256": "d0a026e3d72130777cab44acf9bfad35911c78f5c664550f236f5c8c740730ab",
      "bytes": 1375
    },
    {
      "path": "characters/Jeok Cheongang.md",
      "sha256": "a7e495b91753cb4b18c95ec1d505bb3ebfe1663ebb8f0deb5cb07d2c4f70ad04",
      "bytes": 1502
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "fa23ae1546b6bd298546f7af377be7aa90b1b2a0fdbf9657391040cd4dece7e0",
      "bytes": 1828
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "8400df20190971418a7fb78c84c7884a5d8e375741a642693f3fd40c96ccb041",
      "bytes": 623
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "904406ca0e1b0c39da57c11e5923df421e74498481ccb1bc16da72ee06542272",
      "bytes": 285760
    }
  ],
  "estimated_tokens": 10878
}
-->

# Durable State Update — Chapter 1078

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
1 and safe_through 1078. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 1078. Profile updates may replace only one
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
  "chapter": 1078,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 1078,
    "continuity_sources": [1078],
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
    "The group reached Qinghai Lake with Gung Gibang’s group and a bound black-robed captive.",
    "Cheongheoja, the Kunlun Sect Leader and Hak Woo’s master, arrived at Qinghai Lake; Hak Woo is safe and will meet Taekyung after they leave.",
    "Dozens of ships were arriving to carry the group’s roughly three thousand allies away from Qinghai Lake.",
    "Kunlun surrendered its headquarters to protect lives.",
    "Cheongheoja warned of a hidden ember that may bring disaster; campfires on the shore represent hope of resisting it.",
    "Ma Sanbao serves the Lord of Heaven, who granted him limited power to raise the dead; he controls beasts with a ritual bell.",
    "Ma attributes his subordinates’ near-invisible sword wounds in the reed beds to the Slaughter Saint.",
    "One of Ma’s operatives was captured, and the group’s ritual bells were taken."
  ],
  "continuity_sources": [
    1076,
    1077
  ],
  "open_questions": [
    "Who is the black-robed captive, and what does he know?",
    "What is the connection between Soonja and the Slaughter Saint?",
    "What does the Bow Saint mean by setting everything right?",
    "What happened to the Great Sir’s boy companion?",
    "What is the hidden ember Cheongheoja warned about?"
  ],
  "safe_through": 1077,
  "temporary_decisions": [],
  "version": 1
}
```

## Exact glossary matches

| 진태경    | **Jin Taekyung**   |
| 혁무진    | **Hyuk Mujin**     |
| 적천강    | **Jeok Cheongang** |
| 화왕     | **Fire King**                 | Jeok Cheongang |
| 검성     | **Sword Saint**               | Mae Jonghak    |
| 삼성     | **Three Saints**    |
| 곤륜파    | **Kunlun Sect**                  |
| 암천     | **Dark Heaven**                  |
| 절정     | **Peak**          |
| 초절정    | **Supreme Peak**  |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 중원     | **Central Plains**                               |                                                       |
| 장문인    | **Sect Leader**                              |
| 제자     | **Disciple**                                 |
| 사형     | **Senior Brother**                           |
| 사제     | **Junior Brother**                           |
| 감숙     | **Gansu**              |
| 청해     | **Qinghai**            |
| 곤륜     | **Kunlun**             |
| 본문      | **our sect / this sect**                                        |
| 도사      | **Daoist**                                                      |
| 청허자 | **Cheongheoja** | Kunlun Sect Leader. |
| 학우 | **Hak Woo** | Kunlun Sect top young prodigy known as the Kunlun Cloud Dragon; Taekyung addresses him as Hak. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 맹주 | **Alliance Leader** | Leader of the regional Murim alliance. |
| 조장 | **Captain** | Hyuk Mujin's address for Taekyung as squad leader. |
| 갑자 | **jiazi** | Traditional sixty-year cycle. |
| 시진 | **shichen** | Traditional time unit of approximately two hours. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 곤륜운룡 | **Kunlun Cloud Dragon** | Epithet of a Kunlun Sect young prodigy. |
| 초절 | **supreme mastery** | Realm beyond Peak described as accessible only to the greatest martial artists. |
| 천주 | **Lord of Heaven** | Authority invoked by the masked attackers. |
| 꼬리 | **the “tail”** | Codename for the Black Hunter traced by Butler Kim. |
| 열화 | **Blazing Flame** | Lineage term in Taekyung's declaration as the Fire King's successor. |
| 리치 | **Lich** | Named Monster; fallen archmage and apex undead monster. |
| 장강 | **Yangtze** | The river controlled by the Yangtze River Channel League. |
| 마군 | **Demon Lord** | Shortened title used for the Western Heaven Demon Lord. |
| 청해성 | **Qinghai** | Source form specifying Qinghai as a province. |
| 열화신룡 | **Blazing Flame Divine Dragon** | New sobriquet bestowed on Jin Taekyung. |
| 이동진 | **Moving Formation** | Dark Heaven's inactive long-distance transportation formation. |
| 장제자 | **Senior Disciple** | The Seafaring King's designated successor. |
| 신룡 | **Divine Dragon** | Title used when discussing the Water God Dragon's intentions. |
| 한나절 | **half a day** | Elapsed duration in Jeok's first time-loss episode. |
| 똥개 | **Ddong Gae** | Taekyung's mocking misremembering of Hwang Gae's name. |
| 마후 | **Demon Empress** | Title used for the Southern Heaven Demon Empress. |
| 화신 | **Fire God** | A local deity worshiped by one Nanman believer. |
| 언데드 | **undead** | Supernatural beings that are neither dead nor alive. |
| 진인 | **Perfected One** | Honorific for the two Kongtong Elders killed at Dunhuang. |
| 대술사 | **Grand Mage** | Title of the veiled woman leading the white-robed mages. |
| 청해호 | **Qinghai Lake** | Destination of the retreat; distinct source form from 청해성. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 혁무진 | 진태경 | squad_subordinate_to_squad_leader | Squad Leader | deferential | Hyuk Mujin says he obeys only his squad leader's orders and identifies Taekyung as the Third Young Master. |
| 진태경 | 혁무진 | squad_leader_to_squad_subordinate | Mujin | familiar-and-commanding | Taekyung calls him 무진아 while summoning him from the driver's box. |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 적천강 | 진태경 | overwhelming stranger to interrogated young martial artist | you; you bastard | blunt, threatening, and taunting | Uses 너, 네놈, and 이놈 while demanding Taekyung explain Qi Sense and the System. |
| 진태경 | 적천강 | frightened young martial artist to overwhelming elder | elder | polite and fearful | Uses the honorific 어르신 while explaining that the System may have felt like a cheat. |
| 혁무진 | 적천강 | subordinate_to_overwhelming_elder | Great Hero Jeok | deferential and fearful | Mujin uses 적 대협 while reporting Jeok’s orders and Taekyung’s awakening. |
| 적천강 | 혁무진 | overwhelming_elder_to_junior_martial_artist | you stupid fool | blunt and mocking | Jeok calls Mujin a 멍청한 놈 after knocking him down during the attempted escape. |
| 진태경 | 학우 | former_rival_to_Kunlun_young_prodigy | Hak | mocking and threatening | Taekyung uses Sound Transmission to intimidate Hak Woo into leaving. |
| 학우 | 진태경 | Kunlun_young_prodigy_to_famous_senior | Fellow Daoist Jin | formal and defensive | Hak Woo addresses Taekyung as 진 도우 while denying that he is busy. |
| 혁무진 | 조장님 | pavilion_member_to_squad_leader | Captain | deferential and dubious | Mujin questions whether the pasture should be called the Nanman Ranch instead of the Nanman Beast Palace. |
| 기자 | 진태경 | Japanese reporter to celebrated foreign Hunter | Jin-sama | formal and reverent | Japanese reporters repeatedly address Jin with the honorific 사마. |
| 진태경 | 기자 | Hunter to Japanese reporter | reporter; you | blunt and insulting | Jin rebukes a reporter for talking back after criticizing Yamamoto's delayed arrival. |
| 천주 | 대술사 | master to servant | you | commanding and authoritative | Addresses her through mind-voice, ordering her to report, raise her head, and depart. |
| 대술사 | 천주 | servant to master | Lord of Heaven | extremely deferential | Uses reverent titles and self-abasing language while reporting and pleading. |
| 적천강 | 청허자 | senior martial master to former acquaintance and younger martial master | you / Fellow Daoist | blunt and familiar | Jeok Cheongang mocks Cheongheoja for addressing him as a fellow Daoist. |
| 진태경 | 청허자 | younger martial artist to senior sect leader | Sect Leader | respectful | Uses a formal greeting and bow. |
| 청허자 | 진태경 | senior sect leader to younger martial artist | Fellow Daoist Jin | warm and polite | Greets Taekyung by surname and confirms Hak Woo is well. |

## Listed compact profiles

### Cheongheoja.md

# Cheongheoja (청허자)

- **Safe through:** Chapter 1076
- **Aliases:** None
- **Role:** Cheongheoja is the Kunlun Sect Leader and Hak Woo’s master.
- **Personality:** Warm, composed, and patient, he faces setbacks with resolve and receives even startling company with good humor.
- **Voice:** Measured and gentle, using formal Daoist courtesies and calm metaphors.
- **Relationships:** Hak Woo is his Disciple; he knows Jin Taekyung by reputation and treats him warmly.

### Hak Woo.md

# Hak Woo (학우)

- **Safe through:** Chapter 1076
- **Aliases:** Kunlun Cloud Dragon
- **Role:** Hak Woo is the Kunlun Sect's greatest young prodigy and is known as the Kunlun Cloud Dragon.
- **Personality:** He is wary, easily intimidated by threats to his hair, and eager to avoid unnecessary confrontation.
- **Voice:** He speaks politely and defensively, frequently using Daoist invocations.
- **Relationships:** Jin Taekyung is his former rival and can pressure him into leaving, while Ju Hwaran is an acquaintance he addresses formally.

### Hyuk Mujin.md

# Hyuk Mujin (혁무진)

- **Safe through:** Chapter 1074
- **Aliases:** Swift Wind Sword
- **Role:** Hyuk Mujin is a Level 50 First Rate martial artist who serves as Captain of the Jin Family's Gatekeepers, Vice Squad Leader of the Jin Dragon Squad, and an active member of the Fire Dragon Pavilion.
- **Personality:** Young, disciplined, persistent, and talented; despite being naturally fearful, he faces danger and remains loyal to the person he serves, with irreverent self-deprecation and a taste for glory. He is suspicious of Taekyung, bluntly critical of the family's disgraced third son, and an avid wuxia reader who sometimes mistakes fictional conventions for reality.
- **Voice:** Formal and clipped in official duties; with Taekyung, blunt and occasionally incredulous, while using breezy, irreverent banter to defuse tense situations.
- **Relationships:** He is loyal to Taekyung, who trusts him to act independently, especially in his home region of Shanxi and at the Jin Family of Taiyuan. As a former family gate guard, he knows the most about Head Elder Jin Baekyang among the Fire Dragon Pavilion members accompanying Taekyung. Son of the Hyuk Family Textile Shop's owners; a younger sibling means he need not inherit the business.

### Jeok Cheongang.md

# Jeok Cheongang (적천강)

- **Safe through:** Chapter 1076
- **Aliases:** Fire King; eighteenth Sect Leader of the Fire Gate Clan
- **Role:** Jeok Cheongang is the Fire Gate Clan’s current Sect Leader, a legendary martial master who has surpassed the Three Saints, Jin Taekyung’s Master and intended heir’s mentor, and a trusted confidant who occupies the chief seat of the Murim Alliance’s Five Kings Hall.
- **Personality:** Secretive, sharp-eyed, gruff, dryly teasing, and pathologically afraid of water; he distrusts process-first excuses when outcomes fail and hopes to make good choices while protecting those he still has.
- **Voice:** Sharp and ringing when calling out; otherwise gruff, dryly teasing, blunt, and threatening during interrogation or confrontation.
- **Relationships:** He considers Jin Taekyung his one and only Disciple and trusted confidant, and insists on protecting Taekyung while urging him not to risk his life; he warmly regards Ju Hwaran, sees Mae Jonghak as a kindred spirit, recognizes Cheongpung as Mae's grandson and successor, was close to Hong Dao, accepted Jangcheon as a Disciple before he became Jopil, and was Peng Cheolhu’s longtime rival and friend until Peng’s death, when they parted reconciled as brothers in all but blood; he once fought alongside Murong Baek, now his enemy, and personally killed his former ally the Junzi Saber after that man joined the Demonic Cult.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 1077
- **Aliases:** Blazing Flame Divine Dragon; Apostle of the Earth Mother Goddess; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan and the original owner of his current body, Jeok Cheongang’s Disciple, the Fire Gate Clan’s nineteenth successor, Pavilion Master of the Fire Dragon Pavilion, a Supreme Peak master who has reached the realm of the Ten Kings as its eleventh member and can detect and eavesdrop on nearby Sound Transmissions subject to the participants’ relative levels, and a publicly recognized S-rank-level Hunter with an A-rank license, a traveler between Murim and another world, and the World Hunter Federation’s Alliance Leader; the Emperor appointed him Marquis of Shangshan and Thousand Captain of the Embroidered Uniform Guard.
- **Personality:** Hungry, self-aware, and dryly observant; pragmatic under pressure, willing to risk himself for others, and fiercely defiant when others try to dictate his choices or survival.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, and Jeok Cheongang is his Master and trusted confidant; Hyuk Mujin trusts Taekyung to fight beside him; Taekyung trusts Sama Pyo as a friend despite suspecting his betrayal, and values him beyond his unorthodox affiliation; Peng Cheolhu regarded Taekyung as a worthy successor, and the Bow Saint relayed the Martial God’s message to him.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 1077
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

## Korean source

```text
1078화




청해호는 그 명칭에 담긴 뜻처럼 작은 바다와 같았다.

십여 장에 달하는 수심과 수천 리를 아우르는 광활한 면적.

원래대로라면 청해성으로 향하는 과정에서 말까지 버린 아군이 꼬박 며칠 밤낮을 도보로 이동해야 했겠지만, 곤륜파의 장문인인 청허자(淸虛子)에 이어 도착한 수십여 척의 선박은 삼천여 명이나 되는 아군을 능히 수용할 수 있었다.

촤아아악.

구름의 형태가 음각(陰刻)된 뱃머리가 힘차게 물살을 가른다.

혹독한 추위 때문인지 곳곳에 살얼음이 끼어 있는 청해호의 강물을 말없이 바라보고 있던 그때, 누군가의 음성이 내 귓가로 흘러들어 왔다.

“참으로 희한한 일이지 않습니까? 한겨울이 오려면 앞으로도 한참인데, 벌써부터 이런 광경이라니.”

고개를 돌리자 우직하게 생긴 중년의 도사가 시야에 들어온다.

아직은 낯선 얼굴과 목소리.

하지만 지금으로부터 하루 전, 선박에 오르며 짧게나마 인사를 나누었던 나는 그의 도호(道號)를 어렵지 않게 기억해 낼 수 있었다.

“아, 학소 진인.”

그 순간, 중년 도사의 입가에 걸려 있던 미소가 어색해졌다.

“학수(學洙)입니다. 학소가 아니라.”

“…….”

“…….”

삽시간에 어색해진 공기.

잠시 침묵하던 나는 어렵사리 목소리를 쥐어 짜냈다.

“그, 혹시 최근에 도호 바꾸셨어요?”

“없습니다. 곤륜에 입문(入門)한 이래로 단 한 번도.”

“그럼 혹시 입문하신 지는 얼마나…….”

“적어도 어제는 아닙니다. 이미 사십 년이 넘었으니까요.”

“그러시구나.”

“예.”

어렵지 않게 기억해 내긴 개뿔이.

할 말이 없어진 나는 하늘을 보며 중얼거렸다.

“그, 음. 날씨가 좋네요.”

우르릉, 쾅!

갑자기 뭔 지랄이 났는지 천둥 번개가 내리치기 시작한 하늘을 힐끗 바라본 학소, 아니 학수가 떨떠름한 목소리로 대꾸했다.

“험한 날씨를 좋아하시나 봅니다.”

“……그럼요. 좋아하다 못해 아주 환장하죠.”

진짜 환장하겠다.

되돌리기에는 이미 너무 멀리 와 버린 상황.

조졌음을 직감한 내가 흐린 눈빛으로 캄캄한 하늘만 응시하고 있던 그때, 학수가 피식 실소를 흘렸다.

“이해합니다. 종종 있는 일이지요. 빈도가 딱히 눈에 띄는 편은 아니라서.”

과연 곤륜파의 도사다운 너그러운 배포에, 나는 눈물을 삼키며 고개를 꾸벅 숙였다.

“……죄송합니다.”

“굳이 사과하지 않으셔도 됩니다. 안면을 튼 지 고작 한나절밖에 되지 않았으니 충분히 있을 수 있는 일 아닙니까. 더군다나 진 도우께서는 워낙 중임(重任)을 맡고 계신 몸이니.”

학수는 그 말과 함께 호탕하게 웃어 보였지만, 내가 큰 결례를 저지른 것은 변하지 않는 사실이다.

지금 눈앞에 서 있는 그가, 언젠가 청허자의 뒤를 이어 곤륜파의 장문인이 될지도 모르는 장제자(長弟子)라면 더더욱.

“도우께서 어떤 분이신지는 자주 이야기를 들어 알고 있었습니다. 셋째의 말대로 아주 유쾌하시군요.”

“셋째라고 하시면.”

“짐작하시는 바가 맞습니다. 곤륜운룡 학우, 그 아이가 제 막내 사제지요. 연배만 따지면 사제보다는 제자에 가깝지만 말입니다.”

학수의 나이는 얼핏 보기에도 불혹을 훌쩍 넘어 지천명에 가까워 보이니, 이립도 되지 않은 학우를 제자로 들였어도 이상하지 않을 나이긴 하다.

현실은 청허자를 같은 스승을 모신 사형제 지간이지만.

“여하튼 오래전부터 꼭 한번 뵙고 싶었습니다. 이런 상황에서 뵙게 된 것은 심히 안타깝지만…… 도우께서 본문을 구원코자 천릿길을 마다 않고 오셨으니 이보다 기쁜 일은 없겠지요.”

갑작스러운 학수의 공치사에, 괜히 어색해진 나는 머리를 긁적였다.

이런 감사 인사를 들은 것이 한두 번은 아니지만, 꼭 나 자신이 뭐라도 된 것처럼 영웅 행세를 하려는 마음은 없었으니까.

‘더군다나, 아직 본격적인 전투는 시작도 하지 않았고.’

물론 곧 한자리에 모일 아군의 전력은 내가 경험한 그 어느 때보다도 막강하다.

삼성(三星)에 속한 이가 둘이나 합류했고, 그에 능히 견줄 수 있는 고수인 화왕 적천강 역시 함께하고 있으니까.

거기에 더해 나를 비롯한 여러 초절정 고수와 가려 뽑은 삼천의 정예가 본진과 합류한다면, 청해성을 침범한 암천의 대군을 상대로도 충분히 우위를 점할 수 있을지도 모른다.

하지만…….

‘앞으로의 상황이 어떻게 흘러갈지는, 그 누구도 알 수 없지.’

정확한 수치를 알아낼 수는 없으나, 짐작하는 바에 의하면 현재 암천의 병력은 물경 십만에 달한다.

심지어 그 하나하나가 언데드(Undead)나 다름없는, 인간의 신체 능력을 훌쩍 뛰어넘는 괴물들.

그 사실부터가 이미 심각한 변수였지만, 언젠가부터 줄곧 내 마음을 무겁게 짓누르고 있는 두려움의 실체는 따로 있었다.

‘천주(天主).’

깊이를 짐작할 수 없는 심연 너머에 웅크린 채 천하를, 하늘과 땅을 집어삼키고 있는 절대자.

만약 머지않아 놈이 우리 앞에 나타난다면 어떤 일이 펼쳐질지, 나로서는 상상조차 할 수 없었다.

‘천주가 이번 전투에 참전할 가능성은 충분해. 이건 암천으로서도 결코 물러설 수 없는 싸움이다.’

이미 수족과 같았던 네 명의 마군(魔君)과 마후(魔后)가 내 손에 쓰러졌고, 그 과정에서 수많은 병력 손실이 발생한 상황.

이와 같은 시점에서 십만에 달하는 대군을 청해성에서 잃는다면, 천주로서도 엄청난 피해가 아닐 수 없었다.

다만, 그럼에도 불구하고 한 가지 마음에 걸리는 것이 있다면.

‘그렇다면 왜, 감숙에서 그런 말도 안 되는 선택을 한 거지?’

조용히 입술을 깨문 나는 다시금 떠올렸다.

더, 지금보다도 더 강해지라는 대술사의 그 한 마디를.

목숨이 경각에 달해 있던 나를 죽이지 않고 살려 둔, 그녀의 이해할 수 없는 행동을.

아니.

대술사에게 그러한 지시를 건넨 누군가의 의도를.

‘천주는 나의, 열화신룡 진태경의 죽음을 원치 않는다.’

피와 시체로 뒤덮인 그날의 설원에서 깨달은 진실이, 예리한 송곳이 되어 머릿속을 들쑤신다.

도무지 해결되지 않는 의문과, 믿을 수 없는 짐작을 남긴 채.

‘어쩌면. 어쩌면 천주의 진짜 목적은…….’

불현듯 찾아온 두통 속, 내가 입술을 비집고 흘러나오려는 침음성을 가까스로 삼킨 그때였다.

“……도우. 진 도우, 괜찮으십니까?”

상념을 깨트리는 한 줄이 음성.

어느덧 학수가 나를 걱정스러운 눈빛으로 바라보고 있었다.

“혹여 불편하신 곳이라도 있으신지요. 지금 안색이…….”

말꼬리를 흐리는 학수의 모습에, 나는 반사적으로 강물을 바라보았다. 

맑은 수면 위로 비친 누군가의 경직된 얼굴이, 이내 빠르게 나아가는 뱃머리를 따라 어지럽게 흩어졌다.

지금의 내 마음처럼.

“괜찮습니다. 단지 멀미 때문에 잠시.”

초절정 고수의 입에서 흘러나왔다기에는 너무나도 옹색한 변명.

그런 나를 물끄러미 바라보던 학수가 조심스럽게 입술을 뗐다.

“비록 도우의 심경을 속속들이 헤아릴 재주는 없으나, 마음속 고민이 있다면 언제든지 빈도를 찾아와 주셔도 됩니다.”

그가 특유의 호탕한 웃음을 터트리며 덧붙였다.

“물론 그리 진지하게 드린 말씀은 아니니 괘념치 마십시오. 다만 도우의 마음을 조금 더 가볍게 해 드릴 좋은 소식 정도는 알려 드릴 수는 있겠지요.”

“좋은 소식이라면.”

“지금쯤이면 중원에도 청해성의 상황이 알려졌을 터. 머지않아 검성(劍星), 아니 맹주께서 천하의 의협지사들을 이끌고 합류하실 것입니다.”

기대에 가득 찬 학수의 음성과는 달리, 잠시나마 설마 하는 마음을 품었던 나는 그 말을 듣는 순간 맥이 탁 풀리는 것을 느꼈다.

‘과연 그럴 수 있을까.’

아생연후살타(我生然后杀他).

우선은 내가 살고, 그 이후에 적을 치라는 의미가 담긴 바둑의 오랜 격언이다.

그리고 그런 의미에서 보자면, 작금의 천하는 아직 안정되지 못한 폭탄고나 마찬가지였다.

더군다나.

‘놈들에게 이동진(移動陳)이 있는 이상, 청해성 한 곳에 완전한 총력을 기울이는 건 불가능에 가깝다.’

하지만 나는 혀끝에 감도는 말을 애써 삼켰다.

우직하고, 선해 보이는 눈앞의 저 도사가 품고 있는 희망을 무참하게 꺾어 버릴 수는 없었으니까.

적어도 나 자신조차 혼란에 휩싸여 있는 지금 이 순간만큼은.

“음.”

“왜 그러십니까?”

애매한 반응에 학수가 의아한 표정으로 물었지만, 나는 내심 쓴웃음을 삼키며 고개를 저었다.

그도 곧 냉정한 현실을 알게 될 것이다. 

지금 당장이 아니더라도.

“아뇨. 생각했던 것보다도 더 좋은 소식이라 저도 모르게 그만. 그보다 목적지까지는 얼마나 남았습니까?”

“대략 반나절 정도면 도착할 듯싶습니다.”

“반나절이라, 길어야 두세 시진 정도군요.”

선박으로 청해호를 곧장 가로지른 덕분에 적지 않은 시간이 단축된 상황.

앞으로의 일을 생각하며 고개를 주억거리던 나는, 그 순간 잠시 잊고 있던 한 가지 사실을 떠올리며 중얼거렸다.

“아. 맞다.”

“뭔가 궁금하신 거라도……?”

“아닙니다. 그러고 보니 슬슬 꺼내 줄 때가 된 것 같아서요.”

“예?”

어리둥절하게 되묻는 학수를 뒤로한 채, 나는 어딘가에 있을 집요정을 향해 외쳤다.

“대가리 박아!”

잠시 후, 싸가지 없는 어느 집요정의 억울한 외침이 들려왔다.

“미치겠네, 또 왜요!”

“그냥 불러봤어. 위치 확인 차.”

허겁지겁 달려온 집요정, 아니 혁무진이 내 태연한 대답에 똥 씹은 표정을 지었다.

“아니, 제가 뭐 길거리 똥갭니까?”

“절대 아니지. 착한 똥개가 전생에 무슨 죄를 지어서 너랑 비교를 당하겠냐.”

“……진짜 내가 언젠가는 드러워서 때려치우고 만다.”

“그래, 제발 그래라.”

투덜거리는 녀석의 모습에 피식 웃은 나는 걸음을 내디디며 물었다.

“그보다, 시킨 일은 어떻게 됐어?”

“그렇지 않아도 한창 작업 중이었습니다. 생각했던 것보다 입이 무겁던데요?”

“그래서?”

“발목에 쇠사슬이랑 물통 달아서 더 무겁게 해 줬죠. 아주 좋아 죽던데요.”

“잘했네. 소질 있어.”

“뭘요. 이게 다 조장님한테 배운 거 아니겠습니까.”

혁무진과 두런두런 이야기를 나누며 걸음을 옮기던 그때, 엉겁결에 뒤따라오던 학수가 눈을 껌뻑거렸다.

“그, 실례지만 대관절 무슨 말씀을 하시는 겁니까?”

텅 빈 갑판을 어리둥절하게 바라보는 그의 모습에, 어깨를 으쓱해 보인 나는 입을 열었다.

“보시면 압니다.”

“그러니까 도대체 뭐를…….”

“무진아.”

“옙.”

드르륵.

씩씩하게 앞으로 나선 혁무진이 갑판 밖으로 튀어나온 쇠사슬을 잡아당기자, 전신이 새파랗게 질린 흑의인이 강물 속에서 튀어나왔다.

“푸헉, 말, 말하겠소! 말하겠소!”

“목숨 걸고?”

“물론, 쿨럭. 물론이오!”

꼬박 하루 밤낮을 청해호의 푸른 강물과 한 몸이 되었으니, 이제 좀 고분고분해져도 이상하지 않은 상황.

하지만 나는 심유한 눈빛으로 숨을 헐떡이는 흑의인을 응시했다.

“만약에 조금의 거짓이라도 섞여 있을 시, 너희 부모님은 유병장수한다.”

“…….”

“효자네. 안 그러냐, 무진아?”

“예엡!”

“아, 안 돼! 그것만은……!”

드르륵, 첨벙!

신명나게 대답한 혁무진이 쇠사슬을 풀자, 푸른 강물이 처절한 비명을 집어삼켰다.

장강 찍먹의 유구한 전통은, 청해호에서도 이어지고 있었다.
```

## Final English reading copy

```markdown
# Chapter 1078

Qinghai Lake was like a small sea, just as its name suggested.

Its waters were more than ten jang deep, and it stretched for thousands of li.

If things had gone as they normally would, our allies—who’d even abandoned their horses on the way to Qinghai—would have had to travel on foot for days and nights. But the dozens of ships that arrived after Cheongheoja, the Sect Leader of the Kunlun Sect, could easily carry all three thousand of them.

*Shhhhh!*

A ship’s bow, carved with the shape of a cloud, sliced forcefully through the water.

I was silently watching the river waters of Qinghai Lake, which had a thin layer of ice in places from the bitter cold, when someone’s voice drifted to my ears.

“Isn’t it strange? Winter is still a long way off, yet we’re already seeing this.”

I turned. A sturdy-looking middle-aged Daoist had entered my field of view.

A face and voice I didn’t know yet.

But I’d exchanged a brief greeting with him when I boarded the ship yesterday, and I could easily remember his Daoist name.

“Oh, Perfected One Hakso.”

The smile on the middle-aged Daoist’s face turned awkward.

“It’s Hak Su. Not Hakso.”

“……”

“……”

The air turned awkward in an instant.

After a brief silence, I forced myself to speak.

“Uh, did you happen to change your Daoist name recently?”

“No. Not once since I joined Kunlun.”

“Then how long ago did you join?”

“Certainly not yesterday. It’s been over forty years.”

“I see.”

“Yes.”

So much for easily remembering.

With nothing left to say, I looked up at the sky and muttered, “Uh, well. Nice weather.”

*Rumble, crash!*

Thunder and lightning suddenly tore across the sky, as if something had gone to hell up there. Hakso—no, Hak Su—glanced up and replied in a dubious voice.

“You must like stormy weather.”

“……Of course. I don’t just like it—I’m absolutely crazy about it.”

I’m going to lose my mind.

It was already too late to take it back.

I was staring up at the darkening sky with a distant look, realizing how badly I’d screwed up, when Hak Su let out a quiet laugh.

“I understand. It happens now and then. It’s not as though it happens so often that it stands out.”

At that generous response, befitting a Daoist of the Kunlun Sect, I swallowed back tears and bowed my head.

“……I’m sorry.”

“There’s no need to apologize. We’ve known each other for only half a day. It’s an easy mistake to make. And besides, Fellow Daoist Jin, you have a great responsibility to attend to.”

Hak Su laughed heartily, but that didn’t change the fact that I’d committed a serious discourtesy.

Especially since the man standing before me might one day succeed Cheongheoja as the Sect Leader of the Kunlun Sect. He was its Senior Disciple, after all.

“I’ve often heard about you, so I know what sort of person you are. Just as the third one said, you’re a very amusing man.”

“By the third one, you mean…”

“You’ve guessed correctly. Hak Woo, the Kunlun Cloud Dragon—that child is my youngest Junior Brother. Though by age, he’s closer to being my Disciple than my Junior Brother.”

Hak Su looked well past forty and close to fifty, so he was old enough that taking Hak Woo, who wasn’t yet thirty, as a Disciple wouldn’t have been strange.

In reality, though, they were fellow Disciples who shared the same Master, Cheongheoja.

“Regardless, I’ve wanted to meet you for a long time. It’s unfortunate that we’ve met under these circumstances…but you came all this way to save our sect. I can’t think of anything that would make me happier.”

At Hak Su’s sudden praise, I scratched my head, feeling awkward for no reason.

I’d heard words of gratitude like this more than once, but I had no desire to play the hero, as if I were someone important.

*Besides, the real battle hasn’t even begun.*

Of course, the strength of the allies about to gather in one place was greater than anything I’d ever seen.

Two of the Three Saints had joined us, and the Fire King Jeok Cheongang—a master who could hold his own against them—was here as well.

If several other Supreme Peak masters, myself included, and our handpicked three thousand elites joined the main force, we might even have the upper hand against Dark Heaven’s massive army invading Qinghai.

But…

*No one can know how things will unfold from here.*

I couldn’t get an exact figure, but from what I could tell, Dark Heaven’s forces now numbered a hundred thousand.

And every last one of them was a monster, no different from the undead, with physical abilities far beyond an ordinary human’s.

That alone was a serious variable. But the real source of the fear weighing on my mind lately was something else.

*The Lord of Heaven.*

An absolute being lurking beyond an abyss of unfathomable depth, swallowing the world—the heavens and the earth.

I couldn’t even imagine what would happen if that bastard appeared before us soon.

*There’s a good chance the Lord of Heaven will take part in this battle. Even Dark Heaven can’t afford to back down from it.*

Four Demon Lords and a Demon Empress, who’d been like his own limbs, had already fallen to my hand, and we’d inflicted heavy losses on his forces along the way.

If he lost an army of a hundred thousand in Qinghai, the Lord of Heaven would suffer an enormous blow.

And yet, one thing still bothered me.

*Then why make such an absurd choice in Gansu?*

I quietly bit my lip and recalled the Grand Mage’s words.

*Get stronger. Even stronger than you are now.*

I remembered how she’d let me live instead of killing me, when I’d been on the verge of death.

No.

I remembered the intent of whoever had given the Grand Mage that order.

*The Lord of Heaven doesn’t want me—Jin Taekyung, the Blazing Flame Divine Dragon—to die.*

The truth I’d realized on that snowfield, covered in blood and corpses, jabbed at my mind like a sharp awl.

Leaving behind questions I couldn’t answer and suspicions I couldn’t believe.

*Maybe. Maybe the Lord of Heaven’s real purpose is…*

A headache came on without warning. I barely managed to swallow the groan that was about to escape my lips.

“……Fellow Daoist. Fellow Daoist Jin, are you all right?”

A voice broke through my thoughts.

At some point, Hak Su had begun looking at me with concern.

“Are you feeling unwell? You look…”

As his voice trailed off, I reflexively looked down at the water.

A stiff face reflected on the clear surface, then scattered in the wake of the speeding ship.

Just like my thoughts.

“I’m fine. Just a little seasick.”

A feeble excuse, especially coming from a Supreme Peak master.

Hak Su watched me for a moment before carefully parting his lips.

“I can’t claim to understand everything you’re feeling, but if there’s something weighing on your heart, you can come to me anytime.”

He let out his characteristic hearty laugh, then added:

“Of course, I wasn’t being entirely serious, so don’t worry about it. But I can at least tell you some good news that might lighten your heart a little.”

“What good news?”

“By now, word of what’s happening in Qinghai must have reached the Central Plains. Before long, the Sword Saint—no, the Alliance Leader—will lead the righteous warriors of the world here to join us.”

For a moment, I’d thought, *Could it be?* But when I heard what Hak Su meant by good news, my strength drained away.

*Could that really happen?*

*First secure yourself, then strike your enemy.*

It was an old saying from Go, meaning that you should first make sure you survive, then attack your opponent.

And in that sense, the world was like a bomb that hadn’t been defused.

Besides…

*As long as they have the Moving Formation, it’s almost impossible for us to commit all our forces to Qinghai.*

But I forced myself to swallow the words on the tip of my tongue.

I couldn’t crush the hope held by the honest, kind-looking Daoist before me.

At least not while I was still confused myself.

“Hmm.”

“Is something wrong?”

Hak Su asked, looking puzzled at my ambiguous response. I swallowed a bitter smile and shook my head.

He’d learn the cold truth soon enough.

Even if not right now.

“No. That’s even better news than I expected. It just caught me off guard. Anyway, how much farther to our destination?”

“About half a day, I think.”

“Half a day. So, two or three shichen at most.”

We’d saved a considerable amount of time by crossing Qinghai Lake directly by ship.

I nodded, thinking about what lay ahead, then muttered as I remembered something I’d almost forgotten.

“Oh, right.”

“Is there something you’re curious about?”

“No. I was just thinking it’s about time to haul him out.”

“Pardon?”

Ignoring Hak Su’s bewildered question, I shouted toward the house elf somewhere nearby.

“Head down!”

A moment later, I heard an indignant shout from a rude house elf.

“Damn it, why now?!”

“I just felt like calling you. Wanted to check your location.”

Hyuk Mujin came running over in a hurry. At my unbothered answer, he scowled like he’d swallowed shit.

“Am I some kind of stray dog?”

“Absolutely not. What sin did a good dog commit in a past life to deserve being compared to you?”

“……One day I’m going to quit this filthy job, I swear.”

“Good. Please do.”

I chuckled at his grumbling and started walking.

“Anyway, how’s the job I gave you going?”

“I was just in the middle of working on it. He’s a lot tighter-lipped than I expected.”

“And?”

“I attached a chain and a water jug to his ankle to make him even heavier. He looked like he was having the time of his life.”

“Good work. You’ve got a knack for it.”

“What can I say? I learned it all from you, Captain.”

As I walked along, chatting with Hyuk Mujin, Hak Su followed behind us, caught up in the situation. He blinked.

“Excuse me, but what exactly are you talking about?”

I shrugged at the sight of him staring blankly at the empty deck.

“You’ll see.”

“But what exactly…”

“Mujin.”

“Yes, sir.”

*Rrrrattle.*

Hyuk Mujin stepped forward briskly and grabbed a chain sticking out over the side of the deck. As he pulled, a man in black, his whole body pale blue, emerged from the water.

“Gah! I-I’ll talk! I’ll talk!”

“On your life?”

“Of course—cough—of course!”

He’d spent a full day and night as one with the blue waters of Qinghai Lake. It was hardly surprising that he might be ready to cooperate now.

But I stared at the gasping man in black with a grave expression.

“If even a little of what you say is a lie, your parents will live long, sick lives.”

“……”

“Devoted son, aren’t you? Right, Mujin?”

“Yes, sir!”

“N-No! Anything but that…!”

*Rrrrattle. Splash!*

Hyuk Mujin answered with gusto and let the chain go. The blue water swallowed the man’s desperate scream.

The ancient tradition of dipping someone in the Yangtze lived on at Qinghai Lake.
```
