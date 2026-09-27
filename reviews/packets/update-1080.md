<!-- packet-manifest
{
  "included": [
    {
      "path": "source/1080.txt",
      "sha256": "155fb07e358eb6ac9fdbf63f23880b7daa161626b13037c66f1de3de0d347a86",
      "bytes": 12048
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "fc556f9c9a0c7b3b55c3599e54ac8cc161adad1864dc40537346ff75e0c9bfd4",
      "bytes": 961
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "0515486273d29f48c39f3b929044de416121f8e550da3298bfc40633aa1bc751",
      "bytes": 242815
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "bfbee00a4d3f14a15b204e58d2a2be863d3711e138f138bd56df51bfb58b54d2",
      "bytes": 760
    },
    {
      "path": "characters/Jeok Cheongang.md",
      "sha256": "63321c234282f8593b1b215879b4db29c674017b9a086ba308db6b685ccbd58a",
      "bytes": 1502
    },
    {
      "path": "characters/Jeong Hogun.md",
      "sha256": "b37bc9fffc20c2906450c4c6d9d0665f636fedc42566bc09f70165434254cf95",
      "bytes": 700
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "4be52f2b91a03990a1eadd547d31618e8064907cd7a55afa9932bd7f2bb5d4a1",
      "bytes": 1828
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "910750668efd3865555a375385d681ef604cfe5ef1b21a13a1a1f44817256599",
      "bytes": 623
    },
    {
      "path": "characters/Jung Ho.md",
      "sha256": "b007a1afe10a850a75017aa95140d3d38c634e83c1450ad508157231171beb41",
      "bytes": 700
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "64aed7776995e97697d3df7399bc7971af9cae5f595449f0efd71bddc0765629",
      "bytes": 285915
    }
  ],
  "estimated_tokens": 9811
}
-->

# Durable State Update — Chapter 1080

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
1 and safe_through 1080. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 1080. Profile updates may replace only one
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
  "chapter": 1080,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 1080,
    "continuity_sources": [1080],
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
    "The party has arrived in Xining, Qinghai's capital and a last stronghold against Dark Heaven; crowds from across the province have gathered there.",
    "Hak Su is Cheongheoja’s Senior Disciple, Hak Woo’s senior brother, and a possible successor to the Kunlun Sect leadership.",
    "Taekyung believes the Lord of Heaven does not want him killed, but does not know why.",
    "The black-robed captive survived the interrogation and treatment and can now speak; Mujin is to talk with him."
  ],
  "continuity_sources": [
    1078,
    1079
  ],
  "open_questions": [
    "Who is the black-robed captive, and what does he know?",
    "Why did the Lord of Heaven spare Taekyung in Gansu, and what is his real purpose?",
    "Will the Alliance Leader and other righteous warriors reach Qinghai?",
    "What is the hidden ember Cheongheoja warned about?"
  ],
  "safe_through": 1079,
  "temporary_decisions": [],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 진태경    | **Jin Taekyung**   |
| 적천강    | **Jeok Cheongang** |
| 열화문    | **Fire Gate Clan**               |
| 곤륜파    | **Kunlun Sect**                  |
| 절정     | **Peak**          |
| 초절정    | **Supreme Peak**  |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 중원     | **Central Plains**                               |                                                       |
| 강호     | **martial world**                                | Prefer “Murim” where the setting itself is meant      |
| 문주     | **Sect Leader**                              |
| 제자     | **Disciple**                                 |
| 전각     | **pavilion**                                 | Use “hall” only when established for a specific named building |
| 은인     | **Benefactor**                               |
| 청해     | **Qinghai**            |
| 곤륜     | **Kunlun**             |
| 대협      | **Great Hero** or **Sir** depending tone                        |
| 도사      | **Daoist**                                                      |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 정호군 | **Jeong Hogun** | Commander of the Embroidered Uniform Guard force confronting Jin. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 정호 | **Jung Ho** | Middle-aged Shaolin martial monk leading the traveling group. |
| 문주님 | **Sect Leader** | Honorific title Lee Seowol orders the senior figures to use. |
| 성주 | **City Lord** | Official who sends the invitation for a gathering with young prodigies. |
| 천자 | **Son of Heaven** | Honorific title for the Emperor. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 마도 | **Demonic Path** | Term raised for martial power that appears to defy common principles. |
| 초절 | **supreme mastery** | Realm beyond Peak described as accessible only to the greatest martial artists. |
| 꼬리 | **the “tail”** | Codename for the Black Hunter traced by Butler Kim. |
| 열화 | **Blazing Flame** | Lineage term in Taekyung's declaration as the Fire King's successor. |
| 청해성 | **Qinghai** | Source form specifying Qinghai as a province. |
| 열화신룡 | **Blazing Flame Divine Dragon** | New sobriquet bestowed on Jin Taekyung. |
| 신룡 | **Divine Dragon** | Title used when discussing the Water God Dragon's intentions. |
| 이전 | **Two Halls** | Top-level Murim Alliance organizational grouping. |
| 화신 | **Fire God** | A local deity worshiped by one Nanman believer. |
| 금의위 | **Embroidered Uniform Guard** | Imperial guard force mentioned by Hong Jin. |
| 동창 | **East Depot** | Imperial agency named by Hong Jin. |
| 상산후 | **Marquis of Shangshan** | Title bestowed on Jin Taekyung by the Emperor. |
| 천호 | **Thousand Captain** | Rank held by Jeong Hogun in the Embroidered Uniform Guard. |
| 서녕 | **Xining** | Capital of Qinghai. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 적천강 | 진태경 | overwhelming stranger to interrogated young martial artist | you; you bastard | blunt, threatening, and taunting | Uses 너, 네놈, and 이놈 while demanding Taekyung explain Qi Sense and the System. |
| 진태경 | 적천강 | frightened young martial artist to overwhelming elder | elder | polite and fearful | Uses the honorific 어르신 while explaining that the System may have felt like a cheat. |
| 신의 | 진태경 | physician_to_benefactor | Young Master Jin | formal-polite | The Divine Physician addresses Taekyung as 진 공자 while expressing concern for his injuries. |
| 적천강 | 신의 | senior_martial_master_to_physician | Divine Physician | blunt and familiar | Uses 신의 while recognizing Dong Feng’s medical identity. |
| 신의 | 적천강 | physician_to_legendary_martial_master | Sir Jeok | formal-deferential | Uses 적 대협 while thanking and counseling Jeok. |
| 정호 | 진태경 | Shaolin Discipline Hall Master to patient and Benefactor | Benefactor Jin | formal-polite | Jung Ho repeatedly uses 진 시주 and 시주. |
| 진태경 | 정호 | patient to Shaolin Discipline Hall Master | Monk | polite and familiar | Taekyung addresses Jung Ho as 스님. |
| 진태경 | 정호군 | young martial artist to senior imperial officer | Commander Jeong | casual and teasing, then conciliatory | Jin addresses him by rank while trying to defuse the standoff. |
| 정호군 | 진태경 | imperial officer responding to the Marquis of Shangshan | Marquis of Shangshan | formal and deferential | Accepts the command with a formal acknowledgment of Taekyung’s title. |

## Listed compact profiles

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 1077
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** He is devoted to medicine and the lives he could not save, yet remains composed and self-effacing under mortal danger.
- **Voice:** He speaks in calm, respectful, self-effacing language, framing mortality through quiet philosophical reflections.
- **Relationships:** Mungyeong is the Divine Physician's true identity, the Slaughter Saint was his Master, and Dong Feng is his Disciple.

### Jeok Cheongang.md

# Jeok Cheongang (적천강)

- **Safe through:** Chapter 1078
- **Aliases:** Fire King; eighteenth Sect Leader of the Fire Gate Clan
- **Role:** Jeok Cheongang is the Fire Gate Clan’s current Sect Leader, a legendary martial master who has surpassed the Three Saints, Jin Taekyung’s Master and intended heir’s mentor, and a trusted confidant who occupies the chief seat of the Murim Alliance’s Five Kings Hall.
- **Personality:** Secretive, sharp-eyed, gruff, dryly teasing, and pathologically afraid of water; he distrusts process-first excuses when outcomes fail and hopes to make good choices while protecting those he still has.
- **Voice:** Sharp and ringing when calling out; otherwise gruff, dryly teasing, blunt, and threatening during interrogation or confrontation.
- **Relationships:** He considers Jin Taekyung his one and only Disciple and trusted confidant, and insists on protecting Taekyung while urging him not to risk his life; he warmly regards Ju Hwaran, sees Mae Jonghak as a kindred spirit, recognizes Cheongpung as Mae's grandson and successor, was close to Hong Dao, accepted Jangcheon as a Disciple before he became Jopil, and was Peng Cheolhu’s longtime rival and friend until Peng’s death, when they parted reconciled as brothers in all but blood; he once fought alongside Murong Baek, now his enemy, and personally killed his former ally the Junzi Saber after that man joined the Demonic Cult.

### Jeong Hogun.md

# Jeong Hogun (정호군)

- **Safe through:** Chapter 1074
- **Aliases:** None
- **Role:** Jeong Hogun is a Thousand Captain of the Embroidered Uniform Guard and a highly skilled martial artist whose force includes dozens of Peak masters.
- **Personality:** Disciplined and resolute, he follows imperial orders without hesitation and reads the political consequences of events with care.
- **Voice:** Formal and rigid, emphasizing duty to imperial authority.
- **Relationships:** Jeong Hogun serves under Baek Yeon’s command in the Embroidered Uniform Guard and honors Jin Taekyung as a comrade-in-arms after their shared battle.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 1079
- **Aliases:** Blazing Flame Divine Dragon; Apostle of the Earth Mother Goddess; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan and the original owner of his current body, Jeok Cheongang’s Disciple, the Fire Gate Clan’s nineteenth successor, Pavilion Master of the Fire Dragon Pavilion, a Supreme Peak master who has reached the realm of the Ten Kings as its eleventh member and can detect and eavesdrop on nearby Sound Transmissions subject to the participants’ relative levels, and a publicly recognized S-rank-level Hunter with an A-rank license, a traveler between Murim and another world, and the World Hunter Federation’s Alliance Leader; the Emperor appointed him Marquis of Shangshan and Thousand Captain of the Embroidered Uniform Guard.
- **Personality:** Hungry, self-aware, and dryly observant; pragmatic under pressure, willing to risk himself for others, and fiercely defiant when others try to dictate his choices or survival.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, and Jeok Cheongang is his Master and trusted confidant; Hyuk Mujin trusts Taekyung to fight beside him; Taekyung trusts Sama Pyo as a friend despite suspecting his betrayal, and values him beyond his unorthodox affiliation; Peng Cheolhu regarded Taekyung as a worthy successor, and the Bow Saint relayed the Martial God’s message to him.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 1079
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Jung Ho.md

# Jung Ho (정호)

- **Safe through:** Chapter 1074
- **Aliases:** None
- **Role:** Middle-aged Shaolin martial monk and Master of Shaolin's Discipline Hall who leads the traveling group and wields a Zen staff hung with prayer beads.
- **Personality:** Humble, observant, principled, and concerned with the safety of commoners.
- **Voice:** Formal, restrained, and admonitory, with Buddhist phrasing.
- **Relationships:** Unnamed is his young Martial Uncle; he leads the Shaolin monks traveling with him, addresses Sama Pyo as a Benefactor, and is recognized by Jin Taekyung as Park Jung Ho, a former Garam Middle School classmate.

## Korean source

```text
1080화




밤이 깊어져도 서녕(西寧)의 등불은 꺼지지 않았다.

여전히 거리에 남아 있는 수많은 환영 인파는 서로의 기쁨을 아낌없이 나누었고, 성내의 수뇌부는 그런 이들을 위해 술과 고기를 내주었다.

저들의 마음속에 자리 잡은 그 자그마한 희망의 불씨가 조금이라도 더 오래. 그리고 밝게 타오르길 바라면서.

하지만 지금 이 순간에도 창 틈새를 비집고 흘러드는 바깥의 웃음소리와는 달리, 전각 내부의 분위기는 무겁게 가라앉아 있었다.

“죽상을 하고 앉아 있는 걸 보아하니, 대충 돌아가는 상황을 알겠군.”

불현듯 침묵을 깨트린 적천강이 혀를 차며 말을 이었다.

“뭔가 거지 같은 소식이라도 있는 모양인데, 나중에 가서 지랄염병들 떨지 말고 지금 털어놓거라.”

“그것이…….”

적천강이라서 할 수 있는 말이었지만, 그 상대가 무려 적천강이라 누가 먼저 쉽게 총대를 멜 수 없는 상황.

말꼬리를 흐리며 서로 시선만 교환하는 수뇌부들의 모습에, 창가에 서 있던 내가 불쑥 입을 연 것은 바로 그때였다.

“당장 뭐라 말씀하시기 어려우시다면, 우선 현재 성내의 상황부터 듣죠.”

비록 열화문이라 쓰고 개새끼들이라 읽는 것이 강호의 인식이라지만, 성질 더럽기로 유명한 어느 노괴(老怪)보다는 새파란 제자가 편하게 느껴지는 것은 당연지사.

내 부드러운 어조에 그제야 안색이 풀린 수뇌부 중 누군가가 조심스럽게 입을 열었다.

“아무래도 좋지 않네.”

“음. 좋지 않다?”

“그렇네.”

조용히 입맛을 다신 나는 발언자를 향해 물었다.

“알겠습니다. 그런데 지금 말씀하신 분께서는 혹시 성함이?”

“청해 공화문(共和門)의 문주, 척 모라 하네. 자네가 들어봤는지는 모르겠군.”

당연히 못 들어 봤다.

내가 아는 그 공화춘이라면 모를까, 청해성에 자리 잡은 수십여 개의 무림 문파 목록을 달달 외우지도 않았으니까.

더불어 앞으로도 딱히 기억에 남지 않을 거라는 사실은, 그가 가장 먼저 했던 대답으로 명확해진 것이나 다름없었다.

“예. 우선 공화문의 척 문주님.”

“듣고 있네.”

느슨한 자세로 고개를 끄덕이는 그를 똑바로 응시하며, 나는 담담하게 말을 이었다.

“여기 있기 싫으십니까?”

“……?”

“나가셔도 됩니다. 앞으로도 그렇게 당연한 소리만 늘어 놓으실 생각이면.”

“……!”

“그리고 언제 봤다고 말을 그렇게 편하게 하실까. 어때요, 그쪽 분 생각은?”

덧붙인 물음과 함께 시선을 돌리자, 비단으로 된 관복을 차려입은 중년의 벼슬아치가 마른침을 꿀꺽 삼키며 대답했다.

“사, 상산후께서 하시는 말씀에 소관이 어찌 감히 토를 달겠습니까.”

“대답이 희한하네. 내가 지금 토를 달고 말고를 물은 게 아니었던 것 같은데.”

“배, 백번 천번 지당하신 말씀입니다!”

“그래요, 뭐. 그나저나 계속 서 있었더니 다리가 좀 아프네. 자리 남는 곳 없나?”

사실 며칠을 이대로 서 있어도 끄떡없고, 당장 고개만 좀 돌려도 남아도는 것이 자리였지만 중년의 벼슬아치는 의자를 박차며 벌떡 일어났다.

“여기에 자리 있습니다!”

“어이고, 이러실 필요는 없는데. 심지어 저보다 연배도 한참 높으신 분이.”

“소, 소관이 대관절 어찌해야 하는지…….”

“어쩌긴 뭘 어째. 지금 나 욕먹으라고 설계하는 거예요? 대가리에 피도 안 마른 어린놈이 지위 앞세워서 어른 핍박했다고?” 

“그, 그러시면 앉겠습니다.”

눈동자를 이리저리 굴리던 벼슬아치가 조심스럽게 의자에 엉덩이를 붙이려는 순간, 내가 혼잣말처럼 중얼거렸다.

“이걸 진짜 앉네. 눈치 없게.”

“……예?”

“응? 왜요?”

“아니, 그. 지금 막 하신 말씀이.”

“아, 혹시 들으셨어요?”

“……예.”

“그냥 혼잣말이었는데, 앉으세요.”

“…….”

“왜 자꾸 여러 번 말하게 해. 앉으시라니까?”

만약 눈치 없는 인간이었으면 지금이라도 슬그머니 엉덩이를 붙였겠지만, 눈앞의 중년의 벼슬아치는 이러지도 저러지도 못한 채 동공지진이 일어나는 눈동자로 나를 바라볼 뿐이었다.

하긴, 저 정도 눈치가 있었으니 비교적 젊은 나이에 일찍 성주(城主)씩이나 되는 요직에 앉았을 것이다.

‘지금껏 뒤꽁무니로 이것저것 많이 빼돌린 것도, 저 눈치 덕분이고.’

본의 아니게 투명의자 자세로 전전긍긍하는 청해성주를 뒤로한 채 옆을 슬쩍 쳐다보자, 비틀린 입매로 미소 짓고 있는 정호군의 얼굴이 보였다.

내게 나이 많은 사람을 괴롭히는 취미 따위는 없지만, 서녕으로 오는 도중 그에게서 들은 이야기는 그런 죄책감을 말끔히 씻어 주기에 충분했다.

‘전형적인 탐관오리.’

황실 제일의 무력 집단인 동시에, 동창과 비견될 만한 정보력을 지닌 금의위가 한참 전에 입수한 정보였으니 의심의 여지는 없다.

다만 그보다 중요한 것은, 청해성주의 방만함으로 인해 무너진 현재의 상황이다.

“제가 어디서 얼핏 듣자 하니 성내에 비축된 식량이 그리 많지 않다던데. 성주님은 이거에 대해서 어떻게 생각하세요?”

“그, 그것이.”

“정확한 수치만. 거짓 없이.”

“아, 아무래도 성내에 급속도로 너무 많은 백성들이 몰리는 바람에…….”

“혀가 기시네. 좀 짧게 해 드릴까.”

“하, 한 달! 한 달입니다!”

황급히 대답한 청해성주가 자신 없는 어투로 덧붙였다.

“……아마도.”

“안 되겠다. 정 천호?”

저벅.

내 부름에 정호군이 성큼 앞으로 나서자, 청해성주가 눈을 질끈 감으며 외쳤다.

“보, 보름입니다! 현재 비축된 식량으로는 그 정도가 한계입니다!”

“보름이라, 이번 건 확실해요?”

“목을, 소관의 목을 걸겠습니다!”

가진 것이 많은 놈들은 결코 목숨을 건 도박을 하지 않는다.

그리고 그런 의미에서 청해성주의 대답은, 매우 진한 진실성을 띠는 동시에 나를 열받게 만들었다.

비록 단기간에 수많은 피난민이 몰려들었다지만, 서녕이 이렇게 된 것도 고작 칠 주야 남짓이다.

엄연히 변방(邊方)에 속한 청해성인 만큼, 혹시 모를 외적의 침입을 대비하여 비축된 군량이 중원보다 많을 수밖에 없는 것이 기본.

그런데도 앞으로 고작 보름치의 식량밖에 남지 않았다는 건…….

‘정말 어지간히도 해 처먹었구만.’

나는 한숨과 함께 청해성주를 바라보았다. 때아닌 하체 운동으로 땀이 줄줄 흐르는 그의 얼굴은 잔뜩 겁에 질려 있었다.

“뭘 또 그렇게 쫄아 있어요. 누가 보면 내가 당신 죽이려고 드는 줄 알겠네. 안 그래?”

“그, 그 말씀은.”

“걱정하지 마. 안 죽여요.”

“감사합니다!”

단번에 화색이 도는 청해성주를 향해, 나는 부드럽게 덧붙였다.

“적어도 지금 당장은.”

“앞으로 상산후께 온 마음을 다해 충성을…… 예?”

“뭘 되묻고 그래. 들은 그대론데.”

그 순간, 자신의 귀를 의심하는 청해성주의 등 뒤로 성큼 다가온 금의위 위사 서너 명이 그를 에워쌌다.

“자, 잠깐! 이럴 수는 없습니다!”

“누가 그래. 이럴 수 없다고?”

청해성주에게는 엄청난 불행이겠지만, 황실을 구한 은인이자 천자에게 친히 임명된 열후에게는 충분히 이런 일을 벌일 수 있는 자격과 명분이 차고 넘친다.

그리고 그의 운명은, 내가 서녕에 발을 딛기 이전부터 결정된 것이나 다름없었다.

“해 뜨면 보내라. 혼자 가면 외로우니까 길동무 붙여 주는 것도 잊지 말고.”

“존명(尊命)!”

어느 때보다 굳건한 대답한 정호군의 손짓에, 대기하고 있던 나머지 금의위 위사들이 정해진 바에 따라 신속하게 명령을 이행했다.

“청해성 위지휘사사(衛指揮使司) 송악. 맞소?”

“나, 나는 아무 잘못도 없소!”

“그건 우리가 판단하는 거요. 당신이 아니라.”

“……!”

“상산후께서 내리신 엄명이니 얌전히 따라오시오. 내일 뜰 해라도 보고 싶다면.”

그야말로 순식간이었다.

화려한 갑옷을 입은 장군도, 그 목만큼이나 빳빳한 관복을 걸친 벼슬아치들도 창백한 얼굴로 줄줄이 끌려 나갈 수밖에 없었다.

이 일련의 과정에는 어떠한 저항 따위도 없었다.

아니, 그럴 엄두조차 내지 못했다는 것이 옳았다.

천하를 떨어 울린다는 초절정 고수들의 존재감도 이에 일조했지만, 황실 직속의 금의위에게 맞서는 순간 일가 전체가 역적으로 몰리기 때문이다.

청해성주와 결탁한 탐관오리로 참수당할 것이냐, 역적으로 몰려 멸문지화(滅門之禍)를 당할 것이냐는 죽음의 이지선다 앞에서 그들이 할 수 있는 선택은 한 가지뿐이었다.

현실에 대한 순응.

그리고 끝없는 절망.

하지만 모든 것이 끝났음을 의미하는 통곡과 함께 끌려 나가는 저들과 달리, 종양(腫瘍)을 떼어 낸 백성들은 더욱 단합하고 기뻐할 것이다.

또한 그와 더불어.

“이제야 좀 제대로 된 이야기를 할 준비가 된 것 같은데.”

순식간에 텅 비어 버린 저 십여 개의 빈자리가, 이 공백을 만들어 낸 누군가의 존재감으로 새롭게 채워졌음을 의미한다.

바로 나.

열화신룡(熱火神龍) 진태경의 존재로.

“다들 어떻게 생각하시는지.” 

“……!”

“……!”

숨 막히는 침묵이 전각 내부를 짓눌렀다.

나와 가까운 이들은 소리 없이 웃고 있었으나, 나를 모르던 이들은 캄캄하게 가라앉은 표정과 눈빛으로 서로를 바라보았다.

어느덧 꼿꼿하게 펴진 허리와, 느릿하면서도 초조하게 탁자를 두드리는 손가락들.

어쩌면 저들 중 일부는 내심 나를 무시했거나, 혹은 애써 깎아내렸을지도 모른다.

소문은 언제나 부풀려지는 법이니까.

지금 같은 혼란한 난세 속에서, 영웅이란 때때로 필요에 의해 만들어지기도 하는 법이니까.

하지만 틀렸다.

언제나, 어디에서나 그런 이들은 있었지만 그 결과는 항상 같았다.

그리고 뜻 모를 표정으로 말없이 모든 상황을 지켜보던 이들 또한, 늘 있어 왔다.

지금 이 순간. 시선을 피하는 몇몇 이들과는 달리 나를 똑바로 응시하고 있는 저 젊은 도사처럼.

“소문이란 결국 사람의 눈과 귀를 통해 만들어지는 것, 하여 여느 때처럼 그리 믿지 않았습니다마는.”

주름 하나 없이 가지런한 도포와 도무지 깊이를 알 수 없는 눈동자.

“이렇게 도우를 대면하니, 비로소 그 생각이 옳았음을 다시금 깨달았습니다.”

그와 더불어, 단정하게 정돈된 그 인상처럼 침착하고 무덤덤한 목소리까지.

“역시 소문은 믿을 만한 것이 못 되는 듯합니다. 그에 미치지 못할 때도, 혹은…… 그 예상을 훌쩍 뛰어넘을 때도.”

스륵.

자리에서 일어난 젊은 도사가, 나를 향해 포권지례를 취하며 입을 열었다.

“곤륜파 일대제자 학의(鶴義), 열화신룡 진태경 대협을 뵙습니다.”
```

## Final English reading copy

```markdown
# Chapter 1080

Even as night deepened, the lights of Xining stayed bright.

The countless people still out in the streets shared their joy without holding back, and the city’s leaders provided them with liquor and meat.

They hoped the little sparks of hope nestled in those people’s hearts would burn a little longer—and a little brighter.

But even as laughter from outside slipped through the cracks around the windows, the mood inside the pavilion remained heavy.

“Judging by those long faces, I can guess how things are going.”

Jeok Cheongang broke the silence without warning, clicking his tongue as he continued.

“Sounds like you’ve got some shitty news. Spit it out now instead of making a damn fuss later.”

“Well…”

It was the sort of thing only Jeok Cheongang could say. But because he was Jeok Cheongang, no one could bring themselves to be the first to take the plunge.

The leaders trailed off, exchanging glances. Just then, I spoke up from where I stood by the window.

“If it’s difficult to say right now, let’s start with the current situation in the city.”

The martial world might call the Fire Gate Clan a bunch of bastards, but it was only natural that a young Disciple felt easier to approach than a notorious old monster with a foul temper.

At my gentle tone, one of the leaders finally relaxed enough to speak.

“Things aren’t looking good.”

“Hmm. Not good?”

“That’s right.”

I quietly smacked my lips, then turned to the speaker.

“Understood. And may I ask your name?”

“I’m Cheok Mo, Sect Leader of Qinghai’s Gonghwa Sect. I don’t know if you’ve heard of us.”

Of course I hadn’t.

I might have known Gonghwachun, but I hadn’t memorized the names of the dozens of martial sects in Qinghai Province.

And his very first answer made it clear that I wasn’t likely to remember him in the future, either.

“All right, then. Sect Leader Cheok of the Gonghwa Sect.”

“I’m listening.”

He nodded lazily. I met his gaze and continued evenly.

“Do you want to be here?”

“…?”

“You’re free to leave. If all you’re going to do is state the obvious, that is.”

“……”

“And when did we get so familiar? What do you think, sir?”

I added the question and turned my gaze to a middle-aged official dressed in silk robes. He swallowed nervously before answering.

“H-How could I possibly contradict the Marquis of Shangshan?”

“That’s a strange answer. I don’t think I asked whether you’d contradict me.”

“Y-You are absolutely right!”

“Sure. Anyway, I’ve been standing here for a while, and my legs are getting a bit tired. Is there an open seat?”

I could have stood there for days without a problem, and there were plenty of open seats. But the middle-aged official sprang from his chair.

“There’s a seat right here!”

“Oh, you don’t have to do that. Especially when you’re so much older than me.”

“I-I don’t know what I should…”

“What do you mean, what should you do? Are you trying to set me up to get cursed out? Make it look like some kid who hasn’t even dried the blood from his head is throwing his rank around to bully his elders?”

“Th-Then I’ll sit.”

The official’s eyes darted back and forth as he cautiously started to lower himself into the chair. I muttered as if to myself:

“He’s actually sitting. Doesn’t know how to read the room.”

“…Pardon?”

“Hm? What is it?”

“I mean, what you just said…”

“Oh, did you hear me?”

“…Yes.”

“I was just talking to myself. Go ahead and sit.”

“……”

“Why do I have to keep telling you? Sit down.”

If he’d been completely clueless, he might have eased himself into the chair anyway. But the middle-aged official before me could only stare at me with eyes that seemed to shake, unable to move either way.

Then again, he must have been good at reading the room to have landed such an important post as City Lord at a relatively young age.

*And that same instinct must’ve helped him skim plenty of things off the top over the years.*

Leaving the City Lord of Qinghai sweating through an imaginary squat, I glanced to my side. Jeong Hogun was smiling with a crooked twist to his lips.

I didn’t have a hobby of bullying old men, but what I’d heard from him on the way to Xining had thoroughly washed away any guilt I might have felt.

*A textbook corrupt official.*

The Embroidered Uniform Guard—the imperial family’s foremost military force, with intelligence capabilities comparable to the East Depot—had obtained the information long ago. There was no room for doubt.

More important, though, was the state of affairs his negligence had brought about.

“I heard somewhere that the city’s food stores aren’t all that plentiful. What do you have to say about that, City Lord?”

“Th-That’s…”

“Just the numbers. No lies.”

“W-We had far too many commoners flood the city in a short time…”

“That’s a long tongue you’ve got. Want me to shorten it?”

“On-One month! One month!”

The City Lord of Qinghai blurted out his answer, then added in an uncertain voice:

“…Probably.”

“That won’t do. Thousand Captain Jeong?”

*Step.*

Jeong Hogun stepped forward at my call. The City Lord squeezed his eyes shut and cried out:

“F-Fifteen days! The food we have in storage will last that long at most!”

“Fifteen days. Are you sure about that this time?”

“I-I stake my life on it!”

Men with plenty to lose never gamble with their lives.

And in that sense, the City Lord’s answer rang with a deep sincerity—and made me furious.

A huge number of refugees had arrived in a short time, but Xining had only been like this for about seven days.

Qinghai was a border province. It was only natural that it would have more military provisions stored away than the Central Plains, in case of an invasion.

And yet there was only enough food for fifteen more days…

*He’s really been eating well.*

I sighed and looked at the City Lord. Sweat poured down his face from his impromptu leg workout, and he looked terrified.

“Why are you so scared? Anyone would think I was trying to kill you. Am I?”

“Th-Then…”

“Don’t worry. I won’t kill you.”

“Thank you!”

I smiled gently at the City Lord, whose face had brightened at once, and added:

“At least not right now.”

“I’ll devote my whole heart to serving the Marquis of Shangshan from now on… Pardon?”

“Why are you asking me to repeat myself? You heard me.”

At that moment, three or four Embroidered Uniform Guards came striding up behind the City Lord and surrounded him.

“W-Wait! You can’t do this!”

“Who says we can’t?”

It was a terrible turn of events for the City Lord, but as the man who’d saved the imperial family and been personally appointed a marquis by the Son of Heaven, I had more than enough authority and grounds to do this.

And his fate had been all but decided before I even set foot in Xining.

“Send him off at sunrise. And don’t forget to give him some company on the way. He might get lonely.”

“As you command!”

Jeong Hogun answered more firmly than ever, then gestured. At his signal, the other Embroidered Uniform Guards waiting nearby swiftly carried out their orders.

“Songak of Qinghai’s Regional Military Commission. Is that you?”

“I-I haven’t done anything wrong!”

“That’s for us to decide. Not you.”

“……”

“These are the Marquis of Shangshan’s orders. Come along quietly if you want to see tomorrow’s sunrise.”

It happened in the blink of an eye.

Generals in ornate armor and officials in robes as stiff as their necks, were dragged out one after another, their faces pale.

There wasn’t the slightest resistance throughout the whole process.

No—that wasn’t quite right. They hadn’t even dared to try.

The presence of Supreme Peak masters who could shake the world had something to do with it. But the moment they opposed the imperial Embroidered Uniform Guard, their entire families could be branded traitors.

Beheaded as corrupt officials in league with the City Lord of Qinghai, or branded traitors and wiped out along with their families: faced with those two choices of death, they had only one option.

Accept reality.

And despair without end.

But unlike those men, dragged away to wail as if everything were over, the people would grow more united and rejoice now that the tumor had been removed.

And along with that—

“Looks like we’re finally ready to have a proper discussion.”

Those dozen or so seats, emptied in an instant, meant the presence of someone had filled the void they left behind.

Me.

The presence of Jin Taekyung, the Blazing Flame Divine Dragon.

“What does everyone think?”

“……”

“……”

Suffocating silence weighed down on the pavilion.

Those close to me were smiling quietly, but the faces and eyes of those who didn’t know me had sunk into darkness as they looked at one another.

Their backs, now sitting straight. Their fingers, tapping the table slowly, but with growing impatience.

Some of them might have looked down on me in their hearts, or tried to diminish me.

Rumors always grew out of proportion.

And in an unsettled age like this, heroes were sometimes made because people needed them.

But they were wrong.

There had always been people like that, no matter the time or place. And the outcome had always been the same.

There had also always been those who watched everything in silence, their expressions impossible to read.

Like the young Daoist who now looked straight at me, unlike the few who were avoiding my gaze.

“Rumors are ultimately made through the eyes and ears of those who hear them, so I never put much stock in them, as usual.”

His Daoist robes were neat, without a single wrinkle, and his eyes had a depth impossible to fathom.

“But meeting you in person has shown me again that I was right.”

His voice was calm and unruffled, just like his neatly arranged appearance.

“It seems rumors aren’t very reliable. Sometimes they fall short—and sometimes… they exceed every expectation.”

*Rustle.*

The young Daoist rose from his seat, clasped his hands toward me in greeting, and spoke.

“I am Hak Eui, a First-Generation Disciple of the Kunlun Sect. It is an honor to meet you, Great Hero Jin Taekyung.”
```
