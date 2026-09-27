<!-- packet-manifest
{
  "included": [
    {
      "path": "source/1089.txt",
      "sha256": "658626a64ef5e343ed9e8ae61b82094aa060bb43f842f357eff5652a3b93e29f",
      "bytes": 14474
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "b03b5fe4f59209b70f134160c3eb5e4f2518c0d2badf442da2c2b43166e1d042",
      "bytes": 1640
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "4ed8101452df2425b89e5c8364c1fe6dfdf6c2111129928b6ce5e8f121d10f80",
      "bytes": 243758
    },
    {
      "path": "characters/Blood Lord.md",
      "sha256": "e3d1d158e1aac5ae63019cb62d631b2e648617af14693590cdda52afcc102cc0",
      "bytes": 916
    },
    {
      "path": "characters/Gung Gibang.md",
      "sha256": "1784a54e214965a796344f994547fdfad4c204e474fa3caf8b003e5de4bc8d08",
      "bytes": 563
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "fd4e7c61fa61dce26834e00cf929a6746041020f10ec07650a5f0ac65e35e8ae",
      "bytes": 1828
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "f5912ae31f21e5e74d827818913979f2f210e2c832d4fd01f8f43518e73b1d80",
      "bytes": 623
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "c4a0e6a83aedc85b5783bb09dd09c0203fec4ce272e8879854936f6a4d11be19",
      "bytes": 286755
    }
  ],
  "estimated_tokens": 10276
}
-->

# Durable State Update — Chapter 1089

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
1 and safe_through 1089. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 1089. Profile updates may replace only one
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
  "chapter": 1089,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 1089,
    "continuity_sources": [1089],
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
    "The Yangtze River Channel League and Green Forest Alliance are advancing west with Dark Heaven forces; their combined force is estimated at roughly 30,000, including 10,000 Dark Heaven faithful.",
    "The Blood Lord’s forces are marching on Xining to take Qinghai; securing Jin Taekyung is a further objective if possible.",
    "Potala Palace has allied with Dark Heaven, and Sichuan support can no longer be counted on.",
    "The Great Nation’s vessels guarding the Yangtze tributaries have been destroyed; the enemy controls the river routes for now.",
    "Jin Taekyung has chosen to remain in Xining and defend its civilians against the approaching forces.",
    "Jeok Cheongang supports Taekyung’s decision and intends to put his remaining strength to use.",
    "Most hidden magic formations retain one use; two or three used in the Shaolin attack may be spent.",
    "Mae Jonghak and the New Murim Alliance prepared an operation against Dark Heaven; Zhuge Feng has its intelligence and tasking to execute it.",
    "The Zhuge Clan left its ancestral home and fled to Mount Wudang."
  ],
  "continuity_sources": [
    1087,
    1088
  ],
  "open_questions": [
    "What is the black-robed captive in Qinghai’s identity and what does he know?",
    "Why did the Lord of Heaven spare Taekyung in Gansu, and what is his real purpose?",
    "Will the Alliance Leader and other righteous warriors reach Qinghai?",
    "What is the hidden ember Cheongheoja warned about?",
    "Who is the black-robed man beside Pa Ryun?"
  ],
  "safe_through": 1088,
  "temporary_decisions": [],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 진태경    | **Jin Taekyung**   |
| 암천     | **Dark Heaven**                  |
| 일류     | **First Rate**    |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 중원     | **Central Plains**                               |                                                       |
| 강호     | **martial world**                                | Prefer “Murim” where the setting itself is meant      |
| 청해     | **Qinghai**            |
| 곤륜     | **Kunlun**             |
| 혈주 | **Blood Lord** | Title of the unidentified young man encountered by Han Su. |
| 궁기방 | **Gung Gibang** | Beggars' Sect Successor Beggar and finalist. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 갑자 | **jiazi** | Traditional sixty-year cycle. |
| 시진 | **shichen** | Traditional time unit of approximately two hours. |
| 사술 | **dark arts** | Unorthodox means of obtaining power. |
| 개방 | **Beggars' Sect** | Murim organization counted among the Nine Sects and One Gang. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 피어 | **Fear** | Monster effect that overwhelms a target’s mental fortitude. |
| 후개 | **Successor Beggar** | Title of the Beggars' Sect successor competing in the preliminaries. |
| 꼬리 | **the “tail”** | Codename for the Black Hunter traced by Butler Kim. |
| 그분 | **that person** | Unidentified figure whom Jihoon reveres and credits with disabling cameras and microphones. |
| 개방도 | **Beggars' Sect disciple** | Member of the Beggars' Sect. |
| 석삼 | **Seok Sam** | Caravan porter who died during the current Yongbong Escort Bureau mission. |
| 악귀 | **Fiend** | Descriptive epithet applied to the First Fiend. |
| 청해성 | **Qinghai** | Source form specifying Qinghai as a province. |
| 촌각 | **moments** | Short intervals disappearing from Jeok's day. |
| 식경 | **half an hour** | Time limit given for the requested reports. |
| 만족 | **Man people** | An ethnic group mentioned by the Poison Flower Pavilion owner. |
| 서리 | **seori** | Colloquial term for stealing crops or produce from a field. |
| 대술사 | **Grand Mage** | Title of the veiled woman leading the white-robed mages. |
| 청해호 | **Qinghai Lake** | Destination of the retreat; distinct source form from 청해성. |
| 서녕 | **Xining** | Capital of Qinghai. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 궁기방 | 진태경 | rival_finalists | you bastard | insulting-casual | Gung Gibang answers Taekyung's collective insult with a profane threat. |
| 진태경 | 궁기방 | rival_finalists | you three idiots | insulting-casual | Taekyung addresses Gung Gibang as part of the trio and threatens them before a duel. |
| 혈주 | 진태경 | hostile_opponent_to_hostile_opponent | Sleeping Dragon of Shanxi | casual, amused, and taunting | Addresses Taekyung by his established epithet while asking whether he agrees with the Blood Lord's judgment of Han Su. |
| 혈주 | 대술사 | fellow servant of the same person | you; you bitch | insulting-casual | Blood Lord taunts the Grand Mage and uses a crude insult. |
| 대술사 | 혈주 | fellow servant of the same person | you | contemptuous-casual | The Grand Mage addresses the Blood Lord while rebuking him. |

## Listed compact profiles

### Blood Lord.md

# Blood Lord (혈주)

- **Safe through:** Chapter 1087
- **Aliases:** None
- **Role:** Young-seeming high-ranking Dark Heaven figure who directs its sorcerers’ seed experiments and prepares their deployment for the Lord of Heaven’s great cause.
- **Personality:** Confident, cruel, and controlling; strategically manipulates allies and adversaries, and conceals failures from the Lord of Heaven when he fears being discarded.
- **Voice:** Light, cheerful, and joking even while threatening or killing; turns cold and contemptuous when challenged.
- **Relationships:** He serves the Lord of Heaven and seeks to advance the Lord’s great cause; he regards the deceased Western Heaven Demon Lord and Southern Heaven Demon Empress as powerful allies whose deaths cost Dark Heaven, and considers Jin Taekyung and Cheongpung formidable adversaries.

### Gung Gibang.md

# Gung Gibang (궁기방)

- **Safe through:** Chapter 1076
- **Aliases:** Successor Beggar, Beggar Prince, pure-blooded beggar, ultimate beggar
- **Role:** Gung Gibang is the Beggars' Sect Successor Beggar and a unique eight-knot disciple.
- **Personality:** Vulgar, aggressive, and quick-tempered.
- **Voice:** Blunt, profane, and vividly threatening.
- **Relationships:** Gung Gibang is a rival finalist alongside Baek Woo and Zhuge Gyun, and shares a blunt, teasing friendship with Taekyung.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 1087
- **Aliases:** Blazing Flame Divine Dragon; Apostle of the Earth Mother Goddess; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan and the original owner of his current body, Jeok Cheongang’s Disciple, the Fire Gate Clan’s nineteenth successor, Pavilion Master of the Fire Dragon Pavilion, a Supreme Peak master who has reached the realm of the Ten Kings as its eleventh member and can detect and eavesdrop on nearby Sound Transmissions subject to the participants’ relative levels, and a publicly recognized S-rank-level Hunter with an A-rank license, a traveler between Murim and another world, and the World Hunter Federation’s Alliance Leader; the Emperor appointed him Marquis of Shangshan and Thousand Captain of the Embroidered Uniform Guard.
- **Personality:** Hungry, self-aware, and dryly observant; pragmatic under pressure, willing to risk himself for others, and fiercely defiant when others try to dictate his choices or survival.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, and Jeok Cheongang is his Master and trusted confidant; Hyuk Mujin trusts Taekyung to fight beside him; Taekyung trusts Sama Pyo as a friend despite suspecting his betrayal, and values him beyond his unorthodox affiliation; Peng Cheolhu regarded Taekyung as a worthy successor, and the Bow Saint relayed the Martial God’s message to him.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 1087
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

## Korean source

```text
1089화




유시(酉時)에 막 접어들 무렵, 어느덧 서산으로 조금씩 기울어 가는 태양을 본 늙은 거지는 혼잣말처럼 중얼거렸다.

“희한하군. 아직 해가 질 시간이 아닌데.”

그 말에 가까운 모닥불 근처에 옹기종기 모여있던 또 다른 거지들이 반응했다.

“그럼 지금 같은 계절에 이런 날씨인 건 말이 되고요?”

“맞지. 하루 이틀 일도 아니고.”

“분타주(分舵主)님도 괜히 거기서 찬바람 맞지 마시고, 와서 모닥불이나 좀 쬐시우. 뜨뜻한 국물도 한 사발 하시고.”

하긴, 틀린 말은 아니다.

세상이 요지경이 된 것은 어제오늘 일이 아니었으니까.

늙은 거지, 아니 개방의 청해성 서녕 분타주인 만총은 작게 한숨을 내쉬며 모닥불로 걸음을 옮겼다.

후개(後丐)인 궁기방은 이미 서녕으로 돌아간 지 여러 날이었지만, 휘하의 개방도 삼십여 명과 함께 남아 정보를 수집하고 있던 그였다.

“먹을 것 좀 있나?”

“그 무슨 당연한 말씀을. 가진 거라고는 쥐뿔도 없어도 어떻게든 배는 채우는 게 우리 아니오?”

“정찰 나가 있는 놈들 몫은 남겨뒀고?”

“어허. 누굴 상도덕도 모르는 거지로 보시나. 걱정 마시우. 그놈들도 돌아와서 배터지게 먹을 만큼 해뒀수.”

누런 이를 드러내며 씩 웃은 거지 하나가 김이 모락모락 피어오르는 사발을 내밀자, 만총이 자신도 모르게 입맛을 다셨다.

“향은 끝내주는구먼.”

“드시기나 하슈. 향만 끝내주는 게 아니라는 걸 알게 될 테니까.”

과연 그 말은 사실이었다. 

불과 촌각 만에 게 눈 감추듯 사발을 싹 비운 만총은 부른 배를 두드리며 만족스러운 미소를 지었다.

비록 겉보기에는 잡탕도 이런 잡탕이 없었지만, 청해호(靑海湖)에서 갓 잡은 물고기로 만든 덕분인지 그 맛은 일류 숙수가 만든 것처럼 훌륭하게 느껴졌다.

‘하긴, 몸도 늙었는데 이런 호사라도 있어야지.’

포만감에 나른해진 만총은 생선 가시로 이를 쑤시며 주변을 둘러보았다.

천천히 노을빛에 젖어 들어가는 청해호의 강물을 보고 있자니, 근심과 걱정도 잠시나마 씻겨 내려가는 듯한 기분이었다.

물론, 현실은 여전히 암담하기만 했지만.

‘경치 좋고 배부르면 뭣하나. 그놈들이 없어지기 전까지는 발 뻗고 자지도 못하는 것을.’

암천. 그 무시무시한 악귀들을 떠올리자 만총의 얼굴에 그림자가 드리워졌다.

지금으로부터 약 나흘 전, 진태경을 비롯한 지원군들이 이곳을 지나 서녕에 합류한 후에도 상황은 좀처럼 나아지지 않았다.

아니, 찰나의 희망을 짓밟기라도 하듯 하루가 다르게 악화 되어 가는 중이었다.

‘이대로면 영락없이 앞뒤로 포위당할 텐데……젠장, 용코로 걸렸군.’

당장 곤륜산을 점령한 암천의 대군만 생각해도 등골이 서늘해질 정도인데, 후방에서는 중원 무림의 뒤통수를 거하게 후려친 도적놈들이 개미 떼처럼 몰려들고 있다고 했다.

이런 와중에 그나마 다행인 점이 있다면 딱 하나.

암천의 본대가 아직 본격적인 움직임을 보이지 않고 있다는 것이었다.

‘하지만 이제는 그것도 시간 문제. 놈들은 반드시 들이닥친다. 그것도 빠른 시일 내에.’

생각이 거기까지 미치자 조금 전 느꼈던 포만감이 싹 가시고, 불안과 두려움이 빈자리를 채웠다.

“……염병할.”

삽시간에 기분이 더러워진 만총은 손 닿은 곳에 있던 자갈을 주워 냅다 내던졌다.

쐐애액!

행색은 남루해도 그 역시 개방에서 제법 잔뼈가 굵은 분타주 급의 고수. 

손끝을 떠난 자갈이 끝없이 펼쳐진 청해호를 향해 쏘아졌다.

촤아아악!

거칠게 갈라지는 수면. 그제야 답답했던 속이 조금이나마 풀린 만총은 콧김을 뿜으며 돌아섰다.

아니, 돌아서려고 했다.

자갈로 인해 일어난 파문이 가라앉으며, 서서히 평온함을 되찾는 강물을 보기 전까지는.

‘뭐지?’

그리고 그 불현듯 찾아온 기시감의 정체를, 만총은 그리 오래되지 않아 깨달을 수 있었다.

‘색. 강물의 색이…….’

어둡다.

아니, 먹물이라도 풀어놓을 것처럼 새카맸다.

불과 촌각 전까지만 하더라도 노을빛에 물들어 있던 청해호의 강물은 더 이상 아름답지 않았고, 귓가로 두런두런 들려오는 대화는 유난히도 꺼림칙했다.

“아따, 오늘따라 왜 이리 빨리 어두워진대? 그래도 평소에는 노을 지는 데만 한 식경은 걸리더만.”

“우리가 따져봤자 뭘 어쩌겠소. 그냥 그런 갑다 해야지. 정찰간 놈들 돌아오기 전에 밥이나 더 드쇼.”

“나야 물론 좋지. 아, 분타주께서도 한술 더 뜨시렵니까?”

만총은 대답하지 않았다.

정확히는 대답할 수 없었다.

지금 이 순간, 그의 본능이 머릿속에 붉은 경종을 울리고 있었으니까.

‘이건……뭔가 이상하다.’

물론 다른 개방도들의 반응처럼 별 것 아닌 일일 수도 있다.

추수철이 오기도 전에 서리가 내리고, 인간 같지도 않은 외관을 지닌 거대한 괴물들이 날뛰는 마당에 뭘 더 놀랄 것이 있겠나.

그러나 알 수 없는 직감이 있었다.

환갑이 넘은 나이까지 쌓아온 경륜, 노강호로서 뼈에 새겨진 듯한 본능이.

“정찰대, 정찰대는 언제쯤 돌아온다더냐?”

“예? 아니 갑자기 그건 왜.”

“대답하거라, 어서!”

늘 사람 좋던 늙은 분타주의 불호령에, 당황한 개방도들이 더듬더듬 입을 열었다.

“고, 곧 올 겁니다요.”

“그, 사실 평소보다 반 각 정도 늦긴 했습니다만 코앞까진 왔을 테니 분타주께서 걱정하실 필요는……어라?”

대답하던 개방도 중 하나가 눈을 동그랗게 뜨며 만총의 어깨너머를 바라보자, 모두의 시선이 그곳을 향해 쏠렸다.

약 이백여 장 밖에 자리 잡은 야트막한 언덕.

그 위로 자그마한 점처럼 막 모습을 드러낸 한 무리의 인마(人馬)가 흐릿한 어둠을 뚫고 천천히 언덕을 내려오고 있었다.

“호랑이도 제 말 하면 온다더니. 마침 때맞춰 왔구먼.”

“저저, 게을러터진 놈들 같으니라고. 늦은 주제에 설렁설렁 오면 쓰나?”

“분타주께서는 이만 고정하시우. 내 아주 이번 기회에 혼쭐을 낼 터이니.”

모두가 만총의 눈치를 살피며 한 마디씩을 던지던 그때, 침잠한 눈빛으로 정찰대를 응시하던 그가 신음처럼 뇌까렸다.

“열둘.”

“예?”

“열둘이다. 내 눈이 잘못된 것이 아니라면.”

“그게 무…….”

뜬금없는 말에 의문을 표하던 누군가가 문득 말꼬리를 흐렸다.

지금으로부터 약 두 시진 전, 인근을 둘러보기 위해 떠났던 정찰대의 머릿수는 총 열 명이었으니까.

“그, 그렇다는 건.”

“둘 중 하나겠지. 천운으로 살아남은 생존자를 구했거나.”

손때 묻은 철곤(鐵棍)을 허릿춤에서 빼어 들며, 만총이 나직이 덧붙였다.

“산 채로 씹어 먹어도 시원치 않을 어떤 개자식들이, 정찰대 행세를 하고 있거나.”

“……!”

“지금 당장 배로 이동한다. 우선 닻을 올리고 거리를 벌린 후에 상황을 지켜볼 것이다.”

“며, 명을 받듭니다!”

그제야 상황의 심각성을 알아차린 이들은 언제 그랬냐는 듯 일사불란하게 움직였다. 

그리고 강가에 정박시켜두었던 배에 올라타 빠르게 노를 저은 개방도들이 충분한 거리를 벌렸을 때쯤에는, 적인지 아군인지 모를 정체불명의 무리가 그들이 피워두었던 모닥불 근처까지 다다라 있었다.

“석삼이, 석삼이 거기 있는가!”

불쑥 울려 퍼진 만총의 외침에, 어느덧 확연히 짙어진 어둠 너머에서 대답이 들려왔다.

“나 여기 있네! 무슨 일인가?”

그 순간, 만총의 얼굴이 딱딱하게 굳었다.

아니, 그를 포함한 모든 개방도가 마찬가지였다.

청해호에 머무르던 이들 중, 분타주이자 최연장자인 만총에게 하대를 할 수 있는 개방도는 한 명도 없었으니까.

하지만 다른 무엇보다 가장 큰 충격을 받은 부분은, 짙은 어둠 너머에서 들려온 목소리가 그들이 아는 석삼이의 것과 똑같다는 것이었다.

“부, 분타주.”

귀신이라도 목격한 것처럼 창백한 얼굴을 한 개방도들을 뒤로한 채, 이를 악문 만총이 다시금 외쳤다.

“네놈들은 누구냐!”

잠시 정적이 흘렀다. 

찰나에 불과했으나 그 어느 때보다 길고, 영원처럼 느껴지는 정적이.

그리고 질식할 것만 같은 그 적막함을 단숨에 깨트리는, 낯선 목소리가 불현듯 울려 퍼졌다. 

“이런. 거지새끼들이라 그런지 눈치가 빠르군.”

웃음기마저 묻어있는 들뜬 음성과 함께, 아직 꺼지지 않은 모닥불을 향해 윤곽으로만 보이던 형체가 모습을 드러냈다.

타다닥.

허공으로 피어오르는 불똥 사이, 일말의 소음도 없이 자갈밭을 가로지른 한 쌍의 인마를 목격한 만총이 눈을 부릅떴다.

“이, 이게 무슨……!”

그는 일순간 할 말을 잃었다.

새하얀 뼈를 훤히 드러낸 해골마의 모습 때문이기도 했지만, 그 위에 태연히 앉아있는 사내에게서 지금껏 경험해 본 적 없는 공포를 느꼈기 때문이었다.

히죽.

이질적으로까지 보이는 새하얀 이빨이, 맹수의 그것처럼 날카로운 송곳니가 드러난다.

그뿐인가.

먼 거리에서도 선명하게 번뜩이는 핏빛 눈동자는, 마주한 것만으로도 심신을 옭매는 듯했다.

“네, 네놈은.”

파르르 신형을 떠는 만총을 향해, 사내가 어깨를 으쓱해 보였다.

“뭐, 대충 알잖아. 누구인지.”

더욱더 큰 공포를 불러일으키는 천연덕스러운 태도. 

그러나 만총은 가까스로 목소리를 쥐어 짜냈다.

“정찰대는……그들은 어찌 되었느냐.”

“크. 감동적인데. 구걸하면서 쌓은 정이 상당한가 봐?”

“놈! 묻는 말에 대답하지 못할까!”

“이거 거지 무서워서 말이야 제대로 하겠나. 알겠어, 알겠으니까 너무 흥분하지 말라고.”

진정하라는 듯 손을 내저은 사내가 입맛을 다셨다.

“결론만 말하자면, 다들 좋은 곳으로 갔지. 별로 맛은 없었지만.”

“뭐, 뭐라?”

감히 입에 담을 수조차 없는 어떠한 짐작으로 굳어버린 만총의 모습에, 사내가 눈살을 찌푸렸다. 

“아, 불쾌한 오해는 하지 마. 비루먹은 거지새끼들이라 그런지 몸뚱어리도 영 아니더라고. 장난도 칠 겸 피만 조금 빨아먹은 게 전부니까.”

“……!”

“왜, 당신이 생각하기에는 영 별로였나? 그래도 목소리는 제법 감쪽같았을 텐데.”

으득.

삽시간에 입안을 물들이는 비릿한 혈향.

그럼에도 만총은 온 힘을 다해 이를 악물었다.

단지 형제나 다름없던 수하를 잃었다는 사실에서 오는 분노 때문만이 아니다. 

그래야만, 이렇게라도 해야만 지금 이 순간에도 더욱 강하게 마음을 옥죄어 오는 두려움을 조금이나마 견딜 수 있을 것 같아서였다.

사술(邪術).

그 두 글자가 이토록 섬뜩하게 다가왔던 적이 없었다. 

백여 장이나 떨어진 상대에게서, 당장이라도 목이 달아날 것만 같은 느낌을 받은 것도.

“네놈이구나. 말로만 듣던 그 수괴(首魁)가.”

“뭐, 일단은 그렇다고 해두지. 당장 이곳에서만큼은 그분께 모든 것을 일임받았으니까.”

사내, 아니 혈주(血主)는 미소 띤 얼굴로 만총을 바라보았다.

그리고 그런 그의 주위에서 어떤 반응조차 하지 못한 채 석상처럼 굳어있는 스무 명의 개방도를 천천히 훑다가, 불현듯 입술을 뗐다.

“그나저나, 누구로 할래?”

“뭐?”

“적어도 한 놈은 살려줄 생각이거든. 너희는 하나라도 살아서 좋고, 나는 말을 전할 놈이 필요하고. 서로 좋은 게 좋은 거 아니겠어?”

“……!”

“표정들이 볼만하군. 왜, 설마 이대로 도망칠 수 있을 줄 알았나?”

일백여 장 밖, 딱딱하게 굳은 그들의 얼굴을 바라보며 히죽 웃은 혈주가 문득 뒤를 돌아봤다.

“슬슬 나서지? 어차피 해야 하는 일인데.”

그 한마디에, 어둠 속에서 머무르고 있던 인영 중 하나가 앞으로 나섰다.

스륵.

긴 옷자락이 자갈밭을 스친다. 대꾸할 가치도 없다는 듯, 혈주를 지나쳐 강가에 다다른 대술사가 손을 뻗었다.

“서늘한 북풍(北風)이여.”

우우우웅.

파르르 떨리는 공기와, 청해호의 수면을 타고 몰아치는 거대한 냉기.

그리고 다음 순간, 보았다.

“얼어붙어라.”

드드드득!

결빙(結氷)과 함께, 새하얗게 굳어버린 청해호를.

“……!”

“……!”

만총이, 아니 스무 명의 개방도 모두가 눈을 부릅떴다.

있어서도, 있을 수도 없는 이적(異蹟).

그 믿을 수 없는 현실 앞에 선 그들은 아무것도 할 수 없었다.

저 멀리, 짙은 어둠 너머로 괴물들의 끔찍한 악취가 풍겨오기 시작했음에도.

그리고 산보하듯 빙판을 가로지른 혈주가, 뱃머리 위에 올라서서 그들을 내려다보았을 때도.

“누가 살아남든, 가서 전해라. 내가. 혈주가 간다고.”

그 순간, 만총은 모든 힘을 다해 목소리를 쥐어 짜냈다.

“네놈은 결코 이길 수 없을…….”

퍼걱!

새하얗게 얼어붙은 호수 위로, 선홍빛 피가 흩뿌려졌다.

“그래서, 누가 살아남을지는 정했나?”

차갑고 깊은 밤, 혈주의 핏빛 눈동자가 번뜩이고 있었다.
```

## Final English reading copy

```markdown
# Chapter 1089

Just as the hour of the Rooster began, an old beggar looked at the sun sinking little by little toward the western mountains and muttered to himself,

“How strange. It’s not time for the sun to set yet.”

The other beggars huddled around a nearby campfire reacted to his words.

“Then what about weather like this at this time of year? Does that make sense?”

“Right. It’s not like this just started yesterday or the day before.”

“Branch Master, don’t stand out there getting chilled by the wind. Come warm yourself by the fire. Have a bowl of hot soup, too.”

He had a point.

The world had been going haywire for more than a day or two.

The old beggar—or rather, Man Chong, Branch Master of the Beggars’ Sect’s Xining branch in Qinghai—let out a small sigh and walked toward the fire.

Gung Gibang, the Successor Beggar, had returned to Xining several days ago. Man Chong, however, had stayed behind with around thirty Beggars’ Sect disciples under his command to gather information.

“Got anything to eat?”

“Why, of course. Even if we don’t have a damn thing, we’re the sort who’ll find a way to fill our bellies.”

“You saved some for the ones out on patrol, didn’t you?”

“Come now. Do you take us for beggars with no sense of decency? Don’t worry. There’s enough for them to come back and eat their fill, too.”

One of the beggars grinned, yellow teeth showing, and offered him a steaming bowl. Man Chong found himself smacking his lips.

“That smells incredible.”

“Just eat it. You’ll see it tastes just as good as it smells.”

He was right.

Man Chong polished off the bowl in the blink of an eye, then patted his full belly with a satisfied smile.

It looked like a hodgepodge of the highest order, but perhaps because it had been made with fish freshly caught in Qinghai Lake, it tasted as if it had come from a first-rate chef.

*Well, I’m old. I deserve a little luxury like this.*

Drowsy with contentment, Man Chong picked his teeth with a fish bone and looked around.

As he watched the waters of Qinghai Lake slowly bathe in the sunset, he felt his worries wash away, if only for a moment.

Of course, the reality was still bleak.

*What good are a pretty view and a full belly? I can’t sleep easy until those bastards are gone.*

Dark Heaven. At the thought of those terrifying Fiends, a shadow fell over Man Chong’s face.

The situation had hardly improved, even after Jin Taekyung and the reinforcements passed through here and joined the others in Xining about four days ago.

No—the situation was getting worse by the day, as if to crush that brief glimmer of hope.

*At this rate, we’ll be surrounded from both sides for sure… Damn it. We’re caught in a hell of a mess.*

The mere thought of Dark Heaven’s massive army, which had already taken Kunlun Mountain, was enough to send a chill down his spine. And from the rear, bandits who’d dealt the Central Plains Murim a vicious blow were said to be swarming in like ants.

There was only one thing they had going for them.

Dark Heaven’s main force had yet to make a serious move.

*But that’s only a matter of time now. They’re coming, and soon.*

As far as that thought, the full feeling in his belly vanished. Anxiety and fear filled the space it left behind.

“……Damn it.”

His mood souring in an instant, Man Chong snatched up a pebble within reach and flung it as hard as he could.

Whoosh!

His clothes were shabby, but he was a master of the Beggars’ Sect with years of experience behind him.

The pebble shot from his fingertips toward the endless expanse of Qinghai Lake.

Splash!

The water split violently. Only then did the tightness in his chest ease a little. Man Chong snorted and turned away.

Or tried to.

He stopped when he saw the ripples from the pebble settle and the water slowly return to stillness.

*What is it?*

It didn’t take long for him to understand the sudden sense of déjà vu.

*The color. The color of the water…*

It was dark.

No—it was as black as if someone had poured ink into it.

The waters of Qinghai Lake, which had been tinted with sunset only moments ago, were no longer beautiful. Even the quiet conversations reaching his ears felt unusually ominous.

“Man, why’s it getting dark so fast today? Usually it takes half an hour for the sun to set.”

“What can we do about it? It is what it is. Have some more food before the patrol comes back.”

“I certainly won’t say no. Oh, Branch Master, would you like another bowl?”

Man Chong didn’t answer.

More precisely, he couldn’t.

At that moment, his instincts were sounding a red alarm in his head.

*Something’s… wrong.*

Of course, it could be nothing, just as the other Beggars’ Sect disciples seemed to think.

Frost had fallen before harvest season, and giant monsters with appearances that barely seemed human were running wild. What was left to be surprised by?

But he had a feeling he couldn’t explain.

The experience he’d built up in more than sixty years, the instinct of an old master etched into his bones.

“When will the patrol be back?”

“Huh? Why do you ask all of a sudden?”

“Answer me. Now!”

At the old Branch Master’s sudden bark—he was usually so easygoing—the startled Beggars’ Sect disciples stumbled over their words.

“Th-they should be back soon.”

“W-well, they’re about half a gak later than usual, but they must be close by now. There’s no need for you to worry, Branch Master. Ah?”

One of the disciples trailed off, eyes widening as he looked over Man Chong’s shoulder. Everyone turned to see what he was looking at.

On a low hill about two hundred zhang away, a group of riders had just appeared, tiny as specks. They were slowly descending the hill through the dim darkness.

“Speak of the devil. They’re right on time.”

“Look at those lazy bastards. They’re already late, and now they’re taking their sweet time?”

“Branch Master, you can relax. I’ll give them a proper scolding this time.”

As everyone tossed out remarks while watching Man Chong’s expression, he stared at the patrol with sunken eyes and muttered,

“Twelve.”

“What?”

“Twelve. Unless my eyes are wrong.”

“What does that—”

Someone began to ask, then suddenly faltered.

The patrol that had left about two shichen ago to survey the area had numbered ten.

“Th-that means…”

“Could be one of two things. Either they found survivors who made it through by sheer luck…”

Man Chong drew the iron staff, worn smooth from years of handling, from his waist and added quietly,

“Or some sons of bitches who deserve to be chewed up alive are pretending to be the patrol.”

“……!”

“Get to the boat now. We’ll raise anchor, put some distance between us, then see what happens.”

“W-we’ll do as you say!”

The disciples finally realized how serious the situation was and moved into action without another word.

By the time they’d boarded the boat moored by the shore and rowed far enough away, the mysterious group—friend or foe, they couldn’t tell—had reached the campfire they’d left behind.

“Seok Sam! Seok Sam, are you there?”

Man Chong’s sudden shout was answered from beyond the darkness, which had grown noticeably deeper.

“I’m right here! What is it?”

In that instant, Man Chong’s face went rigid.

So did every other Beggars’ Sect disciple’s.

No one among those who’d been staying at Qinghai Lake could speak informally to Man Chong, the oldest among them and their Branch Master.

But what shocked them more than anything was that the voice coming from beyond the darkness was exactly like Seok Sam’s.

“B-Branch Master…”

Leaving the Beggars’ Sect disciples behind, their faces pale as if they’d seen a ghost, Man Chong gritted his teeth and shouted again.

“Who are you bastards?”

A brief silence followed.

It lasted only a moment, but felt longer than ever—like an eternity.

Then an unfamiliar voice suddenly rang out, shattering the silence that seemed ready to suffocate them.

“Well, I guess beggar bastards are quick on the uptake.”

With a buoyant voice that even carried a hint of laughter, the figure that had only been a silhouette emerged into view, heading for the still-burning campfire.

Tap-tap.

Between the sparks rising into the air, a man and a horse crossed the gravel without a sound. Man Chong’s eyes widened at the sight.

“W-what is that…?”

For a moment, he was speechless.

Partly because of the skeletal horse, its white bones exposed, but more than that, because the man sitting casually atop it filled him with a fear he’d never experienced before.

Grin.

He showed his unnaturally white teeth—sharp fangs like a wild beast’s.

And those blood-red eyes, gleaming clearly even from far away, seemed to bind his body and mind just by meeting his gaze.

“Y-you…”

The man shrugged at Man Chong, whose body was trembling.

“You know who I am, more or less.”

His nonchalant manner only made him more terrifying. But Man Chong managed to force out his voice.

“The patrol… What happened to them?”

“Aw. How touching. Guess you’ve grown pretty attached to them begging for a living?”

“You bastard! Answer the question!”

“I mean, it’s hard to talk properly when a beggar’s yelling at you. Fine, fine. Don’t get so worked up.”

The man waved a hand as if to calm him down, then smacked his lips.

“To sum it up, they went to a better place. Though they didn’t taste like much.”

“W-what did you say?”

Man Chong froze, his mind settling on a suspicion too horrible to put into words. The man frowned.

“Hey, don’t get the wrong idea. Maybe it’s because they were mangy beggar bastards, but their bodies weren’t much to write home about either. I only drank a little blood, just to have some fun.”

“……!”

“What? Not what you expected? That voice was pretty convincing, though.”

Grit.

The taste of blood flooded Man Chong’s mouth.

Even so, he gritted his teeth with all his strength.

It wasn’t only the rage of losing a subordinate who’d been like a brother to him.

He had to clench his teeth. Had to do this, if only to bear the fear that was tightening its grip on him with every passing moment.

Dark arts.

The words had never seemed so chilling.

Nor had he ever felt as if his head could be severed at any moment by someone standing a hundred zhang away.

“So you’re the one. The leader we’ve heard about.”

“Well, let’s say I am. At least here, that person has entrusted everything to me.”

The man—or rather, the Blood Lord—looked at Man Chong with a smile.

Then he slowly scanned the twenty Beggars’ Sect disciples, frozen like statues around him, unable to react. Suddenly, he spoke.

“So, who’ll it be?”

“What?”

“I’m planning to let at least one of you live. You’ll be glad one of you survived, and I need someone to deliver a message. Seems like a good deal for both of us, doesn’t it?”

“……!”

“Quite a sight, those faces. What, did you think you could just run away?”

Grinning at their rigid faces a hundred zhang away, the Blood Lord suddenly turned around.

“Time to get moving, isn’t it? It’s something we have to do anyway.”

At his words, one of the figures lingering in the darkness stepped forward.

Swish.

Long robes brushed the gravel. The Grand Mage, as if the Blood Lord weren’t worth answering, passed him and reached the lakeshore. She extended her hand.

“Cold north wind…”

Wooooom.

The air trembled. A vast chill swept across the surface of Qinghai Lake.

And then, they saw it.

“Freeze.”

Rumble!

With a crack of ice, Qinghai Lake froze white.

“……!”

“……!”

Man Chong and all twenty Beggars’ Sect disciples stared, wide-eyed.

A miracle that should not—and could not—exist.

Faced with that unbelievable reality, they could do nothing.

Not even when the foul stench of monsters began to drift toward them from beyond the thick darkness in the distance.

Not even when the Blood Lord, crossing the frozen surface as casually as if out for a stroll, climbed onto the bow of their boat and looked down at them.

“Whoever survives, go tell them. I—the Blood Lord—am coming.”

At that moment, Man Chong forced out his voice with everything he had.

“You’ll never win…”

Crack!

Scarlet blood sprayed across the white ice.

“So, have you decided who gets to survive?”

In the cold, deep night, the Blood Lord’s blood-red eyes gleamed.
```
