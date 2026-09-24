<!-- packet-manifest
{
  "included": [
    {
      "path": "source/1023.txt",
      "sha256": "150340ffaac4cf132411325cb7760765708f7b5467a89abf179cc96566f5104f",
      "bytes": 13055
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "2faed439d254b15d4600a308dee3473eb96002f1dd746db9a1e8af26da79ee00",
      "bytes": 1521
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "fec4ec0cd94adc2a16893a720ff7a5206cf3abc462dd6dde1d657859aa2f86cd",
      "bytes": 239074
    },
    {
      "path": "characters/Hyuk Mujin.md",
      "sha256": "27511a07453764a00589569284d45830bcad5e608b0006a7f7f50aa0a4a44ed2",
      "bytes": 1375
    },
    {
      "path": "characters/Jeok Cheongang.md",
      "sha256": "e520795e32907e6af30598ffd80cc7200bdef39a147a9e6b853b6d85ee942e91",
      "bytes": 1502
    },
    {
      "path": "characters/Jeong Hogun.md",
      "sha256": "6d580529d9954d6a18616e10d3025495e62ec7aaae26b407a2c84790698fc6fa",
      "bytes": 699
    },
    {
      "path": "characters/Jung Ho.md",
      "sha256": "404ac1fd50cacfe2e282c2ba69ef922c1aebbe934ec9a58c85fa1ac51f1e1e1d",
      "bytes": 699
    },
    {
      "path": "characters/Namho.md",
      "sha256": "becb0958aec348b60b173a4a541b3cc2a645f5732a15b740b26352ef7708285b",
      "bytes": 1092
    },
    {
      "path": "characters/Sama Pyo.md",
      "sha256": "6ab7fab8dcba7843842c45fab9574f68880e894d9eae51fc2478179e85cb1ba8",
      "bytes": 1069
    },
    {
      "path": "characters/Sima Gong.md",
      "sha256": "5fa5a4efae2d74fec21b49275f77c6bce37faae36d7516732620d72a5f3e955a",
      "bytes": 778
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "107226d29d3a00596e274bb32d326b67d072d4bda85484b408975b0987bfdde5",
      "bytes": 277335
    }
  ],
  "estimated_tokens": 11204
}
-->

# Durable State Update — Chapter 1023

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
1 and safe_through 1023. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 1023. Profile updates may replace only one
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
  "chapter": 1023,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 1023,
    "continuity_sources": [1023],
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
    "Taekyung’s five-thousand-strong force has reached the Great Snow Mountain; allied signals confirm the mountain is occupied by their side.",
    "Dark Heaven captured Dunhuang after breaching the Jade Gate Pass, inflicting catastrophic losses on the defenders.",
    "A middle-aged Dark Heaven killer slaughtered more than a hundred Kongtong Sect members, including the Kongtong Sword Dragon; his identity and strength are unknown.",
    "Taekyung suspects Dark Heaven has at least three Supreme Peak masters or one overwhelmingly powerful superhuman; he wonders whether the Lord of Heaven is involved.",
    "Sima Gong ordered Sama Pyo to watch Taekyung’s group. Taekyung still does not know whether the secret orders involving Pyo and Taishan connect to Dark Heaven.",
    "The secret letter received by Sama Pyo remains unexplained.",
    "The Kongtong Sect Leader escaped Dunhuang, but his whereabouts remain unknown."
  ],
  "continuity_sources": [
    1021,
    1022
  ],
  "open_questions": [
    "Who sent Sama Pyo the secret letter, what did it say, and what was its purpose?",
    "Where is the Kongtong Sect Leader?",
    "Who is the middle-aged killer, and what is the extent of his strength?",
    "What hidden strength gave Dark Heaven confidence to invade Gansu, and is the Lord of Heaven involved?",
    "Are Sima Gong’s secret orders involving Sama Pyo and Taishan connected to Dark Heaven?"
  ],
  "safe_through": 1022,
  "temporary_decisions": [],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 혁무진    | **Hyuk Mujin**     |
| 적천강    | **Jeok Cheongang** |
| 사마공    | **Sima Gong**      |
| 태원진가   | **Jin Family of Taiyuan**        |
| 암천     | **Dark Heaven**                  |
| 삼류     | **Third Rate**    |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 사파     | **unorthodox faction**                           |                                                       |
| 문주     | **Sect Leader**                              |
| 몬스터     | **monster**           |
| 대격변     | **Great Cataclysm**   |
| 산서     | **Shanxi**             |
| 태원     | **Taiyuan**            |
| 감숙     | **Gansu**              |
| 정마대전   | **Great Faction War**         |
| 공자      | **Young Master**                                                |
| 정호군 | **Jeong Hogun** | Commander of the Embroidered Uniform Guard force confronting Jin. |
| 정호 | **Jung Ho** | Middle-aged Shaolin martial monk leading the traveling group. |
| 남호 | **Namho** | Hidden Shadow Pavilion code name; literally associated with amber from the south. |
| 사마표 | **Sama Pyo** | Young Sect Leader of the Black Dragon Demon Gate. |
| 삼공자 | **Third Young Master** | Title used for Jin Taekyung. |
| 맹주 | **Alliance Leader** | Leader of the regional Murim alliance. |
| 부천 | **Bucheon** | City with a dense concentration of Gates and Guild headquarters. |
| 산서성 | **Shanxi Province** | Province containing the Lower District Sect branches. |
| 송이 | **Song-i** | Short form used for Song Song; Taekyung's love interest. |
| 조장 | **Captain** | Hyuk Mujin's address for Taekyung as squad leader. |
| 야왕 | **Night King** | Rumored epithet for Jin Taekyung in Taiyuan's red-light district. |
| 성주 | **City Lord** | Official who sends the invitation for a gathering with young prodigies. |
| 전하 | **His Highness** | Formal royal address for the resident prince; the official insists on this form instead of king. |
| 대국 | **Great Nation** | Political wording on the Jin Family's welcome banner. |
| 대태원진가 | **great Jin Family of Taiyuan** | Formal exalted reference to the Jin Family of Taiyuan. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 은영각 | **Hidden Shadow Pavilion** | Former Murim Alliance intelligence organization. |
| 마공 | **demonic martial arts** | Martial arts that appear to defy common principles. |
| 명문혈 | **Mingmen acupoint** | Acupoint into which Jeok Cheongang sends internal energy while treating Hong Dao. |
| 꼬리 | **the “tail”** | Codename for the Black Hunter traced by Butler Kim. |
| 흑룡마문 | **Black Dragon Demon Gate** | Unorthodox faction from Gansu. |
| 공동파 | **Kongtong Sect** | Sect belonging to the Nine Sects and One Gang. |
| 흑야왕 | **Black Night King** | Epithet of Sima Gong, Sama Pyo's father and the Sect Leader who built the modern Black Dragon Demon Gate. |
| 제시 | **Jesse** | The U.S. Secretary of State, introduced by first name. |
| 대설산 | **Great Snow Mountain** | Mountain where Baeksang's wartime account reaches its next episode. |
| 금의위 | **Embroidered Uniform Guard** | Imperial guard force mentioned by Hong Jin. |
| 정천호 | **Commander Jeong** | Commander of the Embroidered Uniform Guard procession. |
| 상산후 | **Marquis of Shangshan** | Title bestowed on Jin Taekyung by the Emperor. |
| 천호 | **Thousand Captain** | Rank held by Jeong Hogun in the Embroidered Uniform Guard. |
| 돈황 | **Dunhuang** | City identified as the foremost defensive line in Gansu. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 혁무진 | 적천강 | subordinate_to_overwhelming_elder | Great Hero Jeok | deferential and fearful | Mujin uses 적 대협 while reporting Jeok’s orders and Taekyung’s awakening. |
| 적천강 | 혁무진 | overwhelming_elder_to_junior_martial_artist | you stupid fool | blunt and mocking | Jeok calls Mujin a 멍청한 놈 after knocking him down during the attempted escape. |
| 사마표 | 정호 | Black Dragon Demon Gate Young Sect Leader addressing a Shaolin Master | Master Jung Ho | Polite and ingratiating | Uses 정호대사 and 대사 while flattering Jung Ho and negotiating responsibility for the killing. |
| 정호 | 사마표 | Shaolin martial monk addressing the Black Dragon Demon Gate Young Sect Leader | Benefactor | Formal and admonitory | Uses 시주 while questioning Sama Pyo and demanding accountability. |
| 사마표 | 적천강 | Young Sect Leader to legendary elder | Great Hero Jeok | formal-deferential | Sama Pyo formally pays his respects to Jeok Cheongang as the Fire King. |
| 적천강 | 사마표 | legendary elder to unorthodox Young Sect Leader | you / young brat | blunt, suspicious, and contemptuous | Jeok addresses Sama Pyo with 네놈 and 어린놈 while probing his lineage and motives. |
| 남호 | 혁무진 | hidden_shadow_agent_to_pavilion_member | you there / Han bastard | performatively hostile and abusive | Namho attacks Mujin and insults him to make the meeting appear to be a genuine expulsion. |
| 혁무진 | 남호 | pavilion_member_to_hidden_shadow_agent | old man | indignant and insulting | Mujin protests Namho’s staged attack and objects to the insult about his parents. |
| 혁무진 | 조장님 | pavilion_member_to_squad_leader | Captain | deferential and dubious | Mujin questions whether the pasture should be called the Nanman Ranch instead of the Nanman Beast Palace. |
| 남호 | 사마표 | guide_to_young_sect_leader | Young Sect Leader | blunt and admonishing | Namho warns Sama Pyo that all grass and animals in the territory belong to the Nanman Beast Palace. |
| 사마표 | 남호 | young_sect_leader_to_guide | Elder Namho | formal and apologetic | Sama Pyo apologizes after Taishan attempts to seize the calf. |
| 혁무진 | 정천호 | strangers; commander and guarded outsider | Commander Jeong | informal-polite shifting to casual | Hyuk initially uses deferential -오 forms, then switches to casual speech and profanity. |
| 남호 | 적천강 | junior_to_senior | Senior | respectful and formal | Namho refers to Jeok as 노선배님 while agreeing with him. |
| 사마공 | 적천강 | unorthodox sect leader to senior martial master | Senior | formal and deferential | Greets Jeok Cheongang as 노선배. |
| 적천강 | 사마공 | senior martial master to longtime martial acquaintance | you | blunt and familiar | Uses direct, contemptuous language while teasing Sima Gong. |
| 사마공 | 사마표 | father to son | Pyo | intimate and familiar | Sima Gong calls him 표야 and 내 아들아. |

## Listed compact profiles

### Hyuk Mujin.md

# Hyuk Mujin (혁무진)

- **Safe through:** Chapter 1022
- **Aliases:** Swift Wind Sword
- **Role:** Hyuk Mujin is a Level 50 First Rate martial artist who serves as Captain of the Jin Family's Gatekeepers, Vice Squad Leader of the Jin Dragon Squad, and an active member of the Fire Dragon Pavilion.
- **Personality:** Young, disciplined, persistent, and talented; despite being naturally fearful, he faces danger and remains loyal to the person he serves, with irreverent self-deprecation and a taste for glory. He is suspicious of Taekyung, bluntly critical of the family's disgraced third son, and an avid wuxia reader who sometimes mistakes fictional conventions for reality.
- **Voice:** Formal and clipped in official duties; with Taekyung, blunt and occasionally incredulous, while using breezy, irreverent banter to defuse tense situations.
- **Relationships:** He is loyal to Taekyung, who trusts him to act independently, especially in his home region of Shanxi and at the Jin Family of Taiyuan. As a former family gate guard, he knows the most about Head Elder Jin Baekyang among the Fire Dragon Pavilion members accompanying Taekyung. Son of the Hyuk Family Textile Shop's owners; a younger sibling means he need not inherit the business.

### Jeok Cheongang.md

# Jeok Cheongang (적천강)

- **Safe through:** Chapter 1022
- **Aliases:** Fire King; eighteenth Sect Leader of the Fire Gate Clan
- **Role:** Jeok Cheongang is the Fire Gate Clan’s current Sect Leader, a legendary martial master who has surpassed the Three Saints, Jin Taekyung’s Master and intended heir’s mentor, and a trusted confidant who occupies the chief seat of the Murim Alliance’s Five Kings Hall.
- **Personality:** Secretive, sharp-eyed, gruff, dryly teasing, and pathologically afraid of water; he distrusts process-first excuses when outcomes fail and hopes to make good choices while protecting those he still has.
- **Voice:** Sharp and ringing when calling out; otherwise gruff, dryly teasing, blunt, and threatening during interrogation or confrontation.
- **Relationships:** He considers Jin Taekyung his one and only Disciple and trusted confidant, and insists on protecting Taekyung while urging him not to risk his life; he warmly regards Ju Hwaran, sees Mae Jonghak as a kindred spirit, recognizes Cheongpung as Mae's grandson and successor, was close to Hong Dao, accepted Jangcheon as a Disciple before he became Jopil, and was Peng Cheolhu’s longtime rival and friend until Peng’s death, when they parted reconciled as brothers in all but blood; he once fought alongside Murong Baek, now his enemy, and personally killed his former ally the Junzi Saber after that man joined the Demonic Cult.

### Jeong Hogun.md

# Jeong Hogun (정호군)

- **Safe through:** Chapter 983
- **Aliases:** None
- **Role:** Jeong Hogun is a Thousand Captain of the Embroidered Uniform Guard and a highly skilled martial artist whose force includes dozens of Peak masters.
- **Personality:** Disciplined and resolute, he follows imperial orders without hesitation and reads the political consequences of events with care.
- **Voice:** Formal and rigid, emphasizing duty to imperial authority.
- **Relationships:** Jeong Hogun serves under Baek Yeon’s command in the Embroidered Uniform Guard and honors Jin Taekyung as a comrade-in-arms after their shared battle.

### Jung Ho.md

# Jung Ho (정호)

- **Safe through:** Chapter 998
- **Aliases:** None
- **Role:** Middle-aged Shaolin martial monk and Master of Shaolin's Discipline Hall who leads the traveling group and wields a Zen staff hung with prayer beads.
- **Personality:** Humble, observant, principled, and concerned with the safety of commoners.
- **Voice:** Formal, restrained, and admonitory, with Buddhist phrasing.
- **Relationships:** Unnamed is his young Martial Uncle; he leads the Shaolin monks traveling with him, addresses Sama Pyo as a Benefactor, and is recognized by Jin Taekyung as Park Jung Ho, a former Garam Middle School classmate.

### Namho.md

# Namho (남호)

- **Safe through:** Chapter 1022
- **Aliases:** Elder Chao
- **Role:** Namho is an eighty-year-old non-Han Hidden Shadow Pavilion agent who spent more than fifty years undercover in Nanman and maintained contact with Central Plains intelligence through the Pavilion’s Hidden Thread; he guides the Fire Dragon Pavilion and represents Jin Taekyung and the Murim Alliance in negotiating the survivors’ chance to rebuild the Murong household.
- **Personality:** Duty-bound, pragmatic, and observant; uses theatrical violence to protect intelligence work and takes a veteran’s concern for the younger generation’s resolve.
- **Voice:** Measured and reflective when advising the younger generation, loudly abusive when maintaining his local cover, and capable of theatrical boasts and dry humor.
- **Relationships:** Namho is a Hidden Shadow Pavilion contact for Jin Taekyung and the Fire Dragon Pavilion, receives intelligence from the Pavilion Master, and knows the code used by the Thousand-Faced Fox.

### Sama Pyo.md

# Sama Pyo (사마표)

- **Safe through:** Chapter 1022
- **Aliases:** Black Dragon Saber
- **Role:** Young Sect Leader and heir of the Black Dragon Demon Gate, a Morning Star reputed to be no less than the Ten Dragons and Phoenixes.
- **Personality:** Outwardly courteous and calculating, he is protective of Taishan and pragmatic in combat; he recognizes that his father's ruthless, survival-driven worldview shaped him, even as its influence weighs on him.
- **Voice:** Polite and ingratiating in public, with sardonic humor and controlled evasiveness.
- **Relationships:** Sama Pyo commands the absolutely loyal Taishan and is Sima Gong's son and heir; his father's ruthless treatment of family shaped his rise and remains a source of inner constraint. He joined the Fire Dragon Pavilion intending to use Jin Taekyung, and Sima Gong has now ordered him to spy on Taekyung's group. He was Ju Hwaran's former fiancé in a political engagement and is openly hostile toward fellow member Song Ilseom.

### Sima Gong.md

# Sima Gong (사마공)

- **Safe through:** Chapter 1022
- **Aliases:** Black Night King
- **Role:** Sima Gong is the Sect Leader who built the Black Dragon Demon Gate into a major unorthodox power and the father of its Young Sect Leader, Sama Pyo.
- **Personality:** Sly and calculating yet outwardly gentle; he calmly accepts sacrificing the rear population as the cost of a strategy he believes offers the best odds of victory.
- **Voice:** Polished and persuasive, with smooth rhetorical turns and a composed, gently teasing manner.
- **Relationships:** Sama Pyo is his youngest son among seven older brothers and nine older sisters; he is personally familiar with Jeok Cheongang, who openly dislikes him.

## Korean source

```text
＃1023화



후욱, 훅.

말도 버린 채 험준한 비탈길을 오르는 발걸음과 함께, 곳곳에서 자욱하게 뿜어져 나오는 새하얀 입김.

사시사철 한겨울처럼 춥고 산소가 희박한 대설산(大雪山)의 환경은 이 땅을 지키려는 이들에게도 예외를 두지 않았다.

아니, 어쩌면 이러한 악조건들은 아군에게 더욱 혹독하게 적용될 수도 있었다.

“쿨럭. 흐읍.”

고지대(高地帶)에 진입한 탓일까.

아니면 늙어 버린 육신 때문일까.

연신 기침을 내뱉으며 가쁘게 호흡하는 남호의 모습에 내가 막 지시를 내리려던 그때, 한발 앞서 그의 곁으로 다가가는 누군가가 있었다.

“호흡을 가라앉히고, 몸의 긴장을 푸시오.”

툭.

침착한 음성과 함께 명문혈(命門穴)을 짚은 손. 동시에 남호를 중심으로 미약한 기운이 들끓었다.

화아악.

조금씩 창백해져 가던 남호의 안색이 한결 편안해진다.

명문혈을 통해 주입된 공력으로 말미암아 본래의 혈색을 되찾은 그가 언제 그랬냐는 듯이 평소처럼 투덜거렸다.

“빌어먹을. 늙은 게 죄지. 여하튼 도와줘서 고맙…….”

미처 끝맺어지지 못한 채 흩어지는 음성.

감사를 표하며 막 돌아선 남호가 무심코 말꼬리를 흐리자, 그의 등 뒤에 서 있던 사마표가 무뚝뚝한 얼굴로 물었다.

“왜 그러시오, 무슨 문제라도?”

하지만 당황은 찰나였고, 늙은 은영각 요원의 대처는 신속하면서도 자연스러웠다.

“응? 아니, 문제는 무슨. 그냥 저쪽에서 뭐가 움직인 것 같길래.”

“저쪽?”

남호가 가리키는 방향을 따라 사마표가 고개를 돌린 그때, 때마침 메마른 나무 뒤에 웅크리고 있던 자그마한 그림자가 후다닥 튀어나와 눈밭을 가로질렀다.

“산토끼였군. 걱정할 필요 없소.”

“그런가? 하긴, 여기까지 놈들이 숨어들어왔을 리 없지. 늙으니 걱정만 많아져서 문제라니까.”

능청스럽게 대꾸한 남호가 나를 바라보며 입맛을 다셨다.

“겨우 이 정도로 숨이 턱 끝까지 차는 걸 보니 늙긴 한 모양이야. 더도 말고 덜도 말고 딱 십 년만 젊었어도 선봉에 섰을 텐데. 안 그런가?”

아는 게 많은 사람일수록 반응이 도드라지는 법.

그럼에도 유연하게 감정을 숨긴 남호를 향해, 나는 담담한 어조로 대꾸했다.

“노망나셨어요? 십 년이 아니라 삼십 년을 회춘해도 어림없습니다.”

단순히 지금의 이 상황을 자연스럽게 넘기기 위해서 한 대답은 아니다.

당장 주위만 둘러봐도 헐떡거리며 대설산을 오르는 이들이 한 무더기였으니까.

‘어쩔 수 없는 일이지. 질보다는 양을 우선시했으니.’

감숙성의 면적이 제아무리 넓다고는 하나 결국은 일개 성.

그럼에도 삼만이라는 어마어마한 머릿수를 끌어모을 수 있었던 것은, 모집 과정에서 수많은 어중이떠중이까지 받아들였기 때문이다.

이제야 겨우 코밑이 거뭇거뭇해지기 시작한 애송이부터, 평생토록 뒷골목만을 전전하다 늙어 버린 삼류 칼잡이까지.

누군가에게 목숨을 위협당하거나, 혹은 누군가를 죽여 본 적이나 있을까 싶은 이들이 온 사방에 가득했다.

한마디로 정의하자면, 무림이라는 이 거대한 바다에서 여타 포식자들의 먹잇감이나 다름없는 잡어(雜語)와 같은 자들.

물론 나는 저들을 경멸하지 않는다.

그럴 자격도, 생각도 없다.

나도 한때 약자였으니까. 더불어 지금 이 순간조차도 다른 누군가에게는 아직 약자에 불과하니까.

하지만 내가 진심으로 우려하고 있는 점은, 머릿수만 부풀려진 이 병력으로 암천의 전력과 맞서야 한다는 것이다.

게다가…….

‘저들 중 과반수는 사파인이지.’

누군가가 그랬다.

흰 고양이든 검은 고양이든, 쥐만 잘 잡으면 그만이라고.

나 역시 그 발언 자체에는 동의한다.

이미 역사가 증명해 주었으니까.

정마대전은 천하 무림이 대통합되는 결정적인 계기였고, 과거 현대의 대격변 당시에는 악명 높던 멕시코 마약 카르텔조차 정부군에 합류하여 몬스터들과 싸웠다.

이렇듯 외적(外敵)의 등장은 어제의 적을 오늘의 아군으로 만들어 주기도 한다.

그러나 현재의 상황에서 중요한 것은, 수많은 저 검은 고양이들의 목에 방울을 단 이가 누구이며 그 진정한 의도가 무엇이냐는 것이었다.

‘흑야왕 사마공.’

정마대전에서 살아남은 가장 크고 힘 있는 검은 고양이이자, 작금의 사파 무림을 지배하는 또 한 명의 맹주(盟主).

만약 그가 이미 다른 마음을 품고 있다면, 돈황에서의 대패와 공동파의 몰락은 오래전에 정해져 있던 과정의 일부에 지나지 않는다.

그리고 그 일련의 과정 끝에는, 암천(暗天)이라는 새로운 하늘이 모두를 기다리고 있을 것이다.

‘그것만큼은 막아야 한다. 무슨 수를 써서라도.’

마음속으로 뇌까린 나는 힐끗 등 뒤를 바라보았다.

묵묵히 걸음을 옮기고 있던 사마표가 그 찰나의 시선을 느끼고 작게 눈인사를 건네 보였다.

평소와 별다를 것 없는 그 모습에, 커다란 바위가 가슴 한구석을 빠듯하게 짓누르는 듯하던 그때였다.

파스스슥.

수십여 장 밖, 잎사귀 하나 붙어있지 않은 앙상한 나무들이 동시에 몸을 떨더니 일단의 무리가 모습을 드러냈다.

나뭇가지 사이로 번뜩이는 수백여 개의 은빛 화살촉과 함께.

하지만 찰나의 경계심은, 이내 누군가의 외침과 함께 한결 수그러들었다.

“활을 거둬라. 감숙 무림의 형제들이다!”

물론, 그들 전부가 그런 것은 아니었다.

“대기. 내 명이 떨어질 때까지 결코 경계를 늦춰선 안 될 것이다!”

우렁찬 목소리와 그에 어울리는 투박한 갑옷.

투구까지 깊게 눌러쓴 채 중무장을 갖춘 사내의 모습을 본 순간, 불현듯 뇌리를 스치는 두 글자가 있었다.

‘군문(軍門).’

사박, 사박.

육중한 갑옷을 걸쳤음에도 표횰한 움직임.

그리 빠르지도, 느리지도 않은 발걸음으로 십여 장의 거리를 좁혀온 사내에게 선봉을 맡고 있던 사마공이 입을 열었다.

아니, 입을 열려고 했다는 표현이 정확할 것이다.

물 흐르듯 자연스럽게 사마공을 스쳐 지나간 사내가, 나를 똑바로 응시하며 이렇게 물었으니까.

“혹, 존함을 여쭈어도 되겠습니까.”

“어허, 무엄하오! 대관절 이분이 누구신 줄 알고 감히 대답을 요구하는 것인가!”

당연하게도, 내가 한 대답이 아니다.

내가 미처 뭐라 하기도 전, 앞으로 나선 혁무진이 한껏 거드름을 피우며 손에 든 은패(銀牌)를 번쩍 치켜들었…… 아니, 잠깐만. 저건 언제 또 가져갔지?

“이분으로 말씀드릴 것 같으면 산서성의 패자인 대태원진가의 삼공자이며, 대국 황실을 수호하는 금의위 정천호이자, 지엄하신 황제 폐하께서 친히 임명하신…….”

“소관, 감숙성 위지휘사사(衛指揮使司) 부천호(副千戶) 홍표!”

흡사 포효와도 같은 외침이 혁무진의 목소리를 집어삼키고, 철탑과도 같던 무릎이 굽혀졌다.

쿵.

둔중한 소음과 함께 한쪽 무릎을 꿇은 사내, 아니 홍표가 나를 향해 힘찬 군례를 올렸다.

“상산후(上山后)를 배알하나이다!”

“상산후를 배알하나이다!”

서늘한 눈밭을 가로지르는 수백의 외침.

그제야 활과 병장기를 거두고 홍표를 따라 일제히 무릎을 꿇고 부복하는 관군들의 모습에, 혁무진이 몸을 부르르 떨었다.

“크으으. 으읏. 아아아.”

“……뭐냐, 그 이상한 소리는.”

“조장님. 저 쌀 것 같습니다.”

“…….”

싸긴 뭘 싸, 미친놈아.

한숨을 푹 내쉬며 고개를 절레절레 흔든 그때, 묘한 눈빛으로 이쪽을 바라보던 사마공과 눈이 마주친 나는 작게 입맛을 다셨다.

“무진아.”

“예?”

“그냥 싸라. 시원하게.”

그 순간, 혁무진이 정색하며 대답했다.

“싸긴 뭘 싸요. 말이 그렇다는 거지.”

“…….”

“앞으로는 아랫사람 앞에서 그런 깨는 말 쓰지 마십쇼. 열후로서의 위엄을 유지하셔야지. 안 그러면 천박해 보여요.”

죽이고 싶다, 진짜로.



* * *



감숙성 위지휘사사 부천호라는 긴 직함을 가진 사내, 홍표는 곰 같은 사내였다.

좋게 말하면 우직하고, 나쁘게 표현하자면 융통성이 없어도 너무 없어서 빠꾸가 없는.

한마디로 정리하자면…….

‘언럭키 정호군이라고 해야 하나.’

한시가 급했던 사정상 뒤에 남겨 두고 올 수밖에 없었던 금의위 천호 정호군을 떠올려 봤을 때, 홍표는 그와 닮았으면서도 확연히 다른 인물이었다.

그리고 오늘에서야 처음 알게 된 홍표의 성격을 이토록 단언할 수 있었던 가장 큰 계기는, 다름 아닌 사마공을 대하는 그의 태도 때문일지도 몰랐다.

“자네가 바로 그 소문의 부천호로군. 공무(公務)를 집행함에 있어서만큼은 천하의 누구보다 철두철미하다는.”

앞서 한 차례 무시당했음에도 부드러운 미소를 띤 채 말을 걸어오는 사마공을, 멀뚱멀뚱 지켜보던 홍표가 입을 열었다.

“호패.”

“응?”

“호패를 제시하시오. 절차에 따라 신분부터 확인하겠소.”

“……호패를 제시하라니, 설마 내게 하는 말인가?”

순수한 의문이 가득한 물음에, 홍표가 망설임 없이 고개를 끄덕였다.

“그렇소만.”

“혹 내가 누구인지 모르는 것인가?”

“재작년 성주님 회갑연 때 먼발치에서 한번 봤소. 내 상관이신 위지휘사 나리께 여쭈어보니, 흑룡마문의 문주라고 하시더군.”

“그렇군. 알면 됐네.”

“되긴 뭐가 된다는 거요? 그때는 그때고, 지금은 지금이지. 본관이 맡은 임무는 이 일대 삼백여 장을 지키고 통행하는 이들의 신분을 확인하는 것. 단지 그뿐이오. 상산후께서는 이미 그 절차를 거치셨고.”

별 희한한 사람 보겠다는 듯이 사마공을 응시한 홍표가 눈살을 찌푸렸다.

“두 번 말하게 하지 마시오. 척 봐도 연배가 있어 보이니 혀가 반 토막 난 것은 이해해 주겠지만, 계속 불응할 시에는 노인장도 재미없을 거요.”

“……!”

순간 주변의 공기가 얼어붙었다고 느낀 것은, 비단 이곳이 만년설로 뒤덮인 대설산이기 때문만은 아니었다.

사마공이 누구인가.

감숙 무림에 막대한 영향력을 행사하는 흑룡마문의 문주고, 그가 차지하는 입지와 권세를 따지자면 성주(城主)와 겸상을 하고도 남는다.

한마디로 무림과 관부 양측에 끈끈한 연줄이 닿아 있는 감숙성의 실력자.

한데 그런 그에게 호패 요구에, 노인장 운운하다니.

그것만으로도 모두가 놀라움을 금치 못할 지경인데, 홍표는 여기에서 멈추지 않고 한 걸음 더 나아갔다.

슥.

“분명히 말했소. 두 번은 없다고.”

나직한 덧붙임과 함께 허리춤에 매어둔 철곤(鐵棍)을 떡하니 꺼내 드는 홍표의 모습에, 사마공은 물론 주위 사람 전부가 할 말을 잃은 그때였다.

“으하, 으하하하! 그렇지, 암, 그게 맞지!”

쩌렁쩌렁 울려 퍼지는 웃음소리. 배꼽까지 붙잡으며 껄껄 웃던 적천강이 홍표를 바라보았다.

“사내라면 응당 본인이 맡은 소임에 충실해야 하는 법. 그래, 네놈의 이름이 뭐라고?”

호의로 가득한 적천강의 물음에, 홍표가 대답했다.

“호패.”

“……으응?”

“그쪽도 호패 준비하시오. 이 노인장 다음은 당신이니까.”

“……!”

“아, 통행증도 같이. 머리카락부터 온통 시뻘건 게 영 수상하기 짝이 없군.”

당장이라도 모두를 질식시킬 것만 같은 침묵 속, 몸을 부르르 떤 혁무진이 개미 울음소리보다 작은 목소리로 속삭였다.

“조장님. 저 진짜 쌀 것 같아요.”

하지만 내가 뭐라 대답하기도 전에, 저 멀리 펼쳐진 새하얀 산등성이 너머에서 메아리처럼 울려 퍼지는 소리가 있었다.

둥, 두둥, 두우웅!

급박함이 담긴 북소리.

전고(戰鼓)의 울림이, 눈 덮인 산맥을 떨어 울렸다.
```

## Final English reading copy

```markdown
# Chapter 1023

Huff, huff.

Footsteps climbed the steep mountain slope without a word, while clouds of white breath billowed here and there.

The Great Snow Mountain was cold year-round, like the middle of winter, and its air was thin. Those who had come to defend this land were no exception to its harsh conditions.

If anything, the brutal environment might have been even harder on our side.

“Cough. Haa…”

Was it because we’d entered the highlands?

Or because his body had grown old?

Namho kept coughing, struggling to catch his breath. I was just about to give him an order when someone stepped up beside him first.

“Steady your breathing and relax your body.”

Tap.

A calm voice, a hand pressing the Mingmen acupoint. At the same time, a faint energy stirred around Namho.

Whoosh.

The pallor creeping across his face eased, and his complexion regained some color. With the internal energy sent through the Mingmen acupoint, Namho looked as if nothing had happened and went back to grumbling as usual.

“Damn it. Getting old’s a crime. Anyway, thanks for the help…”

His words trailed off before he could finish.

Namho had just turned to thank him when his voice faltered despite himself. Standing behind him, Sama Pyo asked with an impassive face,

“What is it? Is something wrong?”

The surprise lasted only an instant. The old Hidden Shadow Pavilion agent recovered quickly and smoothly.

“Hm? No, nothing’s wrong. I just thought I saw something moving over there.”

“Over there?”

As Sama Pyo turned to look where Namho was pointing, a small shadow sprang out from behind a dry tree and darted across the snow.

“It was a mountain hare. No need to worry.”

“Is that so? Well, it’s not like they could’ve snuck all the way up here. Getting old just means you’ve got more to worry about.”

Namho replied nonchalantly, then looked at me and smacked his lips.

“Getting winded from something this small must mean I really am old. If I were just ten years younger—not a day more or less—I’d be leading the charge. Wouldn’t you say?”

The more someone knew, the more they tended to give themselves away.

Even so, Namho had hidden his feelings smoothly. I answered in an even tone.

“Have you lost your mind? You wouldn’t be fit to lead the charge even if you were thirty years younger.”

That wasn’t just an answer meant to brush off the situation.

All around us, plenty of people were huffing and puffing as they climbed the Great Snow Mountain.

*Can’t be helped. We chose quantity over quality.*

Gansu Province was vast, but it was still just one province.

The only reason we’d managed to gather the staggering number of thirty thousand was that we’d taken in all manner of riffraff during recruitment.

From green youngsters whose upper lips had only just begun to darken to Third Rate swordsmen who’d spent their entire lives roaming the back alleys until they’d grown old.

The place was full of people who might never have had their lives threatened—or taken another’s.

In a word, they were like little fish in the vast sea of Murim, nothing more than prey for the predators around them.

Of course, I didn’t look down on them.

I had neither the right nor the inclination to.

I’d once been weak too. And even now, there were still people to whom I was nothing but weak.

What truly worried me was having to face Dark Heaven’s forces with an army whose numbers had been inflated without adding much strength.

And besides…

*More than half of them belong to the unorthodox faction.*

Someone once said that it didn’t matter whether a cat was white or black, as long as it caught mice.

I agreed with the sentiment.

History had already proved it.

The Great Faction War had been the decisive turning point that united Murim under one banner. And during the Great Cataclysm in the modern era, even the infamous Mexican drug cartels had joined the government forces to fight the monsters.

The appearance of an outside enemy could turn yesterday’s foe into today’s ally.

But what mattered now was who had put bells around the necks of all those black cats—and what that person truly intended.

*The Black Night King, Sima Gong.*

The biggest and most powerful black cat to survive the Great Faction War, and another Alliance Leader who now ruled the unorthodox Murim.

If he’d already set his sights on something else, then the crushing defeat at Dunhuang and the fall of the Kongtong Sect might have been nothing more than steps in a process decided long ago.

And at the end of that process, a new Heaven called Dark Heaven would be waiting for everyone.

*I have to stop that. No matter what it takes.*

I muttered the words inwardly and glanced behind me.

Sama Pyo, walking along in silence, caught my brief look and gave me a small nod.

He looked no different from usual. Yet just then, it felt as if a huge boulder were pressing down on one corner of my chest.

Rustle.

Dozens of *jang* away, a group appeared as the bare, leafless trees shivered all at once.

Hundreds of silver arrowheads flashed between the branches.

But the brief flare of alarm soon eased at someone’s shout.

“Lower your bows. They’re brothers from Gansu Murim!”

Of course, not everyone lowered their guard.

“Stand by. Do not let your guard down until I give the order!”

A booming voice, a rough suit of armor to match it.

The sight of a heavily armed man, his helmet pulled down low, brought two words to mind.

*The military.*

Step, step.

Despite the weight of his armor, he moved with easy grace.

The man closed the distance at an unhurried pace—not too fast, not too slow. Sima Gong, who had been leading our group, opened his mouth to speak.

No—that wasn’t quite right. He was about to speak.

The man passed Sima Gong as smoothly as water flowing downstream, fixed his gaze on me, and asked,

“May I ask your name, sir?”

“Have you no manners? Do you even know who this man is, to demand an answer from him?”

Naturally, that wasn’t my answer.

Before I could say a word, Hyuk Mujin stepped forward, putting on airs as he raised the silver tablet in his hand—no, wait. When had he taken that?

“If I may introduce him, he is the Third Young Master of the great Jin Family of Taiyuan, the hegemon of Shanxi Province; a Commander of the Embroidered Uniform Guard who protects the Great Nation’s imperial family; and one personally appointed by His August Majesty the Emperor…”

“Hong Pyo, Deputy Thousand Captain of the Gansu Regional Military Commission!”

A roar swallowed Hyuk Mujin’s voice. The knees of the man, who had stood like an iron tower, bent.

Thud.

With a heavy sound, the man—Hong Pyo—knelt on one knee and gave me a crisp military salute.

“I pay my respects to the Marquis of Shangshan!”

“We pay our respects to the Marquis of Shangshan!”

Hundreds of voices carried across the cold snowfield.

Only then did the imperial troops lower their bows and weapons, kneel in unison like Hong Pyo, and bow low. Hyuk Mujin trembled.

“Grrr. Ugh. Ahhh.”

“…What is that weird noise?”

“Captain. I think I’m gonna burst.”

“…”

Burst, my ass. You lunatic.

I sighed and shook my head. Just then, I met Sima Gong’s gaze as he watched us with a peculiar look, and I clicked my tongue.

“Mujin.”

“Yes?”

“Just do it. Let it all out.”

Hyuk Mujin’s face turned stern.

“What do you mean, let it out? I was just saying.”

“…”

“Don’t say embarrassing things like that in front of your subordinates. You need to maintain your dignity as a marquis. Otherwise, you’ll look vulgar.”

I really wanted to kill him.

* * *

Hong Pyo, the man with the lengthy title of Deputy Thousand Captain of the Gansu Regional Military Commission, was built like a bear.

To put it kindly, he was steadfast. To put it less kindly, he had absolutely no flexibility—and no sense of when to back down.

In a word…

*An unlucky Jeong Hogun, maybe.*

Thinking of Thousand Captain Jeong Hogun, whom we’d had no choice but to leave behind because we were in such a hurry, Hong Pyo reminded me of him, yet was unmistakably different.

And the biggest reason I could make such a firm judgment about Hong Pyo’s character, whom I’d only met today, was probably his attitude toward Sima Gong.

“So you’re the Deputy Thousand Captain everyone’s been talking about. They say no one in the world is more meticulous than you when it comes to carrying out official business.”

Sima Gong had already been ignored once, but he addressed Hong Pyo with a gentle smile. Hong Pyo stared at him blankly for a moment, then spoke.

“Your identity tablet.”

“Pardon?”

“Present your identity tablet. I’ll confirm your identity first, as procedure requires.”

“…You’re asking me to present my identity tablet? Surely you’re talking to me?”

Hong Pyo nodded without hesitation, as if the question were perfectly reasonable.

“I am.”

“Do you not know who I am?”

“I saw you once from a distance at the City Lord’s sixtieth-birthday banquet the year before last. When I asked my superior, the Regional Military Commissioner, he told me you were the Sect Leader of the Black Dragon Demon Gate.”

“I see. Then you know.”

“Know what? That was then. This is now. My assigned duty is to guard this stretch of about three hundred *jang* and verify the identities of those passing through. Nothing more. The Marquis of Shangshan has already gone through the procedure.”

Hong Pyo looked at Sima Gong as if he’d never seen such a strange man before, then furrowed his brow.

“Don’t make me repeat myself. You’re clearly older, so I’ll overlook how casually you speak to me. But keep refusing, old man, and you won’t like what happens.”

“……!”

The air around us seemed to freeze. It wasn’t just because we were on the Great Snow Mountain, covered in everlasting snow.

Who was Sima Gong?

The Sect Leader of the Black Dragon Demon Gate, with enormous influence over Gansu Murim. Given his standing and power, he could sit as an equal with the City Lord.

In short, he was a powerful figure in Gansu Province, with strong ties to both Murim and the government.

And Hong Pyo had demanded his identity tablet and called him an old man.

That alone was enough to leave everyone speechless. But Hong Pyo didn’t stop there. He went a step further.

Shing.

“I said it clearly. There won’t be a second time.”

As he added those quiet words, Hong Pyo drew the iron baton from his waist.

Sima Gong and everyone around him were at a loss for words.

“Ha! Hahahaha! Yes, that’s right! That’s how it should be!”

Jeok Cheongang’s laughter rang out. Holding his stomach, he guffawed as he looked at Hong Pyo.

“A man should fulfill the duty entrusted to him. Now, what was your name again?”

Hong Pyo answered Jeok Cheongang’s friendly question.

“Your identity tablet.”

“…What?”

“You should have yours ready too. You’re next, old man.”

“……!”

“And your travel pass as well. Even your hair is bright red. You look downright suspicious.”

In the silence, heavy enough to suffocate everyone, Hyuk Mujin trembled and whispered in a voice quieter than an ant’s squeak.

“Captain. I really think I’m gonna burst.”

But before I could answer, a sound echoed like a distant call from beyond the white ridge stretching far away.

Boom. Ba-boom. Ba-boom!

A drumbeat, urgent with alarm.

The sound of the war drums shook the snow-covered mountain range.
```
