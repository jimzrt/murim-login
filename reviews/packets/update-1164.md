<!-- packet-manifest
{
  "included": [
    {
      "path": "source/1164.txt",
      "sha256": "2b84a36da74fba9daad1ee71e69114b9552b0e77c7cb5e16e3de61912ecbd564",
      "bytes": 11658
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "1b1db03d90ee39d92e849b492ec2f21651446f2cb620d762efe46d677f84fb6b",
      "bytes": 944
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "509d129dd518be403e2d0bc947311136065b606cb270b6d946707428d649d01c",
      "bytes": 247760
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "eb4586fa72585ec6ac969e7e0cf51aed4e0b26a16837d8490f184218c8814117",
      "bytes": 760
    },
    {
      "path": "characters/Grand Mage.md",
      "sha256": "953afab6181d3b6e2e66007cc2c52ecb2f837139da897ab9237676538dacf503",
      "bytes": 545
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "93a112a1e0f97c5df3cacf2bac40a053987c6f67842ae33037b4ea35ca1a22da",
      "bytes": 1627
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "f50ee181586deb8e0e2e5eee193c822dd3a15efa66451e0251fd055a8eaab4d3",
      "bytes": 623
    },
    {
      "path": "characters/Morgoth.md",
      "sha256": "ec5963a21dfb033d8df75573a706c1ea2d75faf8547f5b2202413ecc8165ff16",
      "bytes": 825
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "97b900dbb29a57db84ee2adbffd58479c504d0863bf1805451d09b1ed9be91d4",
      "bytes": 294489
    }
  ],
  "estimated_tokens": 8717
}
-->

# Durable State Update — Chapter 1164

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
1 and safe_through 1164. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 1164. Profile updates may replace only one
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
  "chapter": 1164,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 1164,
    "continuity_sources": [1164],
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
    "Morgoth holds the damaged but living Skeleton King as a trophy; Jin regards the Skeleton King as a friend and fights Morgoth to protect him.",
    "Morgoth’s Guardians include seven soul-stolen S-rank Hunters presumed dead in the Black Dragon’s invasion; Pai Chen, Joel Schumacher, and Pablo Albatroses are among them.",
    "Jin survived Morgoth’s full-strength Hell Fire but is exhausted; One Against a Thousand caused many monsters to flee in fear.",
    "Morgoth’s Dragon-tooth soldiers are advancing against Jin, and a flash has appeared beyond the horizon."
  ],
  "continuity_sources": [
    1162,
    1163
  ],
  "open_questions": [
    "What caused the flash beyond the horizon?",
    "Can the soul-stolen Hunters be freed from Morgoth’s control?",
    "What will happen in the confrontation between Jin and Morgoth?"
  ],
  "safe_through": 1163,
  "temporary_decisions": [],
  "version": 1
}
```

## Exact glossary matches

| 진태경    | **Jin Taekyung**   |
| 시스템              | **System**                     |
| 몬스터     | **monster**           |
| 마법사     | **mage**              |
| 도사      | **Daoist**                                                      |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 대마도사 | **Grand Mage** | Title used for Magic Johnson. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 모르고스 | **Morgoth** | The being who answers the summoning. |
| 평화 | **Peace Guild** | Guild name. |
| 갑자 | **jiazi** | Traditional sixty-year cycle. |
| 고자 | **eunuch** | Castrated man; Hong Jin openly identifies himself by this term. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 마도 | **Demonic Path** | Term raised for martial power that appears to defy common principles. |
| 스켈레톤 | **Skeleton** | Undead monster species. |
| 메이지 | **Mage** | Skeleton subtype mentioned alongside Soldiers and Warriors. |
| 존슨 | **Johnson** | Co-host of the American talk show that replays Taekyung's viral interview. |
| 소멸 | **Erasure** | Jin's term for the Skeleton Warlord's destruction by the Arch Lich's mana. |
| 마법 | **Magic** | Taekyung's explanation for Dark Heaven's anomalous abilities. |
| 이전 | **Two Halls** | Top-level Murim Alliance organizational grouping. |
| 균열 | **rift** | The dark rift opening in the cliff behind the Inner Palace. |
| 마력 | **magical power** | Distinct from mana; the Skeleton King's area of expertise. |
| 마계 | **Demon Realm** | Realm associated with the S-rank monsters and Leviathan. |
| 육부 | **Six Ministries** | The central government ministries. |
| 적도 | **Red Blade** | Named blade that shatters in Taekyung’s flames. |
| 마법진 | **Magic Formation** | The formation that transports Ma Sanbao and his followers. |
| 드래곤 | **Dragon** | The species to which Morgoth belongs. |
| 용아병 | **Dragon-tooth soldiers** | Guardians born of Dragons and serving them. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 신의 | 진태경 | physician_to_benefactor | Young Master Jin | formal-polite | The Divine Physician addresses Taekyung as 진 공자 while expressing concern for his injuries. |
| 진태경 | 존슨 | Allied Hunter to Grand Mage | Johnson | polite and familiar | Jin repeatedly addresses Magic Johnson directly while requesting explanations and permission to visit the site. |
| 진태경 | 마법사 | rescuer assisting the operation | mage; otherwise you | polite emergency imperative | Taekyung orders the exhausted mage to request rescue under his name. |
| 존슨 | 진태경 | allied friend and comrade-in-arms | Jin | familiar and conversational | Johnson calls Jin 진 while asking what he was thinking. |
| 대마도사 | 진태경 | adversary_to_adversary | you | polite, teasing | She uses polite phrasing while taunting him and warning him not to overexert himself. |
| 진태경 | 대마도사 | adversary_to_adversary | you bitch | insulting-casual | He curses at her while refusing to give up. |
| 모르고스 | 진태경 | enemy Dragon addressing a human opponent | you | formal, measured | Uses 자네 while addressing Jin. |
| 진태경 | 모르고스 | human opponent addressing an enemy Dragon | son | casual and mocking | Calls Morgoth 아들. |

## Listed compact profiles

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 1163
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** He is devoted to medicine and the lives he could not save, yet remains composed and self-effacing under mortal danger.
- **Voice:** He speaks in calm, respectful, self-effacing language, framing mortality through quiet philosophical reflections.
- **Relationships:** Mungyeong is the Divine Physician's true identity, the Slaughter Saint was his Master, and Dong Feng is his Disciple.

### Grand Mage.md

# Grand Mage (대마도사)

- **Safe through:** Chapter 1163
- **Aliases:** None
- **Role:** Magic Johnson is the United States' Grand Mage and a War Mage, one of the two remaining masters of Magic.
- **Personality:** Strategic and ambitious, with a sharp temper when others squander opportunities or act without consulting her.
- **Voice:** He speaks casually and directly, with colloquial phrasing and occasional profanity.
- **Relationships:** He is Jin Taekyung's friend.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 1163
- **Aliases:** Blazing Flame Divine Dragon; Apostle of the Earth Mother Goddess; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan, Jeok Cheongang’s Disciple, the Fire Gate Clan’s nineteenth successor, Pavilion Master of the Fire Dragon Pavilion, a Supreme Peak master and eleventh member of the Ten Kings, a publicly recognized S-rank-level Hunter with an A-rank license, a traveler between Murim and another world, and the World Hunter Federation’s Alliance Leader; he serves as Thousand Captain of the Embroidered Uniform Guard, is enfeoffed as Prince Shangshan, and is widely regarded as a new-age savior.
- **Personality:** Hungry, self-aware, and dryly observant; pragmatic under pressure and fiercely defiant, he protects those he cherishes and is learning to face the fear of leaving them in danger without letting it paralyze him.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother and Jeok Cheongang his Master and trusted confidant; he shares deep loyalty with Hyuk Mujin, whom he values as family, and considers the Skeleton King a friend; seven S-rank Hunter comrades presumed dead are now Morgoth’s soul-stolen Guardians.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 1163
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Morgoth.md

# Morgoth (모르고스)

- **Safe through:** Chapter 1163
- **Aliases:** None
- **Role:** Morgoth is a Dragon and sovereign of a vast palace who collects powerful beings he kills or subdues as Guardians, including seven S-rank Hunters from Earth.
- **Personality:** Composed and intellectually curious, he treats powerful beings as trophies out of possessive desire and will use overwhelming force when challenged.
- **Voice:** He speaks in polished, courteous, formal phrasing, often asking measured questions while expressing condescension or fascination.
- **Relationships:** Asmodeus summoned Morgoth, though Morgoth says he is not devoted to him; Morgoth holds the Skeleton King as a trophy and commands seven soul-stolen S-rank Hunters as Guardians.

## Korean source

```text
＃1164화



그것은 거대하면서도 눈부신, 빛의 기둥이었다.

파아아앗.

일순간 모두의 시선을 빼앗을 만큼 눈부신 섬광.

그리고 아득한 허공으로부터 내리꽂힌 그것의 정체를, 모르고스는 누구보다 잘 알고 있었다.

다만, 이것이 현실로 이루어졌음을 쉽사리 이해할 수 없었을 뿐.

“어떻게?”

불현듯 입술 사이를 비집고 흘러나온 의문에, 누군가가 대답했다.

“뭘 그렇게 놀라고 그래.”

진태경.

바로 그다.

하지만 피로에 젖어 있는 목소리와 달리, 그의 입가에는 지금껏 찾아볼 수 없던 미소가 흐릿하게 맺혀 있었다.

“그냥 그러려니 하고 받아들여. 날씨도 좋은데 괜히 복잡하게 생각하지 말고.”

“……뭐?”

그 순간, 진태경이 손끝을 따라 본능적으로 고개를 든 모르고스는 그제야 잠시 간과하고 있던 중요한 사실을 깨달았다.

갈라져 있었다.

맑은 하늘과 강렬한 햇빛을 빈틈없이 가로막고 있던 먹구름이, 본래의 세상으로부터 모든 것을 분리한 그의 마력이.

또 하나의 마계(魔界)에 가까웠던 흑룡의 광대한 영토가, 어느덧 조금씩 힘을 잃고 있던 것이다.

그리고 이와 같은 균열이 일어날 수 있었던 것은, 모르고스 자신의 과욕과 소멸까지 각오한 누군가의 희생이 있었기 때문이었다.

“말했었지. 그 녀석은 전리품 따위가 아니라고.”

귓가를 파고드는 진태경의 나직한 목소리에, 모르고스는 조금 전 자신의 아공간(亞空間)으로 이동시킨 귀중한 전리품을 떠올렸다.

아니, 스켈레톤 킹을.

“그래, 정말 그럴지도 모르겠군.”

각오가 희생을 낳고, 희생은 지금과 같은 이변으로 이어졌다.

스켈레톤 킹이 목숨을 내던져 일으킨 그 거대한 힘의 폭발이, 지금의 이 상황을 만들어 낸 것이다.

그것이야말로 하찮기 그지없는 저 인간의 마법 따위가, 감히 위대한 흑룡의 권역(權域)을 침범할 수 있었던 가장 큰 이유였다.

하지만…….

“고작 저 정도의 전력으로, 무엇을 뒤바꿀 수 있지?”

조금도 흔들림 없는 음성과 함께, 모르고스는 저 멀리 펼쳐진 지평선을 바라보았다.

정확히는, 어느새 서서히 사그라들기 시작한 섬광 너머로 모습을 드러낸 일단의 무리를.

콰아아아앙!

섬광이 사라지기도 전에 터져 나온 굉음이 천지를 뒤흔든다. 

불현듯 나타나 퇴로를 가로막은 인간들을 향해 달려들던 몬스터 군단의 머리 위로, 인류 최강의 워 메이지(War Mage)가 흩뿌린 불의 비가 끝없이 쏟아져 내리고 있었다.

“이 정도 규모의 워프(Warp)와 대범위 마법이라, 제법 훌륭한걸. 며칠 전의 그 인간 마법사보다도 한 수 위야.”

제법 훌륭하다.

매직 존슨을 향한 모르고스의 평은 단지 그뿐이었으나, 그 안에는 조금의 오만함도 깃들어 있지 않았다.

드래곤은 마법을 위해 태어난, 마법 그 자체라고 해도 무방한 신비로운 생물이며 그는 그중에서도 정점에 오른 존재.

이미 성체가 되기도 전에 마법의 끝자락에 도달한 모르고스에게 있어 타 종족의 마법은 그저 어린아이의 장난에 불과했고, 이와 같은 사실은 지구라는 낯선 세상에서도 변함없었다.

그렇지 않았다면 지크프리트 바스만의 죽음 이후, 매직 존슨과 함께 단둘밖에 남지 않았던 대마도사인 멀린(Merlin)이 며칠 전의 전투에서 스스로 폭사(爆死)를 선택하진 않았을 테니까.

“눈치 빠른 인간이었지. 내가 동료들의 시신을 거두는 것을 보고 망설임 없이 죽음을 택할 정도였으니.”

대마도사는 희귀한 전리품이었기에 모르고스는 약간의 아쉬움을 느꼈지만, 이제는 아니었다.

“자네에게 감사 인사를 전해야겠군. 내게 이토록 좋은 전리품들을 선물해 줄 줄은 몰랐는걸.”

흑요석처럼 번들거리는 두 개의 눈동자에 잠시 억누르고 있던 탐욕이 깃들었다.

몬스터 군단을 분쇄하며 이곳을 향해 가까워지고 있는 수천의 인간 중, 그에게 일말의 위협이라도 될 만한 이들은 고작 두 명뿐.

하지만 그런 매직 존슨과 척 헤이글조차도 모르고스의 시선에는 한낱 전리품에 불과했고, 이미 적지 않은 피로가 누적된 진태경의 앞은 개체 하나하나가 네임드 몬스터나 다름없는 일천의 용아병이 철벽처럼 가로막고 있다.

이전과는 비교도 할 수 없을 만큼 강력한 존재로 재탄생한 일곱 명의 가디언(Guardian)도 함께.

“변하는 것은 아무것도 없네. 이 싸움은 끝났어.”

맞다.

누가 보아도 그렇게 생각할 것이다.

그만큼 모르고스에게는 압도적으로 유리한 상황이었으니까.

그런데.

분명 그럴 것인데, 어째서일까.

진태경은 여전히 웃고 있었다.

동시에 모르고스는, 열기가 일렁이는 그의 두 눈동자에 비친 누군가의 낯선 모습을 보았다.

앞서 내뱉은 말과는 달리 딱딱하게 굳어 있는 자신의 얼굴을.

“뭐가 그리도 우습지?”

참지 못하고 던진 물음에, 진태경이 지팡이처럼 짚고 있던 창을 들어 올리며 대답했다.

“그냥, 조금 기분이 좋아져서.”

“……기분이 좋아졌다고?”

“그래. 이런 상황이 꽤 자주 있었거든. 방금 네가 했던 그 말들도 여러 번 들었지.”

진태경은 입안 가득 고여 있던 가래를 탁 뱉었다.

“뭐 그런 뻔한 얘기들 있잖아. 나는 다른 누구누구와 다르다. 절대 방심하지 않는다. 반드시 죽인다. 다 끝났다. 기타 등등 잡소리.”

수없이 생사를 오갔던 그 많은 시간들.

진태경에게는 두 번 다시 떠올리기도 싫을 만큼 개 같은 기억들이었지만, 지금만큼은 달랐다.

이유?

간단했다.

“참 희한한 게, 그런 새끼들 중에 본인이 내뱉은 말을 지키는 놈은 하나도 없더라고.”

사실이었다.

그들 모두와 싸웠고, 그들 모두를 쓰러트렸다.

팔과 다리가 으스러지고, 오장육부가 뒤섞여 진탕 되고, 죽음의 끝자락에 다다르더라도 결국 살아남은 것은 그였다.

그러나 어쩌면 그토록 매번 승산 없는 전투에서 승리할 수 있었던 가장 근본적인 원인은, 진태경이 지닌 시스템이라는 이능(異能) 때문만이 아니었을지도 모른다.

“왜 그랬을까. 분명히 그중 몇몇은 정말로 날 죽일 수도 있었을 텐데, 쓸데없는 말과 행동으로 시간을 낭비하고 빈틈을 보인 걸까.”

그는 두려웠다.

늘, 언제나, 항상.

전투에 임하는, 심지어 평화로운 일상의 그 모든 순간순간조차도.

언젠가 맞닥트릴 강적에 의해 목숨을 잃는 것이 무서웠고, 누군가의 희생을 딛고 일어서야 한다는 사실에 괴로웠다.

그렇기에 언제나 상대를 만나면 욕설을 퍼부었다.

온갖 모욕을 준 뒤, 마음속 깊은 곳에 잠들어 있던 한 조각의 분노와 슬픔마저 끌어 올려 두려움이라는 감정을 뒤덮었다.

그렇게라도 강해져야 했으니까.

사람들은 그를 영웅이라 불렀지만, 그가 알고 있는 자신은 그 무거운 짐을 감당하기에 너무나도 나약했으니까.

그러나 돌이켜 생각해 보면, 눈앞의 상대에게 두려움을 느낀 것은 비단 그 혼자만이 아니었다.

“그러다가 갑자기 기분이 좋아졌지.”

진태경은 뒤늦게나마 깨달았다.

“내가 지금껏 쓰러트린 놈들도, 나를 두려워했다는 걸 알게 됐거든.”

“……!”

“그놈들이 지껄인 말들도 결국 모두 두려움에서 비롯되었던 거였어. 바로 지금의 너처럼.”

일순간 차갑게 굳은 모르고스의 얼굴을 바라보며, 진태경이 희미하게 웃었다.

“왜, 정곡을 찔렀나?”

모르고스는 대답하지 않았다.

아니, 대답할 수 없었다.

진태경의 말은 모두 사실이었으니까.

스스로를 부정하기에는, 그가 지닌 긍지와 통찰력이 너무나도 드높았으니까.

“……두려움이라.”

잊고 있었다.

정확히는 지금껏 단 한 번 느껴 보았던, 그 나약하기 짝이 없는 감정을 잊고자 애썼다.

하지만 모르고스는 마침내 인정할 수밖에 없었다.

자신이 진태경에게 품고 있는 감정은, 경계심 그 이상이라는 것을.

“그래, 그랬군. 나 역시 조금이나마 자네를 두려워하고 있었던 거야.”

비록 서로에게 느끼는 감정의 크기는 다를지언정, 그 감정이 지닌 본질은 같은 것.

낮은 목소리로 뇌까린 모르고스는 감히 자신에게 두려움을 품게 만든 자그마한 인간을 바라보았다.

동시에, 자신이 해야 할 일을 깨달았다.

“그러나 한 가지는 맹세하지.”

우우웅.

바람이 멎는다. 주위의 공기가 부르르 떨렸다.

“나는, 지금껏 자네가 상대한 그 누구와도 다를 거라는 것.”

그 순간.

슈화악!

돌연 모르고스의 전신을 휘감으며 터져 나온 어둠이 부풀어 올랐다. 

이제는 흔적도 없이 무너진 첨탑(尖塔)만큼이나 높고, 성벽만큼이나 거대하게.

그리고 지금 눈앞에 펼쳐지고 있는 현상이 무엇을 의미하는지, 진태경은 본능적으로 알아차릴 수 있었다.

‘폴리모프(Polymorph).’

어느 날 태양이 흔적도 소멸한다면 이런 광경일까.

마침내 인간의 거죽을 벗어던진 흑룡과 그를 둘러싼 어둠이 머리 위를, 반경 수백 미터의 전장을 검게 물들인다.

마치 이 세상의 종말을 고하는 것처럼.

하지만 그 모든 것을 지켜보는 진태경의 눈동자는 조금도 흔들리지 않았다.

어느덧 주어진 임무를 끝마친 어둠이 서서히 흩어지고, 주인의 명령을 받든 일천의 용아병이 자신을 향해 쇄도하고 있음에도.

‘온다. 반드시.’

그는 알고 있었다.

빛이 있으면 어둠 또한 존재하듯이, 이 어둠 뒤에는 새로운 빛이 기다리고 있음을.

그리고 그 믿음은, 보답받았다.

과거의 어느 날, 진태경이 목 놓아 구원을 청하던 누군가의 목소리에 응답했듯이.

파아아앗!

일순간, 세상이 밝아졌다.

이미 꺼진 모닥불처럼 어둠에 잠겨 가던 지평선이, 더욱 짙은 어둠에 잠식당해 가던 대지가 환하게 물들었다.

수십, 수백 줄기의 빛 기둥으로.

수천, 수만 킬로미터의 거리를 몇 번이고 뛰어넘어 부름에 답한 그들의 마음으로.

-……이게 무슨.

무수한 워프 마법진으로 인해 불길처럼 타오르는 지평선. 

아득한 허공 위에서 천둥처럼 울려 퍼지는 모르고스의 신음에, 진태경이 입을 열었다.

“나도 한 가지 맹세하지.”

나직한 목소리가 바람에 실려 나아간다.

앞으로 내디딘 발걸음과, 코앞까지 닥친 적들을 향해 곧추세워진 창날도 함께.

“너 역시도, 그놈들과 똑같아질 거야.”

화르륵, 서걱!

여명(黎明)이 되어 전장을 밝히는 맹렬한 화염과 함께, 지평선을 따라 내달린 거대한 함성이 전장을 뒤흔들었다.
```

## Final English reading copy

```markdown
# Chapter 1164

It was a pillar of light, vast and dazzling.

*Fwoooosh.*

A flash so brilliant it seized everyone’s attention in an instant.

And Morgoth knew better than anyone what had descended from the distant sky.

He simply couldn’t understand how it had become reality.

“How?”

Someone answered the question that slipped between his lips.

“Why are you so surprised?”

Jin Taekyung.

It was him.

Despite the exhaustion in his voice, a faint smile—one that hadn’t been there before—rested on his lips.

“Just accept it and move on. The weather’s nice. Don’t overthink it.”

“……What?”

Following the direction Jin Taekyung was pointing, Morgoth instinctively raised his head. Only then did he realize he’d overlooked something important.

It had split apart.

The dark clouds that had completely blocked out the clear sky and bright sunlight—his magical power, which had cut everything off from the world as it was.

The Black Dragon’s vast territory, once close to another Demon Realm, had begun to lose its power.

And this rift had opened because of Morgoth’s own greed, and the sacrifice of someone willing to face even Erasure.

“I told you. He wasn’t some trophy.”

At Jin Taekyung’s low voice, which seemed to bore into his ears, Morgoth remembered the precious trophy he had just moved to his subspace.

No. The Skeleton King.

“Yes. Perhaps he wasn’t.”

Resolve had brought about sacrifice, and sacrifice had led to an upheaval like this.

The Skeleton King had risked his life to unleash a tremendous explosion of power. That was what had created the situation before them.

It was the greatest reason that this utterly insignificant human’s Magic could dare to encroach on the domain of the great Black Dragon.

But……

“What can that small force possibly change?”

His voice not wavering in the least, Morgoth looked toward the distant horizon.

More precisely, at the group coming into view beyond the flash, which was already beginning to fade.

*BOOM!*

Before the light had even vanished, a thunderous boom shook heaven and earth.

Above the heads of the monster army charging the humans who had suddenly appeared and blocked their retreat, an endless rain of fire poured down, scattered by humanity’s strongest War Mage.

“A Warp on this scale, and wide-area Magic. Quite impressive. One step above the human mage from a few days ago.”

Quite impressive.

That was all Morgoth said of Magic Johnson, and there wasn’t a trace of arrogance in his appraisal.

Dragons were mysterious creatures born for Magic—Magic itself, one might say—and Morgoth was the very pinnacle of their kind.

Before he had even reached adulthood, Morgoth had already touched the limits of Magic. To him, the Magic of other races was little more than child’s play. That remained true even in this unfamiliar world called Earth.

Otherwise, Merlin—the Grand Mage who, after Siegfried Wassman’s death, was one of only two left alongside Magic Johnson—wouldn’t have chosen to blow himself up in the battle a few days ago.

“He was quick to catch on. When he saw me collecting the bodies of his comrades, he didn’t hesitate to choose death.”

The Grand Mage had been a rare trophy, so Morgoth had felt a trace of regret.

Not anymore.

“I suppose I should thank you. I never expected you to give me such fine trophies.”

Greed, held in check until now, glinted briefly in his two obsidian eyes.

Of the thousands of humans closing in as they crushed the monster army, only two posed even the slightest threat to him.

But even Magic Johnson and Chuck Hagel were no more than trophies in Morgoth’s eyes. And before Jin Taekyung, already weighed down by no small amount of fatigue, stood a thousand Dragon-tooth soldiers, each one practically a named monster in its own right, blocking his way like an iron wall.

Alongside them were the seven Guardians, reborn as beings far more powerful than before.

“Nothing has changed. This battle is over.”

He was right.

Anyone would have thought so.

The odds were overwhelmingly in Morgoth’s favor.

And yet.

They should have been. So why?

Jin Taekyung was still smiling.

At the same time, Morgoth saw an unfamiliar figure reflected in the heat shimmering in Jin’s eyes.

His own face, frozen stiff despite the words he’d just spoken.

“What’s so funny?”

Unable to hold back, Morgoth demanded an answer. Jin Taekyung lifted the spear he’d been leaning on like a staff.

“I just feel a little better.”

“……You feel better?”

“Yeah. I’ve been in situations like this plenty of times. Heard those same things you just said, too.”

Jin Taekyung spat out the phlegm gathered in his mouth.

“You know, the usual stuff. ‘I’m different from everyone else.’ ‘I never let my guard down.’ ‘I’ll kill you for sure.’ ‘It’s all over.’ That kind of crap.”

All those countless times he’d come close to death.

They were memories so awful Jin Taekyung never wanted to think about them again. But this time was different.

Why?

Simple.

“The weird thing is, not one of those bastards ever followed through on what they said.”

It was true.

He’d fought every one of them, and he’d beaten every one of them.

His arms and legs crushed, his insides churned to mush, brought to the edge of death—he had always been the one to survive.

But perhaps the deepest reason he’d won so many hopeless battles wasn’t just the power of the System.

“Why was that? Some of them really could’ve killed me. So why waste time on pointless words and actions, leaving themselves open?”

He was afraid.

Always. Every time.

In battle—and even in every quiet moment of everyday life.

He feared losing his life to some powerful enemy he would meet someday, and he suffered at the thought that he might have to stand on someone else’s sacrifice to survive.

So whenever he met an enemy, he hurled insults at them.

He piled on every kind of abuse, then dragged up even the smallest fragments of anger and grief sleeping deep inside him, smothering his fear beneath them.

He had to make himself stronger, even if that was the only way.

People called him a hero, but the person he knew himself to be was far too weak to carry such a heavy burden.

But looking back, he hadn’t been the only one afraid of the person standing in front of him.

“Then, all of a sudden, I started feeling better.”

Jin Taekyung had finally realized it.

“The guys I beat were afraid of me, too.”

“……!”

“What they said was all just fear talking. Same as you right now.”

Looking at Morgoth’s face, suddenly gone cold, Jin Taekyung smiled faintly.

“What, did I hit a nerve?”

Morgoth didn’t answer.

No—he couldn’t.

Everything Jin Taekyung said was true.

His pride and insight were too great for him to deny it.

“……Fear.”

He’d forgotten it.

More precisely, he’d tried to forget the one time he’d ever felt that pathetic emotion.

But at last, Morgoth had no choice but to admit it.

What he felt for Jin Taekyung was more than caution.

“Yes. I see. I was a little afraid of you, too.”

Though the strength of their feelings differed, their nature was the same.

Muttering in a low voice, Morgoth looked at the tiny human who had dared to make him feel afraid.

At the same time, he understood what he had to do.

“But I’ll swear to you one thing.”

*Vwooom.*

The wind stopped. The air around them shuddered.

“I am nothing like anyone you’ve faced before.”

At that moment—

*Fwoosh!*

Darkness erupted around Morgoth and swelled, engulfing his entire body.

It rose as high as the spire that now lay in ruins, and grew as vast as a fortress wall.

Jin Taekyung instinctively understood what the phenomenon before him meant.

*Polymorph.*

Would the world look like this if the sun vanished without a trace?

The Black Dragon finally shed his human skin. The darkness surrounding him blackened the sky overhead and the battlefield for hundreds of meters in every direction.

As if announcing the end of the world.

But Jin Taekyung’s eyes didn’t waver as he watched it all.

The darkness, having completed its task, was slowly dissipating. At the same time, a thousand Dragon-tooth soldiers, obeying their master’s command, were charging straight at him.

*It’s coming. It has to.*

He knew.

Just as darkness existed wherever there was light, a new light awaited him beyond this darkness.

And his faith was rewarded.

Just as someone had answered the voice with which Jin Taekyung had once cried out for salvation.

*Fwoooosh!*

The world lit up in an instant.

The horizon, sinking into darkness like an extinguished campfire, and the land, being swallowed by an even deeper gloom, were bathed in light.

In dozens, then hundreds of pillars of light.

In the hearts of those who had crossed thousands, then tens of thousands of kilometers, time and again, to answer his call.

“……What is this?”

The horizon blazed like a line of fire, crowded with countless Magic Formations of Warp.

At Morgoth’s groan, which thundered from high in the distant sky, Jin Taekyung spoke.

“I’ll swear one thing, too.”

His low voice rode the wind.

Along with the step he took forward, and the spearhead he leveled at the enemies bearing down on him.

“You’ll end up just like them.”

*Whoosh—slice!*

As fierce flames rose like dawn and lit the battlefield, a mighty roar raced along the horizon and shook the field of battle.
```
