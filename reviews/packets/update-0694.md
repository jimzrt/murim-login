<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0694.txt",
      "sha256": "b2a6d0f5d507bcf1636648ea9d31a076c6d698eb7aa8b906cf4265f9ec48649b",
      "bytes": 14968
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "c878cb21448725943cc8cfb137e6b21293d30481f92b8b84cea4cf68ddfb6794",
      "bytes": 2531
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "513c6fafe9f1840a6e447ad7562b1e3ec4fe9fa5309e776d08b3dfd0909660d4",
      "bytes": 204873
    },
    {
      "path": "characters/Baeksang.md",
      "sha256": "9c50d8c3fd399774d7625092e8782cbfae0080e20063968592e58a40c0b38325",
      "bytes": 942
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "202e1aeadb9ba7eda914993e4db2b11ddbae0245e644eea02cc338fc4c22b1cc",
      "bytes": 553
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "22c6d2cd2746f070c5e08ac7b9ed05b8785c07c557af51784cdc785d39908562",
      "bytes": 1897
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "3c26f838fa1ace2b915226c2a6bd7c47f1bf1385459cdc471f3ddcd318e89873",
      "bytes": 622
    },
    {
      "path": "characters/Southern Heaven Demon Empress.md",
      "sha256": "dea40001f29fc16c8c5c21009c83c6f596ae20ca258af90a421b1c2b85094989",
      "bytes": 770
    },
    {
      "path": "characters/Yayul Cheok.md",
      "sha256": "4080069069957e9bf56135a2a19be8d8d518809b98897b6bbd7aa96f4fde0870",
      "bytes": 902
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "1808165d3ab77a7b3796d58b272d3466179775d5f73d20537877593183b5a34e",
      "bytes": 213279
    }
  ],
  "estimated_tokens": 12257
}
-->

# Durable State Update — Chapter 694

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 694. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 694. Profile updates may replace only one
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
  "chapter": 694,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 694,
    "continuity_sources": [694],
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
    "Jin Taekyung, Yohi, and Muyaho remain in the hidden healing realm deep within the Poisonblood Grounds.",
    "The healing pond saved Muyaho from the brink of death and restored Jin's severe injuries.",
    "The Black Tiger is an ancient guardian spirit born alongside the sacred stone and protects the hidden land beneath Ailao Mountain, formerly the Sacred Land.",
    "The sacred stone sustains the land's abundance, and its power to rule beasts is only one of its abilities.",
    "The Beast King Stone was a powerless stone created by Nanman's first Palace Lord as a legend to unite the tribes; the actual sacred stone was never his possession.",
    "Human wars drained the sacred stone's power, while the Black Tiger watched without intervening and later regretted failing to save the first Palace Lord.",
    "The Black Tiger possesses the Water God Dragon's Origin Essence and wants to use it to restore the sacred stone.",
    "The System changed the Black Tiger's designation to guardian spirit, revealed the Hidden Sacred Land, and created the hidden Quest Last Chance.",
    "Jin must decide whether to strengthen the Ancient Sacred Stone with the Water God Dragon's Origin Essence.",
    "Yohi and Muyaho witnessed a tremor, the awakening of birds and beasts, and a pillar of light enveloping the hidden realm.",
    "Jin still intends to find an exit and return to Nanman before the Southern Heaven Demon Empress's attack causes further deaths.",
    "The System's unidentified discovery remains unresolved."
  ],
  "continuity_sources": [
    693
  ],
  "open_questions": [
    "Will Jin accept the System's offer to strengthen the Ancient Sacred Stone with the Water God Dragon's Origin Essence?",
    "What consequences will follow from the hidden Quest Last Chance and the pillar of light?",
    "How can Jin, Yohi, and Muyaho leave the hidden realm?",
    "Is Heugung truly dead?",
    "What is the System's unidentified discovery?"
  ],
  "safe_through": 693,
  "temporary_decisions": [
    "Render 수왕석 as Beast King Stone, 신석 as sacred stone, and 고대의 신석 as Ancient Sacred Stone.",
    "Render 애뇌산의 망령 as Apparition of Ailao Mountain and 수호령 as guardian spirit.",
    "Render 숨겨진 성지 as Hidden Sacred Land and 마지막 기회 as Last Chance.",
    "Render 흑호's 의념 as telepathic dialogue with em dashes and a calm, ancient voice.",
    "Render 영기 as spiritual energy and 원정 as Origin Essence."
  ],
  "version": 1
}
```

## Exact glossary matches

| 진태경    | **Jin Taekyung**   |
| 열화문    | **Fire Gate Clan**               |
| 남만야수궁  | **Nanman Beast Palace**          |
| 절정     | **Peak**          |
| 초절정    | **Supreme Peak**  |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 중원     | **Central Plains**                               |                                                       |
| 문주     | **Sect Leader**                              |
| 정마대전   | **Great Faction War**         |
| 백상 | **Baeksang** | Great chieftain of the Bai people and Yayul Cheok's sworn younger brother. |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 남천마후 | **Southern Heaven Demon Empress** | Title Honglan uses when revealing her identity. |
| 야율척 | **Yayul Cheok** | Beast Miao King and lord of the Nanman Beast Palace. |
| 검신 | **Sword God** | Alternate title used for Mae Jonghak; kept distinct from 검성, rendered Sword Saint. |
| 세가 | **great family** | Murim category Jin Wikyung hopes the Jin Family will attain. |
| 한족 | **Han Chinese** | Ethnic designation used by the steppe chieftains. |
| 천마 | **Heavenly Demon** | Demonic title used in Jeok Cheongang's impossible comparison. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 피어 | **Fear** | Monster effect that overwhelms a target’s mental fortitude. |
| 남만 | **Nanman** | Historical regional term used for the source of the imported ebony. |
| 초절 | **supreme mastery** | Realm beyond Peak described as accessible only to the greatest martial artists. |
| 꼬리 | **the “tail”** | Codename for the Black Hunter traced by Butler Kim. |
| 열화 | **Blazing Flame** | Lineage term in Taekyung's declaration as the Fire King's successor. |
| 리치 | **Lich** | Named Monster; fallen archmage and apex undead monster. |
| 호위장 | **Captain of the Guards** | The Sichuan City Lord's guard captain. |
| 뇌옥 | **underground prison** | The Tang Clan's subterranean prison. |
| 묘족 | **Miao people** | Ethnic group the Escort Bureau expects to encounter near Yunnan. |
| 오독문 | **Five Poisons Sect** | Formerly dominant Nanman faction destroyed by the Fire Gate Clan. |
| 독물 | **venomous beasts** | Venomous creatures associated with the Nanman Beast Palace. |
| 대전쟁 | **Great War** | The long war that ended after the Great Cataclysm. |
| 고든 | **Gordon** | Pentagon employee tasked with repairing smashed warning lights. |
| 남천 | **South Heaven** | Dark Heaven power that the Lord of Heaven orders the servants to contact. |
| 애뇌산 | **Ailao Mountain** | Mountain crossed by the party on the route to the Nanman Beast Palace. |
| 백호 | **White Tiger** | Yayul Mok's tiger companion. |
| 내궁 | **Inner Palace** | The inner compound of the Nanman Beast Palace. |
| 야율 | **Yayul** | Name used in Taekyung's colloquial address to the Beast Miao King. |
| 외궁 | **Outer Palace** | The outer compound of the Nanman Beast Palace. |
| 대족장 | **Great Chieftain** | Title used for the senior Nanman leader who supposedly ordered the inspection. |
| 마후 | **Demon Empress** | Title used for the Southern Heaven Demon Empress. |
| 궁주 | **Palace Lord** | Title Yohi uses after realizing that Heugung is the Beast Miao King. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 시비 | 진태경 | household_servant_to_visiting_young_hero | Young Hero Jin | formal-polite | The maid summons Taekyung to meet the Family Head. |
| 신의 | 진태경 | physician_to_benefactor | Young Master Jin | formal-polite | The Divine Physician addresses Taekyung as 진 공자 while expressing concern for his injuries. |
| 진태경 | 청년 | celebrated Hunter to younger fellow Hunter | young man | casual, teasing, and profane | Jin addresses the young Hunter after overhearing his criticism and deliberately switches to casual speech. |
| 청년 | 진태경 | frightened junior Hunter to celebrated senior Hunter | you | fearful and deferential | The young Hunter uses 당신 while asking whether Jin is really the person he recognizes from the media. |
| 남천마후 | 진태경 | hostile_supernatural_opponent_to_young_martial_artist | Young Great Hero / Child | lighthearted and taunting | Addresses Taekyung while refusing to explain the Gate. |
| 진태경 | 남천마후 | young_martial_artist_to_hostile_demon_empress | you | hostile and determined | Promises that the Southern Heaven Demon Empress will die when they meet again. |
| 야율척 | 진태경 | Nanman_Beast_Palace_Palace_Lord_to_Jeok_Cheongang's_Disciple | you / Disciple of Old Master Jeok / Jin Taekyung | rough, testing, and later welcoming | Yayul Cheok questions Taekyung as a suspected culprit, strikes him as a test, and then welcomes him after recognizing Jeok's Disciple. |
| 진태경 | 야율척 | Fire_Dragon_Pavilion_Pavilion_Master_to_Nanman_Beast_Palace_Palace_Lord | Great Hero Yayul Cheok | formal and deferential | Taekyung gives Yayul Cheok a formal greeting as the nineteenth successor of the Fire Gate Clan. |
| 백상 | 진태경 | Nanman great chieftain to Murim Alliance Pavilion Head | you bastard | cold, hostile, and contemptuous | Baeksang calls Jin a Han Chinese man, rejects his status, and orders him to leave. |
| 진태경 | 백상 | Murim Alliance Pavilion Head to Nanman great chieftain | you | polite but deliberately provocative | Jin tells Baeksang that Nanman's blood was shed for the world rather than merely for the Central Plains. |
| 진태경 | 백호 | human ally to intelligent spiritual beast | you | casual and familiar | Converses with White Tiger after interpreting its warning. |
| 백상 | 남천마후 | Nanman Great Chieftain to hostile demon empress | Southern Heaven Demon Empress | formal and shocked | Baeksang directly identifies the woman who appears before him. |
| 남천마후 | 백상 | Dark Heaven controller to coerced Nanman leader | Great Chieftain Baeksang / Palace Lord | playful, taunting, and threatening | She repeatedly addresses Baeksang while mocking his grief, acknowledging his effort, and issuing her order. |
| 진태경 | 부족장 | captor to captured tribal chieftain | tribal chieftain | casual, coercive, and mocking | Jin promises to spare the captured chieftain if he answers questions properly. |
| 부족장 | 진태경 | captured tribal chieftain to overpowering enemy | Jin Taekyung | alarmed and desperate | The chieftain recognizes Jin by name while fleeing and then begs for his life. |
| 백상 | 호위장 | Palace Lord to Captain of the Guards | Captain of the Guards | formal and commanding | Baeksang issues orders concerning Ailao Mountain, the missing chieftains, and the pursuit of Yayul Cheok. |
| 호위장 | 백상 | Captain of the Guards to Palace Lord | my lord | formal and deferential | The Captain reports the wildfire and missing chieftains while questioning Baeksang's orders. |

## Listed compact profiles

### Baeksang.md

# Baeksang (백상)

- **Safe through:** Chapter 690
- **Aliases:** None
- **Role:** Baeksang is the Palace Lord of the Nanman Beast Palace, an over-seventy Great Chieftain of the Bai people, and the ruler directing Nanman's general mobilization and purge of disloyal tribes.
- **Personality:** Cold, rigid, meticulous, politically resolute, and strategically manipulative, with enduring grief over Hwi's death and a guarded but still powerful bond with his sworn elder brother that now leaves him visibly conflicted.
- **Voice:** Rigid, formal, restrained, and emotionally distant.
- **Relationships:** Baeksang is Yayul Cheok's sworn younger brother and childhood companion, Yayul Mok's sworn uncle, and the father of deceased Baekhwi, whom the Great Snow Fiend killed; he cultivated Yohi with gold and influence and used her support to advance Dark Heaven's preparations.

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 693
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** Publicly reputed to be selfless and devoted to treating patients in the lowest places.
- **Voice:** Not established.
- **Relationships:** Mungyeong is the Divine Physician's true identity, and Dong Feng is his Disciple.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 691
- **Aliases:** Blazing Flame Divine Dragon; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan, Jeok Cheongang's publicly acknowledged Disciple, the Fire Gate Clan's nineteenth successor, and the Pavilion Master of the Fire Dragon Pavilion within the Murim Alliance, a Supreme Peak master with the Heavenly Martial Physique and Force, a publicly recognized S-rank-level Hunter who formally retains an A-rank license, and an escaped prisoner who has awakened inside an unexplained healing realm after lying unconscious in its pond.
- **Personality:** Hungry, self-aware, dryly observant, pragmatic under pressure, and willing to risk himself for people he has accepted as real. Treats impossible situations like games until their human cost becomes undeniable.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, Jeok Cheongang is his Master, Mungyeong was his recent instructor, Cheongpung is his trusted companion and only true martial rival, Choi Minwoo is his subordinate and trusted manager of media and official arrangements, Ju Hwaran is a trusted Fire Dragon Pavilion member who followed him to Nanman, Chuck Hagel is an American operative allied with him in the covert anti-terror campaign, his mother and sister Hayeon are among those he protects, the Skeleton King is his friend and ally, Xiao Shen regards him as an older brother after Jin saved him, and Jin-ho is his older friend and trusted confidant.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 691
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Southern Heaven Demon Empress.md

# Southern Heaven Demon Empress (남천마후)

- **Safe through:** Chapter 692
- **Aliases:** None
- **Role:** The Southern Heaven Demon Empress is the strategist directing Baeksang's defense of Nanman's Inner and Outer Palaces while advancing a grand plan scheduled to begin within three days.
- **Personality:** Playful, cruel, confident, and casually dismissive of mass death and the suffering of others.
- **Voice:** Light, taunting, amused, and delighted even when discussing murder or imminent catastrophe.
- **Relationships:** She commands and advises Baeksang, treats Jin Taekyung and Yayul Cheok as expendable to the grand plan, and regards Jin's destruction of her trap with amused surprise.

### Yayul Cheok.md

# Yayul Cheok (야율척)

- **Safe through:** Chapter 688
- **Aliases:** Beast Miao King
- **Role:** Yayul Cheok is the over-eighty Beast Miao King, lord of the Nanman Beast Palace, a Supreme Peak master among the Ten Kings, and great chieftain of the Miao people.
- **Personality:** Boisterous, warmhearted, forthright, playful, and politically conscious of the tribal coalition he leads.
- **Voice:** Rough, loud, convivial, and teasing, becoming authoritative when discussing Nanman's laws or political decisions.
- **Relationships:** Jeok Cheongang is an old acquaintance whom he respects; Baeksang is his sworn younger brother and childhood companion, and they fought together during the Great Faction War; Yayul Mok serves as his Young Palace Lord; Jin Taekyung is Jeok's Disciple whom he welcomes into the Nanman Beast Palace.

## Korean source

```text
＃694화



달마저 가려진 깊은 밤.

짙은 어둠에 잠겨 있던 산골짜기에, 희미한 불꽃이 피어오르기 시작했다.

하나, 둘, 셋. 그리고 이내 수백으로 불어난 횃불과 함께 세상이 흔들린다.

드드드득!

지면을 통해 전해지는 떨림. 바람에 휘청이는 횃불 아래에는 크고 작은 그림자와 거친 숨결이 쉼 없이 뿜어졌다.

크르릉.

후우. 후.

군세(軍勢).

그것은 수많은 인간과 짐승이 뒤섞인 하나의 군세였다.

검과 창, 활로 무장한 남만의 전사들은 안장 위에 앉아 쉴 새 없이 어둠 너머를 눈으로 더듬고 있었고, 날카로운 이빨과 발톱을 지닌 맹수들은 계속 달려 나갔다.

그 숫자가 물경 삼천.

그리고 오직 한 사람의 명령에 따라, 정오 무렵 외궁을 벗어난 그들의 목적지는 처음부터 정해져 있었다.

‘애뇌산(哀牢山).’

선두에서 내달리던 호위장의 머릿속에 떠오른 세 글자. 그와 동시에 그의 등 뒤에서 누군가의 외침이 터져 나왔다.

“보입니다!”

과연 그 말대로였다.

호위장은 물론 모두가 볼 수 있었다. 삼천에 달하는 군세가 지닌 횃불과는 비교도 되지 않는 강렬하고, 거대한 화마(火魔)가 일렁이는 모습을.

우둑, 콰아아아!

나이를 가늠할 수 없는 거목이 줄지어 쓰러지고, 닿는 모든 것을 탐욕스럽게 집어삼킨 불길이 더욱더 몸집을 부풀린다.

백 년 전에도 없었고, 어쩌면 백 년 뒤에도 없을 대화재(大火災)을 지켜보는 전사들의 입술 사이로 침음성이 흘러나왔다.

“이, 이럴 수가.”

“그게. 그게 사실이었다니…….”

다른 사람의 입을 통해 전해 듣는 것과 직접 눈으로 확인하는 것은 다르다.

불길에 휩싸인 애뇌산을 바라보는 전사들의 눈동자에 경악과 두려움의 빛이 스쳐 지나갔다.

‘진태경.’

‘놈에 관한 소문이 전부 사실이었어.’

‘그토록 많은 추격대를 뿌리치고 이곳까지 오다니. 도대체 어느 정도의 괴물인 거지?’

당연하게도 이 자리에 있는 전사 중 대다수는 진태경을 직접 마주한 적이 없다.

아니, 그의 진면목을 확인한 적이 없다고 말해야 옳았다.

그들에게 있어 지금까지의 진태경은 그저 중원에서 온 이방인이었고 남만인들과는 조금 다른, 희한한 생김새를 지닌 젊은 청년에 불과했다.

그러나 이제는, 그와 싸워야 한다.

애뇌산을 물 샐 틈 없이 포위한 채 언제 저곳을 뛰쳐나올지 모를 진태경을 척살하는 것이 자신들에게 내려진 임무였다.

하지만…….

‘놈을 막을 수 있을까. 그 괴물을?’

모두의 뇌리에 떠오른 한 가지 의문.

남만야수궁의 시작과 역사를 같이한 금지(禁地). 애뇌산에 관한 이야기를 사는 내내 지긋지긋하게 들었던 그들이다.

그리고 그럴 때마다 늘 빠지지 않는 세 글자가 있었다.

열화문(烈火門).

머나먼 중원 땅 어딘가에 존재한다는 미지의 문파.

아득한 과거, 이 땅에 발을 디딘 열화문의 문주는 남만야수궁이 탄생한 이후에도 백여 년간 계속되던 오독문과의 대전쟁에 종지부를 찍었다고 했다.

수많은 목숨을 앗아 간 오독문의 극독(劇毒)도, 놈들이 부리던 독물도 그가 불러낸 화염 앞에 촛농처럼 녹아내렸다.

심지어는 남만야수궁의 최정예 전사 일백을 한 줌 독수로 만들었다는 오독문의 당대 문주조차 그의 힘을 감당하지 못하고 무릎을 꿇었다고 했다.

‘아니, 산 채로 타 죽었다고 했지.’

그런데 모두가 어린 시절 재미있게 들었던 옛 전설이, 지금 이 순간 과거를 넘어 현재로 다가왔다.

바로 자신들의 눈앞에.

꿀꺽.

누군가의 마른 침 삼키는 소리가 유난히도 크게 울려 퍼진다. 느슨하게 고삐를 말아쥐고 있던 손에는 어느새 한껏 힘이 들어갔고, 불안하게 흔들리는 눈동자와 함께 동요가 퍼져 나간다.

그리고 바로 다음 순간이었다. 굳게 닫혀 있던 호위장의 입술이 열린 것은.

“무엇이 그리 두렵더냐.”

“……!”

공력이 실린 목소리가 전사들의 귓가를 파고든다. 호위장은 힘주어 말을 이었다.

“놈은 혼자. 우리는 삼천이다.”

자신도 모르게 움츠려졌던 전사들의 어깨가 조금씩 펴진다. 흔들리던 시선이 하나둘씩 중심을 되찾기 시작했다.

‘그래. 놈이 아무리 강하다 한들, 결국 피륙으로 이루어진 인간.’

‘지금껏 들었던 진태경에 관한 소문이 모두 사실이라 해도, 이 군세를 당해 낼 수는 없어.’

삼천.

무려 삼천이었다. 단 한 사람을 척살하기 위한 숫자로는 차고 넘치다 못해, 터무니없는 머릿수다.

엄청난 무위로 오독문을 박살 냈다는 열화문의 문주?

자신들이 듣고 자란 이야기를 떠올리면 두려운 마음이 드는 것은 사실이지만, 결국 전설은 전설일 뿐이다.

아니, 설령 그가 살아온다 해도 삼천에 달하는 남만의 전사와 맹수들을 단신으로 상대하는 것은 불가능하다. 불가능해야 했다.

“잊었느냐. 진태경은 남만을 위험에 빠트린 역도요, 정마대전의 은혜를 잊은 금수만도 못한 한족이다.”

빠르게 가까워지는 거대한 화마만큼, 호위장의 목소리에도 힘이 실린다.

스릉.

“남만의 전사들이여! 자랑스러운 내 형제들이여!”

허리춤에서 뽑혀 나온 검이 날카로운 예기를 뿜어낸다.

머리 위에서 쏟아진 달빛과 일렁이는 횃불이 새하얀 검신에 부딪쳐 산산이 부서졌다.

“놈을 추살하라!”

“와아아아아!”

차차차창!

동시에 뽑혀 나온 수백, 수천의 병장기와 거세게 타오르는 횃불. 그리고 삼천에 달하는 군세가 아득한 함성을 내지르며 애뇌산을 향해 박차를 가하던 바로 그 순간.

콰아아아!

호위장은, 이 자리의 모든 인간과 맹수는 볼 수 있었다.

시뻘건 화마(火魔)를 관통하며 솟구치는 빛의 기둥과 뜨거운 불길 앞에 그림자를 드리운 검은 동산을.

아니, 그건 동산이 아니었다.

드드드드득!

“저게 무슨……!”

빠르게 다가오는 검은 동산과 함께 흔들리는 세상 속, 눈을 부릅뜬 채 그 광경을 바라보던 호위장은 알지 못했다.

더 이상 바람이 느껴지지 않는다는 것을.

쉼 없이 애뇌산을 향해 달려가던 삼천 마리의 맹수가, 약속이라도 한 것처럼 제 자리에 멈춰 섰다는 것을.

크르릉.

호위장과 평생을 함께한 호랑이가 낮은 울음소리와 함께 고개를 숙인다.

아니, 비단 그뿐만이 아니었다.

표범도, 곰도, 늑대도. 크고 작은 모든 맹수가 그러했다.

스륵.

꼬리를 말고, 거대한 몸뚱어리를 눕힌다.

그것은 탄생과 동시에 각인되어 있던 본능이자 긴 세월을 거슬러 돌아온 왕에 대한 경배였고, 거부할 수 없는 명령이었다.

- 크아아아앙!

세상을 집어삼키는 포효와 함께, 청백색의 안광(眼光)이 어둠 속에서 빛났다.



* * *



저벅. 저벅.

나직한 발걸음 소리가 적막한 복도를 울린다.

한 사람, 한 사람이 절정에 이른 호위 전사들의 날카로운 눈빛에 시비와 하인들은 엎드려 부복했고, 떨리는 외침이 뒤를 이었다.

“구, 궁주를 뵙습니다!”

두려움이 묻어 나오는 그들의 외침은, 오직 한 사람을 향한 것이다.

철통같은 호위에 둘러싸인 채 내궁(內宮)의 복도를 가로지르던 백상의 시선이 문득 그들을 훑었다.

내궁에서 일하는 이들은 부족도, 나이도 다양하다.

아직 젖살도 빠지지 않은 어린아이부터, 중년의 사내와 여인. 그리고…… 온통 머리가 하얗게 센 호호백발 노파까지.

워낙 늙어 행동거지가 굼뜬 탓에, 홀로 복도의 중앙에서 쩔쩔매는 노파의 모습을 본 호위들이 미간을 찌푸렸다.

그들이 충심을 다해 모시는 백상은 남만야수궁의 주인이요, 이 땅의 왕이다. 아니, 왕이어야 한다.

죽을 날만 기다리는 늙은이가 앞길을 가로막아서는 안 된다.

저벅.

그리고 약속이라도 한 듯, 두어 명의 호위가 노파를 향해 걸음을 내디딘 그 순간이었다.

“멈추어라.”

나직한 목소리와 함께 호위들의 움직임이 덜컥 멈춘다. 자신의 시선에 닿은 노파를 향해, 백상은 들리지 않을 인사를 건넸다.

‘오랜만이구려.’

긴 세월이 흘렀음에도 낯익은 얼굴이다.

백상은 자신의 어린 시절, 야율척과 함께 내궁 안을 들쑤실 때마다 한숨을 푹푹 내쉬던 어느 젊은 여인을 떠올렸다.

‘많이 늙었군.’

당연한 일이다. 초절정에 이르는 무위로 노화를 늦춘 그와는 달리, 그녀는 시간의 순리(順理)를 고스란히 받아들였을 테니까.

“죄, 죄송합니다. 궁주님. 쇤네가 몸이 성치 않은 탓에…….”

감히 고개도 들지 못하고 굽실거리는 노파의 모습에, 백상은 문득 의문이 들었다.

자신은 왜 수하들을 만류한 것일까.

저 노파가 그의 옛 모습을 기억하는 몇 안 되는 사람이어서?

그것이 아니라면…….

지금 이 순간에도 시시각각 다가오고 있을 ‘그 순간’을 늦추고 싶다는 마음 때문에?

‘모를 일이군. 모를 일이야.’

씁쓸했다. 여기까지 왔음에도 마음 한구석에 후회가 남아 있다는 것이.

그리고 거리낌 없이 자신을 구박하던 그녀가, 이제는 두려움으로 눈조차 마주치지 못한다는 것이 그랬다.

‘그리고 이것이, 지금껏 내가 걸어온 길이겠지.’

전부 허망한 감상에 불과하다.

하나뿐인 의형(義兄)과 함께 전장에서 등을 맞대며 싸우고, 적들의 시체를 깔고 앉아 과실주를 나누어 마시고, 어스름한 달빛 아래에서 만나는 두 남녀를 몰래 지켜보던 날들은 이미 오래전에 지났으니까.

“……주군?”

조심스러운 호위의 부름에, 백상의 눈동자가 평소처럼 차갑게 가라앉았다.

“길을 터라.”

“존명.”

기다렸다는 듯이 앞으로 나선 호위들이 거칠게 노파를 밀어 낸다.

겁에 질린 눈빛으로 더욱 바짝 엎드린 사람들을 굽어보던 백상이 말을 이었다.

“또한. 지금 이 시간 부로 내궁에 머무르는 궁인(宮人)들을 추방한다.”

“소, 송구합니다만, 궁인들 전부를 말씀이십니까?”

“그래. 전부.”

궁인은 말 그대로 궁에 머무르며 온갖 잡일을 하는 이들이다. 매 끼니 식사를 준비하는 숙수부터 청소와 빨래를 하는 이까지 전부 궁인이었다.

가혹한 추방령은 둘째치고, 크고 작은 부분을 담당하던 그들이 없어진다면 당장 내궁이 제대로 돌아가지 않을 터.

도대체 왜, 라는 의문이 목구멍까지 솟구쳤지만 호위 중 누구도 입 밖에 내지 않았다.

백상의 말은 곧 법이니까.

그는 남만에 존재하는 유일한 대족장인 동시에, 모든 부족장의 절대적인 충성 맹세를 받아 낸 유일한 궁주다.

새로운 궁주를 부정하며 외궁을 떠난 다섯 개 부족이 모든 권한을 박탈당하고 묘족의 수뇌부마저 뇌옥에 갇힌 지금, 백상의 권위는 무소불위(無所不爲)였다.

“……존명.”

갑작스러운 추방령에 의문을 품긴 했지만, 호위들은 자신의 본분에 따라 명령을 받들었다.

그리고 노파를 시작으로 얼굴이 새하얗게 질린 궁인들이 줄지어 끌려 나가는 모습을 지켜보던 백상은 내심 중얼거렸다.

‘어쩌면 이곳을 떠나는 것이, 그대들에게는 자비가 될 수도 있겠지.’

이제 곧 모든 것이 시작되고, 끝났다.

그 과정에서 얼마나 많은 피가 흐를지, 백상 자신조차 알 수 없었다.

‘아니. 짐작하면서도 믿고 싶지 않았다.’

그래서일지도 모른다. 지난 사십여 년간 오직 한 가지 목표를 위해 철인(鐵人)으로 살았음에도, 지난 한 달간 그 어느 때보다 흔들렸던 것은.

‘변덕. 결국 쓸모없는 변덕이었어.’

야율척. 그리고 진태경.

뇌리를 스치는 두 사람의 이름과 함께, 백상은 멈췄던 걸음을 옮겼다.

저벅. 저벅.

한 걸음. 또 한 걸음.

보보(步步)마다 수많은 생각이 스쳐 지나간다.

사라진 야율척과 진태경은 어찌 되었을까. 지금쯤 어디에서 무엇을 하고 있을까.

남천마후는 그 누구도 모르게 자신이 했던 일을, 마지막 변덕을 알고 있을까?

‘하지만 늦었다. 이제는 그 누구도 돌이킬 수 없어.’

백상은 공허한 뇌까림과 함께 걸음을 멈췄다. 어느새 그의 앞에는 단 하나의 문만이 남아 있을 뿐이었다.

이제 이 문을 열면, 내궁에서 가장 높은 단상이 그를 기다리고 있을 것이다.

그리고 그 아래에는…… 총소집령에 응하여 내궁에 집결한 일만의 전사들이 있겠지.



‘정오. 내일 정오야. 궁에 있는 모든 전사를 모이게 해.’



확실하다. 대계는 이미 완성되었다.

지난밤에 전해진 남천마후의 전언(傳言)을 떠올리며, 백상은 문득 입을 열었다.

“햇볕이 뜨겁구나.”

“……주군?”

문은 열리지도 않았건만, 백상은 자신을 불태울 듯한 열기를 느끼고 있었다.

지금부터 그가 하려는 것은, 용서받을 수도 없고 받아서도 안 되는 끔찍한 죄악이다.

하지만…….

‘이제 어쩔 수 없구나, 휘(輝)아야.’

그리운 아들을 떠올리며, 아버지는 힘차게 문을 열어젖혔다. 탁 트인 시야와 허공이 보이고, 그 아래 결집한 수많은 전사가 보인다.

하지만 백상은 시선은, 그의 모든 감각은 한 곳을 향하고 있었다.

일만에 달하는 전사들의 머리 위, 내궁을 둘러싼 담과 외궁을 방비하는 성벽 너머로 보이는 초록빛 언덕에.

‘저건.’

아득하게 먼 거리였지만, 백상의 눈에는 보였다.

높은 언덕 위에 우뚝 선 한 마리의 거대한 백호가. 정오의 햇빛을 받아 빛나는 은빛 갈기와 그 위에 앉아 있는 또 다른 누군가가.

“……왔구나. 기어코.”

나직한 음성과 함께, 백호의 등 뒤로 수천, 수만 마리에 달하는 짐승들이 모습을 드러냈다.
```

## Final English reading copy

```markdown
# Chapter 694

Deep in the night, with even the moon hidden.

In a mountain valley sunk in thick darkness, faint flames began to bloom.

One, two, three. Then, along with the hundreds of torches that soon multiplied, the world began to shake.

Rumble, rumble, rumble!

Tremors traveled through the ground. Beneath the torches swaying in the wind, large and small shadows shifted as rough breaths poured forth without pause.

Growl.

Hoo. Hoo.

An army.

It was a single army made up of countless humans and beasts mingled together.

The Nanman warriors, armed with swords, spears, and bows, sat atop their saddles and ceaselessly probed the darkness with their eyes, while beasts of prey with sharp teeth and claws continued to charge forward.

Their number was no less than three thousand.

And following the command of a single man, their destination had been decided from the moment they left the Outer Palace around noon.

* Ailao Mountain. *

The three words surfaced in the mind of the Captain of the Guards charging at the front. At that same moment, someone shouted from behind him.

“We can see it!”

Just as he said.

Everyone could see it, not just the Captain of the Guards. A massive, blazing inferno unlike anything produced by the torches carried by the three-thousand-strong army was flickering in the distance.

Crack! Whoosh!

Ancient trees of unknowable age fell in rows, while flames greedily devoured everything they touched and continued to swell in size.

A low groan escaped between the lips of the warriors watching a conflagration such as the world had seen neither in the past hundred years nor perhaps in the hundred years to come.

“I—I don’t believe this.”

“So it was true. It was really true….”

Hearing something from someone else was different from seeing it with your own eyes.

Shock and fear flickered through the eyes of the warriors as they gazed at Ailao Mountain engulfed in flames.

*Jin Taekyung.*

*Every rumor about him was true.*

*He shook off that many pursuit parties and made it all the way here. Just what kind of monster is he?*

Naturally, most of the warriors present had never encountered Jin Taekyung themselves.

No—it would be more accurate to say that they had never witnessed his true nature.

To them, Jin Taekyung had been nothing more than a young man from the Central Plains, an outsider with a strange appearance that differed slightly from that of the Nanman people.

But now, they had to fight him.

Their mission was to seal off Ailao Mountain without a single gap and kill Jin Taekyung, who could come bursting out at any moment.

But…

*Can we stop him? That monster?*

One question rose in everyone’s mind.

They had spent their entire lives hearing endless stories about Ailao Mountain, a forbidden land whose history began alongside the Nanman Beast Palace.

And whenever those stories were told, three words always appeared without fail.

The Fire Gate Clan.

An unknown clan said to exist somewhere in the distant Central Plains.

In the distant past, it was said that the Sect Leader of the Fire Gate Clan came to this land and brought the Great War with the Five Poisons Sect to an end—a war that had continued for more than a century even after the founding of the Nanman Beast Palace.

The Five Poisons Sect’s deadly poison, which had claimed countless lives, and the venomous beasts they commanded had melted like candle wax before the flames he summoned.

It was even said that the Sect Leader of the Five Poisons Sect at the time—who had reduced one hundred of the Nanman Beast Palace’s finest warriors to a mere puddle of poisonous water—could not withstand his power and fell to his knees.

*No. They said he was burned alive.*

And now, the old legend they had all enjoyed hearing as children had crossed over from the past and arrived in the present.

Right before their eyes.

Gulp.

The sound of someone swallowing dryly rang out with unusual clarity. Hands that had been loosely holding the reins now tightened with all their strength, and unease spread alongside their restlessly shifting eyes.

Then, in the very next moment, the Captain of the Guards finally opened his tightly closed lips.

“What are you so afraid of?”

“……!”

His voice, infused with internal energy, pierced the warriors’ ears. The Captain of the Guards continued emphatically.

“He is alone. We are three thousand.”

The warriors’ shoulders, which had unconsciously hunched, slowly straightened. Their wavering gazes began to regain their focus one by one.

*That’s right. No matter how strong he is, he is still a human made of flesh and blood.*

*Even if every rumor we’ve heard about Jin Taekyung is true, he can’t withstand this army.*

Three thousand.

Three thousand, no less. As a number meant to kill a single person, it was more than enough—absurdly excessive.

The Sect Leader of the Fire Gate Clan, who had supposedly crushed the Five Poisons Sect through overwhelming martial might?

When they remembered the stories they had grown up hearing, it was true that they felt afraid. But in the end, a legend was only a legend.

No—even if he came back to life, it was impossible for him to face three thousand Nanman warriors and beasts of prey alone.

It had to be impossible.

“Have you forgotten? Jin Taekyung is a traitor who endangered Nanman, a Han Chinese man no better than an animal who has forgotten the debt he owes for the Great Faction War.”

As the massive inferno drew nearer, the Captain of the Guards put even more force into his voice.

Shing.

“Warriors of Nanman! My proud brothers!”

The sword drawn from his waist gave off a sharp edge.

Moonlight pouring down from overhead and the flickering torchlight struck the snow-white blade and shattered across it.

“Pursue and kill him!”

“Waaaaaah!”

Clang, clang, clang!

Hundreds and thousands of weapons were drawn at once, along with the fiercely burning torches. And just as the army of nearly three thousand warriors drove their mounts toward Ailao Mountain with a distant, thunderous roar—

Whoosh!

The Captain of the Guards, along with every human and beast in this place, saw it.

A pillar of light rising through the blood-red inferno, and a black hill casting a shadow before the searing flames.

No. That was not a hill.

Rumble, rumble, rumble!

“What in the world is that…!”

As the world shook alongside the rapidly approaching black hill, the Captain of the Guards stared wide-eyed at the sight.

He did not know that he could no longer feel the wind.

He did not know that the three thousand beasts charging relentlessly toward Ailao Mountain had stopped in place as though by prior agreement.

Growl.

The tiger that had been with the Captain of the Guards his entire life lowered its head with a low growl.

No. It was not the only one.

The leopard, the bear, and the wolf. Every beast of prey, large and small, did the same.

Ssssh.

They curled their tails and lowered their massive bodies to the ground.

It was instinct etched into them from the moment of birth. It was worship toward a king who had returned after traversing the long years. And it was an irresistible command.

—Kraaaaar!

Along with a roar that devoured the world, blue-white eyes shone in the darkness.

* * *

Step. Step.

Soft footsteps echoed through the silent corridor.

At the sharp gazes of the escort warriors, each of whom had reached the Peak, the maids and servants fell facedown in prostration, followed by trembling cries.

“W-We pay our respects to the Palace Lord!”

Their fearful cries were directed toward only one person.

As Baeksang crossed the Inner Palace corridor under an impregnable guard, his gaze swept over them.

Those who worked in the Inner Palace varied in tribe and age.

There were children whose baby fat had not yet disappeared, middle-aged men and women, and…

An old woman whose hair had gone completely white.

The old woman was so aged that her movements were sluggish, and the guards frowned when they saw her floundering alone in the middle of the corridor.

Baeksang, whom they served with all their loyalty, was the master of the Nanman Beast Palace and the king of this land.

No—he had to be.

An old woman merely waiting for the day of her death could not block his path.

Step.

And just as though they had planned it, two of the guards took a step toward the old woman.

“Stop.”

At the low voice, the guards abruptly halted.

Looking toward the old woman who had entered his line of sight, Baeksang offered a greeting she could not hear.

*It has been a long time.*

Despite the long years that had passed, her face was familiar.

Baeksang remembered a young woman who used to sigh deeply whenever he and Yayul Cheok tore through the Inner Palace during their childhood.

*You’ve grown old.*

It was only natural. Unlike him, who had slowed his aging through martial might that had reached the Supreme Peak, she must have accepted the natural order of time in its entirety.

“I—I’m sorry, my lord. This old woman’s body is not what it used to be….”

At the sight of the old woman bowing and groveling without even daring to raise her head, Baeksang suddenly wondered.

Why had he stopped his subordinates?

Was it because she was one of the few people who remembered what he had been like in the past?

If not…

Was it because he wanted to delay *that moment*, which was drawing closer with every passing second even now?

*I don’t know. I truly don’t.*

It was bitter.

Even after coming this far, regret still remained in one corner of his heart.

And so did the fact that the woman who had once scolded him without restraint could no longer even meet his eyes out of fear.

*And this is the path I have walked all this time, I suppose.*

It was all nothing more than empty sentiment.

The days when he had fought back-to-back with his only sworn elder brother on the battlefield, sat atop the corpses of their enemies and shared fruit wine, and secretly watched a man and woman meet beneath the dim moonlight had long since passed.

“…My lord?”

At the escort’s cautious call, Baeksang’s eyes sank into their usual coldness.

“Clear the way.”

“Yes, my lord.”

As though they had been waiting for the order, the guards stepped forward and roughly shoved the old woman aside.

Baeksang looked down at the people who bowed even lower with terror in their eyes, then continued.

“Also. Effective immediately, all palace attendants residing in the Inner Palace are to be expelled.”

“I—I beg your pardon, my lord, but do you mean all the palace attendants?”

“Yes. All of them.”

Palace attendants were, as the name suggested, people who stayed in the palace and handled all kinds of menial work. They included everyone from the kitchen cooks who prepared every meal to those who cleaned and washed the laundry.

Leaving aside the harshness of the expulsion order, the Inner Palace would not function properly if the people responsible for its countless large and small duties disappeared at once.

The question of *why* rose all the way to their throats, but not one of the guards voiced it.

Baeksang’s word was law.

He was both the only Great Chieftain in all Nanman and the only Palace Lord to have received an absolute oath of loyalty from every tribal chieftain.

The five tribes that had left the Outer Palace in rejection of the new Palace Lord had now been stripped of every authority, and even the Miao leadership was imprisoned in the underground prison.

Baeksang’s authority was absolute.

“…Yes, my lord.”

Though the guards wondered at the sudden expulsion order, they obeyed it according to their duty.

Baeksang watched as the palace attendants, beginning with the old woman, were dragged out in a line, their faces drained of color. Then he muttered inwardly.

*Perhaps leaving this place will be a mercy to you.*

Soon, everything would begin.

And end.

Even Baeksang himself did not know how much blood would flow in the process.

*No. I could guess. I simply didn’t want to believe it.*

Perhaps that was why he had been shaken more over the past month than ever before, despite having lived as an iron man for more than forty years for the sake of a single goal.

*Caprice. In the end, it was nothing but a useless caprice.*

Yayul Cheok.

And Jin Taekyung.

Along with the names that flashed through his mind, Baeksang resumed his halted steps.

Step. Step.

One step. Then another.

Countless thoughts passed through his mind with every step.

What had happened to Yayul Cheok and Jin Taekyung after disappearing? Where were they, and what were they doing now?

Did the Southern Heaven Demon Empress know what he had done without anyone’s knowledge—his final act of caprice?

*But it is too late. No one can turn back now.*

Along with that hollow mutter, Baeksang stopped walking.

Before him, there was now only a single door.

Once he opened it, the highest dais in the Inner Palace would be waiting for him.

And below it…

Ten thousand warriors who had gathered in the Inner Palace in response to the general mobilization order.

*Noon. Tomorrow at noon. Gather every warrior in the palace.*

It was certain.

The grand plan had already been completed.

Remembering the Southern Heaven Demon Empress’s message delivered the previous night, Baeksang suddenly opened his mouth.

“The sunlight is hot.”

“…My lord?”

The door had not even opened, yet Baeksang felt heat that seemed capable of burning him alive.

What he was about to do was a terrible sin that could never be forgiven—and should never be forgiven.

But…

*There is no other way now, Hwi-ah.*

Thinking of his beloved son, the father threw open the door with force.

An unobstructed view and open sky appeared before him, along with the countless warriors gathered below.

But Baeksang’s gaze—all of his senses—was directed toward a single place.

Toward the green hill visible beyond the heads of the ten thousand warriors, beyond the walls surrounding the Inner Palace and the fortress walls defending the Outer Palace.

*That is….*

Though it was an immeasurably distant place, Baeksang could see it.

A massive White Tiger standing tall atop a high hill.

Its silver mane shone beneath the noonday sunlight, and another figure was sitting atop its back.

“…You came. In the end.”

At his quiet words, thousands—perhaps even tens of thousands—of beasts appeared behind the White Tiger.
```
