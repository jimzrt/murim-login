<!-- packet-manifest
{
  "included": [
    {
      "path": "source/1118.txt",
      "sha256": "d1f9f4af8077f7a29ea0b5011274632c3ea05d3b97c2828165d81641e2cbf08f",
      "bytes": 12486
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "9857d4843f9ca9ec962ae470601769ebf9645f796a1785eee37471562307519d",
      "bytes": 1148
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "66b724f4d846741f2cbbc7e843d83ef54cdbfc708dd1f9b56308f753f4d5a999",
      "bytes": 244911
    },
    {
      "path": "characters/Cheongheoja.md",
      "sha256": "051f6f010829b076b1d812ed94b32adee9c1b2231a9d18dc41705f866ab842f3",
      "bytes": 557
    },
    {
      "path": "characters/Hyuk Mujin.md",
      "sha256": "334dbc9f98845552dccfcd1c8e120dd43b2900660b99481a4d9297989606ea2b",
      "bytes": 1375
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "a434d53a6405ba1aafea003b53fdaeb533ec9aac3184aa882d5611598d175a90",
      "bytes": 1828
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "6b48abf6e086c484b6cffde63393d3e40e6a8fbef136e5aa650b68c9d737d8b6",
      "bytes": 623
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "d55475543ec1fb1c82a8c660ed8fc6b6c7536abad3e5c84ebccc42321005d0fd",
      "bytes": 289267
    }
  ],
  "estimated_tokens": 10144
}
-->

# Durable State Update — Chapter 1118

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
1 and safe_through 1118. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 1118. Profile updates may replace only one
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
  "chapter": 1118,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 1118,
    "continuity_sources": [1118],
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
    "The West Gate has fallen, and the South Gate defenders were ordered to retreat to the Inner City.",
    "Cheongheoja remains at the East Gate with a small group of allies.",
    "Hak Eui is alive; a disguised prisoner's corpse led others to believe he had been killed.",
    "Hak Su, formerly Cheongheoja’s Senior Disciple and a Dark Heaven spy known as Number Six, was killed at the East Gate as a Kunlun Sect traitor.",
    "The East Gate defenders opened the iron bridge and gate as a trap; two Black Ghosts and a thousand monsters entered before the gate began closing.",
    "A horn sounded from the direction of the Yangtze River Channel League as the East Gate confrontation continued."
  ],
  "continuity_sources": [
    1116,
    1117
  ],
  "open_questions": [
    "What will happen in the East Gate battle now that the Black Ghosts and monsters have entered?",
    "Will the approaching Yangtze River Channel League reach the East Gate in time?"
  ],
  "safe_through": 1117,
  "temporary_decisions": [
    "Render 육호 as “Number Six” for Hak Su’s Dark Heaven identifier."
  ],
  "version": 1
}
```

## Exact glossary matches

| 진태경    | **Jin Taekyung**   |
| 혁무진    | **Hyuk Mujin**     |
| 쾌풍검    | **Swift Wind Sword**          | Hyuk Mujin     |
| 살성     | **Slaughter Saint**           | —              |
| 진룡대    | **Jin Dragon Squad**             |
| 곤륜파    | **Kunlun Sect**                  |
| 암천     | **Dark Heaven**                  |
| 장강수로맹  | **Yangtze River Channel League** |
| 절정     | **Peak**          |
| 초절정    | **Supreme Peak**  |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 경지     | **realm** / **realm stage**                      | Especially power level                                |
| 살기     | **killing intent**                               |                                                       |
| 검기     | **Sword Energy**                                 | When functioning as projected weapon qi               |
| 후기지수   | **young prodigy** / **rising martial artist**    | Contextual, not a title                               |
| 정파     | **orthodox faction**                             |                                                       |
| 사파     | **unorthodox faction**                           |                                                       |
| 대주     | **Squad Leader** / **Commander**             |
| 부대주    | **Vice Squad Leader** / **Deputy Commander** |
| 제자     | **Disciple**                                 |
| 상태               | **Status**                     |
| 청해     | **Qinghai**            |
| 곤륜     | **Kunlun**             |
| 대사      | **Master** for a senior Buddhist monk                           |
| 청허자 | **Cheongheoja** | Kunlun Sect Leader. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 조장 | **Captain** | Hyuk Mujin's address for Taekyung as squad leader. |
| 개방 | **Beggars' Sect** | Murim organization counted among the Nine Sects and One Gang. |
| 연무장 | **training ground** | Private martial-arts practice area at Taekyung's newly rebuilt pavilion. |
| 강시 | **jiangshi** | Reanimated corpse from folklore; Childeuk and Hong mistakenly identify Taekyung as one. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 녹림맹 | **Green Forest Alliance** | Bandit alliance receiving Black Mountain Stronghold’s tribute. |
| 마도 | **Demonic Path** | Term raised for martial power that appears to defy common principles. |
| 초절 | **supreme mastery** | Realm beyond Peak described as accessible only to the greatest martial artists. |
| 화룡 | **fire dragon** | Fire-dragon image within Taekyung's dantian that awakens before the duel. |
| 천주 | **Lord of Heaven** | Authority invoked by the masked attackers. |
| 꼬리 | **the “tail”** | Codename for the Black Hunter traced by Butler Kim. |
| 장강 | **Yangtze** | The river controlled by the Yangtze River Channel League. |
| 일원 | **One Origin** | Named Tang Clan organizational unit in Tang Sadok's mobilization order. |
| 암초 | **reef** | Reefs blocking the narrow water route. |
| 진룡 | **Jin Dragon** | The two characters embroidered on the Jin Dragon Squad's uniforms. |
| 검기상인 | **the level of injuring others with Sword Energy** | Realm description used for Moon Beauty Saber. |
| 황하 | **Yellow River** | River along which civilization began. |
| 화룡각 | **Fire Dragon Pavilion** | New name chosen for Taekyung's pavilion. |
| 동문 | **East Gate** | One of the Nanman Beast Palace's gates. |
| 흑귀 | **Black Ghost** | The Blood-Sword Demon Lord’s name for the Death Knights. |
| 대인 | **Great Sir** | Name used for the mysterious figure in Ningxia. |
| 청해호 | **Qinghai Lake** | Destination of the retreat; distinct source form from 청해성. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 혁무진 | 진태경 | squad_subordinate_to_squad_leader | Squad Leader | deferential | Hyuk Mujin says he obeys only his squad leader's orders and identifies Taekyung as the Third Young Master. |
| 진태경 | 혁무진 | squad_leader_to_squad_subordinate | Mujin | familiar-and-commanding | Taekyung calls him 무진아 while summoning him from the driver's box. |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 상인 | 청년 | stranger_to_stranger | Young Brother | formal-polite | A merchant uses 소형제 after noticing the young man's sword, and the young man approves of the address. |
| 청년 | 상인 | stranger_to_stranger | friend | casual and shameless | The young man declares that they should be friends after drinking their Yeoahong. |
| 진태경 | 청년 | celebrated Hunter to younger fellow Hunter | young man | casual, teasing, and profane | Jin addresses the young Hunter after overhearing his criticism and deliberately switches to casual speech. |
| 청년 | 진태경 | frightened junior Hunter to celebrated senior Hunter | you | fearful and deferential | The young Hunter uses 당신 while asking whether Jin is really the person he recognizes from the media. |
| 혁무진 | 조장님 | pavilion_member_to_squad_leader | Captain | deferential and dubious | Mujin questions whether the pasture should be called the Nanman Ranch instead of the Nanman Beast Palace. |
| 진태경 | 대인 | young martial artist to benefactor | you | casual and blunt | Taekyung asks who Great Sir is, addressing him as 당신. |
| 대인 | 진태경 | older benefactor to young martial artist | you | familiar conversational | Great Sir addresses Taekyung as 자네. |
| 살성 | 청허자 | fellow martial master and former acquaintance | you | blunt and familiar | Recognizes him from a prior meeting. |
| 진태경 | 청허자 | younger martial artist to senior sect leader | Sect Leader | respectful | Uses a formal greeting and bow. |
| 청허자 | 진태경 | senior sect leader to younger martial artist | Fellow Daoist Jin | warm and polite | Greets Taekyung by surname and confirms Hak Woo is well. |

## Listed compact profiles

### Cheongheoja.md

# Cheongheoja (청허자)

- **Safe through:** Chapter 1117
- **Aliases:** None
- **Role:** Cheongheoja is the Kunlun Sect Leader and Hak Woo’s master.
- **Personality:** Warm, composed, and patient, he faces setbacks with resolve and receives even startling company with good humor.
- **Voice:** Measured and gentle, using formal Daoist courtesies and calm metaphors.
- **Relationships:** Hak Su and Hak Eui are his Disciples; he knows Jin Taekyung by reputation and treats him warmly.

### Hyuk Mujin.md

# Hyuk Mujin (혁무진)

- **Safe through:** Chapter 1097
- **Aliases:** Swift Wind Sword
- **Role:** Hyuk Mujin is a Level 50 First Rate martial artist who serves as Captain of the Jin Family's Gatekeepers, Vice Squad Leader of the Jin Dragon Squad, and an active member of the Fire Dragon Pavilion.
- **Personality:** Young, disciplined, persistent, and talented; despite being naturally fearful, he faces danger and remains loyal to the person he serves, with irreverent self-deprecation and a taste for glory. He is suspicious of Taekyung, bluntly critical of the family's disgraced third son, and an avid wuxia reader who sometimes mistakes fictional conventions for reality.
- **Voice:** Formal and clipped in official duties; with Taekyung, blunt and occasionally incredulous, while using breezy, irreverent banter to defuse tense situations.
- **Relationships:** He is loyal to Taekyung, who trusts him to act independently, especially in his home region of Shanxi and at the Jin Family of Taiyuan. As a former family gate guard, he knows the most about Head Elder Jin Baekyang among the Fire Dragon Pavilion members accompanying Taekyung. Son of the Hyuk Family Textile Shop's owners; a younger sibling means he need not inherit the business.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 1115
- **Aliases:** Blazing Flame Divine Dragon; Apostle of the Earth Mother Goddess; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan and the original owner of his current body, Jeok Cheongang’s Disciple, the Fire Gate Clan’s nineteenth successor, Pavilion Master of the Fire Dragon Pavilion, a Supreme Peak master who has reached the realm of the Ten Kings as its eleventh member and can detect and eavesdrop on nearby Sound Transmissions subject to the participants’ relative levels, and a publicly recognized S-rank-level Hunter with an A-rank license, a traveler between Murim and another world, and the World Hunter Federation’s Alliance Leader; the Emperor appointed him Marquis of Shangshan and Thousand Captain of the Embroidered Uniform Guard.
- **Personality:** Hungry, self-aware, and dryly observant; pragmatic under pressure, willing to risk himself for others, and fiercely defiant when others try to dictate his choices or survival.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, and Jeok Cheongang is his Master and trusted confidant; Hyuk Mujin trusts Taekyung to fight beside him; Taekyung trusts Sama Pyo as a friend despite suspecting his betrayal, and values him beyond his unorthodox affiliation; Peng Cheolhu regarded Taekyung as a worthy successor, and the Bow Saint relayed the Martial God’s message to him.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 1115
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

## Korean source

```text
＃1118화



부우우우우!

저 멀리서 힘차게 울려 퍼진 나팔 소리가 귓가에 닿은 순간, 동문을 지키던 수비군들은 문득 생각했다.

점차 가까워지고 있는 저 소리가, 자신들을 돕기 위해 달려온 지원군의 것이었다면 얼마나 좋았을까 하고.

그러나 그들의 앞에 놓인 현실은 잔인하면서도 선명했다.

“장강수로맹…….”

누군가의 입술을 비집고 흘러나온 신음은 수비군 모두의 마음을 대변하는 것이었다.

비록 보이지는 않지만, 똑똑히 들었다.

서쪽도, 남쪽도, 북쪽도 아니다.

나팔 소리의 근원지는 그들에 서 있는 동문의 성벽 너머에서 울려 퍼지는 중이었고, 이는 곧 한 가지 사실만을 의미했다.

‘놈들이 왔다.’

동쪽에서 찾아올 불청객의 정체는 이미 모두가 알고 있었다.

녹림맹과 장강수로맹.

넓고 푸른 강산(江山)을 누비는 것으로도 모자라, 천하의 한 조각마저 손에 넣으려는 두 개의 거대한 도적 집단.

거기에 더하여 그들과 함께하고 있을 암천의 군세까지.

물경 삼만에 달할 것이라 짐작되는 적의 대군이 마침내 오늘 이 자리에 나타난 것이다.

장강의 긴 강줄기를 따라, 황하(黃河)의 거센 물살마저 거슬러 오며.

그리고 이 참혹한 현실 앞에 침묵하는 그들의 모습에, 두 강시 술사는 입꼬리를 비틀며 웃어 보였다.

“멍청한 것들 같으니.”

“이제야 알겠느냐? 네놈들이 얼마나 얕은 수작을 부린 것인지.”

흑의인과 그 동료는 굳이 기쁨을 감추지 않았다.

비록 수비군의 유인계에 휘말려 성안에 갇힌 상태지만, 당장의 전력만으로도 세 배에 달하는 병력 차이쯤은 가뿐하게 상쇄할 정도.

심지어는 때맞춰 수만 명의 지원군까지 도착해 버렸으니, 조금 전 함정에 빠진 것을 깨닫고 한 순간이나마 긴장했던 자신들의 모습이 부끄럽게 느껴질 정도였다.

‘진정으로, 천주께서 도우시는군.’

자신이 섬기는 새로운 하늘을 떠올리며, 흑의인이 흐릿하게 미소지은 그때였다.

저벅.

당장이라도 후퇴해야 할 이 상황에, 물러서기는커녕 되려 앞으로 걸음을 내딛는 일단의 무리.

‘그래, 곤륜의 말코들이라면 응당 이리 나올 줄 알았지.’

그들의 선두를 차지한 청허자와 곤륜파의 제자들을 발견하고 내심 고개를 끄덕이던 흑의인은, 다음 순간 툭 튀어나와 그 옆에 나란히 서는 얼굴들을 발견하고 한숨을 내쉬었다.

“아까부터 묻고 싶었는데…… 네놈들은 도대체 누구냐?”

얼핏 봐도 평범한 놈들이었다면 신경조차 쓰지 않았을 것이다.

하지만 강시술사인 그가 보기에도 실로 괴상망측한 조합을 자랑하는 일곱 명의 남녀는, 그런 반응 따위는 아랑곳하지 않고 대답했다.

정확히는, 무슨 이유에선지 중심을 차지하고 있는 청년만이 대표로 입을 열었다.

“쾌풍검(快風劍) 혁무진. 그게 바로 나다.”

일순간, 흑의인의 눈동자가 크게 뜨였다.

“쾌풍검?”

“그래. 역시 들어 보았…….”

“처음 들어 보는데.”

“……좋아, 다시 소개하지. 진룡대의 부대주 혁무진이다. 비록 그쪽 일은 잠시 쉬고 있지만.”

“그 역시 들어 본 적 없다. 앞으로도 계속 쉬어도 되겠군. 물론 오늘 이후로는 이승에 남아 있지도 못하겠지만.”

“……제기랄. 그럼 화룡각(火龍閣)의 부각주 혁무진은?”

그러자 이번에는 다른 이들의 눈동자가 크게 뜨였다.

“뭐? 도대체 언제부터? 부각주면 추가 수당도 받나?”

“아니, 다른 사람도 아니고 왜 굳이 혁 무사님을…… 그나저나 공석 아니었나요?”

“모르겠소. 솔직히 우리 중 누군가가 부각주가 된다면 내가 적격이라고 생각했는데, 사파라서 차별받은 것 같군.”

“차별. 안다. 맛있다.”

“이 자식은 진짜 걸신이라도 들렸나. 내가 진짜 살다 살다 우리 스승님보다도 거지 같은 인간은 또 처음 보네.”

“오, 스승부터가 거지인 모양이군. 어쩐지 자네를 처음 보자마자 그놈 참 잘 빌어먹게 생겼다 싶었지.”

이 와중에도 숨길 수 없는 물욕과 불신, 기울어진 정파 연무장에 대한 실망과 끝없는 식탐. 마지막으로 스승에 대한 불충과 숨 쉬듯이 흘러나오는 무례함까지.

마치 진정한 심연을 마주한 듯한 느낌에, 흑의인과 그 동료는 그만 눈앞이 아찔해졌다.

만약 앞서 들려왔던 혁무진의 대답이 아니었다면, 감히 입을 열 엄두조차 내지 못했을 정도로.

하지만 분명, 화룡각이라는 세 글자는 강시 술사인 그들에게도 제법 낯익은 단어였다.

암천의 일원이라면 지위고하를 막론하고 모두가 알고 있는, 어느 한 사람과 깊은 관련이 있었으니까.

“화룡각이라면…… 네놈들이 바로 그 진태경의?”

잠시 짜게 식은 눈빛으로 동료들을 바라보던 혁무진이 준엄한 어조로 대답했다.

“그렇다.”

“그, 말은 고맙지만 엄밀히 따지자면 난 화룡각 소속이 아니라 개방인데.”

“본녀도 아니다. 음. 아마도.”

“……제발 두 분 다 입 좀 다물어 주시면 안 됩니까? 예?”

흑의인은 새삼스러운 눈빛으로 그들을 훑었다.

맡은 역할과 임무로 인해 쾌풍검이니, 진룡대니 하는 자잘한 정보는 몰라도 화룡각만큼은 들어 보았다.

암천의 대계가 번번이 진태경이라는 암초에 가로막힐 때마다, 그를 도와 활약했던 화룡각의 위명 역시 천하를 떨어 울리지 않았던가.

어째서 가장 잔챙이처럼 보이는 놈이 부각주인지는 모르겠으나, 저 괴이한 면면들이 어떻게 한자리에 모여있는지 충분히 이해가 되는 듯했다.

지금 같은 위험한 상황에서도 대담하게 앞으로 나설 수 있는 이유도.

“초록은 동색이라더니, 제 각주처럼 목숨 아까운 줄 모르는 미친 연놈들만 모여있군.”

흑의인은 피식 실소를 흘렸다.

화룡각?

물론 암천에게 있어 저들이 제법 거슬리는 존재였다는 것은 인정한다.

그러나 그건 어디까지나 진태경의 존재가 곁에 있었기에 가능했던 일.

지금 이 순간, 흑의인의 시야에 담긴 화룡각 대원들은 결국 완전히 무르익지 않은 젊은 후기지수들의 집단에 지나지 않았다.

아직 나설 때와 물러날 때를 구분조차 하지 못하는, 어설픈 혈기와 영웅심에 취한 하룻강아지들.

“헛소리를 지껄일 시간에 도망치지 않은 것. 그것이 네놈들이 죽을 수밖에 없는 이유다.”

이빨조차 제대로 나지 않은 하룻강아지들을 상대로 더 무슨 말을 하겠는가.

최후의 발악을 위해 묵묵히 숨을 고르고 있는 늙고 상처 입은 맹수라면 모를까.

‘초절정 고수가 있는 한, 우리 역시 방심은 금물.’

‘걱정도 많군. 저 정도 전력으로는 이것들을 뚫고 우리에게 해를 입힐 수 없어.’

말없이 눈빛을 주고받은 흑의인과 그 동료는, 굳게 다문 얼굴로 검을 겨누고 있는 청허자와 곤륜의 제자들을 주시하며 손에 쥔 요령을 들어 올렸다.

츠츠츠츠.

- 크르르륵.

두 개의 요령이 뿜어내는 파동을 따라 괴성을 흘리는 일천의 괴물들.

장정 둘을 합친 것만큼이나 거대하고, 검기상인(劒氣傷人)의 경지에 이르지 않고서는 치명상을 남길 수 없을 만큼 단단한 내구성과 회복력을 갖춘 그것들은 당장이라도 튀어나갈 준비를 끝마친 채 눈앞의 적들을 노려보았다.

스아아아아.

어느덧 무시무시한 기파를 흩뿌리고 있는 두 기의 흑귀와 함께, 이미 결사항전(決死抗戰)을 각오한 수비군들조차 본능적으로 뒷걸음질 칠 수밖에 없는 압도적인 살기를 뿜어내며.

그리고 마침내.

“한 놈도 빠짐없이, 모조리 죽여라.”

차가운 어조로 내뱉은 명령과 함께, 두 강시술사의 요령이 힘차게 허공을 내리그은 바로 그 순간이었다.

츠츠츠츠츠.

흑귀와 괴물들의 영혼에 깊숙이 각인된 저주의 음파(音波)가 동문 일대를 휩쓸었다.

그 너머에서 들려오는, 나직한 목소리와 함께.

“우리가 왜 도망을 쳐. 헛소리라도 씨부리면서 시간을 벌어야 하는데.”

“……?”

“……?”

일순간, 자신들도 모르게 움직임을 멈춘 흑의인과 그 동료는 멍하니 눈을 깜빡였다.

제 버릇 남 못 주고 불쑥 끼어든 저 잔챙이. 아니 화룡각의 부각주라 자칭하는 혁무진의 말을 이해하지 못해서?

틀렸다.

수비군을 향해 쇄도해가는 흑귀와는 달리, 보이지 않는 무언가에 속박당한 듯이 사지를 부르르 떨고 있는 일천의 괴물들 때문이었다.

‘분명 명령을 내렸는데…… 도대체 어째서?’

그리고 불현듯 떠오른 의문이 두 강시술사의 뇌리를 스친 그때.

“야, 안 되냐?”

뜻 모를 질문과 함께 돌아선 혁무진의 등 뒤로, 이곳에서 만나리라고는 생각도 하지 못했던 한 사람이 모습을 드러냈다.

“최, 최대한 집중해봤는데. 흐읍. 흑귀까지는 절대 무리…….”

“……!”

“……!”

허공에서 맞닿은 시선과 함께 흐려지는 말꼬리.

지금쯤이면 이미 죽었으리라 예상했던, 청해호(靑海湖)에서 살성에 의해 사로잡힌 이후 종적이 묘연해진 동료의 모습을 발견한 두 강시술사는 눈을 부릅떴다.

그리고 보았다.

청해호 인근에서 죽음을 맞이했던 또 다른 강시술사들의 것이 분명한, 그의 손에 들린 십여 개의 요령과 멍투성이가 된 얼굴 위로 번지는 서글픈 미소도.

“그, 미안하네. 그렇게 됐네.”

그 순간.

쐐애애애액!

어둠을 가르며 날아든 휘황한 빛줄기가, 유령마와 함께 바람처럼 쏘아지던 두 기의 흑귀를 가로막았다.

콰아앙!

거대한 굉음과 함께 사방을 휩쓰는 거센 바람.

그와 동시에 자욱한 흙먼지 너머에서 모습을 드러낸 청허자와 산발의 괴인, 아니 대인(大人)이 흑귀들을 향해 입을 열었다.

“감히, 어딜 가려 하느냐.”

“이러지 말고 우선 대화로…… 오, 방금 그 대사 꽤 멋졌소.”

사면의 성벽을 둘러싼 급박한 난전에 잠시 가려져 있던, 또 다른 초절정 고수의 존재를 깨달은 두 강시술사는 이를 악물었다.

그리고 어쩌면, 지금 이 순간 그들을 가장 분노케 하는 것은 어느 잔챙이의 입가에 맺힌 시건방진 미소일지도 몰랐다.

“만약 조장님, 아니 각주님께서 계셨다면 이렇게 말씀하셨겠지.”

혁무진의 손짓에 따라, 포로로 잡혀있던 강시 술사가 미친 듯이 양손에 들린 요령을 흔들었다.

한 개도 아닌, 십여 개나 되는 요령을.

츠츠츠츠츠!

그리고 살아생전 어느 때보다 강렬한 생존 본능이 실린 그 다급한 딸랑이질은, 그가 평소 발휘할 수 있는 능력의 한계를 한 단계 뛰어넘었다.

그러니까 그말인 즉슨.

- 큭, 크륵?

어제의 동료였으나 오늘의 적으로 만난 두 강시 술사의 통제력을 완전히 빼앗을 수는 없어도, 일천의 괴물들을 혼란에 빠트릴 수 있을 만큼은 되었다는 뜻이었다.



- 크아아아악!

- 구어어어어!



어지럽게 번뜩이는 붉은 안광과, 본래의 목표를 잃어버린 살기.

쿠웅!

콰드드드득!

속박에서 풀린 채 적아를 가리지 않고 미쳐 날뛰기 시작하는 괴물들과, 이 믿지 못할 상황에 얼어붙은 두 강시 술사의 귓가로 혁무진의 한 마디가 화살처럼 파고들었다.

“지금부터, 서로 죽여라.”

부우우우우!

지금 이 순간에도 빠르게 다가오는 나팔 소리 위로, 괴물들의 흉성과 수비군들이 내지르는 함성이 뒤섞였다.
```

## Final English reading copy

```markdown
# Chapter 1118

Boooooo!

The moment the blast of a horn rang out from far away and reached their ears, the defenders guarding the East Gate found themselves thinking:

*If only that sound, drawing closer by the moment, belonged to reinforcements rushing to help us.*

But the reality before them was cruel—and crystal clear.

“The Yangtze River Channel League……”

The groan that slipped from someone’s lips spoke for every defender.

They couldn’t see it, but they heard it loud and clear.

Not the west. Not the south. Not the north.

The horn was sounding beyond the East Gate wall where they stood. That could only mean one thing.

*They’re here.*

Everyone already knew the identity of the uninvited guests arriving from the east.

The Green Forest Alliance and the Yangtze River Channel League.

Two vast gangs of bandits who roamed the broad, blue rivers and mountains—and still weren’t satisfied, reaching for a piece of the world itself.

And, on top of that, the forces of Dark Heaven that must be accompanying them.

An enemy army estimated at no less than thirty thousand had finally appeared here, today.

Following the long course of the Yangtze, and even pushing upstream against the Yellow River’s mighty current.

At the sight of the defenders falling silent before this brutal reality, the two jiangshi sorcerers twisted their mouths into grins.

“You fools.”

“Do you understand now how shallow your little scheme was?”

The black-robed man and his companion made no effort to hide their delight.

They may have fallen for the defenders’ trap and ended up inside the fortress, but their forces alone were enough to easily offset a three-to-one disadvantage.

And now, tens of thousands of reinforcements had arrived right on time. They were almost embarrassed to recall how tense they’d been a moment ago, when they realized they’d fallen into a trap.

*Indeed, the Lord of Heaven is helping us.*

The black-robed man was smiling faintly as he thought of the new heaven he served when—

Step.

A group of people took a step forward. In a situation where they ought to retreat at once, they were moving forward instead.

*Of course. I knew the Kunlun fools would come out like this.*

The black-robed man gave an inward nod when he spotted Cheongheoja and the Kunlun Disciples at the front. Then, in the next moment, he saw a few faces pop out and line up beside them—and sighed.

“I’ve been meaning to ask for a while now… Who the hell are you people?”

If they’d looked even remotely ordinary, he wouldn’t have spared them a thought.

But the seven men and women made up a truly bizarre group, even by the standards of a jiangshi sorcerer. Unfazed by his reaction, they answered.

To be precise, for some reason, only the young man standing at the center spoke for them.

“Swift Wind Sword Hyuk Mujin. That’s who I am.”

The black-robed man’s eyes widened.

“Swift Wind Sword?”

“That’s right. So you’ve heard of—”

“Never heard of you.”

“…Fine. Let me introduce myself again. I’m Hyuk Mujin, Vice Squad Leader of the Jin Dragon Squad. Though I’m taking a little break from that job.”

“I haven’t heard of that either. You might as well keep taking a break. Not that you’ll be around in this world after today.”

“…Damn it. Then what about Hyuk Mujin, Vice Captain of the Fire Dragon Pavilion?”

This time, it was the others’ eyes that widened.

“What? Since when? Do Vice Captains get extra pay?”

“Why would they make Warrior Hyuk Vice Captain of all people? Wasn’t the position vacant?”

“I don’t know. Honestly, I thought I was the best fit among us, but I guess I’m being discriminated against because I’m from the unorthodox faction.”

“Discrimination. Know. Delicious.”

“Is this guy possessed by a glutton or what? I’ve never met anyone more of a deadbeat than my own Master, and I’ve been alive a long time.”

“Oh, so your Master’s a beggar too. No wonder. The moment I saw you, I thought you looked like you knew how to beg for a living.”

Greed and distrust they couldn’t hide even now. Disappointment with the orthodox faction’s rigged playing field. Endless appetite. And last of all, disrespect toward their Master and a steady stream of rudeness, as natural as breathing.

It felt like staring into the depths of a true abyss. The black-robed man and his companion were left dizzy.

If they hadn’t heard Hyuk Mujin’s answer just before, they might not have dared open their mouths at all.

But the three characters that made up Fire Dragon Pavilion were quite familiar to the jiangshi sorcerers.

Everyone in Dark Heaven knew them, regardless of rank. They were closely connected to one particular person.

“If you’re from the Fire Dragon Pavilion… are you Jin Taekyung’s people?”

Hyuk Mujin looked at his companions with a somewhat chilly gaze, then answered in a solemn tone.

“That’s right.”

“Thanks, but strictly speaking, I’m not with the Fire Dragon Pavilion. I’m from the Beggars’ Sect.”

“Neither am I. I think.”

“…Could the two of you please shut up for once? Please?”

The black-robed man studied them with a fresh look.

Because of his role and duties, he hadn’t known the minor details about Swift Wind Sword or the Jin Dragon Squad, but he had heard of the Fire Dragon Pavilion.

Whenever Dark Heaven’s grand plans were thwarted by the obstacle that was Jin Taekyung, hadn’t the Fire Dragon Pavilion made a name for itself by helping him? Its reputation had shaken the whole world.

He didn’t know why the one who looked most like a nobody was its Vice Captain, but he could understand how this strange assortment of people had ended up in one place.

And why they could step forward so boldly in a dangerous situation like this.

“Birds of a feather flock together. You’ve gathered all the crazy men and women who don’t value their lives, just like your Pavilion Master.”

The black-robed man let out a quiet laugh.

The Fire Dragon Pavilion?

He’d admit that they’d been a thorn in Dark Heaven’s side.

But they’d only managed that because Jin Taekyung had been there with them.

At that very moment, the members of the Fire Dragon Pavilion in his sight were nothing more than a group of young prodigies who hadn’t fully matured.

Puppies drunk on clumsy bravado and heroism, still unable to tell when to step forward and when to back down.

“The reason you’re going to die is that you didn’t run away while you had the chance, instead of wasting time spouting nonsense.”

What more was there to say to puppies whose teeth hadn’t even come in properly?

It was another matter if he faced an old, wounded beast quietly catching its breath for one last struggle.

*As long as there’s a Supreme Peak master here, we can’t let our guard down.*

*You worry too much. With forces like theirs, they can’t break through this and hurt us.*

The black-robed man and his companion silently exchanged glances. They watched Cheongheoja and the Kunlun Disciples, who aimed their swords at them with grim faces, and raised the ritual bells in their hands.

Tss-tss-tss-tss.

—Grrrrrr.

The thousand monsters groaned, stirred by the waves pulsing from the two ritual bells.

Each was as large as two grown men put together, with such toughness and regenerative power that they couldn’t be dealt a fatal wound without reaching the level of injuring others with Sword Energy. Ready to lunge at any moment, they fixed their eyes on the enemies before them.

Ssshhhh.

Alongside the two Black Ghosts, already radiating terrifying energy, they poured out such overwhelming killing intent that even the defenders—who had resolved to fight to the death—couldn’t help but take an instinctive step backward.

And then, at last—

“Kill every last one of them.”

The two jiangshi sorcerers swung their ritual bells through the air with a sharp command. At that very instant—

Tss-tss-tss-tss-tss.

The cursed sound waves, branded deep in the souls of the Black Ghosts and monsters, swept across the East Gate.

Along with a quiet voice coming from beyond them.

“Why would we run? We need to buy time by spouting whatever bullshit we can.”

“…?”

“…?”

The black-robed man and his companion stopped moving without realizing it and blinked blankly.

Was it because they couldn’t understand the words of that nobody—Hyuk Mujin, who’d butted in out of habit and now claimed to be the Fire Dragon Pavilion’s Vice Captain?

No.

Unlike the Black Ghosts, who were charging toward the defenders, a thousand monsters were trembling, their limbs shaking as if something invisible had bound them.

*I gave the command… So why?*

Just as the question suddenly crossed the two jiangshi sorcerers’ minds—

“Hey, can’t you do it?”

Along with the baffling question, one person appeared behind Hyuk Mujin, who had turned around. Someone they’d never imagined they would meet here.

“I tried to focus as hard as I could. Hngh. But there’s no way I can manage the Black Ghosts…”

“……!”

“……!”

Their eyes met in midair, and his voice trailed off.

The two jiangshi sorcerers stared wide-eyed at their missing companion. They’d thought he would be dead by now. Ever since the Slaughter Saint had captured him at Qinghai Lake, he’d vanished without a trace.

And they saw the dozen or so ritual bells in his hands—undoubtedly belonging to the other jiangshi sorcerers who’d died near Qinghai Lake—and the sad smile spreading over his bruise-covered face.

“Sorry. That’s how it went.”

At that moment—

SHWEEEE!

A dazzling streak of light cut through the darkness and blocked the two Black Ghosts, who were racing forward like the wind alongside their ghost horse.

KWA-BOOM!

A deafening crash sent a fierce wind sweeping in every direction.

At the same time, through the thick cloud of dust, Cheongheoja and a wild-haired eccentric—no, a Great Sir—appeared and spoke to the Black Ghosts.

“Where do you think you’re going?”

“Why don’t we talk this over first… Oh, that line was pretty cool.”

The two jiangshi sorcerers gritted their teeth as they realized another Supreme Peak master had been hidden amid the frantic fighting around the four walls.

And perhaps what angered them most at that moment was the insolent smile on the face of one nobody.

“If Captain—no, if the Pavilion Master were here, he’d say this.”

At Hyuk Mujin’s gesture, the captured jiangshi sorcerer shook the ritual bells in both hands like mad.

Not just one, but more than ten.

Tss-tss-tss-tss!

The desperate jingle, driven by a stronger instinct to survive than at any other point in his life, pushed him one step beyond the limit of his usual ability.

In other words—

—Ghk, grrk?

He couldn’t completely seize control from the two jiangshi sorcerers—yesterday’s companions, now his enemies—but he could throw the thousand monsters into confusion.

—Kraaaagh!

—Gueeeeee!

Their red eyes flashed wildly, their killing intent no longer fixed on its original target.

THOOM!

KRRRUNCH!

Freed from their restraints, the monsters began rampaging madly, no longer distinguishing between friend and foe. As the two jiangshi sorcerers froze at this unbelievable sight, Hyuk Mujin’s words pierced their ears like arrows.

“From now on, kill each other.”

Boooooo!

Over the horn sounding ever closer by the moment, the monsters’ ferocious roars mingled with the defenders’ shouts.
```
