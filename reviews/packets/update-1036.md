<!-- packet-manifest
{
  "included": [
    {
      "path": "source/1036.txt",
      "sha256": "4ae3e333cb8893d4c27da42cf2db1f23d24430a2d76eb5ce08ee656303e76b3c",
      "bytes": 13297
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "54f7150b108df4ef6714a82089b29b5849e43ed8efac66920b3c494039490f96",
      "bytes": 1501
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "383045aaa550afcd5ef9913b67eee36e7dfcbd478f5edeb7be10bfbb7930e01e",
      "bytes": 240741
    },
    {
      "path": "characters/Blood-Sword Demon Lord.md",
      "sha256": "38a8de9285952cbeaba6c14613d270d2368dd36460840f11b13b3391c801df79",
      "bytes": 914
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "5f21ab6af9afb39805cd6abad26d3c0c7d8b793a65581e7f6bc02533fc134f45",
      "bytes": 760
    },
    {
      "path": "characters/Jeok Cheongang.md",
      "sha256": "d2a7d451db7ffe3668371482863bb58a2a65a44f0e285c5ac113912b70c0a94b",
      "bytes": 1502
    },
    {
      "path": "characters/Taishan.md",
      "sha256": "58786e5c94a85be5c96edf0ef99b9e6480aca459f4412379dbc3ccfc11dd2cc3",
      "bytes": 686
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "9fcdc873075b9cb2d4039976a1b6c6915530d22e136ba779219b7eb6f324ba96",
      "bytes": 279401
    }
  ],
  "estimated_tokens": 9937
}
-->

# Durable State Update — Chapter 1036

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
1 and safe_through 1036. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 1036. Profile updates may replace only one
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
  "chapter": 1036,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 1036,
    "continuity_sources": [1036],
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
    "The Blood-Sword Demon Lord serves the Lord of Heaven and commands the invading army.",
    "The Blood-Sword Demon Lord commands more than thirty thousand soldiers and seven Black Ghosts.",
    "Four Black Ghosts, former Demonic Cult fiends who once shared a faction with the Blood-Sword Demon Lord, were destroyed by Heavenly Strike.",
    "Jeok Cheongang and Jin Taekyung are fighting on the battlefield.",
    "Roughly twenty white-robed followers take orders from the Lord of Heaven through an unnamed woman who served him more closely than the Blood-Sword Demon Lord.",
    "The Blood-Sword Demon Lord believes the Lord of Heaven distrusts him and is resolved to prove himself.",
    "The Blood-Sword Demon Lord is Chuk Banghyeol; Qi Sense showed his level rising from 170 to 180 as he approached.",
    "A white-robed figure invoked the Wind Ghost’s power and imbued the Blood-Sword Demon Lord with it; Taekyung identified this power as Magic."
  ],
  "continuity_sources": [
    1034,
    1035
  ],
  "open_questions": [
    "What are the identity and purpose of the Lord of Heaven?",
    "Did Dark Heaven cause the Great Faction War?",
    "Who is the unnamed white-robed woman, and what is the white-robed followers’ purpose?",
    "How do the white-robed followers’ Magic and the Wind Ghost’s power work?",
    "How were the former Demonic Cult fiends made into Black Ghosts?"
  ],
  "safe_through": 1035,
  "temporary_decisions": [],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 적천강    | **Jeok Cheongang** |
| 암천     | **Dark Heaven**                  |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 단전     | **dantian**                                      | Preserve the wuxia term                               |
| 깨달음    | **enlightenment** / **insight**                  | Martial enlightenment                                 |
| 검기     | **Sword Energy**                                 | When functioning as projected weapon qi               |
| 일격     | **One Strike**                         |
| 시스템              | **System**                     |
| 레벨               | **Level**                      |
| 몬스터     | **monster**           |
| 마법사     | **mage**              |
| 하남     | **Henan**              |
| 사천     | **Sichuan**            |
| 귀가      | **your family**                                                 |
| 혈검마군 | **Blood-Sword Demon Lord** | Antagonist commanding the army advancing on the Great Snow Mountain. |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 태산 | **Taishan** | Sama Pyo's giant subordinate. |
| 남만 | **Nanman** | Historical regional term used for the source of the imported ebony. |
| 백염 | **White Flame** | Name of Jin Taekyung's newly forged spear. |
| 아귀 | **A-Gwi** | Legendary Dogon from Sichuan. |
| 마도 | **Demonic Path** | Term raised for martial power that appears to defy common principles. |
| 화룡 | **fire dragon** | Fire-dragon image within Taekyung's dantian that awakens before the duel. |
| 호북 | **Hubei** | Province on Ju Gongsan's route from Guangdong to Henan. |
| 강기 | **Force** | Generic manifestation of concentrated martial energy; distinct from Sword Force. |
| 마군 | **Demon Lord** | Shortened title used for the Western Heaven Demon Lord. |
| 이동진 | **Moving Formation** | Dark Heaven's inactive long-distance transportation formation. |
| 중단전 | **Middle Dantian** | Martial energy center opened by Jin during the battle. |
| 의지 | **Will** | System attribute that replaces Endurance after its dramatic increase. |
| 외공 | **external arts** | Martial arts focused on extreme bodily training. |
| 무한 | **Wuhan** | Capital of Hubei Province near Dongting Lake. |
| 수신룡 | **Water God Dragon** | Legendary name for the true master of Dongting Lake; distinct from the modern Sea Serpent. |
| 마법 | **Magic** | Taekyung's explanation for Dark Heaven's anomalous abilities. |
| 혈어 | **Blood Fish** | Local name for the aggressive mutated fish in the Gate's waterways. |
| 신룡 | **Divine Dragon** | Title used when discussing the Water God Dragon's intentions. |
| 도산검림 | **a mountain of sabers and a forest of swords** | Idiom describing the lethal life of martial artists. |
| 인벤토리 | **Inventory** | System storage summoned by Jin. |
| 검마 | **Sword Demon** | A Demonic Cult swordsman whose final technique is compared with One Annihilation. |
| 균열 | **rift** | The dark rift opening in the cliff behind the Inner Palace. |
| 흑귀 | **Black Ghost** | The Blood-Sword Demon Lord’s name for the Death Knights. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 적천강 | 신의 | senior_martial_master_to_physician | Divine Physician | blunt and familiar | Uses 신의 while recognizing Dong Feng’s medical identity. |
| 신의 | 적천강 | physician_to_legendary_martial_master | Sir Jeok | formal-deferential | Uses 적 대협 while thanking and counseling Jeok. |
| 적천강 | 수신룡 | legendary_martial_master_to_dying_spirit_beast | you | wary and trembling | Jeok asks what the Water God Dragon is after witnessing its mental communication. |
| 태산 | 적천강 | subordinate of a Young Sect Leader to legendary elder | Fire King | clipped, childlike, and deferential | Taishan gives his awkward greeting and expresses admiration for Jeok's strength. |
| 적천강 | 태산 | legendary elder to giant subordinate | you / strange fellow | blunt, startled, and grudgingly tolerant | Jeok addresses Taishan as 네놈 while reacting to his greeting and appetite. |
| 신의 | 태산 | senior physician to younger ally | Young Hero Taishan | urgent and respectful | The Divine Physician uses this address while pleading with Taishan to keep moving. |
| 혈검마군 | 적천강 | former opposing martial masters | Senior Jeok | respectful and familiar | Addresses Jeok as 선배 while teasing him. |
| 적천강 | 혈검마군 | former opposing martial masters | you; you bastard | blunt and hostile | Uses 너 and 네놈 while confronting him. |

## Listed compact profiles

### Blood-Sword Demon Lord.md

# Blood-Sword Demon Lord (혈검마군)

- **Safe through:** Chapter 1035
- **Aliases:** None
- **Role:** The Blood-Sword Demon Lord is a formidable martial master who commands the force advancing on the Great Snow Mountain and now serves the Lord of Heaven.
- **Personality:** Devoted to his master and proud of his abilities, he is deeply wounded by perceived distrust and resolves to prove his worth.
- **Voice:** Casually familiar and self-amused, addressing Jeok Cheongang respectfully as Senior while trading blunt insults; his easy laughter can turn to a low, cold intensity.
- **Relationships:** He serves the Lord of Heaven with deep devotion but believes his master does not fully trust him; he has been ordered not to kill Jin Taekyung, admires Jeok Cheongang, and once shared the Demonic Cult with the fiends who became Black Ghosts.

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 1035
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** He is devoted to medicine and the lives he could not save, yet remains composed and self-effacing under mortal danger.
- **Voice:** He speaks in calm, respectful, self-effacing language, framing mortality through quiet philosophical reflections.
- **Relationships:** Mungyeong is the Divine Physician's true identity, the Slaughter Saint was his Master, and Dong Feng is his Disciple.

### Jeok Cheongang.md

# Jeok Cheongang (적천강)

- **Safe through:** Chapter 1035
- **Aliases:** Fire King; eighteenth Sect Leader of the Fire Gate Clan
- **Role:** Jeok Cheongang is the Fire Gate Clan’s current Sect Leader, a legendary martial master who has surpassed the Three Saints, Jin Taekyung’s Master and intended heir’s mentor, and a trusted confidant who occupies the chief seat of the Murim Alliance’s Five Kings Hall.
- **Personality:** Secretive, sharp-eyed, gruff, dryly teasing, and pathologically afraid of water; he distrusts process-first excuses when outcomes fail and hopes to make good choices while protecting those he still has.
- **Voice:** Sharp and ringing when calling out; otherwise gruff, dryly teasing, blunt, and threatening during interrogation or confrontation.
- **Relationships:** He considers Jin Taekyung his one and only Disciple and trusted confidant, and insists on protecting Taekyung while urging him not to risk his life; he warmly regards Ju Hwaran, sees Mae Jonghak as a kindred spirit, recognizes Cheongpung as Mae's grandson and successor, was close to Hong Dao, accepted Jangcheon as a Disciple before he became Jopil, and was Peng Cheolhu’s longtime rival and friend until Peng’s death, when they parted reconciled as brothers in all but blood; he once fought alongside Murong Baek, now his enemy, and personally killed his former ally the Junzi Saber after that man joined the Demonic Cult.

### Taishan.md

# Taishan (태산)

- **Safe through:** Chapter 1031
- **Aliases:** Tiger Giant Child
- **Role:** Taishan is a giant subordinate of Sama Pyo in the Black Dragon Demon Gate and a member of the Fire Dragon Pavilion.
- **Personality:** Childlike, obedient, food-obsessed, and dim-witted, with intense wariness toward strangers and absolute trust in Sama Pyo; becomes explosively violent when his meat is threatened.
- **Voice:** Clipped, simple, and childlike.
- **Relationships:** He serves Sama Pyo, whom he calls Lord, trusts Jin Taekyung as Pavilion Master, and has grown attached to the Fire Dragon Pavilion members.

## Korean source

```text
＃1036화



애초에 짐작할 수 없었던 것일까, 아니면 그만큼 믿기 힘든 현실이었기에 애써 부정하고 있던 것일까.

이번만큼은 그 의문에 대한 답을 스스로 내릴 수 있다.

나는…… 아마도 후자였던 것 같다.

‘사실이었어. 전부.’

백지처럼 새하얗게 변한 머릿속을 후려친 깨달음.

그와 동시에 마음속에 품고 있던 한 줌의 믿음이, 이곳에서의 상식이 허물어지는 것을 나는 느꼈다.

이미 하남과 사천에서 일찍이 그 존재를 드러냈던 기묘한 술법, 이동진.

호북에서 무언가에 의해 타락하여 미쳐 날뛰었던 수신룡과 수많은 혈어(血魚)들.

그런 혈어를 먹고 괴물과도 같은 모습과 힘을 갖추게 된 어느 평범하기 그지없던 어부.

그 모든 현상의 원인이자, 거기에 그치지 않고 남만의 밀림에서 또다시 모습을 드러내었던 균열(龜裂).

더불어 바로 오늘 이 자리에서 맞닥트린, 흑귀(黑鬼)라 불리는 익숙한 존재들까지.

그리고.

그리고…….

마침내 선명하게 드러났다.

지금 이 순간 보란 듯이 내 눈 앞에 펼쳐지고, 귓가를 파고들었으며, 감각을 통해 또렷하게 흘러들어온다.

지금까지의 그 모든 전조, 징조, 징후.

이중 무엇이라 불러도 상관없는 그 모든 것들이, 마침내 거대한 둑을 허물어트리고 터져 나와 나를 덮치고 있었다.

마음속으로만 만지작거리고 있던 의심을 확신으로 바꾸며.

바로, 마법(魔法)이라는 두 글자로.

스아아아.

바람이 분다. 인간의 한계를 아득히 뛰어넘어 버린 속도와 힘을 지닌 그림자가 긴 잔상을 남기며 이곳을 향해 미끄러진다.

그러나 나는 손가락 하나 까딱하지 못했다.

느려진 세상 속, 전신의 피가 차갑게 식어 버린 듯한 기분이 되어 그 광경을 멍하니 지켜볼 수밖에 없었다.

‘이건, 도대체…….’

거대한 폭탄이 터진 자리에 남은 것은 폐허와 후폭풍뿐이다.

바로 그 폐허나 다름없게 된 지금의 내 머릿속에서는 수많은 단어와 물음표가 폭발의 여파에 휩쓸려 이리저리 흩날리고 있었다.

마법, 마법사, 몬스터, 혈검마군, 버프.

대규모 공격 마법과 아군의 희생. 무수한 죽음과 사방에 흘러넘칠 핏물. 그 속에서 둥둥 떠다닐 조각난 시체들.

어찌 이런 것이 가능한가.

어떻게 이리되었는가.

그리고 마지막으로.

‘나는, 이제 어떻게 해야 하는 거지?’

모든 것이 머릿속에서 흩어지고, 정답을 찾을 수 없는 의문만이 홀로 남은 그때.

덥석.

단단하고 거친, 동시에 익숙한 누군가의 손아귀가 내 어깨에 닿았다.

아니, 닿았다고 느낀 순간 나는 이미 강한 힘에 이끌려 힘없이 뒤로 밀려 나가고 있었다.

이제야 다시 흐르기 시작하는 현실의 시간과, 그 틈새를 찢으며 벼락처럼 휘둘려진 한 줄기의 섬광을 깨달으며.

후우웅, 콰앙!

하늘이 쪼개지는 듯한 굉음과 동시에 되돌아온 감각.

어느새 등 뒤의 허공 어딘가로 붕 떠오른 나는, 전신을 사로잡은 부유감(浮游感)과 함께 들이닥친 엄청난 여파를 느낄 수 있었다.

콰드드드득!

지진이라도 난 것처럼 뒤집히는 땅거죽과 온 사방을 녹이고 부수는 두 개의 거대한 힘.

반경 수십여 장에 달하는 공간을 단숨에 집어삼킨 강대한 격돌의 중심에는, 석상처럼 굳어 있던 나를 밀어 내고 혈검마군을 막아선 적천강이 있었다.

“갈(喝)-!”

언제 이렇게 멀리 날아온 것일까.

그럼에도 심후한 공력을 실어 내지른 적천강의 외침이, 단순한 기합이 아니라는 것쯤은 알 수 있었다.

‘나를 향한 외침이야. 정신을 일깨우기 위한.’

귓가로 흘러들어와 반쯤 넋이 나가 있던 정신을 일깨운 그 일갈에, 나는 비로소 참았던 숨을 내뱉을 수 있었다.

‘그래, 아직 끝나지 않았다.’

어떻게 이런 일이 현실로 벌어질 수 있는지는 아직까지도 도무지 이해할 수 없었지만, 당장 코앞에 닥친 사선(死線)의 고비에서 그것이 무슨 상관이란 말인가.

이미 엎질러진 물 앞에서 이해라는 단어는 무소용이다.

지금 이 전장에서 내가 할 수 있는 것은 현실을 인정하고, 타개(打開)하는 것뿐이다.

그리고 그것이 곧, 모두를 살리는 길이었다.

스륵.

아직도 사라지지 않은 부유감 속에서, 나는 부드럽게 신형을 비틀었다.

앞서 한 차례의 레벨 업으로 완전히 회복된 근육과 공력은 뇌리에서 전해진 명령을 한 치의 오차도 없이 신속하게 이행했다.

‘지금.’

퍼엉, 쐐애애액!

공력이 실린 발끝으로 허공을 밟고, 이십여 장 밖에서 혈검마군과 격돌하는 적천강을 향해 폭발하듯 쏘아졌다.

아니, 정확히는 그러려고 했다.

바람을 가르며 나아가던 그때, 보이지 않는 막강한 힘이 나를 향해 들이닥치기 전까지는.

우우우웅.

공기가, 바람이 지워졌다.

그리고 그 사실을 알아차림과 동시에, 나는 저 멀리서 흐릿하게 울려 퍼지는 음성을 들을 수 있었다.

“태산(太山)이여.”

“……!”

그 나직한 음성에 담긴 뜻과 의미를 알아차린 나는 눈을 부릅떴지만, 오십여 장이나 떨어진 언덕에서 순백색의 면사(面紗) 아래로 흘러나오는 그 맑은 목소리를 막을 수는 없었다.

“떨어트리고, 짓눌러라.”

바로 그 순간.

화아아악!

태산과도 같은 거대한 중압감이 내 전신을 짓눌렀다.

아니, 추락시켰다.

내가 잠시 떠올라 있던 그 짧은 틈에 구름처럼 모여들어 창과 활을 겨누고 있던 무수한 적들 사이로.

‘중력 마법……!’

나는 입술 사이로 흘러나오려는 경악성을 삼켰다.

그리고 이 생각지도 못한 또 하나의 마법에 저항하는 대신, 고스란히 받아들여 공격의 수단으로 삼았다.

콰아아앙!

만근의 무게를 실어 내리꽂히자 지면이 갈라지고 주위의 적들이 중심을 잃으며 휘청인다. 그와 함께 나를 옥죄던 중압감도 자연스럽게 흩어지는 것이 느껴졌다.

‘그럴 수밖에.’

중력이란 특정한 개인이 아니라 공간에 적용되는 것.

허공에 머무를 때의 나는 가장 먼저 중력 마법의 영향을 받겠지만, 지면에 착지한 이후부터는 아니다.

마법사들이 분명한 저 백의인들이 조금이라도 나를 속박하기 위해서는, 아군인 암천의 교도들까지 중력 마법의 표적이 될 수밖에 없다.

결국, 이렇게라도 적천강과의 합류를 늦추겠다는 건데…….

‘그래, 못 할 것 없지.’

영혼 없는 목각인형처럼 비틀거리는 그들을 향해, 나는 제 자리에서 신형을 돌아 세우며 손에 쥔 백염을 쓸어가듯 휘둘렀다.

콰아아아!

강맹함을 넘어, 파괴적으로까지 들리는 파공성.

횡격(橫擊)은 누구나 할 수 있는 간단한 공격이지만, 백염의 투명한 창날에 실려 터져 나오는 강기의 물결은 지금 나를 포위한 적들 중 누구도 막을 수 없는 일격이었다.

그 누구도.

서걱! 콰드드득!

모든 것이 베이고, 부서진다.

병장기도, 사람도.

그러나 눈 깜짝할 사이에 반경 삼 장에 달하는 공간이 죽음의 땅으로 변모했음에도, 두려움이 제거된 그들은 캄캄한 두 눈으로 나를 직시한 채 계속해서 들이닥쳤다.

여덟 글자의 교언(敎言)을 홀린 듯이 중얼거리며.

“천상천하.”

“만마앙복.”

“천상천…….”

퍼걱!

머리가 사라진 몸뚱어리가 기울어진다. 뒤이어 휘둘려진 창날은 섬광이 되어 옆으로 다가오는 세 명의 적을 가로질렀다.

스칵!

검기(劍氣)가 맺힌 병장기도, 외공(外功)으로 단련된 신체로도 압도적인 무력 앞에서는 역부족이다.

나는 조각조각 나뉘어 흩어지는 강철과 피륙의 파편을 뚫고 망설임 없이 나아갔다.

하나의 벽처럼 앞을 가로막은 적들 사이를 벼락처럼 스쳐 지나가며 끊임없이 머릿속에서 떠올리고 명령했다.

‘인벤토리 오픈, 소환. 소환. 소환.’

서걱, 푹, 콰드득!

거침없이 베고, 찌르고, 짓뭉갰다.

손아귀에 잠시 머물렀던 병장기들은 이내 하나, 혹은 두셋의 생명을 집어삼키며 떠났고 도무지 그 크기를 짐작할 수 없는 광활한 아공간 속에는 아직도 수많은 날붙이가 숨어 있었다.

불현듯 뇌리를 스친, 어떤 말도 안 되는 상상을 현실로 만들 수 있지 않을까 싶을 만큼.

‘아니야. 가능할 리가 없어.’

하지만 어째서일까.

캉!

사방에서 짓쳐 들어오는 병장기들을 튕겨 내고.

뻐억!

사각에서 다가오는 적의 머리를 일권으로 으스러트리고.

쉬이이익, 서걱!

앞을 가로막은 적들을 베고, 또 베어 낼수록 강해져만 가는 이 알 수 없는 확신은.

‘이게 과연, 단순한 상상에 지나지 않는 걸까.’

쏴아아악!

신형을 돌려세우며 휘두른 창날의 궤적을 따라 맺히는 피안 개.

곧이어 그 죽음의 공백을 메우기 위해 온 사방에서 밀려드는 적들의 모습을 바라보며, 나는 짧게 심호흡했다.

‘결국은 모르는 거야. 직접 해보기 전까지는.’

생각해 보면 항상 그랬다.

매번 벽을 넘어서기 위해서는 그 이상을 해야 했다. 불가능을 가능으로 만들고, 상상은 현실로 뒤바꾸어야 했다.

지금 이 순간처럼.

‘인벤토리 오픈.’

숨결 한 번 내뱉을 시간. 그 정도면 충분하다.

나는 죽여도 죽여도 끊임없이 빈 자리를 채우며 앞길을 막아서는 무수한 적들을 뒤로한 채, 조용히 눈을 감고 머릿속으로 떠올렸다.

인벤토리라 불리는 그 허무한 공간 어딘가에 자리 잡은, 날카롭고 번뜩이는 강철의 동산을.

그리고 마침내, 명령했다.

‘소환.’

그건 분명 미친 짓이었다. 상상이라는 단어로만 존재할 수 있는.

하지만 그 허무맹랑하고도 간절한 부름에도, 시스템은 응답했다.

늘 변함없었던 시스템만의 방식으로.

띠링.

작지만 맑고 선명한, 한 번의 종소리.

띠링. 띠링. 띠리링.

종소리가 겹겹이 덧씌워진다. 그 미세한 물결이, 어느덧 파도가 되어 공간을 집어삼킨다.

띠리리리리링!

먹먹해지는 귓가. 상상을 현실로 이룬 첫걸음.

지금껏 들어 본 적 없을 만큼 거대하고도 장엄한 종소리를 들으며, 나는 감았던 눈을 떴다.

동시에 보았다.

스아아악.

머리 위, 보이지 않는 공간의 틈새를 비집고 나타나 어둠을 드리운 무언가를.

또한 들었다.

스르릉.

수백에 달하는 무수한 강철이 맞물리며 울려 퍼지는 서늘한 소음을.

그리고 마지막으로.

‘할 수 있다.’

느꼈다. 깨달았다.

내가 지닌 가능성이, 주어진 한계가 생각했던 것 이상으로 높고 아득하다는 것을.

조금 전 떠올렸던 그 말도 안 되는 상상을, 일부나마 현실로 뒤바꿀 힘이 내게는 있다는 것을.

화아악.

느려진 세상 속, 내 몸속 깊은 곳에서 거대한 기운이 솟구쳐 올랐다.

하단전에 똬리를 튼 화룡이 전신의 사지 백해로 흘러 들어가고, 들썩이는 심장을 따라 혈류가 빠르게 샘솟았다.

쿵. 쿵. 쿵.

거센 떨림. 가파르게 맥동하는 심장.

‘아니. 아니야.’

그래, 지금의 이 박동은 단지 심장에서 느껴지는 것이 아니다.

옥당혈(玉堂血).

무림인이라 불리는 이들이 새로이 명명하길, 중단전(中丹田).

바로 지금, 내 모든 신경과 감각은 오직 그곳에 있다.

용암이 파도치는 하단전을 지나, 하늘까지 솟구친 그 드높은 봉우리에.

힘과 속도로 재단할 수 없는 의지의 영역에.

키이이잉.

눈앞이 아득해진다. 누군가 머리를 바늘로 쑤시는 것 같은 격통이 전해졌다.

하지만 나는 무언가에 홀린 사람처럼 두 팔을 펼쳤다.

시야를 물들인 섬광 속에서, 고통보다 더욱 큰 전율을 느꼈다. 아무것도 잡혀있지 않은 텅 빈 손아귀였으나, 촉감의 영역을 벗어난 그곳에서 모든 것을 하나하나를 더듬고 부여잡았다.

하나, 둘, 셋.

열, 스물, 서른.

그리고 마침내…….

‘일백.’

나는 눈을 떴다.

영원과도 같았으나, 찰나에 불과했던 그 시간 속에서.

마치 보이지 않는 손에 붙잡힌 듯, 무수한 적들을 향해 겨누어진 일백 개의 도산검림(刀山劍林) 아래에서.

그렇게, 굳게 닫혀 있던 입술을 뗐다.

“비켜.”

솨아아아아악!

하늘이, 번뜩이는 섬광으로 뒤덮였다.
```

## Final English reading copy

```markdown
# Chapter 1036

Had I been unable to guess from the start, or had I been trying so hard to deny it because reality was that hard to believe?

This time, at least, I could answer that question for myself.

*I think it was the latter.*

*It was true. All of it.*

The realization struck my mind, now as white as a blank page.

At the same time, I felt the last shred of faith I’d held in my heart crumble, along with everything I’d thought I knew about this world.

The strange Moving Formation, whose existence had already been revealed long ago in Henan and Sichuan.

The Water God Dragon and countless Blood Fish, corrupted by something in Hubei and sent into a rampage.

An utterly ordinary fisherman who’d eaten those Blood Fish and gained monstrous strength and an equally monstrous appearance.

The cause of all those phenomena—and not just that, but the rift that had appeared once more in the jungles of Nanman.

And the familiar beings called Black Ghosts, whom I’d come face-to-face with right here today.

And.

And…

At last, everything came into focus.

In this very moment, it was laid out before my eyes for all to see. It pierced my ears and flowed clearly through my senses.

All those portents, signs, and omens that had come before.

Whatever you wanted to call them, all of them had finally burst through a colossal dam and swept over me.

Turning the suspicion I’d only toyed with in my heart into certainty.

With one word:

Magic.

Shaaah.

The wind blew. A shadow with speed and power far beyond human limits glided toward me, leaving a long afterimage.

But I couldn’t even twitch a finger.

In a world gone slow, with my whole body feeling as if the blood in it had turned cold, all I could do was stare, dumbfounded.

*What is this…?*

Where a massive bomb had exploded, nothing remained but ruins and the shock wave.

And in my mind, now little better than those ruins, words and question marks scattered in every direction in the wake of the blast.

Magic, mage, monster, Blood-Sword Demon Lord, buff.

A large-scale attack spell and the sacrifice of our allies. Countless deaths and blood overflowing in every direction. Mangled corpses floating among it all.

How could this be possible?

How had it come to this?

And finally—

*What am I supposed to do now?*

Everything scattered through my mind. I was left alone with a question I couldn’t answer.

Then—

Grab.

A hard, rough hand—familiar, too—landed on my shoulder.

No. The instant I felt it, a powerful force had already dragged me backward, sending me stumbling without strength.

Only then did I realize that time had begun flowing again—and that a streak of light had been swung like lightning through the gap.

Whoooom—KABOOM!

A roar like the sky splitting apart, and my senses returned.

Somewhere in the air behind me, I was already soaring, caught up in a weightless sensation. The enormous shock wave hit me along with it.

KRRRACK!

The earth flipped as if in an earthquake. Two immense forces melted and crushed everything around them.

At the center of that tremendous clash, which had swallowed an area dozens of *jang* across, Jeok Cheongang had shoved me aside when I froze like a statue and stepped in to stop the Blood-Sword Demon Lord.

“Gah!”

How had I flown so far?

Even so, I could tell that Jeok Cheongang’s shout, backed by his profound internal energy, wasn’t just a battle cry.

*He’s shouting at me. Trying to bring me back to my senses.*

The shout reached my ears and jolted my half-dazed mind awake. Only then could I let out the breath I’d been holding.

*Right. It’s not over yet.*

I still couldn’t understand how something like this could happen in the real world, but what did that matter when death was right in front of me?

There was no use in understanding when the water had already spilled.

Here on this battlefield, all I could do was accept reality and find a way through it.

And that was how I’d save everyone.

Slip.

Still feeling weightless, I smoothly twisted my body.

The muscles and internal energy I’d fully recovered after that last Level Up carried out the order from my mind with perfect speed and precision.

*Now.*

Boom—shwaaash!

I stepped on the air with a qi-charged foot and shot forward like an explosion, toward Jeok Cheongang, clashing with the Blood-Sword Demon Lord twenty *jang* away.

No—that was what I meant to do.

Until a tremendous invisible force came crashing down on me as I cut through the wind.

Wooooong.

The air vanished. The wind vanished.

And as soon as I realized it, I heard a voice ringing faintly from far away.

“Taishan.”

“……!”

My eyes widened as I recognized the meaning behind that quiet voice. But there was nothing I could do to stop it, coming from a hill fifty *jang* away, beneath the pure-white veil of a woman dressed in white.

“Bring him down. Crush him.”

At that very moment—

Fwooom!

A weight as immense as Taishan pressed down on my whole body.

No—it made me fall.

Down through the ranks of countless enemies, who’d gathered like clouds during the brief moment I’d been airborne and aimed their spears and bows at me.

*Gravity magic…!*

I swallowed the cry of shock that was about to slip through my lips.

And instead of resisting this unexpected spell, I let it take hold and turned it into a weapon.

KWA-BOOM!

I came crashing down with the weight of ten thousand *geun*. The ground split, and the enemies around me staggered, losing their balance. At the same time, I felt the crushing pressure around me naturally disperse.

*Of course it did.*

Gravity acted on a space, not on a specific person.

I’d been the first to feel its effects while I was airborne, but once I landed, that changed.

The white-robed figures were clearly mages. If they wanted to bind me even a little, their gravity magic would have to target the Dark Heaven followers who were their allies, too.

So they were trying to delay me from joining Jeok Cheongang, even if only for a moment…

*Fine by me.*

The enemies staggered like lifeless wooden puppets. I turned in place and swept the White Flame in my hand across them.

KWA-AAAH!

The sound of the spear cutting through the air was more than fierce—it was destructive.

A horizontal strike was a simple attack anyone could perform. But none of the enemies surrounding me could stop the wave of Force bursting from White Flame’s translucent spearhead.

Not one of them.

SHHK! KRRRACK!

Everything was cut apart and crushed.

Weapons and people alike.

In the blink of an eye, the ground within a three-*jang* radius had become a field of death. Yet the fear had been stripped from them. They stared at me with dark, unseeing eyes and kept charging.

As if bewitched, they murmured the eight words of their creed.

“Heaven above, earth below.”

“All demons bow.”

“Heaven above…”

CRUNCH!

A body without a head toppled over. The spearhead swung again, flashing sideways through three enemies approaching from the side.

SHK!

Neither a weapon imbued with Sword Energy nor a body trained in the external arts was enough against overwhelming force.

I pressed forward without hesitation, piercing through the fragments of steel and flesh that scattered around me.

I streaked like lightning between the enemies blocking my way like a wall, thinking and commanding without pause.

*Open Inventory. Summon. Summon. Summon.*

SHHK, THUNK, KRRRACK!

I cut, stabbed, and crushed without holding back.

The weapons that had rested briefly in my hands disappeared after devouring one, or two or three, lives. And countless blades still lay hidden in the vast subspace, too immense to measure.

For a moment, the thought crossed my mind that perhaps I could make some ridiculous idea real.

*No. There’s no way.*

But why?

CLANG!

I knocked away the weapons slashing at me from every direction.

THWACK!

I crushed an enemy’s head with one punch as he approached from my blind spot.

SHWEEESH—SHHK!

The more I cut down the enemies in front of me, the stronger this inexplicable certainty grew.

*Could this really be nothing more than a fantasy?*

SHWAAASH!

Blood scattered along the arc of my spear as I turned and swung it.

I took a quick breath as I watched the enemies surge in from every direction to fill the gap left by the dead.

*I don’t know until I try it myself.*

Now that I thought about it, it had always been that way.

Every time I needed to break through a wall, I had to go beyond it. I had to make the impossible possible, turn imagination into reality.

Just as I would now.

*Open Inventory.*

The time it took to exhale once. That was all I needed.

Leaving behind the countless enemies who blocked my way, endlessly filling every empty space no matter how many I killed, I quietly closed my eyes and pictured the mountain of gleaming, razor-sharp steel somewhere inside the void called the Inventory.

Then, at last, I gave the command.

*Summon.*

It was certainly insane. Something that could only exist as an idea.

But even in response to that absurd, desperate call, the System answered.

In its own familiar way.

Ding.

One small, clear chime.

Ding. Ding. Ding-ding.

The chimes piled on top of one another. Their faint ripples became a wave, and the wave swallowed the space around me.

Ding-ding-ding-ding-ding!

My ears grew muffled. This was the first step toward making imagination real.

I opened my eyes to a chime so vast and majestic I’d never heard anything like it.

And saw.

Shaaah.

Something looming over my head, forcing its way through a gap in unseen space and casting darkness below.

I also heard.

Shrring.

The cold ring of hundreds of pieces of steel sliding against one another.

And finally—

*I can do this.*

I felt it. I understood.

The possibilities within me, the limits I’d been given, were far higher and more distant than I’d imagined.

I had the power to turn that ridiculous idea I’d just pictured into reality—at least in part.

Fwoosh.

In the slowed world, an immense force surged up from deep within me.

The fire dragon coiled in my lower dantian flowed into every limb and bone. My blood surged faster, following the pounding of my heart.

Thump. Thump. Thump.

A fierce tremor. My heart pounded sharply.

*No. That’s not it.*

Right. That beat wasn’t coming from my heart alone.

The Jade Hall Acupoint.

What the people called martial artists had newly named the Middle Dantian.

At this very moment, all my senses and nerves were focused there.

Past the lower dantian, where lava rolled in waves, up to that lofty peak that reached toward the heavens.

Into a realm of Will that couldn’t be measured by strength or speed.

Kiiiiing.

My vision blurred. A sharp pain stabbed through my head, as if someone were driving a needle into it.

But as if possessed, I spread both arms.

In the flash that filled my vision, I felt a thrill greater than the pain. My hands were empty, holding nothing—but beyond the realm of touch, I traced and grasped each and every thing.

One, two, three.

Ten, twenty, thirty.

And at last…

*One hundred.*

I opened my eyes.

In that time that had felt like eternity, yet lasted no more than an instant.

Beneath a mountain of sabers and a forest of swords—a hundred blades aimed at countless enemies as if held by an invisible hand.

And then, I parted my tightly closed lips.

“Move.”

SHWAAAAASH!

The sky filled with flashes of light.
```
