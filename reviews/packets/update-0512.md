<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0512.txt",
      "sha256": "4bfdf9c8c316452880ae94d26c16c07c0ebb4120cb4d6330c3fe4fd0038f7f98",
      "bytes": 12866
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "b268b09416f6881e534eeae274da2fbeca929d44783f8e6a164a44e247c518d2",
      "bytes": 4029
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "7a940d6d20abcb8ae9ec4b915b5b11c7d43c0ea48013eb1497ccfb9e76b8388a",
      "bytes": 163620
    },
    {
      "path": "characters/Jeok Cheongang.md",
      "sha256": "80cf010b097cec0c35cd0629cde83b4fbce92a941beac6d9d8867b6bc9bc94fd",
      "bytes": 1630
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "d55e1b559aab842913d6859ee4f86aff71a3a23ad89553d949f27b82a0965ae8",
      "bytes": 154523
    }
  ],
  "estimated_tokens": 9941
}
-->

# Durable State Update — Chapter 512

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 512. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 512. Profile updates may replace only one
complete line in Aliases, Role, Personality, Voice, or Relationships. Do not
return Safe through updates; the controller sets that field automatically.
Each profile field should be one concise sentence; never append semicolon-separated
chapter history.
`names` contains only newly required Korean-to-English rows that are absent from
Exact glossary matches; Korean keys must occur in the source. Do not repeat
glossary matches. The controller drops rows already in the names ledger.
`address_pairs` contains only newly required speaker→addressee rows that are
absent from Matched address pairs. Speaker and addressee must be Hangul source
spellings such as 진태경 or 혁무진, never English names. Arabic digits are
allowed in titles such as 1팀장. At least one endpoint must occur in the source.
The controller drops pairs already in the address ledger. Do not invent
risk-register rows. Beat plot paragraphs are plain strings; continuity and
translation decisions are concise list items.
Return this exact shape:

{
  "chapter": 512,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 512,
    "continuity_sources": [512],
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
    "Jeok Cheongang's Heart Demon and the dark memories binding him have been expelled; he has entered a new realm and achieved Returned to Youth.",
    "Mungyeong is the Slaughter Saint and former Divine Physician, a Returned to Youth Supreme Peak master and the greatest assassin in history; Mu Song and five Water Dragon Stronghold subordinates know he is exceptionally powerful but not that he is the Slaughter Saint.",
    "Mungyeong is training Taekyung to refine the stability and precision of the violent internal energy produced by the Fire Gate Divine Technique through Rising on Duckweed, Crossing Water.",
    "Zhuge Feng's Demon-Sealing Formation blocks all mana from the exposed Gate by drawing in natural qi, but whether it is permanent and repeatable remains unresolved.",
    "Jang Taebo is the Jin Family of Taiyuan's Master of Ironcraft Hall and is summoning renowned artisans to process the Water God Dragon's remains.",
    "War has begun and the New Murim Alliance is being formed at Mount Song; Taekyung believes Dark Heaven planned the Gate incident, while Jin Wikyung's Hubei arrangement was designed to create an opening among rival unorthodox factions.",
    "The Southern Heaven Demon Empress is traveling toward Yunnan and expects to cause further deaths.",
    "Jin Mukyung remains secluded in the training hall after losing to Cheongpung, refusing to emerge until he achieves a great accomplishment.",
    "Taekyung is pursuing two Yangtze River Channel League swift ships and has partially replenished his internal energy after traveling with five trained sharks.",
    "Mu Song wants to aid the Murim Alliance, but the Seafaring King alone decides the Yangtze River Channel League's major matters; the League and Green Forest Alliance may become rear threats.",
    "The North Sea Ice Palace remains isolationist, while Jeok Cheongang believes the Nanman Beast Palace will probably support orthodox Murim because of its historical goodwill toward the Fire Gate Clan.",
    "A stranger capable of walking across the Yangtze's surface has approached Taekyung after he released the trained sharks."
  ],
  "continuity_sources": [
    511
  ],
  "open_questions": [
    "Will the Demon-Sealing Formation remain effective permanently, and can equivalent formations be installed repeatedly if more Gates appear?",
    "What is the Lord of Heaven's identity, and how is he connected to the dangerous force Taekyung associates with his original world?",
    "Where is the Southern Heaven Demon Empress ultimately headed, and what does she intend to do in Yunnan?",
    "Will the Nanman Beast Palace, North Sea Ice Palace, Yangtze River Channel League, and Green Forest Alliance support, ignore, or oppose the New Murim Alliance?",
    "Who is the stranger walking across the Yangtze, and why has he approached Taekyung?"
  ],
  "safe_through": 511,
  "temporary_decisions": [
    "Render 새외무림 as Outer Murim, 새외 as Outer Lands, 북해빙궁 as North Sea Ice Palace, 야수묘왕 as Beast Miao King, and retain Nanman Beast Palace for 남만야수궁.",
    "Render 소뢰음사 as Small Thunderclap Temple, 광풍사 as Mad Wind Society, 포달랍궁 as Potala Palace, 오독문 as Five Poisons Sect, 독곡 as Poison Valley, 천축 as India, and 갠지스강 as Ganges River.",
    "Render 파사국 as Persia, 회교도 as Muslims, 영웅건 as hero headband, 대막 as great desert, 귀염권 as Ghost Flame Fist, and 장성 as Great Wall.",
    "Retain established renderings including Energy-Dispersing Poison, Seven-Step Soul-Chasing Powder, Blood Fish, Mutated Minnow, innate qi, true-origin qi, Heart Demon, Returned to Youth, Demon-Sealing Formation, and New Murim Alliance; use oar, throwing blade, stern, fire qi, river bandit, and Stronghold Lord where applicable.",
    "Render 궁예 as Gung Ye with an explanatory footnote, 연계 퀘스트 as Linked Quest, and 가짜 무림인-2단계 as Fake Murim Martial Artist—Stage 2."
  ],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 적천강    | **Jeok Cheongang** |
| 화왕     | **Fire King**                 | Jeok Cheongang |
| 살성     | **Slaughter Saint**           | —              |
| 화산파    | **Huashan**                      |
| 소림     | **Shaolin**                      |
| 무림맹    | **Murim Alliance**               |
| 암천     | **Dark Heaven**                  |
| 절정     | **Peak**          |
| 초절정    | **Supreme Peak**  |
| 무인     | **martial artist**                               | Default term                                          |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 기연     | **fortuitous encounter**                         | Use sparingly                                         |
| 정파     | **orthodox faction**                             |                                                       |
| 마교     | **Demonic Cult**                                 |                                                       |
| 중원     | **Central Plains**                               |                                                       |
| 강호     | **martial world**                                | Prefer “Murim” where the setting itself is meant      |
| 기루     | **pleasure house**                               |                                                       |
| 가주     | **Family Head**                              |
| 보상               | **Reward**                     |
| 헌터      | **Hunter**            |
| 레이드     | **raid**              |
| 하남     | **Henan**              |
| 사천     | **Sichuan**            |
| 화산     | **Huashan**            |
| 구화산    | **Mount Jiuhua**       |
| 정마대전   | **Great Faction War**         |
| 노부      | **this old man / I**                                            |
| 본문      | **our sect / this sect**                                        |
| 평화 | **Peace Guild** | Guild name. |
| 사마외도 | **demonic, heterodox arts** | Suspected martial-arts origin of Pung Yang's insidious forms. |
| 전서구 | **messenger pigeon** | Pigeon delivering the Lower District Sect's Jeongyang Branch report. |
| 구파일방 | **Nine Sects and One Gang** | Major Murim grouping. |
| 오대세가 | **Five Great Families** | Major Murim grouping. |
| 전하 | **His Highness** | Formal royal address for the resident prince; the official insists on this form instead of king. |
| 무재 | **martial talent** | Innate aptitude for learning martial arts. |
| 세가 | **great family** | Murim category Jin Wikyung hopes the Jin Family will attain. |
| 소림사 | **Shaolin Temple** | Temple invoked in Chulwoo’s comparison of Baek Museong’s conduct. |
| 산동악가 | **Shandong Yue Family** | Family to which Ak Bulgun belongs. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 탈주 | **Escape** | Song associated with Won Myunghoon. |
| 숭산 | **Mount Song** | Mountain where Shaolin Temple is located. |
| 마도 | **Demonic Path** | Term raised for martial power that appears to defy common principles. |
| 초절 | **supreme mastery** | Realm beyond Peak described as accessible only to the greatest martial artists. |
| 노야 | **Old Master** | Taekyung's private address for Jeok Cheongang. |
| 꼬리 | **the “tail”** | Codename for the Black Hunter traced by Butler Kim. |
| 오대 | **Five Squads** | Named Tang Clan organizational group in Tang Sadok's mobilization order. |
| 쾌조선 | **swift ship** | Fast vessel operated by the Yangtze River Channel League. |
| 암초 | **reef** | Reefs blocking the narrow water route. |
| 한나절 | **half a day** | Elapsed duration in Jeok's first time-loss episode. |
| 새외 | **Outer Lands** | Lands outside the Central Plains and its Murim. |
| 사어 | **sa-eo** | Sino-Korean term for shark, distinct from the ordinary Korean term 상어. |
| 상어 | **shark** | Ordinary Korean term for shark used in the protagonist's clarification. |
| 수상스키단 | **Shark Water-Ski Team** | Taekyung's joking name for the trained sharks traveling behind him. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 상인 | 적천강 | merchant_to_legendary_martial_master | Great Hero Jeok | deferential and flattering | Praises Jeok Cheongang while presenting the Poison-Averting Ring and requesting help. |
| 적천강 | 상인 | legendary_guest_to_merchant | you | blunt and transactional | Cuts off the merchant’s praise, asks his identity and origin, and accepts the gift without committing to the requested favor. |

## Listed compact profiles

### Jeok Cheongang.md

# Jeok Cheongang (적천강)

- **Safe through:** Chapter 510
- **Aliases:** Fire King; eighteenth Sect Leader of the Fire Gate Clan
- **Role:** Jeok Cheongang is the current Sect Leader of the Fire Gate Clan, a legendary wandering martial master who has achieved Five Qi Returning to Origin, Furnace Fire Pure Blue, and Returned to Youth, and Jin Taekyung's Master who has broken free of his Heart Demon and entered a new realm.
- **Personality:** Secretive, cryptic, sharp-eyed, gruff, dryly teasing, casually threatening or violent when dissatisfied, pathologically afraid of water, and more deeply trusting of Taekyung than anyone else despite responding to his impossible claims with mockery and violence.
- **Voice:** Sharp and ringing when calling out; otherwise gruff, dryly teasing, blunt, and threatening during interrogation or confrontation.
- **Relationships:** Jin Taekyung is his publicly acknowledged Disciple and intended heir to the Fire Gate Clan; Jeok recognizes Taekyung's Heavenly Martial Physique and has invested heavily in his growth. Jeok regards Mae Jonghak, the Sword Saint, as a kindred spirit and recognizes Cheongpung as Mae's grandson and successor. He was a close friend of Hong Dao, Shaolin's Abbot and Dharma King, whose death left him determined to act against the forces responsible. He rescued Jangcheon during an Anhui epidemic, accepted him as a Disciple, and regarded him as an only son and grandson despite Jangcheon becoming the murderer Jopil. Jeok is a long-standing rival of Peng Cheolhu, the Thunderbolt Saber King.

## Korean source

```text
＃512화



“……이런 미친놈을 봤나.”

황당함이 가득 담긴 목소리와 짙은 어둠 속에서도 도드라지는 붉은 머리카락.

예상치 못한 한 사람을 마주한 나는 눈을 동그랗게 떴다.

“어? 여긴 웬일이세요?”

“그건…….”

순간적으로 멈칫한 적천강이 말꼬리를 흐렸다.

“뱃멀미가 나서 잠깐 내렸다.”

“아, 뱃멀미요. 노야께서 뱃멀미.”

그냥 초절정 고수도 아니고, 바로 그 화왕이다.

그런 적천강이 뱃멀미에 시달리는 것보다는, 차라리 스파이더맨이 고소공포증으로 은퇴했다는 게 더 신빙성 있겠다.

“뭐냐, 그 웃음은.”

나도 모르게 올라간 입꼬리를 억지로 내리며 대답했다.

“원래 얼굴이 웃는 상인데요.”

“죽을상으로 만들어 주랴?”

“아뇨.”

“불만 있으면 말로 해라. 음흉하게 쪼개지 말고.”

“아니 뭐, 제가 언제 불만 있다고 했습니까. 그런데 등 뒤에 숨기고 계신 건 뭐예요?”

“수, 숨기긴 노부가 뭘 숨겼단 말이냐.”

“뒷짐 진 손에 들고 계신 거요. 뭐길래 부끄러워서 숨기기까지 하신대. 무림 여고생짱이신가.”

“숨긴 게 아니라니까!”

내 예리한 지적에 버럭 외친 적천강이 뒷짐을 지고 있던 손을 엉거주춤 풀었다.

커다란 나뭇잎에 싼 무언가를 만지작거리는 손길에서 갈등이 느껴졌다.

‘그나저나 음식 같은데, 냄새 한번 끝내주네.’

바람을 타고 날아오는 육향(肉香)이 장난 아니다. 한나절 넘게 생선회, 생선구이만 들어갔던 위장이 요동치는 건 당연했다.

꾸르르륵.

“돼지고깁니까?”

“소다.”

“낚시로 잡으신 건 아니겠네요.”

“당연히 미리 실어 놓은 게지. 수적 놈들이 향신료를 발라 구우니 맛이 제법이더구나.”

“그거 맛있겠네요.”

“둘이 먹다 다섯이 죽어도 모르지.”

“그 정도면 극독인데요.”

“그 정도로 맛있느니라.”

“그럼 저도 한 번 줘 보세요. 맛이나 보게.”

“허, 참. 웃기지도 않은 놈이로고. 노부가 네놈 주려고 가져온 줄 아느냐?”

“아하, 직접 드시려고 챙기신 겁니까?”

“물론이다.”

“그러니까 노야께서 뱃멀미가 심해서 쾌조선을 탈주하셨는데, 끔찍이도 싫어하시는 강물 한복판에 내버려 둔 채 쾌조선은 떠나고 그 와중에 굳이 먹을 걸 챙겼다…….”

나는 적천강을 바라보며 천천히 고개를 끄덕였다.

“확실히 일리가 있네요.”

“……!”

“주세요.”

적천강이 퉁명스러운 목소리로 대답했다.

“옛다. 처먹어라.”

“어이쿠, 감사합니다.”

“원래는 노부가 먹으려고 했는데, 입맛이 없어져서 네 녀석 주는 거다.”

“알죠. 다 알죠. 세상 사람들이 다 아는 얘기를 뭘 또 그렇게 자꾸 하세요.”

“……염병할.”

적천강의 툴툴거림을 한 귀로 흘린 나는 정신없이 고기를 흡입했다.

짧지만 전투적인 식사가 끝나갈 즈음에는 눈치를 보며 주위를 맴돌던 네 마리의 상어도, 저 멀리 희미하게 보이던 쾌조선도 시야에서 사라진 뒤였다.

“아, 놓쳤네.”

“사어 말이냐?”

“아뇨. 어차피 슬슬 놓아줄 생각이었어요.”

“그럼, 쾌조선?”

나는 손가락에 묻은 양념을 쪽 빨며 대답했다.

“예.”

“그런 것치고는 그다지 아쉬워 보이지 않는데?”

“아쉬워할 이유가 없어서요.”

“희한한 놈이로고. 쾌조선을 따라잡기 위해 사어를 부려 예까지 쫓아온 것이 아니냐?”

그래, 그랬지. 나로서는 부정할 수 없는 말이다.

하지만…….

“슬슬 후회하고 있었거든요.”

“후회?”

“네. 후회요.”

“어째서냐?”

“이렇게 해서는…… 의미가 없잖습니까.”

공력을 보충한다는 핑계로 상어를 사로잡아 여기까지 왔지만, 쾌조선에 가까워질수록 불편해지는 마음을 끝까지 무시할 수는 없었다.

그리고 아마도 그건, 지금까지 내가 살아온 방식에 어긋났기 때문이었을 것이다.

‘나도 모르게 느슨해졌던 거야.’

이미 과거로서는 상상할 수도 없던 힘을 얻었다. 내 이름에는 막대한 부와 명예, 세상의 관심이 꼬리표처럼 붙어 다닌다.

어쩌면 나는…… 그렇게 찾아온 보상들에 심취해 있던 것일지도 모르겠다.

‘예전이었다면 그러지 않았겠지.’

무언가를 얻기 위해서는 그에 상응하는 대가를 지불해야 한다.

형편에도 맞지 않는 값비싼 안전 구역(Safety Sector)에 가족이 살 집을 마련하고, 어머니의 병원비를 대기 위해 쉴 틈 없이 레이드에 매달렸던 F급 헌터였다면 상어를 이용한 꼼수 따위는 부리지 않았을 거다.

구화산에서 일 년간의 혹독한 수련을 겪으면서도 끝끝내 현실로 도망치지 않았던 그때의 나도 마찬가지다.

“차라리 거기에서 암초나 붙잡고 있을 걸 그랬습니다.”

내 푸념 섞인 너스레에 적천강이 눈살을 찌푸렸다.

“그럼 쾌조선과의 거리가 더 멀어졌을 텐데.”

“좀 멀어지면 어떻습니까. 멀어진 거리만큼 배우는 게 있었겠죠.”

“하남에 도착할 때까지 영영 따라잡지 못할 수도 있다.”

“상관없습니다. 따라잡는 게 목표가 아니니까.”

적천강의 굳어 있던 얼굴이 스르륵 풀렸다.

“한나절 만에 가장 중요한 것을 깨달았구나.”

나는 그런 적천강을 향해 고개를 숙였다. 지금만큼은 차마 그를 마주할 면목이 없었다.

“한나절이나 걸렸네요. 죄송합니다.”

“처음에는 걱정되는 마음에 널 기다렸고, 그다음에는 호되게 혼을 낼 생각이었다.”

적천강의 입장에서는 기가 찼을 것이다. 수련하라고 위탁 교육까지 보낸 놈이 상어 수상스키단을 꾸려 꼼수를 썼으니.

하지만 지금, 입술 사이로 흘러나오는 그의 목소리는 부드러웠다.

“분명 그리할 생각이었는데…… 이것으로 되었다. 지금부터라도 네 힘으로 따라잡아 보거라.”

말을 마친 적천강이 걸음을 내디뎠다. 그의 발끝을 따라 흩어지는 물결은 나와는 비교도 되지 않을 정도로 잔잔했다.

내 시선을 눈치챈 그가 한 마디를 툭 내뱉었다.

“본문의 무공은 흐름이 유독 거칠다. 이 풍랑을 스스로 가라앉히기 위해 수년을 허비해야 했지.”

“수년…….”

“네놈도 이미 알고 있을 게다. 하루아침에 배울 수 있는 것이 아니라는 것을.”

“알고 있습니다. 하루아침이 아니라 아직 열흘이 남았다는 것도.”

나는 어깨를 으쓱하며 덧붙였다.

“하지만 제 옆에는 어느 길로 가야 하는지 알려 주는 훌륭한 조언자 두 명이 있습니다. 그러니 노야께서 겪으셨던 과정보다는 훨씬 수월할 겁니다.”

화왕과 살성. 그들은 나보다 윗줄의 강자이며 이미 한참 앞서 내가 가고 있는 길을 지나간 사람들이다.

이 정도면 누구의 도움도 없이 스스로 깨달아야 했던 적천강보다는 훨씬 좋은 조건 아닌가.

내 말을 들은 적천강이 실소를 흘렸다.

“이런 얍삽한 놈 보게. 또 편법을 쓰겠다는 말을 당당히도 하는구나.”

“편법이라고 하시면 제가 섭섭하고, 보통은 이런 걸 두고 기연(機緣)라고 부르더라고요.”

“허, 말은 청산유수로군.”

“그래도 부정은 안 하시네요.”

“그야 생각해 보면 맞는 말이니까. 하지만 노부와 네 녀석의 차이는 그뿐만이 아니다.”

“……?”

“무재(武才). 네놈의 그 천인공노할 만큼 뛰어난 신체와 재능이라면 하남에 도착하기 전까지 새싹 하나쯤은 틔우겠지.”

아름드리나무도, 화려한 꽃도 결국 시작은 작은 새싹 하나다.

적천강은 꽃을 피우기 전까지 수년이 걸렸지만, 나는 다를 것이다.

한동안 말없이 나를 바라보던 그가 불쑥 입을 열었다.

“배가 보이질 않는구나. 얼른 저 빌어먹을 놈들을 쫓아가야겠다.”

“조심히 가세요. 가는 길에 사어라도 마주치면 한 번 잡아서 타 보시고.”

“그 말은 노부와 함께 가지 않겠다는 뜻이렷다.”

짓궂은 노인네. 이미 내심 짐작하고 있으면서도 나를 떠보는 모습에 피식 웃음이 나왔다.

“저는 잠시 후에 따라가겠습니다.”

“잠시라, 한나절은 걸리겠군.”

“아무래도 찝찝해서. 그럴 생각입니다.”

“쯧쯧. 사서 고생하는 방법도 가지가지로고.”

말을 그렇게 해도 어느새 올라간 입꼬리는 숨길 수 없다.

나를 물끄러미 바라보던 적천강이 신형을 돌려 짙은 어둠을 향해 쏘아졌다.

그렇게 그의 뒷모습이 점이 되어 사라진 뒤에도, 나는 한참을 그 자리에 서 있었다.

그리고 마침내 해가 떠오르고, 햇빛이 강물을 달구었을 무렵.

철벅.

거친 물살과 함께 걸음을 내디뎠다.

목표는 쾌조선, 아니 하남이었다.



* * *



천하 무림이 가마솥 안의 물처럼 들끓었다.

처음에는 단순한 소문에 불과했던 것은 호사가들의 입을 타고 사방으로 퍼져 나갔고, 어느 날 하남 숭산(嵩山)에서 솟구친 수십, 수백 마리의 전서구에는 그 소문을 사실로 만들 전서가 매달려 있었다.



천하 무림에 고하노라.



짧은 문장으로 시작된 전서는 천하 각지로 전달되었고, 전서의 내용을 알게 된 이들은 깨달았다.

그 누구도 피할 수 없는 격동의 시기가 도래했음을.

신(新) 무림맹(武林盟).

전신이 흉터로 가득한 노강호는 시체가 산을 이루고 핏물이 강이 되어 흐르던 정마대전을 떠올렸고, 평화로운 시기에 태어나 참혹했던 과거를 겪지 못한 젊은 무인들은 온갖 감정에 휩싸였다.

“때가 왔군.”

“드디어……!”

난세는 영웅을 낳는 법.

누군가는 이름을 떨칠 기회가 왔다는 생각에 흥분을 감추지 못했고.

“이, 이럴 수가!”

“결국. 결국 이리 되었는가.”

누군가는 곧 들이닥칠 죽음에 대한 두려움으로 몸을 떨었다.

그러나 당대의 정파 무림은 역사가 증명한 승리자였다.

수십여 년 전, 그토록 강대하던 마교조차 중원을 차지하지 못하고 패퇴하지 않았던가.

비록 소림과 사천에 한바탕 혈풍이 들이닥쳤으나, 대부분의 무림인들에게 그것은 분노하고 맞서 싸워야 할 이유였지, 두려워하며 물러설 만한 일이 아니었다

“의기(意氣) 있는 자, 병장기를 찬 무인이라면 무림맹의 깃발 아래 서라!”

천하에 울려 퍼진 외침.

그리고…… 그 외침에 답하는 이들이 있었다.

“숭산 소림. 입맹을 청합니다.”

“화산 역시 무림맹에 합류하겠소.”

구파일방(九派一幇). 오대세가(五大世家).

작금의 천하 무림을 지탱하는 열다섯 개의 기둥이 움직이기 시작했다.

그중에서도 소림사와 화산파가 가장 먼저 무림맹의 깃발을 세웠고, 나머지 명문 대파 역시 앞다투어 입맹을 청했다.

저잣거리와 기루, 객잔에 북새통을 이룬 호사가들은 연일 그 이야기로 떠들어대기 바빴다.

“들었나? 구파일방과 오대세가가 모두 입맹했다더군.”

“아직 알려진 지 하루밖에 되지 않았는데, 벌써 말인가?”

“소식이 느리군. 그거야 당연한 일이지. 문제는 그 외 다른 문파들일세.”

“산동악가(山東岳家)도 합류할 예정이라던데.”

“그건 좀 의외로군. 아무래도 무림과 관부 사이에서 위치가 어정쩡하지 않나.”

“하후검가(夏侯劍家) 쪽 소식은 어떤가?”

“전대 가주가 정마대전 때 전사했던 것으로 알고 있네. 아마 현 가주 입장에서는 아비의 원수를 갚기 위해서라도 참전하겠지. 이제 암천이 마교의 후신이라는 건 모르는 사람이 없지 않나.”

“무림맹은 정파 무림의 상징일세. 문제는 사마외도와 새외야.”

호사가들이 대화를 나누는 그 순간에도, 천하 무림 곳곳에서는 각자의 움직임이 일어나고 있었다.

그리고 들불처럼 번져가는 열기 속에서, 열흘이라는 시간이 흘렀다.
```

## Final English reading copy

```markdown
# Chapter 512

“…What a lunatic.”

The voice was thick with disbelief, and the red hair stood out even in the deep darkness.

I opened my eyes wide when I came face-to-face with someone I never expected to see.

“Oh? What brings you here?”

“That’s…”

Jeok Cheongang hesitated, his voice trailing off.

“I got seasick and got off for a bit.”

“Ah, seasick. The Old Master got seasick.”

This wasn’t just any Supreme Peak master. This was the Fire King himself.

It would have been more believable for Spider-Man to retire because of acrophobia than for Jeok Cheongang to suffer from seasickness.

“What’s with that smile?”

I forced down the corners of my mouth and answered.

“I naturally have a smiley face.”

“Want me to make it look ready to die?”

“No, thank you.”

“If you have a complaint, say it to my face. Don’t grin at me like a creep.”

“I never said I had a complaint. But what are you hiding behind your back?”

“H-hiding? What are you talking about? What would this old man be hiding?”

“The thing you’re holding in your clasped hands. Whatever could it be that you’re so embarrassed you have to hide it? Are you some kind of Murim high-school girl boss?”

“I said I’m not hiding anything!”

Jeok Cheongang shouted at my sharp observation and awkwardly lowered his clasped hands.

He was fiddling with something wrapped in a large leaf, and the conflict in his movements was obvious.

*It looks like food. And damn, does it smell good.*

The meaty aroma carried on the wind was incredible. My stomach had spent more than half a day digesting nothing but raw fish and grilled fish, so of course it began to churn.

*Grrrrowl.*

“Is it pork?”

“Beef.”

“You didn’t catch it fishing, did you?”

“Of course not. It was loaded in advance. Those river bandits coated it with spices and grilled it. It’s quite good.”

“That sounds delicious.”

“It’s so good that five people could die while two were eating and they wouldn’t even notice.”

“That sounds like deadly poison.”

“It’s that delicious.”

“Then give me some. I’ll have a taste.”

“Hah. You’re not even funny. Did you think I brought it for you?”

“Ah. So you packed it for yourself?”

“Of course.”

“So you got seasick, abandoned the swift ship, and were left in the middle of the river you hate so much while the swift ship sailed away, and yet you still went out of your way to bring food…”

I looked at Jeok Cheongang and slowly nodded.

“That does make a certain amount of sense.”

“…!”

“Give it here.”

Jeok Cheongang answered in a surly voice.

“Here. Stuff your face.”

“Why, thank you.”

“I was originally going to eat it myself, but I lost my appetite, so I’m giving it to you.”

“I know. I know everything. Why do you keep explaining something the whole world already knows?”

“...Damn it.”

I let Jeok Cheongang’s grumbling pass in one ear and devoured the meat.

By the time my short but fiercely fought meal was coming to an end, the four sharks that had been circling nearby while watching me warily had disappeared from sight. So had the swift ship that had been faintly visible in the distance.

“Ah, I missed it.”

“You mean the sa-eo?”

“No. I was planning to let them go soon anyway.”

“Then the swift ship?”

I licked the sauce from my fingers as I answered.

“Yes.”

“You don’t seem particularly disappointed for someone who missed it.”

“I have no reason to be disappointed.”

“What a strange fellow. Didn’t you use the sa-eo to chase the swift ship all the way here so you could catch up?”

He was right. I couldn’t deny it.

But…

“I was starting to regret it.”

“Regret?”

“Yes. Regret.”

“Why?”

“Because doing this… has no meaning.”

I had captured the sharks and come all the way here under the pretext of replenishing my internal energy. But the closer I got to the swift ship, the harder it became to ignore the discomfort in my heart.

And perhaps that was because I had acted against the way I had lived until now.

*I’d let myself grow careless without realizing it.*

I had already gained power I could never have imagined in the past. Enormous wealth, fame, and the attention of the world followed my name like labels attached to it.

Perhaps I had become intoxicated by the rewards that had come with all of that.

*I wouldn’t have acted this way before.*

To obtain something, you had to pay a price equal to its value.

If I had still been the F-rank Hunter who had secured a home for my family in an expensive Safety Sector far beyond our means and thrown myself into raids without rest to pay my mother’s hospital bills, I would never have used some cheap trick involving sharks.

The same went for the version of me who had endured a year of brutal training at Mount Jiuhua without once running away to reality.

“I should’ve just held on to a reef back there.”

Jeok Cheongang frowned at my complaining joke.

“Then you would have fallen even farther behind the swift ship.”

“So what if I fell a little farther behind? I would have learned something equal to the distance I lost.”

“You might never catch up before we reach Henan.”

“I don’t care. Catching up isn’t the goal.”

Jeok Cheongang’s stiff expression slowly relaxed.

“You realized the most important thing in half a day.”

I lowered my head toward him. At that moment, I couldn’t bring myself to meet his eyes.

“It took me half a day. I’m sorry.”

“At first, I waited because I was worried about you. After that, I planned to give you a thorough scolding.”

From Jeok Cheongang’s perspective, it must have been utterly absurd. He had even outsourced my training, only for me to put together a Shark Water-Ski Team and use a cheap trick.

But his voice, flowing between his lips now, was gentle.

“I certainly intended to do that… but this will do. From now on, try to catch up using your own strength.”

Jeok Cheongang finished speaking and stepped forward. The ripples scattering from his toes were so calm they could not even be compared to mine.

Noticing my gaze, he tossed out a single remark.

“Our sect’s martial arts have an especially violent flow. I wasted years calming this storm on my own.”

“Years…”

“You already know it. You know this isn’t something you can learn overnight.”

“I know. I also know that it isn’t overnight. There are still ten days left.”

I shrugged and added,

“But I have two excellent advisors beside me to tell me which way to go. So it should be much easier than the process you went through, Old Master.”

The Fire King and the Slaughter Saint. They were both experts far above me, people who had already traveled far ahead along the path I was taking.

Didn’t that put me in a much better position than Jeok Cheongang, who had been forced to realize everything on his own without anyone’s help?

Jeok Cheongang let out a quiet laugh.

“Look at this sly bastard. You’re proudly announcing that you intend to use another shortcut.”

“I find it hurtful that you call it a shortcut. Most people call something like this a fortuitous encounter.”

“Hah. Your tongue is as smooth as flowing water.”

“But you aren’t denying it.”

“Because you’re right, when I think about it. But that isn’t the only difference between you and this old man.”

“…?”

“Martial talent. With that outrageously excellent body and talent of yours, you should be able to sprout at least one bud before reaching Henan.”

A towering tree and a gorgeous flower both began with a single small bud.

It had taken Jeok Cheongang years to bloom, but I would be different.

After watching me in silence for a while, he suddenly spoke.

“I can’t see the ship anymore. We should hurry and chase those damned bastards.”

“Take care. If you run into a sa-eo on the way, catch one and try riding it.”

“That means you don’t intend to come with me.”

What a mischievous old man. He had clearly already guessed what I intended, yet he was still testing me. I couldn’t help but chuckle.

“I’ll follow in a little while.”

“A little while? That’ll be half a day.”

“It still doesn’t sit right with me. So yes, that’s what I intend to do.”

“Tsk, tsk. There are all sorts of ways to make life difficult for yourself.”

Even as he said that, he couldn’t hide the corners of his mouth lifting into a smile.

Jeok Cheongang stared at me for a moment, then turned and shot toward the deep darkness.

Even after his back had become a dot and disappeared, I stood there for a long while.

At last, the sun rose, and the sunlight began to heat the river.

*Splash.*

I stepped forward through the rough current.

My destination was the swift ship.

No—the destination was Henan.



* * *



The entire Murim world seethed like water in a cauldron.

What had begun as a simple rumor spread in every direction on the lips of gossipmongers. Then one day, dozens—hundreds—of messenger pigeons rose from Mount Song in Henan, each carrying a letter that would turn the rumor into fact.



*To the Murim of the world.*



The letters began with that brief sentence and were delivered across the land. Those who learned their contents realized the truth.

An era of upheaval that no one could escape had arrived.

The New Murim Alliance.

An old martial-world veteran whose entire body was covered in scars remembered the Great Faction War, when corpses had formed mountains and rivers had flowed with blood. Young martial artists born in peaceful times, who had never experienced that horrific past, were swept up in every imaginable emotion.

“The time has come.”

“At last…!”

It was said that troubled times gave birth to heroes.

Some could not hide their excitement at the thought that their chance to make a name for themselves had arrived.

“H-how can this be!”

“So it’s finally come to this.”

Others trembled with fear at the deaths that would soon descend upon them.

But the orthodox Murim of the present era was the victor proven by history.

Had even the mighty Demonic Cult not been defeated and driven back without taking the Central Plains several decades ago?

Although a bloody storm had struck Shaolin and Sichuan, to most martial artists it was a reason to grow angry and fight back—not something that warranted retreating in fear.

“Those with conviction! Any martial artist who carries a weapon, stand beneath the Murim Alliance’s banner!”

The cry rang out across the land.

And there were those who answered it.

“Shaolin of Mount Song requests to join the alliance.”

“Huashan will join the Murim Alliance as well.”

The Nine Sects and One Gang. The Five Great Families.

The fifteen pillars supporting the Murim of the present world began to move.

Shaolin Temple and Huashan were the first to raise the Murim Alliance’s banner, and the other prestigious sects and great factions rushed to request membership as well.

Gossipmongers filling the markets, pleasure houses, and inns were busy talking about it day after day.

“Have you heard? They say the Nine Sects and One Gang and the Five Great Families have all joined the alliance.”

“It’s only been a day since the news became known. Already?”

“Your information is slow. Of course they have. The question is what the other sects will do.”

“I heard the Shandong Yue Family intends to join as well.”

“That’s a bit unexpected. Aren’t they in an awkward position between the Murim and the authorities?”

“What news have you heard from the Hahou Sword Family?”

“I understand the former Family Head died in the Great Faction War. From the current Family Head’s perspective, he’ll probably enter the war if only to avenge his father. There isn’t anyone left who doesn’t know that Dark Heaven is the successor to the Demonic Cult, is there?”

“The Murim Alliance is the symbol of orthodox Murim. The problem is those who practice demonic and heterodox arts—and the Outer Lands.”

Even as the gossipmongers carried on their conversation, movements were taking place all across the Murim world.

And amid the heat spreading like wildfire, ten days passed.
```
